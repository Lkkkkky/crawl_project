'''
  @File     : 抢购.py
  @IDE      : IntelliJ IDEA
  @Author   : Jing3
  @Date     : 2024/10/8 3:42
'''

import requests
import execjs
import hashlib
import time
import re
import json
import subprocess
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.jd.com/",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
cookies = {
    "__jdu": "1468058068",
    "shshshfpa": "c273795a-d734-cfaa-ce50-9d031a6538ec-1700461744",
    "shshshfpx": "c273795a-d734-cfaa-ce50-9d031a6538ec-1700461744",
    "areaId": "19",
    "user-key": "e2c2f1c9-05f5-4953-b352-b9dad9179828",
    "ipLoc-djd": "19-1601-50258-62836",
    "_pst": "jd_MhNyBaXRXFnl",
    "unick": "lkyyyyyyyyyyy",
    "pin": "jd_MhNyBaXRXFnl",
    "_tp": "LckDemJZ9vjD7CXeUJhnPA%3D%3D",
    "mt_xid": "V2_52007VwMXVVRZVlMeThBsBW4LRQAOX1RGHk4bXxliUxBQQVECXhxVEQgCZgUTVlkIAllPeRpdBmIfElNBW1NLH04SXwRsAxBiX2hRahxIH1QAYjMRVV1e",
    "autoOpenApp_downCloseDate_auto": "1729446478007_1800000",
    "PCSYCityID": "CN_440000_440100_0",
    "TrackID": "1Qea09rv2vI6b9d_sX6efCjXMzHP0SVPYsMQwy0EKasEmqwnrna_P90FmBJQLY7J6rVRmF8mH2N6dekbImCUpnArGfRgMo0yujCHzRpzU6dBnE51nkeeHCkcSJJKoGriL",
    "light_key": "AASBKE7rOxgWQziEhC_QY6yauEGIs-waHyn8jTWHTwGQGR5AHe5-eSXSUUgh9DXqK93nhvqJ",
    "pinId": "8iMjBrpr1TnSWYxYoJoW6g",
    "unpl": "JF8EAJpnNSttDBgEDR9QHxcTQ1xXWw4KTkdXZm8MV11cGFMCT1AbQBh7XlVdWBRLFx9uZBRUXlNJVA4YAisSEXteU11bD00VB2xXVgQFDQ8WUUtBSUt-S1tXV1QOSh4AbGYDZG1bS2QFGjIbFxdCXFBXXA9CJwJfYDVkbV1MUAUaASsTIEptFgoBAU4SCmdvSFRYX0JVARIDHBsgSm1X",
    "3AB9D23F7A4B3CSS": "jdd03SHHR7HCVAO4D4OCSDSIWSXEE4MOIEPIUNLGHXXVVANTJVFYEPODQK76V7LLAH4AWCTIWGK2SSONE362YELGJVYGV24AAAAMS5MSHCVQAAAAADD37XZ2HQCLR2EX",
    "_gia_d": "1",
    "thor": "1F63723E3B0B854D9454AB8BE6A4EAB5D6AE0AE74007F05D682072A2346EEFEAFA58CFF5080DA29DA4FBD50C91050B5E11D1350A2A0C383890D5B7B3E8D7C2EE66C51AB5A2E76D0CBAAD6118896E517CBD5D3D15B9051A386208E5D026C06F972EBA764C951A2F193CE93220F9B23AA9E9BF25E407B69585CA8562A9B234949DB4AD78711535D78A7C95470C76C03E6FA829C18F4D55C7A350ABD2FFE8239D49",
    "__jda": "76161171.1468058068.1728325094.1730521884.1730521915.19",
    "__jdc": "76161171",
    "__jdv": "76161171|baidu|-|organic|notset|1730521915042",
    "__jdb": "76161171.2.1468058068|19.1730521915",
    "flash": "3_qENzdjQAle7QjmfaSEGb-0vI1U43j6W_os-WKcaoTL0RlphIk_zZV9sHZM1L76ZJJG26UJhWmjiC7o8RC9fpK2V5VFqBodRxdReyA0JOa6IaCojf9lUKw6UwN6wxi3Nnk2mwjEW5NG-z4Q5y2bDpLDlUdeRJEKkN4CnKErFsFNWOlV**",
    "3AB9D23F7A4B3C9B": "SHHR7HCVAO4D4OCSDSIWSXEE4MOIEPIUNLGHXXVVANTJVFYEPODQK76V7LLAH4AWCTIWGK2SSONE362YELGJVYGV24",
    "umc_count": "1",
    "shshshfpb": "BApXSVpgt6PdAhddKJXMhHnyZ9HSho4k2BkIHEGtj9xJ1MvT02IO2"
}
url = "https://api.m.jd.com/"
def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()
def get_goods_list():
    t = int(time.time() * 1000)
    params = {
        "appid": "www-jd-com",
        "body": "{\"page\":0,\"pagesize\":25,\"area\":\"19_1601_50258_129167\",\"source\":\"pc-home\"}",
        "clientVersion": "1.0.0",
        "client": "pc",
        "functionId": "pc_home_feed",
        "t": str(t),
        "uuid": "76161171.369041817.1728735580.1730534902.1730537892.7",
        "loginType": "3",
        "x-api-eid-token": "jdd03IP7ZOEW6HMAOR2YF23KYRWMTUEY6WE6YJCO4HO45KAOUDW75RJ6AXP3E73LX34Z3DYL6ZVYZKZQ2OLMLEB35CY63C4AAAAMS5QMKRTYAAAAADR3LD4JC6XONFAX",
        "callback": "jsonpMore2Goods",
        "_": str(t)
    }
    data = {
        "appid": "www-jd-com",
        "body": sha256(params['body']),
        "clientVersion": "1.0.0",
        "client": "pc",
        "functionId": "pc_home_feed",
        "t": t
    }
    for t in range(2):
        params['body']="{\"page\":" + str(t) + ",\"pagesize\":25,\"area\":\"19_1601_50258_129167\",\"source\":\"pc-home\"}"
        data['body']=sha256(params['body'])
        result = subprocess.run(['node', r'E:\Program Files\Desktop\Jing3\逆向\京东h5st\11.2.js', json.dumps(data)],
                                capture_output=True, text=True, encoding='utf-8')

        print(result.stdout)
        h5st = re.findall(r'\$\$(.*?)\$\$', result.stdout)[0]
        print(h5st)
        # ddddd=re.findall(r'receive data-->(.*?)',result.stdout)[0]
        # print(ddddd)
        params['h5st'] = h5st
        response = requests.get(url, headers=headers, cookies=cookies, params=params)

        # subprocess.call("cls", shell=True)
        print(response)
        res = response.text.replace('jsonpMore2Goods(', '').replace(')', '')
        # print(res)
        res_json = json.loads(res)
        cnt = len(res_json['data'])
        for i in range(cnt):
            print(res_json['data'][i]['t'])
# for i in range(5):
#     get_goods_list(str(i))
#     time.sleep(2)

get_goods_list()
# get_goods_list(1)
# get_goods_list(2)
# get_goods_list(3)