'''
=========================================================    
       @File     : 实现.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/19 17:38
       @Desc     : 
=========================================================   
'''
import requests
import execjs
res=execjs.compile(open('enc.js','r',encoding='utf-8').read()).call('enc','17896686831','00000000ab')
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.gldzb.com",
    "Pragma": "no-cache",
    "Referer": "https://www.gldzb.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Timestamp2": "1739955719199",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    # "encryptData": res[0],
    # "iv": res[2],
    # "key": res[1],
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "timestamp": "1739955719523",
    "token;": "",
    "uuidHashCode": "5c957c2493c94e03b222df6247732bd8"
}
url = "https://gldzb-gateway.gldzb.com/gldzb-manage-api/api/web/loginByAuth"

print(res)
data = {
    "encryptData": res[0],
    "key": res[1],
    "iv": res[2]
}
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)