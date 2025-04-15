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
        "acw_tc": "0a47308617344862050743041e00d5c199fceb820ec21bc404acc9226da357",
        "QCCSESSID": "c19ae5884f0906b9f922d69479",
        "tfstk": "goMEsP4cvppehJDerl2PQNdCWTwLQJYfUYa7q0muAy4hd9_o_0g-d7YLdYuapAGCFyTLU00bUETXhKiKvJeklE_tWi4zEuv7rCNhx_7vFETXhdwC0OkMl2O-xa9a2Pq3q7VkblqQc8j3q44gsoqf-82orhygvo5uxkfnjOqzSz2uE4mMbuhAQDmlQoNHDFLg9d6sBWzmxPWqXAr3Q6n37TXoQfPUoTzNETDaYcZ8XpW2NrcYRSarSd6UUcqr7SGeu9urqmhu_Y7HAq0ia4qt6U5zubmIMbVwxpmaLyPaAVjc_JloJYPKTgKxjJ0tMrFH6FEZdxNzk57M-cia-SlrRFBuRjoi7SM15twmMVkzi-jrqaEMxeM-TafztlEalh-Nqh_s7l1JXo5Rw52YbrtQA_C8tlEalh-Nw_FgHlzXAk1..",
        "CNZZDATA1254842228": "1201975009-1729578908-https%253A%252F%252Fdocs.qq.com%252F%7C1734487524"
    }
    # cookies = {
    #     "qcc_did": "d9c083fc-0227-45db-ab6a-738b7b250319",
    #     "UM_distinctid": "192b2efbaa180e-0fda9ace36d7bd-4c657b58-1fa400-192b2efbaa2959",
    #     "_uab_collina": "173259661767951837153542",
    #     "acw_tc": "1a0c39d617344045344152744e003e4c99779ebfd9c38ecc43adc17b20ad0e",
    #     "QCCSESSID": "7773554e5477ae6b267a4b5c1d",
    #     "tfstk": "g7oxspifZQA0b7rHmnTusyAKRz9uXcH4njkCj5Vc5bh-dv505rA464hsarVjXASTCAGw35v2rxk4blOHtcKn3xuSWw8yZl9sFl2OZVAeSxk4bTyxOvlZ31hNaKMbffZ7PRegfGs1lLK737sbCiw1NLeaNls_fP6WVJeT1RZs1Y98Q7N_flG2ECF5h5jtSU8r2nKeiGIt2-UY6GxdjGl5xrFIh7I6O0ev1WMbwGs_i70kfYHDMMku0cGLKjx5DXHsLVa-X_OL_0HScVMPMLZKe403k4dfX7m0ByZ_yOsselgq90ZBA_erPx0s0jBOf-omxPFUydsaSui3R2GAQpk7cRGa8cAF0SMsLDu3vnCUH4ML2grixD3na6VLIZ9JeN7al8Pi3mzARM4Dp8FHHhQN7zJzeWvJeN7al8y8tKKO7NzyU",
    #     "CNZZDATA1254842228": "1201975009-1729578908-https%253A%252F%252Fdocs.qq.com%252F%7C1734405971"
    # }
    url = "https://www.qcc.com/web/search"
    params = {
        "key": key
    }
    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
    except:
        logger.info('企查查风控')

    try:
        name = re.findall("\"Name\":\"(.*?)\",", response.text)[0]
        phone = re.findall("\"ContactNumber\":\"(.*?)\",", response.text)[0]
        print(key, '--->', phone)
    except:
        logger.info(key,'--->联系方式查找失败')
        name='暂无公司中文名称'
        phone='暂无联系方式'
    try:
        address = re.findall("\"Address\":\"(.*?)\",", response.text)[0]
        print(key,'--->',address)
    except:
        logger.info(key,'--->联系地址查找失败')
        address = '暂无联系地址'
    return name,phone,address

# list=['范楠', 'VickyLei', '上海隶孟电子商务有限公司', '广州星颜生物科技有限公司', '金华市浦江县馨艺服装厂', '深圳执一科技有限公司', '苏州若态电子商务有限公司', '广州市鑫依风尚服饰批发商行', '义乌市启伟皮具有限公司', '深圳市云中飞电子有限公司', 'KT AT Marketing LTD', '广州宏拓电子商务有限公司', 'Anna', '广州雅辰服装有限公司', '广州维拓电子有限公司', '佛山市古邦客电子商务有限公司', '厦门鹭无央生物科技有限公司', '广州八零一服饰有限公司']
# for i in list:
# get_phone('上海隶孟电子商务有限公司')
#     time.sleep(15)