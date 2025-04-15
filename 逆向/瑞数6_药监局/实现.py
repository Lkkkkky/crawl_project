'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/10/23 20:15
       @Desc     : 
=========================================================   
'''
from idlelib.iomenu import encoding
from uu import encode
#  带上第一次的cookie  ！！！！坑 陷阱
import requests

from lxml import etree
from loguru import logger
import execjs



headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.nmpa.gov.cn/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
def first_request():
    url = "https://www.nmpa.gov.cn/"
    response = requests.get(url, headers=headers)
    html=etree.HTML(response.text)
    ts_code=html.xpath('//script[1]/text()')[0]
    logger.success(response)
    # logger.info(ts_code)
    content=html.xpath('//meta[2]/@content')[0]
    # logger.info(content)
    logger.info('第一次响应返回的cookie:{}'.format(response.cookies.get_dict()['NfBCSins2OywS']))
    cookies['NfBCSins2OywS']=response.cookies.get_dict()['NfBCSins2OywS']
    return ts_code, content

def second_request():

    with open('test_main.js',encoding='utf-8') as f:
        js_code=f.read().replace('&&content&&',content).replace("'$$ts$$'",ts_code)
        cookie=execjs.compile(js_code).call('get_cookie')
    logger.info(f'生成的cookie为:{cookie}')

    cookies[cookie.split('=')[0]]=cookie.split('=')[1]

    response = requests.get(url='https://www.nmpa.gov.cn/',headers=headers,cookies=cookies)
    logger.info(response.status_code)
    response.encoding='utf-8'
    print(response.text)


if __name__ == '__main__':
    cookies = {}

    ts_code, content = first_request()
    second_request()
    print(cookies)