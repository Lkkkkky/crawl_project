'''
=========================================================    
       @File     : 市场捡漏.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/25 09:25
       @Desc     : 
=========================================================   
'''
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
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJoNV91c2VyOjE1NzgwNDQ4NTk0OTQ2MjUyODAiLCJyblN0ciI6IkNRS3o0R1RrYXdObnFBclJ6MkxoWWY0S0FKQlJ1VWZTIn0.eq0UODwy3DqWHMQaP5Elw_utcMeVBAxzkwFJOnsd44Y",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
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
    "token": "f23b3f3fff5c26e4a7a5591723fd6ff8"
}
def search_low_price(id,price):
    ret = execjs.compile(open('enc.js', 'r', encoding='utf-8').read()).call('getdata')
    # print(ret)

    url = "https://api.shengqingqy.cn/market/app/market/list"
    data = {
        "pageNum": "1",
        "pageSize": "20",
        "type": "1",
        "key": "",
        "status": "",
        "sortType": "4",
        "productId": id,
        "sign_appid": "h5_23514861",
        "timestamp": str(int(time.time())),
        "nonce": ret[0],
        "sign": ret[1]
    }

    response = requests.get(url, headers=headers, data=data).json()
    try:
        logger.info('目前最低价为:'+response['rows'][0]['id']+response['rows'][0]['name']+'----'+response['rows'][0]['price'])
        if int(response['rows'][0]['price'].replace('.0',''))<price:
            make_order(response['rows'][0]['id'])
    except:
        logger.info('暂无挂售')

    # time.sleep(32)
def make_order(nft_id):
    ret = execjs.compile(open('enc.js', 'r', encoding='utf-8').read()).call('getdata')

    url = "https://api.shengqingqy.cn/order/app/order/preOrder"
    params = {
        "productId": nft_id,
        "count": "1",
        "type": "3",
        "firstBuyId": "",
        "ruleId": "",
        "randomCode": "",
        "sign_appid": "h5_23514861",
        "timestamp": str(int(time.time())),
        "nonce": ret[0],
        "sign": ret[1]
    }
    response = requests.get(url, headers=headers, params=params).json()
    if response['code']==200:
        requests.get('https://api.day.app/YToREckaeQXotQJPrn7MWa/青龙拿下啦！！！！！')

for  i in range(100000):
    # jianlou('1893330885271785474',200)#后羿
    search_low_price('1893873287012458497',100)#小钻头
    search_low_price('1893647694191648769',1000)#牛
    search_low_price('1893914526362361858',1000)#大钻头
    search_low_price('1893287210907533314',10)#腊梅
    search_low_price('1894059474810425345',10)#猫猫
    search_low_price('1893647384007467009',500)#老鼠
    # jianlou('1893654319371640833',100)#宫阙
    # jianlou('1893329560060084226',1000)#嫦娥

