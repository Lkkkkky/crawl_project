'''
=========================================================
       @File     : 企查查实现.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/26 12:57
       @Desc     :
=========================================================
'''
import time
import requests
import re
from loguru import logger
def get_phone(key):
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
        "_uab_collina": "173259661767951837153542",
        "acw_tc": "0a47308717334540045136185e013a3676073dcf223726d0326f72d71b78da",
        "QCCSESSID": "022571b65af4263ae9e817dbbb",
        "tfstk": "fZFtsVV6xMjigD8ppK6nmsxgVC7H6SUZSlzWimmMhkELPz-ihAjZDJEbYAm_MrRxlrZV7mbNKPzZgjslqSCu7PS_25rQ6dOBRyuJfFOhuCHqgjslxAF7Uwl44qr0t5aCJq0mlqZjc6TIYqnX1oisdHg-zjGjGoOBdqgx5qMXG2_KuDijGjGvYinB5mAYnL9bJz564IdY92sqVPKvi2FIWAn755dXGUgtB0asvg7js9HQuxF2uIH758rqPlt1DmPLR5w7VMvif83Yr-U11BGg_PwSh7s2huhTDYNspEOtTPiK92N5oLo39cqb6v_kwxcQZYG_K9Sinf38c5r9kIZ7-zVZLSIJAmyizXgYga9xDxszj7V8Ek-o2qv1Jwp23AgEmPPZBLOoIa3KqNCv3KkF82nlJwp23AgEJ0bOMKJqLw5..",
        "CNZZDATA1254842228": "1201975009-1729578908-https%253A%252F%252Fdocs.qq.com%252F%7C1733454057"
    }
    url = "https://www.qcc.com/web/search"
    params = {
        "key": key
    }
    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
    except:
        logger.info('企查查风控')

    try:
        phone = re.findall("\"ContactNumber\":\"(.*?)\",", response.text)[0]
        print(key, '--->', phone)
    except:
        logger.info(key,'--->联系方式查找失败')
        phone='暂无联系方式'
    try:
        address = re.findall("\"Address\":\"(.*?)\",", response.text)[0]
        print(key,'--->',address)
    except:
        logger.info(key,'--->联系地址查找失败')
        address = '暂无联系地址'
    return phone,address

# list=['范楠', 'VickyLei', '上海隶孟电子商务有限公司', '广州星颜生物科技有限公司', '金华市浦江县馨艺服装厂', '深圳执一科技有限公司', '苏州若态电子商务有限公司', '广州市鑫依风尚服饰批发商行', '义乌市启伟皮具有限公司', '深圳市云中飞电子有限公司', 'KT AT Marketing LTD', '广州宏拓电子商务有限公司', 'Anna', '广州雅辰服装有限公司', '广州维拓电子有限公司', '佛山市古邦客电子商务有限公司', '厦门鹭无央生物科技有限公司', '广州八零一服饰有限公司']
# for i in list:
# get_phone('上海隶孟电子商务有限公司')
#     time.sleep(15)