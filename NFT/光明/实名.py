'''
=========================================================    
       @File     : TEST.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/3/19 15:21
       @Desc     :
=========================================================
'''
import requests
import json
import time
import execjs
from loguru import logger

session=requests.session()
def login(phone):

    headers = {
        "Host": "m.4008117117.com",
        "Pragma": "no-cache",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        # "device-type": "IOS",
        # "guestid": "F208293D766C49A9A792CA8167AE3A57",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Cache-Control": "no-cache",
        "tenantid": "1",
        "User-Agent": "tmall-app/2.0 CFNetwork/1331.0.7 Darwin/21.4.0",
        "Content-Type": "application/json; charset=UTF-8"
    }

    url = "https://m.4008117117.com/api/user/web/login/identify"
    data = {
        "password": "030109smz",
        "identify": phone,
        "isApp": True,
        # "deviceId": "6436CEBD-C2AC-4A5A-BB40-45154922E6DF",
        "deviceType": "IOS",
        "androidId": "",
        "deviceMac": "02:00:00:00:00:00",
        "deviceOs": "iOS15.4.1",
        "userAgent": "",
        "deviceSource": "Apple:iPhone 12 Pro",
        # "uuid": "1742300836133_fe2dda9fd53fb34abb78"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = session.post(url, headers=headers, data=data)
    ck=response.cookies.get('draco_local')
    print(ck)
    return ck

def get_tk(ck):
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
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    ck = response.cookies.get('draco_local')
    print(ck)
    print(response.text)
    print(response)
    return ck


def get_nft_token(ck2):
    headers = {
        "Host": "issue.4008117117.com",
        "Accept": "*/*",
        # "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhYTc1NTRiYWEyNDNkODA3MjY5NWU3OTUxMGQxNjVkZDM2YWIxMGJiNjkzNjUzNmI2NmJlNjExMWQ1YzU0MDYyMzgyNThhNWFlMzkzOTlkMmVmNThiZGQ3OGU2ZDAwY2M0Yzk1YjhjYTUyOGRkY2U3ODRlMzgxN2M3OTA1MzBmZjYxNDYzNjVkODE4OTg1NmE3ZWE1MGU3MjBiOGUyNzMzMzU1MjQzMzU1NzIwMGQwZTE5MjA1ZTZmNTc4ZDRhZjExNDllZTBlMTA2MGMxYTQzOWI0MDM4NDE2ZTAxMWZhNDg3NDBlMzE3NDMwZTIyNjdhODRmZTliNzNlYTE1Nzg5ZWY5NjlmMmNmN2Q5NWEzMDI3NGM2ODdjMjlkZjVkM2Y5NjMwZWMyZjc4MTQ3NGYzMjk3ZGRjOWYyNWNkNDJhNTljMDFmMWI3NGFiNDhmNzNmZGRkNmU4NTBjNWQ4Mjk2NGY3MzlmMzIyNDZkZGVkYmJkNDRmMGI0OTg2MGZjZDRkMjQ5ZTI1MTIzNWUzYjRiZWQ4NDAwMmNmYzQyOTdjOTkxMTU1N2YxYTFmZmNmY2YxODIyYTA5NDNhNWMxYjk0NzQ3Y2ExZWZhNTljNjZhOTYwYzhlNWVlMGUwM2JiMWIiLCJleHAiOjE3NDI3NTQxMDJ9.N8rpn0vcBCirxgbEV33Hzs8US7MeNh8nOTT_iuBYKMyeMy3B5kIqeY7CpyxkePa7Uwq9g4lB_FoS3c_Tae1-9Q",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://issue.4008117117.com",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Referer": "https://issue.4008117117.com/?t=1742667705757&&token=%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiJkMmJiMDVlYzJiZDIzYjUxM2VlNWNmMjAyZWY1NzY5ZTBmYWFkNzA3OGZjYWI2M2NmZTk3OWFlM2JjY2I1YzA3IiwibmJmIjoxNzQyNjY3Njk5LCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDUyNTk2OTksImlhdCI6MTc0MjY2NzY5OX0.GJqYkbsNmh964oJb5XZXXo_Nzbbzi-4xuQdh0kE-FDE%22&fromType=guangming"
    }

    url = "https://issue.4008117117.com/casting/customerUser/anyone/registerOrLoginByGmToken"
    data= f'{{"gmToken":"\\"{ck2}\\""}}'

    response = requests.post(url, headers=headers, data=data).json()

    # print(response['data']['token'])
    print(response)
    return response['data']['token']


def shiming(token):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Authorization": token,
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-type": "application/json",
        "Origin": "https://issue.4008117117.com",
        "Pragma": "no-cache",
        "Referer": "https://issue.4008117117.com/pages/authentication/authentication?returnUrl=https%3A%2F%2Fissue.4008117117.com%2F%3F%26token%3D%2522eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiI0NDkxOTQ5NDEzODI4NDUyNTk2MjgzNjlmZWQ5YmUxZGQ4Mzg1ODU3ZjNlYWU5NzAwZGY0N2Q4YTk1OTgwYTg4IiwibmJmIjoxNzQyNTUwNjcyLCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDUxNDI2NzIsImlhdCI6MTc0MjU1MDY3Mn0.glGnrmFmJmmWPdjdONYT7t1Th61VaMdqiQncPHhH5CU%2522%26fromType%3Dguangming",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
        "X-Requested-With": "com.brightdairy.personal"
    }
    cookies = {
        "JSESSIONID": "1803A3A397E069B84339D2B80990F2F7",
        "guestId": "dedc56a9-ccb2-4249-acb3-b8b07be9e356",
        "guestId.sig": "W_EO7HqfB7I0zU14SFExSOjX43Y",
        "Hm_lvt_6a5f1ed482525d435338c545ad0e23b4": "1742383611,1742383652",
        "HMACCOUNT": "DDC3E44D29B30C7E",
        "acw_tc": "ac11000117425494399677643e00647f8939aa5bf7bc3e3c763a5f53afdbef",
        "tenantId": "1",
        "draco_local": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiI0NDkxOTQ5NDEzODI4NDUyNTk2MjgzNjlmZWQ5YmUxZGQ4Mzg1ODU3ZjNlYWU5NzAwZGY0N2Q4YTk1OTgwYTg4IiwibmJmIjoxNzQyNTUwNjczLCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDUxNDI2NzMsImlhdCI6MTc0MjU1MDY3M30.Tz0Eqh0vMq2qyZxi2Fe_ouvwQ--WIt9LIFUTIkh_qk0",
        "Hm_lpvt_6a5f1ed482525d435338c545ad0e23b4": "1742550686"
    }
    url = "https://issue.4008117117.com/casting/authentication/realName"
    name='沈铭哲'
    sfz='445122200301093711'
    mobile='13727901673'
    ret = execjs.compile(open('enc.js', 'r', encoding='utf-8').read()).call('enc',name,sfz,mobile)
    data = ret

    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    print(response.text)
    print(response)


def sm():
    with open('成功手机号_未sm_dg.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 去除每行的换行符并存储到数组中
    lines = [line.strip() for line in lines]


    for i in lines:
        ck=login(i)
        ck2=get_tk(ck)
        token=get_nft_token(ck2)
        shiming(token)
        logger.info(i,'----实名成功')


sm()