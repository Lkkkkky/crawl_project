'''
=========================================================    
       @File     : 通道合成.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/25 15:29
       @Desc     : 
=========================================================   
'''
import requests
import json
# print(ret)
from  loguru import  logger
import requests
import json
import execjs
import time

for i in range(10000):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJoNV91c2VyOjE1NzgwNDQ4NTk0OTQ2MjUyODAiLCJyblN0ciI6IkNRS3o0R1RrYXdObnFBclJ6MkxoWWY0S0FKQlJ1VWZTIn0.eq0UODwy3DqWHMQaP5Elw_utcMeVBAxzkwFJOnsd44Y",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://m.shengqingqy.cn",
        "Pragma": "no-cache",
        "Referer": "https://m.shengqingqy.cn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36 Edg/133.0.0.0",
        "content-language": "zh-CN",
        "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "token": "562746e1e56a310bb5f210a36cc05b76"
    }
    url = "https://api.shengqingqy.cn/activity/app/new/compose/prepareToCompose"
    ret = execjs.compile(open('enc.js', 'r', encoding='utf-8').read()).call('getdata')

    data = {
        "ruleSetId": "1894287467796152322",
        "willConsumes": [
            {
                "productId": "1893873287037624321",
                "relationId": "1893873287012458497",
                "tag": "A",
                "memberNftIds": [
                    "1805809190139655646",
                    "1805809190139656372",
                    "1805809190139660122"
                ],
                "number": 3,
                "consumeNum": 3
            },
            {
                "productId": "1893287210962059266",
                "relationId": "1893287210907533314",
                "tag": "B",
                "memberNftIds": [
                    "1805809190139409390",
                    "1805809190139418444",
                    "1805809190139418971",
                    "1805809190139419996",
                    "1805809190139421681",
                    "1805809190139422244",
                    "1805809190139424687",
                    "1805809190139425639",
                    "1805809190139430820",
                    "1805809190139671068",
                    "1805809190139671069",
                    "1805809190139671070",
                    "1805809190139680804",
                    "1805809190139680805",
                    "1805809190139680806",
                    "1805809190139680807",
                    "1805809190139680808",
                    "1805809190139680809",
                    "1805809190139680810",
                    "1805809190139697603"
                ],
                "number": 20,
                "consumeNum": 20
            }
        ],
        "sign_appid": "h5_23514861",
        "timestamp": 1740468583,
        "nonce": ret[0],
        "sign": ret[1]
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    if response.json()['code']!=500:
        requests.get('https://api.day.app/YToREckaeQXotQJPrn7MWa/青龙合成成功！！！！！')
    print(response.text)
    time.sleep(0.32)

