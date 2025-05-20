'''
=========================================================    
       @File     : 抽签.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/3/21 14:58
       @Desc     : 
=========================================================   
'''
import requests
import json
import time
import csv

from twisted.conch.ssh.session import packRequest_window_change

fi= open('抽签详细_dg.csv',mode='a+',encoding='utf-8',newline='')
# 字典写入
csv_writer=csv.DictWriter(fi,fieldnames=['手机号','密码','签号'])
# 写入表头
# csv_writer.writeheader()
session=requests.session()

def login(phone,password):

    headers = {
        "Host": "m.4008117117.com",
        "Pragma": "no-cache",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "device-type": "IOS",
        "guestid": "F208293D766C49A9A792CA8167AE3A58",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Cache-Control": "no-cache",
        "tenantid": "1",
        "User-Agent": "tmall-app/2.0 CFNetwork/1331.0.7 Darwin/21.4.0",
        "Content-Type": "application/json; charset=UTF-8"
    }

    url = "https://m.4008117117.com/api/user/web/login/identify"
    data = {
        "password":password ,
        "identify": phone,
        "isApp": True,
        "deviceId": "6436CEBD-C2AC-4A5A-BB40-45154922E6DF",
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
    print('登录成功')
    return ck

def get_nft_ck(ck):
    headers = {
        "User-Agent": "okhttp/3.12.1",
        "Connection": "Keep-Alive",
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "x-requested-with": "XMLHttpRequest",
        "guestid": "Z9p+BAWU9cMDABwTOZ0ttPVN",
        "tenantid": "1",
        "device-type": "ANDROID"
    }
    cookies = {
        "acw_tc": "1a0c380917426646979307546e0038a7c1626f3831298ca5182022dd1e2f12",
        "guestId": "52ea773b-ca18-4249-99a6-a3de84b753ff",
        "guestId.sig": "csowDBtDPiopipLwk7Rds3ugOuc",
        "draco_local": ck,
        "tenantId": "1",
        "SESSION": "Y2EyOGI5NWMtOGNmOS00MWE4LWIzZmMtZTI3ZGNmZTUyZGQ2"
    }
    url = "https://m.4008117117.com/api/user/web/identify/getEmployee"
    params = {
        "_": str(int(time.time()*1000))
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(response.cookies)


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
# def changeauth(ck):
#     headers = {
#         "Host": "issue.4008117117.com",
#         "Accept": "*/*",
#         "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
#         "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI3MjhmZjJhYzg3ZmE0ZjhiYzcyYjk2MTFiN2Y0MTJhM2JkOGYxZjk1N2QzMWM1MzZlODdjMjdiZmIyMjRiM2RmMGM3NTI0ODBjZjVlNjIxNTM5OGMzNmNjOTBjYmEwNzMyNTkxMjVhMTM3NTZjNmY2Y2E5ODAxNjJkOWNiMGY2NWNjYjFhZTRhMDVlYTMyMzcxZGZlZWY4YThkZWE2MGRjMzc2NTRkNWY2N2I2ZmFjNWQ2MGVlMzRiNjRlMGNiNjUzM2ViODQ2ZWRiNDU1NTM5ZTIzNDNiMzYyNGYxOTQ4ZDdkYThlY2FkNWQ0ZjkxMGY2ZTUwMDNmZDhkZGRlNTA3YjlhM2Q4YzkzOTNlODAxYmRmYWJlNzMwYTI5MTNlZDMyYzYwYWQ0ZWYzOTVkNTFiYjJlZDgzNDVkZDBiYzE3NDUwYmU5YWNlYjQ3OGI1ZWY4Y2ZhY2QyOGIwMjRiYzY4NjYyMTdjMWUzNzgzMTdiZWU5YWUxODg1NGQ0MTAzOTQ5ZTA2Njk4NTJlZTZiMjU2OWE1YzBjYzg1MmRhM2NjMyIsImV4cCI6MTc0MjYyNjA4M30.yWlZG5Su7YUDo-huga_Ho0M6XvzPob-o-UVfdp3qahlj2BBBcn3N_TZbdLP2pOBXoPu3JVzby92FRFsSGB2k2A",
#         "Referer": "https://issue.4008117117.com/pages/collectionDetail/collectionBuy?id=34&returnURL=https%3A%2F%2Fissue.4008117117.com",
#         "Accept-Language": "zh-CN,zh-Hans;q=0.9"
#     }
#     cookies = {
#         "JSESSIONID": "F728C9D3F3A4FDC092A3A08528511DCF",
#         "Hm_lpvt_6a5f1ed482525d435338c545ad0e23b4": "1742539686",
#         "Hm_lvt_6a5f1ed482525d435338c545ad0e23b4": "1742324264,1742331627,1742375010,1742484788",
#         "draco_local": ck,
#         "tenantId": "1",
#         "guestId": "6f8f4269-d6fb-4c7a-9c9c-eac7874b0da2",
#         "guestId.sig": "m5NUXecwuVhwr7EQV3PA5g5-ljA",
#         "acw_tc": "0a47315217425390619781766e0034dcdbd131c3fc3c7ccdf60e6440e382ad",
#         "HMACCOUNT": "D4C50A6FEB04715B"
#     }
#     url = "https://issue.4008117117.com/casting/customerUser/customerUser"
#     response = session.get(url, headers=headers)
#
#     print(response.text)
#     print(response)

def chouqian(tk):
    headers = {
        "Host": "issue.4008117117.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Authorization": tk,
        "Referer": "https://issue.4008117117.com/pages/collectionDetail/collectionBuy?id=37&returnURL=https%3A%2F%2Fissue.4008117117.com",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9"
    }
    cookies = {
        "JSESSIONID": "72263F3FCC727F40576A2FF810C48F24",
        "Hm_lpvt_6a5f1ed482525d435338c545ad0e23b4": "1745856563",
        "Hm_lvt_6a5f1ed482525d435338c545ad0e23b4": "1744217794,1744464829,1745278844,1745847099",
        "draco_local": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiJiYjVhOTdhMGQxMzQzYzE2ZmNlZGRhMGQ3ODIzMjgyYmZiMzM5NWE1N2QxN2Q3YjA1MTdiY2E3MTcwNjdkMjg1IiwibmJmIjoxNzQ1ODU2NTU2LCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDg0NDg1NTYsImlhdCI6MTc0NTg1NjU1Nn0.1VTidJttnulD1JrQocN2SqNsnG0RLBpuYJvaX421Qe4",
        "tenantId": "1",
        "guestId": "6f8f4269-d6fb-4c7a-9c9c-eac7874b0da2",
        "guestId.sig": "m5NUXecwuVhwr7EQV3PA5g5-ljA",
        "acw_tc": "1a0c399a17458565096836130e007c5e4540fc7a384746c40a82842e93648d",
        "HMACCOUNT": "AD2F251C623B892A"
    }
    url = "https://issue.4008117117.com/casting/collection/reservation/50"
    response = session.get(url, headers=headers).json()

    print(response)
    return response['data']['reservationCode']
#
#

def task():
    with open('抽签详细_dg.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 去除每行的换行符并存储到数组中
        lines = [line.strip() for line in lines]

        for i in lines[1:-1]:
            # print(i)
            phone=i.split(',')[0].strip()
            password=i.split(',')[1].strip()

            ck=login(phone,password)
            get_nft_ck(ck)
            tk=get_nft_token(ck)
            # print(tk)
            # changeauth(ck)
            # num=chouqian(tk)
            check(phone,tk)
            # dict={
            #     '手机号':i,
            #       '密码':password,
            #       '签号':num
            #     }
            # csv_writer.writerow(dict)



def check(phone,tk):

    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Authorization": tk,
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://issue.4008117117.com/pages/collectionDetail/collectionBuy?id=37&returnURL=https%3A%2F%2Fissue.4008117117.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
        "X-Requested-With": "com.brightdairy.personal"
    }
    cookies = {
        "JSESSIONID": "E3D31E31FA2ADDA42D4E8470DD3E61F8",
        "Hm_lvt_6a5f1ed482525d435338c545ad0e23b4": "1745857020",
        "acw_tc": "1a0c39a017459000783126647e0075352cf1eb1bbf0680daf2d13f136528a5",
        "tenantId": "1",
        "guestId": "75b3b1f5-d66e-418d-8e83-b08c4f2da97b",
        "guestId.sig": "Npmj28BgzdymOACgDqdiKTiuOZM",
        "HMACCOUNT": "9E0B7A3C517FA2EB",
        "draco_local": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiJmNmJlMzExYTJhMDE0ODE3M2E4ZDg4ZDI5NGYyZTU1ZmVkMWJmNzJkMzI2MGVjNmJiM2YxMjg4YTA1ZmUzMTU4IiwibmJmIjoxNzQ1OTAwMTE2LCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDg0OTIxMTYsImlhdCI6MTc0NTkwMDExNn0.AKcKQL4T-pWwS9ncSI9a46Cr0g5I2Fk6h1C9Z2RW1bY",
        "Hm_lpvt_6a5f1ed482525d435338c545ad0e23b4": "1745900704"
    }
    url = "https://issue.4008117117.com/casting/collection/anonymous/37"

    response = requests.get(url, headers=headers, cookies=cookies).json()
    if response['data']['reservationStatus']==5:
        print(f'{phone}中签啦')
    # print('查询成功')
task()