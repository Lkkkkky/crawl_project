import time
import requests
import ddddocr
import json
import 豪猪模块
from loguru import logger
import sys
import os

# 添加全局计数器
failure_count = 0

pwd='20030531lky'

def get_captcha():
    headers = {
        "Host": "m.4008117117.com",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "device-type": "IOS",
        "Accept-Encoding": "gzip, deflate, br",
        "guestid": "F208293D766C49A9A792CA8167AE3A58",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Cache-Control": "no-cache",
        "tenantid": "1",
        "User-Agent": "tmall-app/2.0 CFNetwork/1331.0.7 Darwin/21.4.0",
        "Connection": "keep-alive",
        "Pragma": "no-cache"
    }
    cookies = {
        "SESSION": "MWVkMjBiZDItOGUyNi00YzhhLTkxMGMtOTI4NjBiNTMxYzcx",
        "guestId": "6f8f4269-d6fb-4c7a-9c9c-eac7874b0da2",
        "guestId.sig": "m5NUXecwuVhwr7EQV3PA5g5-ljA",
        "acw_tc": "1a0c399d17423128693386495e00402e1e93007e19758cc0575cf9431b6511"
    }
    url = "https://m.4008117117.com/api/user/web/get-captcha"
    params = {
        "_": "1742313024749"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    # logger.info(response.text)
    return response.json()['data']['token'],response.json()['data']['imageUrl']

def sms_send(token,image,phone):
    global failure_count
    image = image.split('data:image/png;base64,')[1]
    ocr = ddddocr.DdddOcr(det=False, show_ad=False)
    code = ocr.classification(image)
    logger.info(code)
    headers = {
        "Host": "m.4008117117.com",
        "Pragma": "no-cache",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "device-type": "IOS",
        "guestid": "F208293D766C49A9A792CA8167AE3A58",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Cache-Control": "no-cache",
        "Accept-Encoding": "gzip, deflate, br",
        "tenantid": "1",
        "Content-Length": "88",
        "User-Agent": "tmall-app/2.0 CFNetwork/1331.0.7 Darwin/21.4.0",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=UTF-8"
    }
    cookies = {
        "SESSION": "MWVkMjBiZDItOGUyNi00YzhhLTkxMGMtOTI4NjBiNTMxYzcx",
        "guestId": "6f8f4269-d6fb-4c7a-9c9c-eac7874b0da2",
        "guestId.sig": "m5NUXecwuVhwr7EQV3PA5g5-ljA",
        "acw_tc": "1a0c399d17423128693386495e00402e1e93007e19758cc0575cf9431b6511"
    }
    url = "https://m.4008117117.com/api/user/web/login/login-send-sms-code"
    data = {
        "captcha": code,
        "token": token,
        "mobile": phone
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data).json()
    if(response.get("success") == True):
        logger.info('注册验证码发送成功！')
        failure_count = 0
        return
    else:
        logger.info('发送验证码失败,正在重试')
        failure_count += 1  # 增加失败计数
        if failure_count >= 5:
            failure_count=0 # 重置计数器
            logger.info('连续失败5次，重启脚本')
            python = sys.executable
            os.execv(python)
        time.sleep(10)
        captcha_token,image=get_captcha()
        sms_send(captcha_token,image,phone)
        return

#注册账号
def login(phone,sms_code):
    headers = {
        "Host": "m.4008117117.com",
        "Pragma": "no-cache",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "device-type": "IOS",
        "guestid": "F208293D766C49A9A792CA8167AE3A58",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Cache-Control": "no-cache",
        "Accept-Encoding": "gzip, deflate, br",
        "tenantid": "1",
        "Content-Length": "289",
        "User-Agent": "tmall-app/2.0 CFNetwork/1331.0.7 Darwin/21.4.0",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=UTF-8"
    }
    cookies = {
        "SESSION": "MWVkMjBiZDItOGUyNi00YzhhLTkxMGMtOTI4NjBiNTMxYzcx",
        "guestId": "6f8f4269-d6fb-4c7a-9c9c-eac7874b0da2",
        "guestId.sig": "m5NUXecwuVhwr7EQV3PA5g5-ljA",
        "acw_tc": "1a0c399d17423128693386495e00402e1e93007e19758cc0575cf9431b6511"
    }
    url = "https://m.4008117117.com/api/user/web/login/login-by-sms-code"
    data = {
        "mobile": phone,
        "smsCode": sms_code,
        "app": True,
        "deviceId": "6436CEBD-C2AC-4A5A-BB40-45154922E6DF",
        "deviceType": "IOS",
        "androidId": "",
        "deviceMac": "02:00:00:00:00:00",
        "deviceOs": "iOS15.4.1",
        "userAgent": "",
        "deviceSource": "Apple:iPhone 12 Pro",
        "uuid": "1742300836133_fe2dda9fd53fb34abb78"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    # logger.info(response.text)

def get_captcha_setpwd():
    headers = {
        "Host": "m.4008117117.com",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "device-type": "IOS",
        "Accept-Encoding": "gzip, deflate, br",
        "guestid": "F208293D766C49A9A792CA8167AE3A58",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Cache-Control": "no-cache",
        "tenantid": "1",
        "User-Agent": "tmall-app/2.0 CFNetwork/1331.0.7 Darwin/21.4.0",
        "Connection": "keep-alive",
        "Pragma": "no-cache"
    }
    cookies = {
        "draco_local": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiI5OWI4MGZkMzZhNTc0Zjg4ODgyODYxYzA5OGUzNTI4MDNmYzZjYzJlN2IxNDZkNDg3NDljNzA4MzVlYmNiYmEzIiwibmJmIjoxNzQyMzE0NTc5LCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDQ5MDY1NzksImlhdCI6MTc0MjMxNDU3OX0.MWAUMTlSfDV2qyJh2_jTPNHyauurobRrAB-JT4zw2N8",
        "tenantId": "1",
        "SESSION": "NWQ3NzUwNmEtZTRiNi00NDNjLTkyOTgtMmU0ZmFhM2UwM2Qz",
        "guestId": "6f8f4269-d6fb-4c7a-9c9c-eac7874b0da2",
        "guestId.sig": "m5NUXecwuVhwr7EQV3PA5g5-ljA",
        "acw_tc": "1a0c399d17423128693386495e00402e1e93007e19758cc0575cf9431b6511"
    }
    url = "https://m.4008117117.com/api/user/web/get-captcha"
    params = {
        "_": "1742314588373"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    # print(response.text)
    return response.json()['data']['token'], response.json()['data']['imageUrl']

def sms_send_setpwd(token,image,phone):
    image = image.split('data:image/png;base64,')[1]
    ocr = ddddocr.DdddOcr(det=False, show_ad=False)
    code = ocr.classification(image)
    logger.info(code)
    headers = {
        "Host": "m.4008117117.com",
        "Pragma": "no-cache",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "device-type": "IOS",
        "guestid": "F208293D766C49A9A792CA8167AE3A58",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Cache-Control": "no-cache",
        "Accept-Encoding": "gzip, deflate, br",
        "tenantid": "1",
        "Content-Length": "88",
        "User-Agent": "tmall-app/2.0 CFNetwork/1331.0.7 Darwin/21.4.0",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=UTF-8"
    }
    cookies = {
        "draco_local": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiI5OWI4MGZkMzZhNTc0Zjg4ODgyODYxYzA5OGUzNTI4MDNmYzZjYzJlN2IxNDZkNDg3NDljNzA4MzVlYmNiYmEzIiwibmJmIjoxNzQyMzE0NTg4LCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDQ5MDY1ODgsImlhdCI6MTc0MjMxNDU4OH0.6doQXlF4ksh1pe9HpO5hkeR3rtDhkY5xFAX1mTvxckY",
        "tenantId": "1",
        "SESSION": "NWQ3NzUwNmEtZTRiNi00NDNjLTkyOTgtMmU0ZmFhM2UwM2Qz",
        "guestId": "6f8f4269-d6fb-4c7a-9c9c-eac7874b0da2",
        "guestId.sig": "m5NUXecwuVhwr7EQV3PA5g5-ljA",
        "acw_tc": "1a0c399d17423128693386495e00402e1e93007e19758cc0575cf9431b6511"
    }
    url = "https://m.4008117117.com/api/user/web/password/send-sms"
    data = {
        "captcha": code,
        "token": token,
        "mobile": phone
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data).json()
    logger.info(response)
    if (response.get("success") == True):
        logger.info('重置密码验证码发送成功！')
        return
    else:
        logger.info('发送重置密码验证码失败,正在重试')
        time.sleep(10)
        setpwd_captcha_token,setpwd_image = get_captcha_setpwd()
        sms_send_setpwd(setpwd_captcha_token,setpwd_image, phone)
        return

#重置密码
def setpwd(sms_code,phone):
    headers = {
        "Host": "m.4008117117.com",
        "Pragma": "no-cache",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "device-type": "IOS",
        "guestid": "F208293D766C49A9A792CA8167AE3A58",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Cache-Control": "no-cache",
        "Accept-Encoding": "gzip, deflate, br",
        "tenantid": "1",
        "Content-Length": "92",
        "User-Agent": "tmall-app/2.0 CFNetwork/1331.0.7 Darwin/21.4.0",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=UTF-8"
    }
    cookies = {
        "draco_local": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiI5OWI4MGZkMzZhNTc0Zjg4ODgyODYxYzA5OGUzNTI4MDNmYzZjYzJlN2IxNDZkNDg3NDljNzA4MzVlYmNiYmEzIiwibmJmIjoxNzQyMzE0NTg4LCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDQ5MDY1ODgsImlhdCI6MTc0MjMxNDU4OH0.6doQXlF4ksh1pe9HpO5hkeR3rtDhkY5xFAX1mTvxckY",
        "tenantId": "1",
        "SESSION": "NWQ3NzUwNmEtZTRiNi00NDNjLTkyOTgtMmU0ZmFhM2UwM2Qz",
        "guestId": "6f8f4269-d6fb-4c7a-9c9c-eac7874b0da2",
        "guestId.sig": "m5NUXecwuVhwr7EQV3PA5g5-ljA",
        "acw_tc": "1a0c399d17423128693386495e00402e1e93007e19758cc0575cf9431b6511"
    }
    url = "https://m.4008117117.com/api/user/web/password/reset-by-sms"
    data = {
        "mobile": phone,
        "smsCode": sms_code,
        "password": pwd,
        "confirm": pwd
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    logger.info(response.text)
    
    # 检查响应内容是否为{"data":true,"success":true}
    try:
        resp_json = response.json()
        if resp_json.get("data") == True and resp_json.get("success") == True:
            requests.get('https://api.day.app/YToREckaeQXotQJPrn7MWa/做号成功！！！！！')
            logger.info(f"手机号 {phone} 重置密码成功，保存到文件")
            # 将成功的手机号保存到txt文件
            with open("成功手机号-sy.txt", "a") as f:
                f.write(f"{phone}\n")
    except Exception as e:
        logger.error(f"解析响应失败: {e}")
user_account='db9d44ce09b33035e60f817d368429e124b49f64671f21ed'
user_key='876bacf58d02fd8080c8fb9a1cb6acb6d473ed0abc06dee8'
haozhu_token = 豪猪模块.login(user_account,user_key)
with open('成功手机号_实名.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

cnt=500
for i in range(cnt):
    try:
        # 注册
        phone=豪猪模块.get_phone(haozhu_token,'56080')
        if phone in lines:
            logger.info('手机号已存在,重新获取')
            continue
        captcha_token,image=get_captcha()
        sms_send(captcha_token,image,phone)
        yzm=豪猪模块.get_yzm(haozhu_token,'56080',phone)
        login(phone,yzm)
        #改密
        time.sleep(30)
        # phone='19260296922'
        豪猪模块.get_phone_zhiding(haozhu_token,'56080',phone)
        setpwd_captcha_token,setpwd_image=get_captcha_setpwd()
        sms_send_setpwd(setpwd_captcha_token,setpwd_image,phone)
        setpwd_yzm=豪猪模块.get_yzm_no(haozhu_token,'56080',phone)
        setpwd(setpwd_yzm,phone)
    except :
        time.sleep(10)