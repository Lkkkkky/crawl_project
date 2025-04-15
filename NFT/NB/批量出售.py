'''
=========================================================    
       @File     : 批量出售.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/27 10:43
       @Desc     : 
=========================================================   
'''
import requests
import json
import time
import hashlib

cnt=0
timestamp=str(int(time.time()*100))
from loguru import logger

def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

def get_nft_detail(page):

  headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://h5.newbee.net.cn",
    "platformn": "h5",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://h5.newbee.net.cn/",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "signature": "2bd17b71495819c32b37b39388bcb2ac",
    "token": "ecd9f038-b001-40ed-9ff8-b176cc71aa6b",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "x-token": "318cd71edb4383042285385700e5ea3e"
  }
  url = "https://api.newbee.net.cn/api/user_collect"
  params = {
    "page": str(page),
    "per_page": "50",
    "product_id": "14698",
    "product_type": "virtual",
    "timestamp": "1740624056390",
    "type": "own_valid"
  }
  response = requests.get(url, headers=headers, params=params).json()
  for i in response['data']['data']:
      print(i)
      batch_sell(i['id'],i['item_id'],i['item']['sn'],'245687',cnt)
      time.sleep(10)

  print(response)
def batch_sell(id, item_id, sn, pwd,cnt):
  cur_pri=int(get_current_price())
  xtoken=md5(f'api/user_collect/onsalenew?amount={cur_pri}&cid={id}&item_id={item_id}&pay_password={pwd}&paytypes=140,121&product_id=14698&sn={sn}&timestamp={timestamp}&key=6rnrdpjjv6wz2sspxqeibesov1itxddc')
  headers = {
      "accept": "*/*",
      "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
      "cache-control": "no-cache",
      "content-type": "application/json;charset=UTF-8",
      "origin": "https://h5.newbee.net.cn",
      "platformn": "h5",
      "pragma": "no-cache",
      "priority": "u=1, i",
      "referer": "https://h5.newbee.net.cn/",
      "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-site",
      "signature": "2bd17b71495819c32b37b39388bcb2ac",
      "token": "ecd9f038-b001-40ed-9ff8-b176cc71aa6b",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
      "x-token": xtoken
  }
  url = "https://api.newbee.net.cn/api/user_collect/onSaleNew"
  data = {
      "amount": cur_pri,
      "cid": id,
      "item_id": item_id,
      "pay_password": pwd,
      "paytypes": "140,121",
      "product_id": 14698,
      "sn": sn,
      "timestamp": int(time.time()*100)
  }
  data = json.dumps(data, separators=(',', ':'))
  response = requests.post(url, headers=headers, data=data)
  if response.json()['msg']=='操作成功':
      cnt += 1
      logger.info(f'第{cnt}卖出成功----{cur_pri}')


  print(response.text)
  print(response)

def get_current_price():
    timestamp = str(int(time.time() * 1000))
    xtoken = md5(f'api/market/getcollprice?id=14698&timestamp={timestamp}&key=6rnrdpjjv6wz2sspxqeibesov1itxddc')
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://h5.newbee.net.cn",
        "platformn": "h5",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://h5.newbee.net.cn/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "signature": "2bd17b71495819c32b37b39388bcb2ac",
        "token": "ecd9f038-b001-40ed-9ff8-b176cc71aa6b",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/133.0.0.0",
        "x-token": xtoken
    }
    url = "https://api.newbee.net.cn/api/market/getCollPrice"
    params = {
        "id": "14698",
        "timestamp": timestamp
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()['data']['current_price'].replace('.00','')
get_nft_detail(1)