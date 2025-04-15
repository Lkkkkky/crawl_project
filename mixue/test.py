import requests
import json


headers = {
    "Host": "mxsa.mxbc.net",
    "Content-Type": "application/json;charset=utf-8",
    "Origin": "https://mxsa-h5.mxbc.net",
    "Accept-Encoding": "gzip, deflate, br",
    "Access-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eG1pbmlfMTQ0OTM2OTU5MTYwOTc5NDU2MSIsImlhdCI6MTcyMjA2NjU3Nn0.jmF8X2FIbIOVUmo57jUc-syN1yK6nEb8zhY75YNP1OZMB1yE8-1wWGN8SGl_pR-xV1wtL-ODf3g6O6CJtSlQyA",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN miniProgram/wx7696c66d2245d107",
    "Referer": "https://mxsa-h5.mxbc.net/",
    "Content-Length": "164",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9"
}
url = "https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm"
params = {
    "type__1286": "n4+xuD9DBDyGGQGC7G8DlxG2b7NqyBhDMh38TD"
}
data = {
    "marketingId": "1816854086004391938",
    "round": "11:00",
    "secretword": "茉莉奶绿 奶香四溢",
    "sign": "42d07b5a549b5fe196be4d85eec1eb71",
    "s": 2,
    "stamp": 1723173210255
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, params=params, data=data)

print(response.text)
print(response)