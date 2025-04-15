import requests
import json
import execjs
import time
from datetime import datetime, timedelta

# 定义目标时间（今天的 16:30:00）
import requests
import json


for i in range(10000):
    ret = execjs.compile(open('enc.js', 'r', encoding='utf-8').read()).call('getdata')
    import requests
    import json

    headers = {
        "Host": "api.shengqingqy.cn",
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJoNV91c2VyOjE1NzgwNDQ4NTk0OTQ2MjUyODAiLCJyblN0ciI6InFkbUZLU3dVZmx6ZzdVa0xlZkp1TFE1QmtKa09JYm9YIn0.CwSYNjR0sBrHIRYrXVnyoGN5yu8CD1l5jYsulYr7tgw",
        "Content-Language": "zh-CN",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "token": "bf5f11d90d9411a078cab0779d094ad6",
        "Content-Type": "application/json",
        "Origin": "https://m.shengqingqy.cn",
        "Content-Length": "157",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
        "Referer": "https://m.shengqingqy.cn/",
        "Connection": "keep-alive"
    }
    url = "https://api.shengqingqy.cn/market/app/market/1697439"
    data = {
        "memberNftId": "1805809190139463739",
        "sign_appid": "h5_23514861",
        "timestamp": 1740489985,
        "nonce": ret[0],
        "sign": ret[1]
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)

    print(response.text)
    print(response)
    time.sleep(1)