'''
=========================================================    
       @File     : 注册.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/3/30 23:03
       @Desc     : 
=========================================================   
'''
import requests
import 豪猪模块
import json
from loguru import logger

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

def register(mobile,code):
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
    url = "https://api.happy.xmhuquan.top/api/user/register"
    data = {
        "mobile": mobile,
        "password": "00000000ab",
        "code": code,
        "inviter_code": "G646101393"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data).json()

    print(response)
    return response['data']['userinfo']['token']


def realname(phone,token,name,sfz):
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
        "token": token
    }
    url = "https://api.happy.xmhuquan.top/api/user/RealAuthentication"
    data = {
        "real_name": name,
        "id_card": sfz
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    try:
        if response.json()['msg'] == '实名认证成功':
            with open('成功手机号.txt', 'a') as f:
                f.write(f"{phone}\n")
            logger.info(f'手机号{phone}实名认证成功')
    except Exception as e:
        logger.error(f'实名认证响应解析失败: {e}')
    print(response.text)
    print(response)


haozhu_token=豪猪模块.login('db9d44ce09b33035e60f817d368429e124b49f64671f21ed','876bacf58d02fd8080c8fb9a1cb6acb6d473ed0abc06dee8')
def task(name, sfz):
    phone=豪猪模块.get_phone(haozhu_token,'96067')
    ver_token=vertify()
    phone=send(phone, ver_token)
    yzm=豪猪模块.get_yzm(haozhu_token,'96067',phone)
    token=register(phone,yzm)
    realname(phone,token,name,sfz)
   

# 读取lz.txt文件并执行任务
with open('lz.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    if '----' in line:
        name, sfz = line.strip().split('----')
        try:
            task(name, sfz)
        except Exception as e:
            logger.error(f'处理任务失败: {e}')
            continue