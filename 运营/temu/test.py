'''
=========================================================    
@File     : test.py
@IDE      : PyCharm
@Author   : Jing3
@Date     : 2025/4/22 20:49
@Desc     :
=========================================================   
'''
import asyncio
import time
import csv
import websockets
import json
from curl_cffi import requests  # 假设你在用 curl_cffi 请求



headers = {
"accept": "application/json, text/plain, */*",
"accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
"anti-content": '0aqWfqnvGctaj99mw6gdAqu301umv6YCcxe_1hveB-csgjftFZf8iOMmAGgQgVH42JsquSkzE97pN0zUJ0v0J4YZe1Hl7uLHRBOkdlkr0OD8SguwguFMDe1g7XoPmIRwyme4Hc8lNwwbODg6EchD_MnNGTPzTg5gvKXz0MKq9hIg1wv52_KN-22v2m8-SFQxrmCtqew0UXpRuiMWmm3c-6AKzMlKw5fsw0Q5xPS6AP5xrXXe5-BsGMY7AMg1DyoDR1XKpzDeEGmNBNujrzPSI29YS0BQdRnVte0M5tK91VG9-u9gb6G9YFPEBYVdc8f_kbz4ze9hE1zm3au9nukeE4XhqXp0q18L6he1nS3bVGVah1mKCnEvEh0C8R7XalokzrJC0QTydUTCmQ_j-tf1rj71L-ABH17uLFZS1YWHkxN8spxRtCc5FWZuLXCfS7k48z-lgsFzxbv5NRrHiS6I3CrrbpXGysgF1Kicx-Ip',
"cache-control": "no-cache",
"content-type": "application/json;charset=UTF-8",
"origin": "https://www.temu.com",
"pragma": "no-cache",
"priority": "u=1, i",
"referer": "https://www.temu.com/search_result.html?search_key=s&search_method=user",
"sec-ch-ua": "\"Microsoft Edge\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-model": "\"\"",
"sec-ch-ua-platform": "\"Windows\"",
"sec-ch-ua-platform-version": "\"10.0.0\"",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
"x-document-referer": "https://www.temu.com/search_result.html?search_key=s&search_method=recent&refer_page_el_sn=200254&srch_enter_source=top_search_entrance_10005&refer_page_name=home&refer_page_id=10005_1744987250647_5zww89yphz&refer_page_sn=10005&_x_sessn_id=eqqzv2oa6c&prerender=1744987255814",
"x-phan-data": "0aeJx7xMxiYPiI2Sra0NzExNLC3NTYxMTcQAfCszA0NbA0MYkFAK_ECK0"
}
cookies = {
"region": "37",
"language": "zh-Hans",
"currency": "CAD",
"api_uid": "Cm08RWfruKA4rABjx8/cAg==",
"timezone": "Asia%2FShanghai",
"webp": "1",
"_nano_fp": "XpmYXqdoXpT8npToXC_Nw951mYbUNZWTNJl0jexO",
"_bee": "oz4pNbffVEJnn8MU5Pr1dw8qFoOJoanI",
"njrpl": "oz4pNbffVEJnn8MU5Pr1dw8qFoOJoanI",
"dilx": "zuITjBsRXKjoJXPt1g6hR",
"hfsc": "L3yOe4ww6Dr/15bIfQ==",
"g_state": "{\"i_l\":0}",
"_hal_tag": "AL15muzG4UiftknN5gvH6pygmIbpI6JhdTFixWgNPCf4xThlvJRyZqruJKdpX5r9MawOy/D2GrA8tcp55wBJIQ==",
"AccessToken": "5RQ46ZB4JW6UTWYDJD6WTQGO2ED7CCBGZD7ODEOJVZU6XYTCU4OA011025374956",
"user_uin": "BB5YALAEHUYP56KGEEY77Y67WEOLLATEHD4YHQBV",
"isLogin": "1744899468402",
"_u_pa": "%7B%22nrpt%22%3A0%7D",
"_ttc": "3.tQzDRmDUpWPs.1776523249",
"__cf_bm": "dNnA7_afoQWl1qy6mkBFUkTigyrJcw1s4ijLFuEPhYY-1744988148-1.0.1.1-cr2a1ty9_B6s.2vJMS0iATes.NUcWjj7Pg_dbfJskUcYT0tj4bwZtEdBcZsUSIYZmThYXi71Mc0TuXuVZDskyMJm6tm9dT7xjK.3Bvo27g0"
}
url = "https://www.temu.com/api/poppy/v1/search"
params = {
"scene": "search"
}
data = {
"scene": "search",
"pageSn": 10099,
"offset": 0,
"listId": "84764efff7b74b7aa2785f22bf59d4d3",
"pageSize": 120,
"query": "s",
"filterItems": "",
"searchMethod": "user",
"disableCorrect": False
}

data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers,cookies=cookies, params=params, data=data,
             proxies={'http': '127.0.0.1:33210', 'https': '127.0.0.1:33210'})
print(response.text)


