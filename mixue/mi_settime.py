# -*- coding: utf-8 -*-


import hashlib
import json
import time
import requests
import threading

# ----------------------------------------
round = "11:00"
keyword = "茉莉奶绿 甜蜜再续"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eG1pbmlfMTgxNzQ1NDQxNTExNzE5MzIxOCIsImlhdCI6MTcyMjcxODYwN30.682BUXnt3jltAaTHGN9A5f6rDcjMHsLfvPn3n_3OTeHV-NGjWgv4wF1rmpg7GPXYgsYfmrT56BcNGABjv8HnAQ"
tk='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eG1pbmlfMTgxNzQ3NjEyNTE0OTI1MzYzMyIsImlhdCI6MTcyMzIwODEyNH0.hGP3JOkfgei9-ZSXw8w_H1CyCr78zHghT0-zI_XNp-3szRKYKD0ABa3RkkDULyfImuGkmgv_eX-ywP3qGFrUyg'
# ----------------------------------------

import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

with open("./js加密.js", "r", encoding="utf-8") as f:
    js = execjs.compile(f.read())


def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()


session = requests.session()
headers = {
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Access-Token": token,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN miniProgram/wx7696c66d2245d107",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://mxsa-h5.mxbc.net",
    "X-Requested-With": "com.mxbc.mxsa",
    "Referer": "https://mxsa-h5.mxbc.net/",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
session.headers = headers
url = "https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm"
params = {}


def send(round: str, keyword: str,token):
    t = int(time.time() * 1000)
    print(t)
    data = {
        "marketingId": "1816854086004391938",
        "round": round,
        "s": 2,
        "secretword": keyword,
        "sign": "",
        "stamp": t
    }
    sig = []
    for k in data.keys():
        if k == "sign": continue
        sig.append(k + "=" + str(data[k]))
    sig = "&".join(sig) + "c274bac6493544b89d9c4f9d8d542b84"

    # MD5加密算法
    data["sign"] = md5(sig)

    copy_data = {
        "marketingId": data["marketingId"],
        "round": data["round"],
        "secretword": data["secretword"],
        "sign": data["sign"],
        "s": data["s"],
        "stamp": data["stamp"]
    }

    N = json.dumps(copy_data, ensure_ascii=False)
    # .replace(" ", "")  有空格的话加上
    print(N)
    type_ = js.call("R_type", N)
    params["type__1286"] = type_["type__1286"]
    try:
        response = session.post(url, params=params, data=N.encode())
        print(response.request.headers)
        print(response.request.url)



        return response
    except:
        return 0


while True:

    settime='2024-08-12 11:00:00'
    tt=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    if tt>settime :
        s = send(round, keyword,token)

        if s.status_code != 405:
            print(s.text)
            requests.get(f'http://47.236.198.227:8080/fhFfdJTuxzwbWPky6Tw9u5/蜜雪/{s.text}')
            time.sleep(2)
            continue
        if s.status_code == 200:
            requests.get(f'http://47.236.198.227:8080/fhFfdJTuxzwbWPky6Tw9u5/蜜雪/{s.text}')
            print(s.text)
            break
