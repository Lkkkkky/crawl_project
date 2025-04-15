'''
=========================================================
       @File     : 快捷下单.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/26 14:35
       @Desc     :
=========================================================
'''
import requests
import json
import time
import hashlib
from loguru import logger
import execjs
import re

token='dfa1720a-9340-4eb3-8dee-f5e6383f98b2'
def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

#快捷下单获取NB订单号
def fast_buy(id):
    timestamp=int(time.time()*1000)
    xtoken=md5(f'api/market/fastbuy?product_id={id}&timestamp={timestamp}&key=6rnrdpjjv6wz2sspxqeibesov1itxddc')
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
        "token": token,
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/133.0.0.0",
        "x-token": xtoken
    }
    url = "https://api.newbee.net.cn/api/market/fastBuy"
    data = {
        "product_id": id,
        "timestamp": timestamp
    }

    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    logger.info(response.text)

    if response.json()['code']==1:
        requests.get('https://api.day.app/YToREckaeQXotQJPrn7MWa/NB拿下啦！！！！！')
        return response.json()['data']['order_id']

#提交NB订单号到汇付，获取汇付订单号，提取支付链接
def order_submit(id):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://h5.newbee.net.cn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://h5.newbee.net.cn/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "signature": "2bd17b71495819c32b37b39388bcb2ac",
        "token": token,
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/133.0.0.0",
        "x-token": "d38c23d7b9fc8bae8f6ca56379343274"
    }
    timestamp = int(time.time() * 1000)
    url = "https://pay.newbee.net.cn/pay/order/submit"
    data = {
        "id": id,
        "pay_type": 140,
        "return_url": f"https://h5.newbee.net.cn/#/pages/userCenter/orderDetail?order_id={id}&v={timestamp}",
        "timestamp": timestamp
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    if response.json()['code']==1:
        logger.info( response.json()['data'].replace('\\',''))
        return response.json()['data'].replace('\\','')
#支付密码校验
def hf_password(pwd,orderinfo):
    ret = execjs.compile(open('enc.js', 'r', encoding='utf-8').read()).call('get_enc',pwd,orderinfo)
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "check_value": "862b0fafdb0652515dc9988c15c444821a2cbcb937db81284de38165e0d105ea",
        "content-type": "application/json",
        "hide_head": "0",
        "mer_cust_id": re.findall('hfpwallet(.*?)pay',orderinfo),
        "origin": "https://hfpay.cloudpnr.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://hfpay.cloudpnr.com/h5/pages/cashier/index?uuid=hfpwallet6666000137842973pay262769ab-e705-48af-bfe2-3d00404a8268",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/133.0.0.0",
        "uuid": orderinfo
    }
    url = "https://hfpay.cloudpnr.com/api/hfpwalleth5/transpasswordcheck"
    data = {
        "password": ret
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    print(response.text)
    print(response)
#支付订单
def pay(orderinfo):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "check_value": "3a849b97b182c1d6698ae75124450f5e92bcdb11c968633ed3f58b88ef9b4312",
        "content-type": "application/json",
        "hide_head": "0",
        "mer_cust_id": re.findall('hfpwallet(.*?)pay',orderinfo),
        "origin": "https://hfpay.cloudpnr.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": f"https://hfpay.cloudpnr.com/h5/pages/cashier/index?uuid={orderinfo}",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/133.0.0.0",
        "uuid": orderinfo
    }
    url = "https://hfpay.cloudpnr.com/api/hfpwalleth5/paystatquery"
    data = {}
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)

    print(response.text)
    print(response)


id=fast_buy(12452)
orderinfo=order_submit(id).replace('https://hfpay.cloudpnr.com/h5/pages/cashier/index?uuid=','')


hf_password('698698', orderinfo)
pay(orderinfo)