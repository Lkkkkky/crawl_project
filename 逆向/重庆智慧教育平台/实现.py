# https://higher.cq.smartedu.cn/index/home

import requests
import json
import execjs
from time import time
from hashlib import md5


t=int(time()*1000)
print(t)
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://higher.cq.smartedu.cn",
    "Pragma": "no-cache",
    "Referer": "https://higher.cq.smartedu.cn/index/home",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sg": "d41d8cd98f00b204e9800998ecf8427e",
    "ts": str(t)
}
cookies = {
    "_abfpc": "57f8d494213dd35a362bd44505f2434fe6d96183_2.0",
    "cna": "3d63cf3feca371efa206ba6de007ca0a",
    "Hm_lvt_deeb6849ac84929e8ae01644f8d27145": "1728461669,1728489846",
    "Hm_lpvt_deeb6849ac84929e8ae01644f8d27145": "1728489846",
    "HMACCOUNT": "63D4C43D932FC87A"
}
# 从服务器获取随机数nonce
url = "https://higher.cq.smartedu.cn/api/auth/user/login/"


url2 = "https://higher.cq.smartedu.cn/api/auth/user/login/do"


response = requests.get(url,headers=headers, cookies=cookies)
# print(response)
res=json.loads(response.text)
nonce=res['result']["NONCE"]
print(nonce)


# 由nonce算出DLMM
arr=execjs.compile(open('js.js','r',encoding='utf-8').read()).call('get_enc',nonce)
DLMM=arr[0]
print(DLMM)
data = {
    "CNONCE": arr[1],
    "DLMM": DLMM,
    "NONCE": nonce,
    "QMLX": "",
    "YZMLP": "",
    "DLZH": "17896686831"
}
data = json.dumps(data, separators=(',', ':'))
print(data)

response = requests.post(url2, headers=headers, cookies=cookies, data=data)
print(response.text)
res_sqlp=json.loads(response.text)['result']
res_2=execjs.compile(open('js.js','r',encoding='utf-8').read()).call('get_result',res_sqlp)
print(res_2)
SQLP=json.loads(res_2)['SQLP']
print(SQLP)



ss=SQLP+"_2Cqooc&#(*@&("+ str(t)
print(ss)
url3='https://higher.cq.smartedu.cn/api/user/profile/info'

headers['SQLP']=SQLP
headers['sg']=md5(ss.encode('utf-8')).hexdigest()
print(headers)
response = requests.get(url3, headers=headers,cookies=cookies)
print(response.text)

s2='755df4509dcc4f4a822aef1d6f46a9cb_2Cqooc&#(*@&(1728498910706'

print(md5(s2.encode('utf-8')).hexdigest())