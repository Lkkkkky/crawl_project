'''
=========================================================    
       @File     : 商家信息.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/28 18:15
       @Desc     : 
=========================================================   
'''
import requests
from loguru import logger
from lxml import etree
import re

def get_asin_seller(url_):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "device-memory": "8",
        "downlink": "5.55",
        "dpr": "1",
        "ect": "4g",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "rtt": "100",
        "sec-ch-device-memory": "8",
        "sec-ch-dpr": "1",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua-platform-version": "\"10.0.0\"",
        "sec-ch-viewport-width": "1912",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "viewport-width": "1912"
    }
    cookies = {
        "session-id-time": "2082787201l",
        "i18n-prefs": "USD",
        "lc-main": "zh_CN",
        "sp-cdn": "\"L5Z9:CN\"",
        "session-id": "140-6530178-9717009",
        "ubid-main": "135-1159067-0664264",
        "session-token": "eaeN1yvP0bFSP9pQeJhT5DAryqAn0CjVRhsbK2pjkG0E2+V90fJJpOMfLHhGFXYo3R3rAy/XEPsB+Aisu/zme4C+wEWdK5r20HEW2Tzs31O0Eofrl+ezXWeQzLtesq6Q0Zqkb2Zgems44IQ9BgApJYNBJ1hh7qW2aRbOt8mJpHoT/9+v2RI1CUEXdFPr4hn4BlH+ESBsLGBcYxydQmgcnWN+rYdeWEw0kCyiM6zXbItRIWT7o1FT1pG9eD3pEGWwXqRcecaeBdQceEVsCmUdNstriHEsrMR9PwcHViCP+CBYo4QVSUEfOVIoBNMTDhjlzCK8Uq6N4DPVKMjxG1U9f6PPpsSpjG5t",
        "csm-hit": "tb:D1Z8EJGWFXJ48YP3C6NK+s-112V3HDRCWK6E8SJ58HG|1732790764296&t:1732790764296&adb:adblk_no"
    }
    url = url_
    try:
        response = requests.get(url, headers=headers, cookies=cookies,timeout=10)
        res_html=etree.HTML(response.text)
        seller=res_html.xpath('//input[@id="deliveryBlockSelectMerchant"]/@value')[0]
        asin=re.findall("asin: \"(.*?)\"",response.text)[0]
        print('asin-->', asin, 'seller-->', seller)
    except Exception as e:
        logger.info(e)
        asin=''
        seller=''
    return asin,seller


def get_company_name(seller,asin):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "device-memory": "8",
        "downlink": "10",
        "dpr": "1",
        "ect": "4g",
        "pragma": "no-cache",
        "priority": "u=0, i",
        # "referer": "https://www.amazon.com/dp/B0DGSMGXR4/ref=sr_1_1_sspa?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=36LGZVZRFXCYL&dib=eyJ2IjoiMSJ9.H9lHYnH5_gpu1NjWw0k-hPxoUeVx9WBKzf2gKH6ocU3GjHj071QN20LucGBJIEps.Gd-zM66cZBUNRC8yAREi3O8mYS8lfzsjt37CZxdlAzw&dib_tag=se&keywords=%E7%94%B5%E8%84%91&qid=1732423327&sprefix=diannao%2Caps%2C321&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "rtt": "50",
        "sec-ch-device-memory": "8",
        "sec-ch-dpr": "1",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua-platform-version": "\"10.0.0\"",
        "sec-ch-viewport-width": "1912",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "viewport-width": "1912"
    }
    cookies = {
        "session-id-time": "2082787201l",
        "i18n-prefs": "USD",
        "lc-main": "zh_CN",
        "sp-cdn": "\"L5Z9:CN\"",
        "session-id": "140-6530178-9717009",
        "ubid-main": "135-1159067-0664264",
        "session-token": "3twid+oR02hLtfkxePobJLn5DjE8Km7lAqesx4f8epUs1PW8L6wlIhBj8bqDHWrb58ssn3qY9lGam2lf3Ca5wH0q/ArUtoxwch5s1Ze6epuIZm9nBbV0oacfWJ+W3neX7Z1Wg53pQou3N8A+ZzGxfciQ8xTPCjTPGm5Syd+VMdpdmGgltGdck4Ta82g07a0U/M9U/1AFi00LTmhW9uiO7sWGOjsb4m7lkA6CHuDOAqc9B8paEtITZbMUopIYaUJ5GK76kGFz3wEbnWkbkN8IMD+EH+zyTUqfccc+zyvKznVIuYGlB+y2GDhRJF8k8xyV112tzzon8a6F/BaFwy3QwpDhMsJlFUa3",
        "csm-hit": "tb:D1Z8EJGWFXJ48YP3C6NK+s-6XKF9SZHGHER4FH562QF|1732791898491&t:1732791898491&adb:adblk_no"
    }
    url = "https://www.amazon.com/sp"
    params = {
        "language": "zh",
        "ie": "UTF8",
        "seller": seller,
        "asin": asin,
        "ref_": "dp_merchant_link",
        "isAmazonFulfilled": "1"
    }
    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        # print(response.text)
        res_html=etree.HTML(response.text)
        # company_name=res_html.xpath('//div[@id="page-section-detail-seller-info"]//div[@class="a-row a-spacing-none"]/span[2]/text()')[0]
        company_name=res_html.xpath('//*[@id="page-section-detail-seller-info"]/div/div/div/div[2]/span[2]/text()')[0]
        # print(company_name)
        company_address='-'.join(res_html.xpath('//div[@class="a-row a-spacing-none indent-left"]/span/text()'))
        return [company_name, company_address]
        # print(company_address)
    except Exception as e:
        logger.info(e)



asin,seller=get_asin_seller("https://www.amazon.com/dp/B09JL6BKBW/ref=sr_1_1_sspa?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=2W9URSHSWWR7E&dib=eyJ2IjoiMSJ9.chUBCAb2p-lJQ2mTMEN74d5A8nFKkUnBDV2kfiBEHPDedOoxREMVU_Gi8swXO7bld59WLPGMSNQLlOrnpC8ReuCZlYTyzVBpXzSPuBPqSnw2DVuwtBmLjnK4iT7knEdcTP5pjv4jJ_sMVZR5WFmsaA.2qgcdhrczMs_YlNImsKbUUXc03FPQIoPMKQ2zzgfvpQ&dib_tag=se&keywords=%E9%A6%99%E6%B0%B4&qid=1732794676&sprefix=xiangsh%2Caps%2C306&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
get_company_name(seller,asin)