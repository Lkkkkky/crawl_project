'''
=========================================================
       @File     : 通过审核.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/26 19:45
       @Desc     :
=========================================================
'''
'''
=========================================================    
       @File     : 提交审核.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/24 19:11
       @Desc     : 
=========================================================   
'''
import requests
import json

for i in range (979,1039):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://cbsadmin.dropwiz.net",
        "Referer": "https://cbsadmin.dropwiz.net/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "System-Token": "cbs:system:TOKEN:8ad2b8c4e4c6240414b59936973145fd",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
        "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://api.dropwiz.net/system/goods/auditPass"
    data = {
        "auditResult": 1,
        "auditSpuId": i,
        "remark": ""
    }

    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)

    print(i,'---->'+response.text)

    print(response)