import asyncio
import time
import csv
import websockets
import json
from curl_cffi import requests  # 假设你在用 curl_cffi 请求
from faker.generator import random

f= open('temu商详2.csv',mode='w',encoding='utf-8',newline='')
offset=0
csv_writer=csv.DictWriter(f,fieldnames=['good_title','current_sku_id','sales_num','link_url','goods_id','price_info'])

csv_writer.writeheader()

async def receive_message(websocket):

        try:
            await websocket.send('')
            print("等待浏览器发送参数...")
            msg = await websocket.recv()
            print("收到参数：", msg)
            global offset
            return  msg
        except websockets.exceptions.ConnectionClosed:
            print("连接关闭")

def get_info():
    msg=asyncio.run(receive_message())
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "anti-content": msg,
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
        "_u_pa": "%7B%22nrpt%22%3A0%7D",
        "isLogin": "1744899468402",
        "user_uin": "BB5YALAEHUYP56KGEEY77Y67WEOLLATEHD4YHQBV",
        "AccessToken": "5RQ46ZB4JW6UTWYDJD6WTQGO2ED7CCBGZD7ODEOJVZU6XYTCU4OA011025374956",
        "_ttc": "3.tQzDRmDUpWPs.1776523249",
        "__cf_bm": "BB.k.doeaPnF_xDMVSZE0kZDmUjn6N7fOXrncVsphEs-1745325490-1.0.1.1-VLiGhMXi4f1_rLkwIc378oYMckGTeSyd3Q9M.sp5kBDbq0hLPou_42WaTVIivg3pyYsFGfVZ.meOkLUTA.u7LaS6DYsiDxzqMimOcmmxapA"
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
    response = requests.post(url, headers=headers,  params=params, data=data,
                             proxies={'http': '127.0.0.1:33210', 'https': '127.0.0.1:33210'})
    print(response.text)

    offset += 80
    list = json.loads(response.text)['result']['data']['goods_list']
    for i in list:
        format_dict = {
            'good_title': i['page_alt'],
            'current_sku_id': i['current_sku_id'],
            'sales_num': i['sales_num'],  # 销量
            'link_url': 'https://www.temu.com/' + i['link_url'],
            "goods_id": i['goods_id'],
            'price_info': i['price_info']['price_str']
        }
        csv_writer.writerow(format_dict)
        print(format_dict)

    # print(response.text)
    print(response)
    time.sleep(random.randint(1, 10))
async def main():
    print("WebSocket 服务启动中...")
    async with websockets.serve(receive_message, '127.0.0.1', 1234):
        await asyncio.Future()  # 永远运行

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n服务手动关闭。")