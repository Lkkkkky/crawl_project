'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/3/25 11:21
       @Desc     : 
=========================================================   
'''
import requests
import json
import time
import base64
import threading
from concurrent.futures import ThreadPoolExecutor
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
import generate_device_id
def process_phone(phone):
    session = requests.session()
    ck = login(phone, session)
    ck2 = get_tk(ck, session)
    token = get_nft_token(ck2)
    return token

def login(phone, session):
    headers = {
        "Host": "m.4008117117.com",
        "Pragma": "no-cache",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        # "device-type": "IOS",
        # "guestid": "F208293D766C49A9A792CA8167AE3A58",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Cache-Control": "no-cache",
        "tenantid": "1",
        "User-Agent": "tmall-app/2.0 CFNetwork/1331.0.7 Darwin/21.4.0",
        "Content-Type": "application/json; charset=UTF-8"
    }

    url = "https://m.4008117117.com/api/user/web/login/identify"
    data = {
        "password": "20030531lky",
        "identify": phone,
        "isApp": True,
        # "deviceId": generate_device_id.generate_device_id(),
        # "deviceType": "IOS",
        "androidId": "",
        "deviceMac": "02:00:00:00:00:00",
        "deviceOs": "iOS15.4.1",
        "userAgent": "",
        "deviceSource": "Apple:iPhone 12 Pro",
        # "uuid": "1742300836133_fe2dda9fd53fb34abb78"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = session.post(url, headers=headers, data=data)
    ck = response.cookies.get('draco_local')
    print(f"手机号 {phone} 登录成功，获取到ck: {ck}")
    return ck

def get_tk(ck, session):
    headers = {
        "Host": "m.4008117117.com",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        # "device-type": "IOS",
        # "guestid": "F208293D766C49A9A792CA8167AE3A58",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Cache-Control": "no-cache",
        "tenantid": "1",
        "User-Agent": "tmall-app/2.0 CFNetwork/1331.0.7 Darwin/21.4.0",
        "Pragma": "no-cache"
    }
    cookies = {
        "draco_local": ck,

    }
    url = "https://m.4008117117.com/api/user/web/identify/getEmployee"
    params = {
        "_": str(int(time.time()*1000))
    }
    response = session.get(url, headers=headers, cookies=cookies, params=params)
    ck = response.cookies.get('draco_local')
    print(f"获取到tk: {ck}")
    return ck

def get_nft_token(ck2):
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            headers = {
                "Host": "issue.4008117117.com",
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh-Hans;q=0.9",
                "Content-Type": "application/json",
                "Origin": "https://issue.4008117117.com",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                "Referer": "https://issue.4008117117.com/?t=1742667705757&&token=%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiJkMmJiMDVlYzJiZDIzYjUxM2VlNWNmMjAyZWY1NzY5ZTBmYWFkNzA3OGZjYWI2M2NmZTk3OWFlM2JjY2I1YzA3IiwibmJmIjoxNzQyNjY3Njk5LCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDUyNTk2OTksImlhdCI6MTc0MjY2NzY5OX0.GJqYkbsNmh964oJb5XZXXo_Nzbbzi-4xuQdh0kE-FDE%22&fromType=guangming"
            }

            url = "https://issue.4008117117.com/casting/customerUser/anyone/registerOrLoginByGmToken"
            data = f'{{"gmToken":"\"{ck2}\""}}'

            response = requests.post(url, headers=headers, data=data).json()
            
            if response and 'data' in response and response['data'] and 'token' in response['data']:
                print(f"获取到NFT token: {response['data']['token']}")
                return response['data']['token']
            else:
                print(f"获取NFT token失败，响应数据异常: {response}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
                raise Exception("获取NFT token失败，响应数据不完整")
                
        except Exception as e:
            print(f"获取NFT token出错: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            raise Exception(f"获取NFT token失败，已重试{max_retries}次")
    
    raise Exception("获取NFT token失败，超过最大重试次数")

def main():
    # 从文件读取手机号列表
    with open('成功手机号-sy.txt', 'r') as f:
        phone_numbers = f.read().splitlines()
    
    # 创建线程池
    with ThreadPoolExecutor(max_workers=10) as executor:
        # 提交任务到线程池
        futures = [executor.submit(process_phone, phone) for phone in phone_numbers]
        
        # 获取所有线程的结果
        tokens = [future.result() for future in futures]
        
        print("所有token获取完成：", tokens)

if __name__ == "__main__":
    main()

def get_captcha(tk):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Authorization": tk,
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://issue.4008117117.com",
        "Pragma": "no-cache",
        "Referer": "https://issue.4008117117.com/pages/collectionDetail/collectionBuy?id=34&returnURL=https%3A%2F%2Fissue.4008117117.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
        "X-Requested-With": "com.brightdairy.personal"
    }

    url = "https://issue.4008117117.com/casting/captcha/get"
    data = {
        "captchaType": "clickWord",
        "clientUid": "point-c4236bdf-c6c4-4156-8b67-2ddeff7d3b94",
        "ts": int(time.time()*1000)
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data).json()
    return response['repData']['originalImageBase64'],response['repData']['secretKey'],response['repData']['token'],response['repData']['wordList']

def check(pointJson, token, tk):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Authorization": tk,
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://issue.4008117117.com",
        "Pragma": "no-cache",
        "Referer": "https://issue.4008117117.com/pages/collectionDetail/collectionBuy?id=34&returnURL=https%3A%2F%2Fissue.4008117117.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
        "X-Requested-With": "com.brightdairy.personal"
    }

    url = "https://issue.4008117117.com/casting/captcha/check"
    data = {
        "captchaType": "clickWord",
        "pointJson": pointJson,
        "token": token
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    print(response.text)
    print(response)

def order(encrypted_data, token, tk):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Authorization": tk,
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://issue.4008117117.com",
        "Pragma": "no-cache",
        "Referer": "https://issue.4008117117.com/pages/collectionDetail/collectionBuy?id=34&returnURL=https%3A%2F%2Fissue.4008117117.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
        "X-Requested-With": "com.brightdairy.personal"
    }

    url = "https://issue.4008117117.com/casting/order/create/order"
    data = {
        "validate": encrypted_data,
        "token": token,
        "buyNumber": 1,
        "buyPrice": 199,
        "collectionId": "34",
        "inviteCode": "",
        "orderPrice": 199
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    print(response.text)
    print(response)

def process_phone(phone):
    session = requests.session()
    ck = login(phone, session)
    ck2 = get_tk(ck, session)
    tk = get_nft_token(ck2)
    image,secretKey,token,wordlist = get_captcha(tk)
    loc = verify(image,wordlist)
    converted_loc = convert_coordinates(loc)
    print(converted_loc)
    encrypted_data = aes_encrypt(token+'---'+converted_loc,secretKey)
    pointJson = aes_encrypt(converted_loc,secretKey)
    check(pointJson, token, tk)
    order(encrypted_data, token, tk)
    print(response.text)
    print(response)
image,secretKey,token,wordlist=get_captcha()
loc=verify(image,wordlist)
converted_loc = convert_coordinates(loc)
print(converted_loc)
encrypted_data = aes_encrypt(token+'---'+converted_loc,secretKey)
pointJson=aes_encrypt(converted_loc,secretKey)
check(pointJson, token)
order(encrypted_data,token)