'''
  @File     : 抢购.py
  @IDE      : IntelliJ IDEA
  @Author   : Jing3
  @Date     : 2024/10/3 12:34
'''
import requests
import execjs
cb=execjs.compile(open('js.js','r',encoding='utf-8').read()).call('get_cb')
fp=execjs.compile(open('js2.js','r',encoding='utf-8').read()).call('get_cb')
print(cb)
print(fp)
def get_image():

    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://dun.163.com/",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "_ga": "GA.1.28bf115cd48c0.131b69ad3ce41cf257f4",
        "__root_domain_v": ".163.com",
        "_qddaz": "QD.594528554584280",
        "Hm_lvt_4671c5d502135636b837050ec6d716ce": "1728554578,1728582278",
        "Hm_lpvt_4671c5d502135636b837050ec6d716ce": "1728582278",
        "HMACCOUNT": "EA1E6DCED1333B4F"
    }
    url = "https://c.dun.163.com/api/v3/get"
    params = {
        "referer": "https://dun.163.com/trial/jigsaw",
        "zoneId": "CN31",
        "dt": "XapiY4mNlxJFVwBREEbXCTpyvFLKUJoB",
        "irToken": "m2SoOPUbA7pBc1FRVFLGWDs6lMTtAYeQ",
        "id": "07e2387ab53a4d6f930b8d9a9be71bdf",
        "fp": fp,
        "https": "true",
        "type": "2",
        "version": "2.28.0",
        "dpr": "1",
        "dev": "1",
        "cb": cb,
        "ipv6": "false",
        "runEnv": "10",
        "group": "",
        "scene": "",
        "lang": "zh-CN",
        "sdkVersion": "",
        "loadVersion": "2.5.0",
        "iv": "4",
        "user": "",
        "width": "320",
        "audio": "false",
        "sizeType": "10",
        "smsVersion": "v3",
        "token": "dc06dd8c8d884dd2b51b29b09721684d",
        "callback": "__JSONP_eqkkyom_1"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(response.text)
    print(response)
get_image()
