'''
=========================================================    
       @File     : try.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/17 16:43
       @Desc     : 
=========================================================   
'''
import requests
import json
import execjs

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://aq.99.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://aq.99.com/",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
url = "https://checkcode.99.com/slide"
rsakey="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDMjeiNR7Y3GZXs0xjZxbphRSimSLbpYeVSpmWN10r66w6ZLrSHBjsODDmwnKnzKgvptYBz+3rZKx3Z4ZonND1lED5Majzt0NtviqDqV0uQOtjepFDwQfxE3Y01xRJr9N/HyJjVrMTjCpllPWfvVNyKR0tVJBCyAYhGFqBcbMhWVwIDAQAB"
dis=150
slide_image="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"
w=execjs.compile(open('练习.js','r',encoding='utf-8').read()).call('get_enc',rsakey,dis,slide_image)
data = w
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)