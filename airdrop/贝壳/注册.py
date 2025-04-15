import requests
import json
import random
import string

def generate_random_username(length=10):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length)) + '@163.com'
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://shellscoin.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://shellscoin.com/h5/",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "token;": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
}
for i in range(2000):
    url = "https://shellscoin.com/api/user/register"

    data = {
        "username": generate_random_username(),
        "password": "00000000ab",
        "code": "MzI3MDE0",
        "lang": "zh-tw"
    }

    data = json.dumps(data, separators=(',', ':'))

    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()

    if response_json.get("code") == 1:
        token = response_json["data"]["userinfo"]["token"]
        with open("token.txt", "a+") as file:
            file.write(token)
            file.write('\n')
        print("Token saved to token.txt")
    else:
        print("Registration failed:", response_json.get("msg"))
