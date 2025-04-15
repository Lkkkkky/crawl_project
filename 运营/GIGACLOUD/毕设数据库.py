'''
=========================================================    
       @File     : 毕设数据库.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/1/8 14:33
       @Desc     : 
=========================================================   
'''
import requests
import json

def GIGA_get_goods_list(keyword):
    headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "ori-status-in-response": "code",
            "origin": "https://www.gigab2b.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.gigab2b.com/index.php?route=product/search&search=boy&search_source=0",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
            "x-csrf-token": "9mGlwSJsh02AP3fEdMPgRLoLJQgoZawWY52XKySZ",
            "x-requested-with": "XMLHttpRequest, XMLHttpRequest"
        }
    cookies = {
    "_ga": "GA1.1.408575259.1733361903",
    "_gcl_au": "1.1.1151540469.1733361903",
    "_pk_id.2.185c": "a2b8705262873a34.1733361904.",
    "hubspotutk": "e0ac6d6ae1ea998f165da8110cf1f836",
    "__hs_opt_out": "no",
    "_fbp": "fb.1.1733729031869.450488541383874844",
    "acw_tc": "ac11000117363177104948943e0052a6143fe750af7901729ade521804b329",
    "_ayo": "9baa4c61a31d2849c7c7ca2b7c50abc1",
    "country": "USA",
    "currency": "USD",
    "OCSESSID": "d6cd840024c208fe4b33298018",
    "gmd_device_id": "e044ce02-ef3f-4fbd-aad9-04d33b028a78",
    "_pk_ses.2.185c": "1",
    "__hstc": "114550104.e0ac6d6ae1ea998f165da8110cf1f836.1733361999612.1733737821247.1736317714259.4",
    "__hssrc": "1",
    "acw_sc__v2": "677e1b25a18f7a9dd86cfdd0b07a1bc9b4573122",
    "tfstk": "gLOSKvt-guqWrnZDr03VfDHFYGfBdHGZFy_pSeFzJ_C8vkLO038yaYXCHHs2ag8PwX9BjhZFp6ReJzAXfWPrqYYLO65KbclZ_U4lt6nwUawWkzbF5WeLY9IYk67QRjLSiUYltrxXmCQprkTfEU5R9HCAHabR97e8wq6A8w1Lw9F8HoIcJ6Cd2gLAHN77wkBRvqTAmw1L9WKpkbtb5wM5qUgS6tyVhVwyPiNL9I_xxGT7TW7XiaaVbUSjXAdb9Ts9yiNKjtQRHMsD6mkXoHpJ4ZxI1m19InOCB6G7ja9v5sIP6AwfNE-k1_dsV77Vdg9vwtaL9FLke9pBV0wl2L-fIZBYRfb2biLkwKg3DUKNV_QA3f36k9p2ZOArD719IU5yphn4Ugp1JgPz_G_-WJwxsW_fbqgbKJfMY7Y903y6STQcPtujlupheZbfbqgbKJXRoa6qlqZJK",
    "is_partner": "0",
    "login_flag": "",
    "__hssc": "114550104.12.1736317714259",
    "_ga_39N4BF4XSG": "GS1.1.1736317712.5.1.1736317893.0.0.0",
    "SERVERID": "66839549c43026f0ffd947819a6794bc|1736317895|1736317710",
    "SERVERCORSID": "66839549c43026f0ffd947819a6794bc|1736317895|1736317710"
    }
    url = "https://www.gigab2b.com/index.php"
    params = {
    "route": "/product/list/search"
    }
    id_list=[]
    res_list=[]
    for i in range(10):
        data = {
            "page": i,
            "limit": 120,
            "scene": 1,
            "search": keyword
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data).json()
        # print(response)
        if (response['data']['product_list'] not in id_list):
            id_list.append(response['data']['product_list'])
    for t in id_list:
        for x in t:
            res_list.append(x)
    return res_list
