import requests
import json

combo = ""

while ':' not in combo:
    combo = input("Enter the account details in email:password format: ")

username = combo.split(':')[0]
password = combo.split(':')[1]

with requests.Session() as session:
    response = session.post("https://authserver.mojang.com/authenticate", json={ 'agent' : {"name" : "Minecraft", "version" : 1}, 'username': username, 'password': password})
    if response.status_code == 200:
        text = response.text
        if "Invalid credentials. Invalid username or password" in text:
            print(username + ' failed to login!\nPress enter to exit.')
            input()
        else:
            data = response.json()
            uuid = data['selectedProfile']['id']
            token = data['accessToken']
            print("Token: " + token)
            headers = {"Authorization": f"Bearer {token}"}
            response2 = session.get("https://api.mojang.com/user/security/challenges", headers=headers)
            if response2.status_code == 200:
                print("Token is now a valid bearer token for the next couple minutes.")
            else:
                print("Something went wrong. Response2 status code: " + response2.status_code)
    else:
        print("Something went wrong. Response status code: " + response.status_code)
