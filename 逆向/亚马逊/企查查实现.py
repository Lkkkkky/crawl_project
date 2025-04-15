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
        "QCCSESSID": "990e2f1ce2344aa5e0347e0761",
        "acw_tc": "1a0c39d617332935866284699e0041e20a1e92ce6304e22eb27b59f6ffb25b",
        "tfstk": "fu2BzY4dQeYQxP1FG3IZ5x1aFik7Rz6qP3i8mupe2vHpyUEx7DyF-u37PPugPbjnz437zuFFbtW4xkDoez_V3tlCWHg3d4LreHdWoT7VutWZLn9_BZzEKmWWf00tv0h-wG9tV0M-vXddfVnSmQLLyzEOf0opp4hp9hLtx0H-yzHRflheRni5O2qCb7HEyOILkk36hl2svuA3vV9JeRNsOqLS5Lp8CDZZqcXBh_uYi2lqPPBwdYZtVPG4OZ9QPuE0wfwWJMzYW7a-j5bWNqN8YSV-1MBLfvgI1Dz9DCMQwy2StWtlmlHLSS0m91bifJyqNqc6WwEaf2hbNy7Me2PbXPG4QFJqHS4_FjHA4NJqlDIvNhGDFcgVfGOkZx4yKoIaKIas9cmI_Gs6J7cKjcgVfGOkZXniAfS1feFl.",
        "CNZZDATA1254842228": "1201975009-1729578908-https%253A%252F%252Fdocs.qq.com%252F%7C1733293675"
    }
    url = "https://www.qcc.com/web/search"
    params = {
        "key": key
    }

    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        phone=re.findall("\"ContactNumber\":\"(.*?)\",",response.text)[0]
        print(key,'--->',phone)
    except:
        logger.info('联系方式查找失败')
        phone='暂无联系方式'
    return phone

list=['范楠', 'VickyLei', '上海隶孟电子商务有限公司', '广州星颜生物科技有限公司', '金华市浦江县馨艺服装厂', '深圳执一科技有限公司', '苏州若态电子商务有限公司', '广州市鑫依风尚服饰批发商行', '义乌市启伟皮具有限公司', '深圳市云中飞电子有限公司', 'KT AT Marketing LTD', '广州宏拓电子商务有限公司', 'Anna', '广州雅辰服装有限公司', '广州维拓电子有限公司', '佛山市古邦客电子商务有限公司', '厦门鹭无央生物科技有限公司', '广州八零一服饰有限公司']
for i in list:
    get_phone(i)
    time.sleep(15)