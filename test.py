import time

import requests
import json



def login(token):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "baggage": "sentry-environment=production,sentry-release=e1495ce3034700b6b57f86fcc782f13025130199,sentry-public_key=9c619d9c8b984da6b158a79cb8973c86,sentry-trace_id=2c93fd60356844b0810345e76ae2e7ea",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://www.globalinterpark.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.globalinterpark.com/zh/login",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sentry-trace": "2c93fd60356844b0810345e76ae2e7ea-8e0d4db689555c84-0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        "x-cbt-user-lang": "zh"
    }
    cookies = {
        "language": "zh",
        "_gid": "GA1.2.563853466.1743932922",
        "_gat_UA-60117844-2": "1",
        "_ga": "GA1.2.511048288.1743932922",
        "hide-sns-sign-up-block-popup": "true",
        "_ga_3840G72Z4Q": "GS1.1.1743932922.1.1.1743932936.0.0.0"
    }
    url = "https://www.globalinterpark.com/api/sign-in/email"
    data = {
        "email": "1158356001@qq.com",
        "password": "00000000ab@",
        "token": token
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    print(response.text)
    print(response.cookies)

def createtask():
    headers={
        "content-type": "application/json",
    }
    data={
        "clientKey":"444ca4fc17c6533bf452d4d19a374794005a7d9d65131",
        "task":
            {
                "type":""
                       "     ",
                "websiteURL":"https://www.globalinterpark.com",
                "websiteKey":'0x4AAAAAAAKC1nc26lcmHwc5'
            }
    }
    res=requests.post('https://cn.yescaptcha.com/createTask',headers=headers,json=data)
    print(res.text)
    return res.json().get('taskId')

def getTaskResult(taskId):
    headers = {
        "content-type": "application/json",
    }
    data = {
    "clientKey":"444ca4fc17c6533bf452d4d19a374794005a7d9d65131",
    "taskId": taskId
}
    res=requests.post('https://cn.yescaptcha.com/getTaskResult',headers=headers, json=data)
    print(res.text)
    return res

id=createtask()
for i in range(30):
    res=getTaskResult(id)
    try:
        if res.json()['solution']['token']:
            login(res.json()['solution']['token'])
            break
    except Exception:
        pass
    time.sleep(5)
