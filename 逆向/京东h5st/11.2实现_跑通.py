'''
=========================================================    
       @File     : 11.2实现_跑通.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/2 17:33
       @Desc     : 
=========================================================   
'''
import requests

import execjs
import hashlib
import time
import re
import json
import subprocess
def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://re.jd.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "__jdu": "1468058068",
    "shshshfpa": "c273795a-d734-cfaa-ce50-9d031a6538ec-1700461744",
    "shshshfpx": "c273795a-d734-cfaa-ce50-9d031a6538ec-1700461744",
    "_pst": "jd_MhNyBaXRXFnl",
    "unick": "lkyyyyyyyyyyy",
    "pin": "jd_MhNyBaXRXFnl",
    "_tp": "LckDemJZ9vjD7CXeUJhnPA%3D%3D",
    "TrackID": "1Qea09rv2vI6b9d_sX6efCjXMzHP0SVPYsMQwy0EKasEmqwnrna_P90FmBJQLY7J6rVRmF8mH2N6dekbImCUpnArGfRgMo0yujCHzRpzU6dBnE51nkeeHCkcSJJKoGriL",
    "light_key": "AASBKE7rOxgWQziEhC_QY6yauEGIs-waHyn8jTWHTwGQGR5AHe5-eSXSUUgh9DXqK93nhvqJ",
    "unpl": "JF8EAJpnNSttDEkGABIEGhAVHlQEW1wBT0QCO2BQB1VfTFVWGVIfFkd7XlVdWBRLFx9sZhRVX1NOVA4YBCsSEXteU11bD00VB2xXVgQFDQ8WUUtBSUt-S1tXV1QOSh4AbGQBZG1bS2QFGjIbFxdCXFBXXA9CJwJfYDVkbVBJUgAZBysTIEptFgoBCEMfAWllSFRYX0JVARIDHBsgSm1X",
    "3AB9D23F7A4B3C9B": "SHHR7HCVAO4D4OCSDSIWSXEE4MOIEPIUNLGHXXVVANTJVFYEPODQK76V7LLAH4AWCTIWGK2SSONE362YELGJVYGV24",
    "mt_xid": "V2_52007VwMXVVRZVlMeThBsB2BWQQZeXVdGHkxKCBliAUUCQQhVXU9VS1QDNQISUghaUg1PeRpdBmIfElJBW1NLHksSWQVsBhpiX2hSah9BEFwCZgEUUFxZYlkYQA%3D%3D",
    "token": "8fc06d810e5d7af31d91dd743775aca6,2,962247",
    "areaId": "19",
    "3AB9D23F7A4B3CSS": "jdd03SHHR7HCVAO4D4OCSDSIWSXEE4MOIEPIUNLGHXXVVANTJVFYEPODQK76V7LLAH4AWCTIWGK2SSONE362YELGJVYGV24AAAAMTIXZBDTYAAAAACUBP7LEG623ZUEX",
    "_gia_d": "1",
    "jsavif": "1",
    "ipLoc-djd": "19-1601-50258-129167",
    "shshshfpb": "BApXStYr6RvZAhddKJXMhHnyZ9HSho4k2BkIHEGtk9xJ1MvT02IO2",
    "wlfstk_smdl": "9q262ovltyljxa23t93jfsb03ozck97u",
    "logintype": "wx",
    "logining": "1",
    "npin": "jd_MhNyBaXRXFnl",
    "thor": "1F63723E3B0B854D9454AB8BE6A4EAB5D6AE0AE74007F05D682072A2346EEFEAA9B302A6E848768AEF5DD5639D2DC5F5F27F4463A6770F64EEEED2F13871FEC800E12AFCF44BCDA1205B03B863054ED6149FEB4FD1033CB6509E1BB594F046B6FF4C6AFA9FE418877A9026BCEC227EAA40103CCD105FFF918A8D28E72FAC9DE7AB1E7ED9599798527ADDD628B056432DCC9DB8EAC3F51DA968C9923FFB98A09B",
    "flash": "3__oGO858578jRmOHvtzZYDFwRMYX2g_InH0dKpGOJBnM9HSbeGkNpzEhrQqBQ8-_5qD8bHo1ecdlBh15wGCM0hjkAcxDfJX3GNqtS6T20jA51OWlq63Di2Y-OTJKTV0ncvtgo6J7f_jC9JfuoXgkRriPKwMFWsqA-lC6WXSxYIuDSHk**",
    "pinId": "8iMjBrpr1TnSWYxYoJoW6g",
    "__jda": "229668127.1468058068.1728325094.1730741760.1732045290.21",
    "__jdb": "229668127.6.1468058068|21.1732045290",
    "__jdc": "229668127",
    "__jdv": "229668127|baidu-search|t_262767352_baidusearch|cpc|172887082225_0_e3c487034d8a4085b0e6db9660b3a55f|1732045418920"
}


def get_good_list(page):
    for p in range(page):
        t = int(time.time() * 1000)

        url = "https://api.m.jd.com/"
        params = {
            "appid": "www-jd-com",
            "body": '{"page":'+str(p)+',"pagesize":25,"area":"19_1601_50258_129167","source":"pc-home"}',
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

        h5st = execjs.compile(open('11_2.js', 'r', encoding='utf-8').read()).call('h5st', t, sha256(params['body']))

        params['h5st'] = h5st

        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        res = response.text.replace('jsonpMore2Goods(', '').replace(')', '')
        # print(res)
        res_json = json.loads(res)
        cnt = len(res_json['data'])
        for i in range(cnt):
            print(res_json['data'][i]['t'])

get_good_list(3)