'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/10 10:19
       @Desc     : 
=========================================================   
'''
import requests
import json
import time
from loguru import logger
for i in range(30000):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "device-id": "0e32f58346054fc48ad80a0d7bd47bfb",
        "language-type": "zh_CN",
        "origin": "https://h5.18art.art",
        "platform-type": "h5_browser",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://h5.18art.art/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "trade-area-type": "0",
        "trans-id": "94e1a35e8fe542d6b8512dc4665fc873",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/132.0.0.0",
        "user-token": "rWpHXFzJkaUAcuWutg+PAW5eB1YE36sxJ+sK+KGo/FU=",
        "x-cloudbase-phone": "17819461984"
    }
    cookies = {
        "JSESSIONID": "awLYRZ7pUhIEkMrxdbjpzaeFw9y50nJ1/f2mmmHoYkc=",
        "USER-TOKEN": "rWpHXFzJkaUAcuWutg+PAW5eB1YE36sxJ+sK+KGo/FU="
    }
    url = "https://api-app.18art.art/nft-web/v1.2/nft/product/getProductListByAlbumId"
    params = {
        "page": "1",
        "pageSize": "50",
        "order": "1",
        "albumId": "100522609",
        "onSale": "1"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
    logger.info(response)
    try:
        if response['data']['list']['albumId']==100522609:
            try:
                goods_list=response['data']['list']
                url = "https://api-app.18art.art/nft-web/v1/nft/order/create"
                for i in goods_list:
                    data = {
                        "albumId": i['albumId'],
                        "gId": i['gId'],
                        "type": 0,
                        "gNum": i['gNum'],
                        "price": i['priceCny']
                    }
                    data = json.dumps(data, separators=(',', ':'))
                    response = requests.post(url, headers=headers, cookies=cookies, data=data)
                    if(response.json()['code']!=103):
                        requests.get('https://api.day.app/YToREckaeQXotQJPrn7MWa/拿下')
                        logger.info(response.text)
                        logger.info(response)
                    # time.sleep(0.3)
            except:
                logger.info(response)

    except:
        time.sleep(1)
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "cache-control": "no-cache",
#     "device-id": "0e32f58346054fc48ad80a0d7bd47bfb",
#     "language-type": "zh_CN",
#     "origin": "https://h5.18art.art",
#     "platform-type": "h5_browser",
#     "pragma": "no-cache",
#     "priority": "u=1, i",
#     "referer": "https://h5.18art.art/",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "trade-area-type": "0",
#     "trans-id": "94e1a35e8fe542d6b8512dc4665fc873",
#     "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/132.0.0.0",
#     "user-token": "rWpHXFzJkaUAcuWutg+PAW5eB1YE36sxJ+sK+KGo/FU=",
#     "x-cloudbase-phone": "17819461984"
# }
# cookies = {
#     "JSESSIONID": "awLYRZ7pUhIEkMrxdbjpzaeFw9y50nJ1/f2mmmHoYkc=",
#     "USER-TOKEN": "rWpHXFzJkaUAcuWutg+PAW5eB1YE36sxJ+sK+KGo/FU="
# }
