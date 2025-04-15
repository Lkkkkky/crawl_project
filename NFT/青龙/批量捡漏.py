'''
=========================================================    
       @File     : 批量捡漏.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/24 11:31
       @Desc     : 
=========================================================   
'''
import time

import execjs




# print(ret)
from  loguru import  logger
import requests
import json


token='4b06d27abd0bd74fc148b36f0aea9a94'
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJoNV91c2VyOjE1NzgwNDQ4NTk0OTQ2MjUyODAiLCJyblN0ciI6IkM5ZVpyUTZwdDJkaXM0TTRwVnBwZkwyTmk4UFgwWGJXIn0.h8HSBf3Ip9jWK_2N2wDVMIOMX484XSWJ2-Y1ZKG5t6U",
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
    "token": token
}
def jianlou(id,price,name):
    ret = execjs.compile(open('enc.js', 'r', encoding='utf-8').read()).call('getdata')

    url = "https://api.shengqingqy.cn/order/app/order/batchSubmit"
    data = {
        "captchaRandstr": "",
        "captchaTicket": "",
        "payMethod": "4",
        "productId": id,
        "hasAuto": True,
        "maxPrice":price,
        "count": 5,
        "sign_appid": "h5_23514861",
        "timestamp": 1740382195,
        "nonce": ret[0],
        "sign": ret[1]
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    logger.info(response.text+'----'+name)
    if response.json()['code']!=500:
        requests.get('https://api.day.app/YToREckaeQXotQJPrn7MWa/青龙拿下啦！！！！！')
        time.sleep(30)

    time.sleep(0.4)
for  i in range(100000):
    # jianlou('1893330885271785474',200)#后羿
    # jianlou('1893873287012458497',130,'小钻头')#钻头
    # jianlou('1894631622500728833',30,'青龙卡')#青龙卡
    # jianlou('1893287210907533314',10,'腊梅')#辣妹
    jianlou('1899707708548382721',100,'光头')#光头
    # jianlou('1894042622404132865',58,'仙童')#仙童
    # jianlou('1893647694191648769',300,'牛')#牛
    # jianlou('1894093782761848833',300,'仙鹤')#仙鹤
    # jianlou('1893970643526557697',2000,'范小勤')#范小勤
    # jianlou('1893960860168683521',200,'时空之门')#时空之门
    # jianlou('1893647384007467009',500)#老鼠
    # jianlou('1893654319371640833',100)#宫阙
    # jianlou('1893329560060084226',1000)#嫦娥

