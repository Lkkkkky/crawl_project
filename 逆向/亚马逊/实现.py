'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/21 20:41
       @Desc     : 
=========================================================   
'''
import json
import time

import requests
from lxml import etree

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "device-memory": "8",
    "downlink": "1.55",
    "dpr": "1",
    "ect": "3g",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.amazon.com/s?k=pc&i=black-friday&crid=1DB2GS6EWUNUS&sprefix=%2Cblack-friday%2C1624&ref=nb_sb_noss",
    "rtt": "350",
    "sec-ch-device-memory": "8",
    "sec-ch-dpr": "1",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-viewport-width": "1920",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "viewport-width": "1920"
}
cookies = {
    "session-id": "134-5570334-3900766",
    "session-id-time": "2082787201l",
    "i18n-prefs": "USD",
    "ubid-main": "135-3503916-5104164",
    "skin": "noskin",
    "session-token": "WbHYy60Z3KEiOGOFyRHpsIFvP0VA7Iv5kmW9cYQKcA/W1fX9gkQZqq6UthcVTFOYRQSKVZQLmVJc6wF5W/w2g/QJIujFLXAbKBK491oCUmSXs60DceFoK58J/qqES+DM6WnGxFxkVMWWlsX9LltPcpecUgikl9Co97AghvnBYQ7ehXY7gooCEGRXpmQVzni/jsXppldNo7PkBzd4IaaW/mPpSeQp+q0yEIEqPzqfM8rfa3Q5AHilUnGO7QpmcybM1hGzNNb8X4s5auwhUShiNB4QEqammPosLNA8lSnXnQw0xlYW8Zua6LOyj0mFatsLyp4t7nDL+ruFT2xwKLjBL9t35cz0/JA8",
    "csm-hit": "tb:WTR5XX2VBHSDQXESTRHY+s-55BQ2PSQ9DT4XB77GJAJ|1732192586955&t:1732192586955&adb:adblk_no"
}
url = "https://www.amazon.com/s"




for page in range(2):
    t = str(int(time.time()))

    params = {
        "k": "pc",
        "i": "black-friday",
        "bbn": "384082011",
        "page": str(page),
        "crid": "1DB2GS6EWUNUS",
        "qid": t,
        "sprefix": ",black-friday,1624",
        "ref": "sr_pg_2"
    }
    response = requests.get(url, headers=headers, cookies=cookies,params=params)
    res_html = etree.HTML(response.text)
    goodlist = res_html.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]')
    for i in goodlist:
        good_name = i.xpath('./text()')[0]
        print(good_name)
