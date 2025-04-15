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
session=requests.session()
def login(phone):

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
        "password": "20030531lky",
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
    print(response.text)
    print(response)
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
    print(response)
def registerOrLoginByGmToken(ck):
    headers = {
        "Host": "issue.4008117117.com",
        "Accept": "*/*",
        # "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI4YjAzZTg3YjIzYWNiNGQ1ZWFhZTZhOWZhMGZiNjJiMDY0Yzc0MTViNDgxYmI1ZmQ4YjAzZWE5MWRmMzRlYTcxMmYyMGI5ZDg0MDViNzljYmVhNTAzYWZmOWE1ZjJkY2ZlODBlNzMwZDliMDdhNTNiMGMyYTc0MmZiODJiNjE4YWM4NmQwOTI0OTViNmM5ODRkNjFiMTZjNzQ5MDFjNmExMmVmZTY2NjI3MTVmNzBiMzkzZTU3YjVlODJmMTE4ZjY4NjVkM2VhN2MzYzExYjAyOGY3ODgzOWVkZjg1MjBmZTBlMjlmMmJmZTNlNjM4NmM1ZGM4ZWVkNmNmNjZiZDMzNzE1MTRhOGY4ZmRmYTNhNTNmNTQyMmNkOGM2YjExM2Q3YWM1ZWEyYThjNmZhZTFmN2M1NTE0MzgwZjBiNGVhYzE0ZGIyYmMxMzk3YmU4MDA1OGQ2ZjkwMjNlMjg1MjVjNzM5OGRjNmRiNDFkNTdhOWU3NmQ2ZjQ0NWRlMWU5MDI4ZTE1NjQ2MjhkNzEwNWZmM2IwMGU3MWFlZThiNTgwOWRlMjc2ZDIyOTA1NzdmMGFhMjAxMjA4MWZlN2ZlYTIzMjI2Y2RjZTk2MjI3NTZjZGFkMGMyOGNjNGNkMjM2NmQiLCJleHAiOjE3NDI2MzM3MzB9.JOYy10GjEn2sXbBYSOsXW7wAvrwkspJdAwWt1_3Da0RwqDAUNROnUKiFoqXT0fYWXwvNPZDLxcleL3nvIwU9Rg",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://issue.4008117117.com",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Referer": "https://issue.4008117117.com/?&token=%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiI0NTk1NzIwMTVjYjc5ZWMzYWVkN2FjNDc3NGIxZDg5OTFlMjZiNmQ2ZTY4NjE4MjQ5ZDcwN2U0NmYwNmFmOWVkIiwibmJmIjoxNzQyNTUxNTkyLCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDUxNDM1OTIsImlhdCI6MTc0MjU1MTU5Mn0.tIuTYD5Ywwam4aT9mbeS0jF6BS4C3uQRwKG7OyckVb8%22&fromType=guangming"
    }
    cookies = {
        "JSESSIONID": "126BE96CC5FEFF69EF42547D0B0B3B16",
        "Hm_lpvt_6a5f1ed482525d435338c545ad0e23b4": "1742551596",
        "Hm_lvt_6a5f1ed482525d435338c545ad0e23b4": "1742324264,1742331627,1742375010,1742484788",
        "acw_tc": "1a0c380917425515955581469e003d895fb01aac0e959eb5b75fb4f23762d8",
        "draco_local": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiI0NTk1NzIwMTVjYjc5ZWMzYWVkN2FjNDc3NGIxZDg5OTFlMjZiNmQ2ZTY4NjE4MjQ5ZDcwN2U0NmYwNmFmOWVkIiwibmJmIjoxNzQyNTUxNTkyLCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDUxNDM1OTIsImlhdCI6MTc0MjU1MTU5Mn0.tIuTYD5Ywwam4aT9mbeS0jF6BS4C3uQRwKG7OyckVb8",
        "guestId": "6f8f4269-d6fb-4c7a-9c9c-eac7874b0da2",
        "guestId.sig": "m5NUXecwuVhwr7EQV3PA5g5-ljA",
        "tenantId": "1",
        "HMACCOUNT": "D4C50A6FEB04715B"
    }
    url = "https://issue.4008117117.com/casting/customerUser/anyone/registerOrLoginByGmToken"
    data = {"gmToken":ck}
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    print(response.text)
    print(response)
