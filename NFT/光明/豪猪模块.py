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
    response = requests.get(f'https://api.haozhuma.com/sms/?api=getPhone&token={token}&sid={item_id}&uid=56080-BZ3VPZ1B0B')#只取实卡
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
    for i in range(60):  # 将循环次数从100改为60
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
    return get_yzm(token, item_id, new_phone)  # 递归调用自身重新获取
#释放全部
def cancelRecv(token):
    res=requests.get(f'https://api.haozhuma.com/sms/?api=cancelRecv&token={token}')
    print(res.text)
#如果不来码  不再重新获取
def get_yzm_no(token,item_id,phone):
    for i in range(60):  # 将循环次数从100改为60
        response = requests.get(f'https://api.haozhuma.com/sms/?api=getMessage&token={token}&sid={item_id}&phone={phone}&uid=56080-BZ3VPZ1B0B')#只取实卡
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