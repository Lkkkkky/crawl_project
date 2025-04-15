'''
=========================================================    
       @File     : 豪猪模块.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/3/19 02:00
       @Desc     : 
=========================================================   
'''
import requests
import time
import sys
import os
from loguru import logger

# 添加全局计数器
failure_count = 0


def login(api_account,api_key):
    response=requests.get(f'https://api.haozhuma.com/sms/?api=login&user={api_account}&pass={api_key}')
    token=response.json()['token']
    # logger.info(response.text)
    response=requests.get(f'https://api.haozhuma.com/sms/?api=getSummary&token={token}')
    logger.info('登录成功,余额为:'+response.json()['money'])
    #返回令牌
    return token
def get_phone(token,item_id):
    response = requests.get(f'https://api.haozhuma.com/sms/?api=getPhone&token={token}&sid={item_id}&ascription=2')#只取实卡
    #
    #返回获取到的手机号
    # logger.info(response.text)
    logger.info('获取手机号成功:'+response.json()['phone'])
    return response.json()['phone']
def get_phone_zhiding(token,item_id,phone):
    response = requests.get(f'https://api.haozhuma.com/sms/?api=getPhone&token={token}&sid={item_id}&phone={phone}')#只取实卡
    logger.info(response.text)
    #返回获取到的手机号
    return response.json()['phone']
def get_yzm(token,item_id,phone):
    global failure_count
    for i in range(30):  # 将循环次数从100改为60
        response = requests.get(f'https://api.haozhuma.com/sms/?api=getMessage&token={token}&sid={item_id}&phone={phone}')#只取实卡
        if(response.json()['code']=='0'):
            logger.info(response.text)
            failure_count = 0  # 重置计数器
            #返回获取到的验证码
            return response.json()['yzm']
        logger.info(f'正在获取验证码----{phone}')

        time.sleep(1)
    # 如果60次尝试后仍未获取到验证码，则重新获取
    new_phone=get_phone(token,item_id)
    logger.info(f'获取验证码超时，重新获取----{new_phone}')
    ver_token = vertify()
    send(new_phone, ver_token)
    return get_yzm(token, item_id, new_phone)  # 递归调用自身重新获取
#释放全部
def cancelRecv(token):
    res=requests.get(f'https://api.haozhuma.com/sms/?api=cancelRecv&token={token}')
    print(res.text)
#如果不来码  不再重新获取
def get_yzm_no(token,item_id,phone):
    for i in range(60):  # 将循环次数从100改为60
        response = requests.get(f'https://api.haozhuma.com/sms/?api=getMessage&token={token}&sid={item_id}&phone={phone}')#只取实卡
        if(response.json()['code']=='0'):
            logger.info(response.text)
            #返回获取到的验证码
            return response.json()['yzm']
        logger.info(f'正在获取验证码----{phone}')
        time.sleep(1)
    # 如果60次尝试后仍未获取到验证码，则重新获取

    return 'no'  # 递归调用自身重新获取
# token=login()
# phone=get_phone(token,'56080')#光明随心订
# get_yzm(token,'56080')
# user_account='db9d44ce09b33035e60f817d368429e124b49f64671f21ed'
# user_key='876bacf58d02fd8080c8fb9a1cb6acb6d473ed0abc06dee8'
# haozhu_token = login(user_account,user_key)
# cancelRecv(haozhu_token,'56080','13385178442')


def vertify():
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Origin": "https://h5.happy.xmhuquan.top",
        "Pragma": "no-cache",
        "Referer": "https://h5.happy.xmhuquan.top/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/134.0.0.0"
    }
    url = "https://proxy-api.dingxiang-inc.com/api/a"
    params = {
        "w": "330",
        "h": "165",
        "s": "50",
        "ak": "9579faf11be4029ce75e43771a84929d",
        "c": "67e95c30ZlZnDSEKJxN66CrVZ44te7J3ovy27EX1",
        "jsv": "5.1.49",
        "aid": "dx-1743346946662-99229375-2",
        "wp": "1",
        "de": "0",
        "uid": "",
        "lf": "0",
        "tpc": "",
        "t": "E8D303B4D7857773B638240CBDF414FCA46FBF66C15F9A5F0E7DA909E88BD3877A216D0776A9A81A017C721B722045C888E10BB25ABD2382767B43CF1F573199C7EFD264B27A18B52BDDA45848825300",
        "_r": "0.7078678147231363"
    }
    response = requests.get(url, headers=headers, params=params).json()

    print(response)
    return response.get('t')

def send(mobile,verify_token):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://h5.happy.xmhuquan.top",
        "Pragma": "no-cache",
        "Referer": "https://h5.happy.xmhuquan.top/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/134.0.0.0",
        "token": "7697cd6f-32b5-4b5a-84da-9da72006d1e6"
    }
    url = "https://api.happy.xmhuquan.top/api/sms/send"
    data = {
        "mobile": mobile,
        "event": "register",
        "verify_token": verify_token

    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    if response.json()['msg']=='已被注册':
        phone=豪猪模块.get_phone(haozhu_token,'96067')
        send(phone,verify_token)
        return phone
    print(response.text)
    print(response)
    return mobile