def changeauth(ck):
    headers = {
        "Host": "issue.4008117117.com",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI3MjhmZjJhYzg3ZmE0ZjhiYzcyYjk2MTFiN2Y0MTJhM2JkOGYxZjk1N2QzMWM1MzZlODdjMjdiZmIyMjRiM2RmMGM3NTI0ODBjZjVlNjIxNTM5OGMzNmNjOTBjYmEwNzMyNTkxMjVhMTM3NTZjNmY2Y2E5ODAxNjJkOWNiMGY2NWNjYjFhZTRhMDVlYTMyMzcxZGZlZWY4YThkZWE2MGRjMzc2NTRkNWY2N2I2ZmFjNWQ2MGVlMzRiNjRlMGNiNjUzM2ViODQ2ZWRiNDU1NTM5ZTIzNDNiMzYyNGYxOTQ4ZDdkYThlY2FkNWQ0ZjkxMGY2ZTUwMDNmZDhkZGRlNTA3YjlhM2Q4YzkzOTNlODAxYmRmYWJlNzMwYTI5MTNlZDMyYzYwYWQ0ZWYzOTVkNTFiYjJlZDgzNDVkZDBiYzE3NDUwYmU5YWNlYjQ3OGI1ZWY4Y2ZhY2QyOGIwMjRiYzY4NjYyMTdjMWUzNzgzMTdiZWU5YWUxODg1NGQ0MTAzOTQ5ZTA2Njk4NTJlZTZiMjU2OWE1YzBjYzg1MmRhM2NjMyIsImV4cCI6MTc0MjYyNjA4M30.yWlZG5Su7YUDo-huga_Ho0M6XvzPob-o-UVfdp3qahlj2BBBcn3N_TZbdLP2pOBXoPu3JVzby92FRFsSGB2k2A",
        "Referer": "https://issue.4008117117.com/pages/collectionDetail/collectionBuy?id=34&returnURL=https%3A%2F%2Fissue.4008117117.com",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9"
    }
    cookies = {
        "JSESSIONID": "F728C9D3F3A4FDC092A3A08528511DCF",
        "Hm_lpvt_6a5f1ed482525d435338c545ad0e23b4": "1742539686",
        "Hm_lvt_6a5f1ed482525d435338c545ad0e23b4": "1742324264,1742331627,1742375010,1742484788",
        "draco_local": ck,
        "tenantId": "1",
        "guestId": "6f8f4269-d6fb-4c7a-9c9c-eac7874b0da2",
        "guestId.sig": "m5NUXecwuVhwr7EQV3PA5g5-ljA",
        "acw_tc": "0a47315217425390619781766e0034dcdbd131c3fc3c7ccdf60e6440e382ad",
        "HMACCOUNT": "D4C50A6FEB04715B"
    }
    url = "https://issue.4008117117.com/casting/customerUser/customerUser"
    response = session.get(url, headers=headers)

    print(response.text)
    print(response)



def chouqian():
    headers = {
        "Host": "issue.4008117117.com",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI4YzdjZjljZThmYWViZTlkMjJlMjZjMzEzMDBhNTI2ODY0Yzc0MTViNDgxYmI1ZmQ4YjAzZWE5MWRmMzRlYTcxMmYyMGI5ZDg0MDViNzljYmVhNTAzYWZmOWE1ZjJkY2ZlODBlNzMwZDliMDdhNTNiMGMyYTc0MmZiODJiNjE4YWM4NmQwOTI0OTViNmM5ODRkNjFiMTZjNzQ5MDFjNmExMmVmZTY2NjI3MTVmNzBiMzkzZTU3YjVlODJmMTE4ZjY4NjVkM2VhN2MzYzExYjAyOGY3ODgzOWVkZjg1MjBmZTBlMjlmMmJmZTNlNjM4NmM1ZGM4ZWVkNmNmNjZiZDMzNzE1MTRhOGY4ZmRmYTNhNTNmNTQyMmNkOGM2YjExM2Q3YWM1ZWEyYThjNmZhZTFmN2M1NTE0MzgwZjBiNGVhYzE0ZGIyYmMxMzk3YmU4MDA1OGQ2ZjkwMjNlMjg1MjVjNzM5OGRjNmRiNDFkNTdhOWU3NmQ2ZjQ0NWRlMWU5MDJhNTE2NzIyNzQyNWQ0NzJkNjc4OTEzNzkzOTJhNTg5OTRlY2JjNzk4MjhmZDE4NWUxNTA3MWY1Mzc5NGIyNTViNmE3YzM3OGU0ZDU0ZmMxNDAzNTU5ZTc2NTg2MGNiNGIiLCJleHAiOjE3NDI2MzczMjN9.p4zd_Mu93-Tlkkv9aR_n13YzUlZ0xdlaXN80Lchrry3l7jNg58Q6DYWvi5_RM2Y-mVcaIZMlQDhRmx77rsJg0A",
        "Referer": "https://issue.4008117117.com/pages/collectionDetail/collectionBuy?id=34&returnURL=https%3A%2F%2Fissue.4008117117.com",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9"
    }

    url = "https://issue.4008117117.com/casting/collection/reservation/37"
    response = session.get(url, headers=headers)

    print(response.text)
    print(response)


#
#
ck=login('19220214835')
get_nft_ck(ck)
registerOrLoginByGmToken(ck)
# changeauth(ck)
# chouqian()

