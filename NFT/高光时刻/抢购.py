'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/1/23 16:19
       @Desc     : 
=========================================================   
'''
import requests
import json
import time
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Random import get_random_bytes

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjNzE5NzRlYmVjNTFjNDEyMmZlODJiMTE0MTZkMmRhYWI1YzI5N2YyZThmODVjNjBmNmRjZWMyMWYzZDMyYjU3M2Y1YTcwMjNjYjQwZTJlNjE3ZTAyMjEzY2QxZWQ2OWJhMTJlNjNmYjM2OGM2NWY3YTg3NGVmMzI5ZTRhODk5Y2JiZjgyMjgzNjVhM2Y1ZjkxMzgzYzVmYmVjYjUyYTA2NzVhZjgyODZmM2Q5MGI5OWU2OTM3YjBiMTY1ODYwYmVhMTQzMmQ4Yjg2OTMwM2U1NWY1YjllNTA1N2E1MTUyMGNkZmNiMmMyODY3ZmUxMDE0MjY4ODE2NWI1MDMwMWYxODkyNzE2YzM1ZGNiZGFjZGE4MWQ4MGRiZTAyZDZjMmNhYmRjYmFiMzFkNWRlZTFmZTdiZTk4NjhkMTc5NzNkOTRjYjNhZDZmNzRmMDRkZTRmZDVlNGVkNmRjMDkzNWJhODhhODczMWE0MmU1ODk2Y2I4NDQ5NzliNGQxN2YzZGFjY2I5ZDU2OWE1YzA4NzBiMjQzODAzMzU3YTg0NmU1NGUwNzQ0ZTE4ZTc5ZTRkNDBhY2E2MjFlZGQ0MTA5N2U2IiwiZXhwIjoxNzM3NzAzODg1fQ.MsHzAcZ6fONNo_XWfthAZsmwtn9CyX7-KeypB-0AsyZMll7fQXYrCqg5SolR3t7ULRgP0vqlUm-jifgVGDTMHA",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://collection.zamplus.com",
    "Pragma": "no-cache",
    "Referer": "https://collection.zamplus.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Microsoft Edge\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://collection-captcha-auth.zamplus.com/captcha/get"
data = {
    "captchaType": "clickWord",
    "clientUid": "point-51e9dba8-eb74-4a89-979e-192664efa460",
    "ts": int(time.time()*1000)
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data).json()
img_b64=response['repData']['originalImageBase64']
wordList=response['repData']['wordList']
token=response['repData']['token']
secretKey=response['repData']['secretKey']
# print(img_b64)
print(wordList)




b = img_b64  ## 图片二进制流base64字符串

def verify():
    url = "http://api.jfbym.com/api/YmServer/customApi"
    data = {
        ## 关于参数,一般来说有3个;不同类型id可能有不同的参数个数和参数名,找客服获取
        "token": 'RALIiXl3wn4_i_C9OCaaBmDnNhWDn_NpoK6VbkGa7To',
        "type": "30100",
        "image": b,
        'extra':','.join(wordList)
    }
    _headers = {
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, headers=_headers, json=data).json()
    loc=response['data']['data']
    print(response)
    return loc


def aes_encrypt(data, key):
    # 确保密钥长度为16字节
    key = key.encode('utf-8')
    # 将数据转为字节，并进行PKCS7填充
    data = data.encode('utf-8')
    data = pad(data, AES.block_size)
    # 使用AES加密（ECB模式）
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(data)
    # 返回加密后的数据，进行base64编码
    return base64.b64encode(encrypted).decode('utf-8')

# 使用示例

def convert_coordinates(coord_str):
    # 以'|'分割坐标对
    coord_pairs = coord_str.split('|')

    # 生成目标格式的坐标字典列表
    result = []
    for pair in coord_pairs:
        x, y = map(int, pair.split(','))
        result.append({"x": x, "y": y})

    # 使用json.dumps将列表转化为JSON字符串，并去掉空格
    return json.dumps(result, separators=(',', ':'))



loc=verify()
converted_loc = convert_coordinates(loc)

encrypted_data = aes_encrypt(token+'---'+converted_loc,secretKey)
pointJson=aes_encrypt(converted_loc,secretKey)
print(encrypted_data)

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjNzE5NzRlYmVjNTFjNDEyMmZlODJiMTE0MTZkMmRhYWI1YzI5N2YyZThmODVjNjBmNmRjZWMyMWYzZDMyYjU3M2Y1YTcwMjNjYjQwZTJlNjE3ZTAyMjEzY2QxZWQ2OWJhMTJlNjNmYjM2OGM2NWY3YTg3NGVmMzI5ZTRhODk5Y2JiZjgyMjgzNjVhM2Y1ZjkxMzgzYzVmYmVjYjUyYTA2NzVhZjgyODZmM2Q5MGI5OWU2OTM3YjBiMTY1ODYwYmVhMTQzMmQ4Yjg2OTMwM2U1NWY1YjllNTA1N2E1MTUyMGNkZmNiMmMyODY3ZmUxMDE0MjY4ODE2NWI1MDMwMWYxODkyNzE2YzM1ZGNiZGFjZGE4MWQ4MGRiZTAyZDZjMmNhYmRjYmFiMzFkNWRlZTFmZTdiZTk4NjhkMTc5NzNkOTRjYjNhZDZmNzRmMDRkZTRmZDVlNGVkNmRjMDkzNWJhODhhODczMWE0MmU1ODk2Y2I4NDQ5NzliNGQxN2YzZGFjY2I5ZDU2OWE1YzA4NzBiMjQzODAzMzU3YTg0NmU1NGUwNzQ0ZTE4ZTc5ZTRkNDBhY2E2MjFlZGQ0MTA5N2U2IiwiZXhwIjoxNzM3NzAzODg1fQ.MsHzAcZ6fONNo_XWfthAZsmwtn9CyX7-KeypB-0AsyZMll7fQXYrCqg5SolR3t7ULRgP0vqlUm-jifgVGDTMHA",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://collection.zamplus.com",
    "Pragma": "no-cache",
    "Referer": "https://collection.zamplus.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Microsoft Edge\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://collection-captcha-auth.zamplus.com/captcha/check"
data = {
    "captchaType": "clickWord",
    "pointJson": pointJson,
    "token": token
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjNzE5NzRlYmVjNTFjNDEyMmZlODJiMTE0MTZkMmRhYWI1YzI5N2YyZThmODVjNjBmNmRjZWMyMWYzZDMyYjU3M2Y1YTcwMjNjYjQwZTJlNjE3ZTAyMjEzY2QxZWQ2OWJhMTJlNjNmYjM2OGM2NWY3YTg3NGVmMzI5ZTRhODk5Y2JiZjgyMjgzNjVhM2Y1ZjkxMzgzYzVmYmVjYjUyYTA2NzVhZjgyODZmM2Q5MGI5OWU2OTM3YjBiMTY1ODYwYmVhMTQzMmQ4Yjg2OTMwM2U1NWY1YjllNTA1N2E1MTUyMGNkZmNiMmMyODY3ZmUxMDE0MjY4ODE2NWI1MDMwMWYxODkyNzE2YzM1ZGNiZGFjZGE4MWQ4MGRiZTAyZDZjMmNhYmRjYmFiMzFkNWRlZTFmZTdiZTk4NjhkMTc5NzNkOTRjYjNhZDZmNzRmMDRkZTRmZDVlNGVkNmRjMDkzNWJhODhhODczMWE0MmU1ODk2Y2I4NDQ5NzliNGQxN2YzZGFjY2I5ZDU2OWE1YzA4NzBiMjQzODAzMzU3YTg0NmU1NGUwNzQ0ZTE4ZTc5ZTRkNDBhY2E2MjFlZGQ0MTA5N2U2IiwiZXhwIjoxNzM3NzAzODg1fQ.MsHzAcZ6fONNo_XWfthAZsmwtn9CyX7-KeypB-0AsyZMll7fQXYrCqg5SolR3t7ULRgP0vqlUm-jifgVGDTMHA",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://collection.zamplus.com",
    "Pragma": "no-cache",
    "Referer": "https://collection.zamplus.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Microsoft Edge\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "Hm_lvt_6a5f1ed482525d435338c545ad0e23b4": "1737617241",
    "HMACCOUNT": "4D4F61CE5656C745",
    "token": "Bearer%20eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjNzE5NzRlYmVjNTFjNDEyMmZlODJiMTE0MTZkMmRhYWI1YzI5N2YyZThmODVjNjBmNmRjZWMyMWYzZDMyYjU3M2Y1YTcwMjNjYjQwZTJlNjE3ZTAyMjEzY2QxZWQ2OWJhMTJlNjNmYjM2OGM2NWY3YTg3NGVmMzI5ZTRhODk5Y2JiZjgyMjgzNjVhM2Y1ZjkxMzgzYzVmYmVjYjUyYTA2NzVhZjgyODZmM2Q5MGI5OWU2OTM3YjBiMTY1ODYwYmVhMTQzMmQ4Yjg2OTMwM2U1NWY1YjllNTA1N2E1MTUyMGNkZmNiMmMyODY3ZmUxMDE0MjY4ODE2NWI1MDMwMWYxODkyNzE2YzM1ZGNiZGFjZGE4MWQ4MGRiZTAyZDZjMmNhYmRjYmFiMzFkNWRlZTFmZTdiZTk4NjhkMTc5NzNkOTRjYjNhZDZmNzRmMDRkZTRmZDVlNGVkNmRjMDkzNWJhODhhODczMWE0MmU1ODk2Y2I4NDQ5NzliNGQxN2YzZGFjY2I5ZDU2OWE1YzA4NzBiMjQzODAzMzU3YTg0NmU1NGUwNzQ0ZTE4ZTc5ZTRkNDBhY2E2MjFlZGQ0MTA5N2U2IiwiZXhwIjoxNzM3NzAzODg1fQ.MsHzAcZ6fONNo_XWfthAZsmwtn9CyX7-KeypB-0AsyZMll7fQXYrCqg5SolR3t7ULRgP0vqlUm-jifgVGDTMHA",
    "Hm_lpvt_6a5f1ed482525d435338c545ad0e23b4": "1737618390"
}
url = "https://collection.zamplus.com/api/trade/order/create/order"
data = {
    "validate": encrypted_data,
    "token": token,
    "buyNumber": 1,
    "buyPrice": 168,
    "collectionId": "716",
    "inviteCode": "",
    "orderPrice": 168
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)



