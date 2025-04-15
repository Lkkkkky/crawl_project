'''
=========================================================    
       @File     : 企查查实现.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/26 12:57
       @Desc     : 
=========================================================   
'''
import requests
import re

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.qcc.com/web/search?key=Yiwushijiadedianzishangwu%20Co.,%20Ltd.",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "qcc_did": "d9c083fc-0227-45db-ab6a-738b7b250319",
    "UM_distinctid": "192b2efbaa180e-0fda9ace36d7bd-4c657b58-1fa400-192b2efbaa2959",
    "acw_tc": "0a472f8417325965676051368e00392108d99c819234745647c79af6c80e0e",
    "QCCSESSID": "7559e61d46e7a1d9c0640d05c5",
    "_uab_collina": "173259661767951837153542",
    "tfstk": "foo-BLZZ7IAo4hXAkwT0twIx-CvDSDHzMbk1xWVlRjhxCA5uRzAz9qhIgzV5qLzdAvGTKzTEr2eKZjco9vJzdWGI9W0kohDrUkrBsXKMjYWDYmZxwaN5hpwaQJO7fgsoUkrBi8nsQKkr1cIyB0ZBHowLKwZQPgaXHRyQAgaCVZ1bgSNQA7a7lowaQJ1CAW9xhSyQAWML3BFfFWjK-7WZ45s5GMIKD-OUIYdhx-n7ezFsF0ICAOw8y5M7MCJQqEUjLynFLMFSFVlUCb1WszkIkje8vnb7fx3I6-oWj_eqrxMgGABFYYZ-WcESyI74qbnbc0gOdMMY27zLer5JM5irhcrboh9thmloUmHhdHwmsSMrVkK6QuE7NoeqxIS79qgIqzrFNC4rdqhYelszocmTWy1g6JbWHKQF8zw4tYozyNsgrdeYsLKd8wz23-FMHKQF8zw4H5vJvw7UuK5..",
    "CNZZDATA1254842228": "1201975009-1729578908-https%253A%252F%252Fdocs.qq.com%252F%7C1732596892"
}
url = "https://www.qcc.com/web/search"
params = {
    "key": "马安山锦胜财富广场AB栋B512"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
phone=re.findall("\"ContactNumber\":\"(.*?)\",",response.text)
print(phone)
print(response.text)
print(response)