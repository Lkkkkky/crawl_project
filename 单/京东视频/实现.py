'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/10/21 01:52
       @Desc     : 
=========================================================   
'''
import requests
import requests
import hashlib
import time
import re
import json
import subprocess
t = int(time.time()*1000)
def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "origin": "https://h5.m.jd.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://h5.m.jd.com/",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "x-referer-page": "https://h5.m.jd.com/active/faxian/video/index.html",
    "x-rp-client": "h5_1.0.0"
}
cookies = {
    "__jdu": "1468058068",
    "shshshfpa": "c273795a-d734-cfaa-ce50-9d031a6538ec-1700461744",
    "shshshfpx": "c273795a-d734-cfaa-ce50-9d031a6538ec-1700461744",
    "areaId": "19",
    "PCSYCityID": "CN_440000_440100_0",
    "user-key": "e2c2f1c9-05f5-4953-b352-b9dad9179828",
    "ipLoc-djd": "19-1601-50258-62836",
    "_pst": "jd_MhNyBaXRXFnl",
    "unick": "lkyyyyyyyyyyy",
    "pin": "jd_MhNyBaXRXFnl",
    "_tp": "LckDemJZ9vjD7CXeUJhnPA%3D%3D",
    "mba_muid": "1468058068",
    "unpl": "JF8EAJhnNSttC0kBBhkHTxoQTA0BWwkIHERXPWVXBFVZTFNSH1UbERB7XlVdWBRLFh9sZhRUWVNPUQ4eCisSEXteU11bD00VB2xXVgQFDQ8WUUtBSUt-S1tXV1QOSh4AbGQBZG1bS2QFGjIbFxdCXFBXXA9CJwJfYDVkbVFOUQQZMhoiEXsfAAJZCE0UBCJnAFNUWU9dBBwLKxMgSA",
    "logintype": "wx",
    "npin": "jd_MhNyBaXRXFnl",
    "__jdv": "229668127|baidu-search|t_262767352_baidusearch|cpc|172887082225_0_b3d234e916ad4e1fbec3ca9066f5f121|1729411331442",
    "3AB9D23F7A4B3C9B": "SHHR7HCVAO4D4OCSDSIWSXEE4MOIEPIUNLGHXXVVANTJVFYEPODQK76V7LLAH4AWCTIWGK2SSONE362YELGJVYGV24",
    "mt_xid": "V2_52007VwMXVVRZVlMeThBsBW4LRQAOX1RGHk4bXxliUxBQQVECXhxVEQgCZgUTVlkIAllPeRpdBmIfElNBW1NLH04SXwRsAxBiX2hRahxIH1QAYjMRVV1e",
    "flash": "3_9hMLDZcW_XbJYTR0zBewKqlj1NU0J0rFbt6nSP4jIJQEF431CcHN9egsZuhje0nBBeMQB-Tci_jMqMwZkhAcfZxiiI48XDe0SUpXH9qXr1QitveavpWThRPsNt0W9__olQ2Rl_RpHz81baFRlDaSUcAzH8D-nOr9IddvCQrqBEtTFe**",
    "3AB9D23F7A4B3CSS": "jdd03SHHR7HCVAO4D4OCSDSIWSXEE4MOIEPIUNLGHXXVVANTJVFYEPODQK76V7LLAH4AWCTIWGK2SSONE362YELGJVYGV24AAAAMSVMFPZPQAAAAAC4ORWSXN5WAP7UX",
    "__jda": "181111935.1468058068.1728325094.1729430606.1729446477.15",
    "__jdc": "181111935",
    "autoOpenApp_downCloseDate_auto": "1729446478007_1800000",
    "shshshfpb": "BApXS8PUDqPdAhddKJXMhHnyZ9HSho4k2BkIHEGth9xJ1MvT02IO2",
    "__jdb": "181111935.8.1468058068|15.1729446477",
    "mba_sid": "17294464771832278419014034785.4"
}
url = "https://api.m.jd.com/video_videoDetail"
data = {
    "functionId": "video_videoDetail",
    "appid": "content_H5",
    "client": "wh5",
    "clientVersion": "1.0.0",
    "t": str(t),
    "ext": "{\"clientPageId\":\"MvideoDetail\"}",
    "x-api-eid-token": "jdd03SHHR7HCVAO4D4OCSDSIWSXEE4MOIEPIUNLGHXXVVANTJVFYEPODQK76V7LLAH4AWCTIWGK2SSONE362YELGJVYGV24AAAAMSVMFPZPQAAAAAC4ORWSXN5WAP7UX",
    "body": "{\"id\":\"566450383\",\"style\":\"\",\"channel\":\"h5VedioDetail\",\"monitorSource\":\"h5share\",\"modeid\":\"2\",\"playtype\":\"\"}",
    "h5st": "20241021015050122;8555275975394065;349b4;tk03wa0a81c1218nrtWqkiFtUHDvIoA7JhC6K71At8plqh1tDN957-6Xw-Ed6BnbXgdqYqjyw40R-yzr4cEiiTz6IYjT;3be141d7007446d3b12f964a5591978b4276bae2a8d783d33f34d1c88b2cced1;3.1;1729446650122;24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e355076cc27b11bb228be53f32ed2056525f166d6a25fdcc95f56236d114cd8ee1073e51025a9c8a4469ed2fdee11bada503e8b357dcfa10e8382dc3d4dde0ce3322a12a2ade1ce82566b0f02bfd5c2335"
}
data2={
    "appid": "www-jd-com",
    "body": sha256(data['body']),
    "clientVersion": "1.0.0",
    "client": "pc",
    "functionId": "pc_home_feed",
    "t": t
}
result=subprocess.run(['node',r'E:\Program Files\Desktop\Jing3\单\京东视频\js2.js',json.dumps(data2)],capture_output=True,text=True,encoding='utf-8')
# print(result.stdout)
h5st=re.findall(r'\$\$(.*?)\$\$',result.stdout)[0]
print('h5st==',h5st)
# ddddd=re.findall(r'receive data-->(.*?)',result.stdout)[0]
# print(ddddd)
data['h5st']=h5st
print(data)
response = requests.get(url, headers=headers, cookies=cookies, params=data)

print(response.text)
print(response)