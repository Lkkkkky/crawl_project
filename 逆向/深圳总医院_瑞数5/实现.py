'''
  @File     : 抢购.py
  @IDE      : IntelliJ IDEA
  @Author   : Jing3
  @Date     : 2024/10/7 14:55
'''
import execjs
import requests
import json
from lxml import etree
import re

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://sugh.szu.edu.cn/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}
url1 = "https://sugh.szu.edu.cn/"
response = requests.get(url1, headers=headers)

ck1=response.cookies.get_dict()['ihkYnttrQXfVO']
content=re.findall('<meta content="\{(.*?)">',response.text)[0]
js_code=re.findall("text/javascript\" r='m'>(.*?)</script>",response.text)[0]
# print(ck1)
# print(js_code)
# print(content[0])
# print(response.text)

cookies={
    'ihkYnttrQXfVO':ck1
}
url2='https://sugh.szu.edu.cn//IkxfQuImHWbf/szBN0h1em4ON.87f8093.js'
response=requests.get(url2,cookies=cookies,headers=headers)
ts=response.text
# print(response.text)
with open('动态js.js','r',encoding='utf-8') as f:
    code =f.read()
code =code.replace('&&content&&',content)
code =code.replace("'$$ts$$'",ts)
code =code.replace("'$$jscode$$'",js_code)

ck2=execjs.compile(code).call('get_cookie')
cookies['ihkYnttrQXfVP']=ck2.split('=')[1].split(';')[0]
# ck2=ck2.split('=')[1]
print(cookies)
response=requests.get(url1,headers=headers,cookies=cookies)
html=etree.HTML(response.text)
print(response.text)