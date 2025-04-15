'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/31 11:20
       @Desc     : 
=========================================================   
'''
import requests
import json
import csv
import time
import 天眼查

f=open('天眼查2.csv','a+',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['company_name','天眼查|企业昵称','卖家精灵|地址','天眼查|联系地址','phoneList','品类'])
# csv_writer.writeheader()

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.sellersprite.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.sellersprite.com/v3/product-research?market=US&page=1&size=60&symbolFlag=true&monthName=bsr_sales_nearly&selectType=2&filterSub=false&weightUnit=g&order%5Bfield%5D=total_units&order%5Bdesc%5D=true&productTags=%5B%22BestSeller%22%5D&nodeIdPaths=%5B%223760911%3A19323855011%22,%223760911%3A18066620011%22,%223760911%3A19219848011%22,%223760911%3A17038387011%22,%223760911%3A23946846011%22,%223760911%3A51570011%22,%223760911%3A17242866011%22,%223760911%3A11056591%22,%223760911%3A11057241%22,%223760911%3A98174186011%22,%223760911%3A11058281%22,%223760911%3A10079992011%22,%223760911%3A3777891%22,%223760911%3A14760453011%22,%223760911%3A3778591%22,%223760911%3A11060451%22,%223760911%3A8797459011%22,%22172282%3A172541%22,%22172282%3A21608214011%3A21608216011%22,%22172282%3A21608214011%3A10063711011%22,%22172282%3A21608214011%3A18007817011%22,%22172282%3A172623%22,%22172282%3A300334%22,%221055398%3A3610841%3A2422430011%22,%221055398%3A3610841%3A2422451011%22,%221055398%3A3610841%3A2423187011%22,%221055398%3A3610841%3A16175642011%22,%223375251%3A2614635011%22,%223375251%3A706814011%3A11443874011%22%5D&sellerTypes=%5B%22FBM%22,%22FBA%22%5D&dimensionTypeList=%5B%5D&sellerNationList=%5B%22CN%22%5D&video=",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "_ga": "GA1.1.1725716021.1733292510",
    "_gcl_au": "1.1.1354440191.1733292511",
    "_fp": "c73c65c6f28d1cdc1884fe35ef171e7e",
    "MEIQIA_TRACK_ID": "2pjvtfvzpBjFTs0idlvI5OYc5Mr",
    "MEIQIA_VISIT_ID": "2pjvtanIVUCBKYsJRffmAQRhCvp",
    "current_guest": "NIMEXkHCzXlB_241231-116108",
    "Hm_lvt_e0dfc78949a2d7c553713cb5c573a486": "1735614457",
    "HMACCOUNT": "4D4F61CE5656C745",
    "ecookie": "hajuY9O6OALNPsFP_CN",
    "065346b796c5567d93f7": "0789e80265dfd27da83c93b1daa7bc6b",
    "_gaf_N1": "414bf101d975533ae7f3112db480ac90",
    "_gaf_fp": "1eac88d094a75804a8a735503d2b81c7",
    "rank-login-user": "5762765371od93uOgn3+e3JxbtLuwjQrbKaINPsu5tKywnyDqHaEBvqJbNv/6NoSQ6MgBi16+s",
    "rank-login-user-info": "eyJuaWNrbmFtZSI6IumYs+mYsyIsImlzQWRtaW4iOmZhbHNlLCJhY2NvdW50IjoiMTczKioqKjY3NjkiLCJ0b2tlbiI6IjU3NjI3NjUzNzFvZDkzdU9nbjMrZTNKeGJ0THV3alFyYkthSU5Qc3U1dEt5d255RHFIYUVCdnFKYk52LzZOb1NRNk1nQmkxNitzIn0=",
    "Sprite-X-Token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjE2Nzk5NjI2YmZlMDQzZTBiYzI5NTEwMTE4ODA3YWExIn0.eyJqdGkiOiJTaElCNnFmVlA1X1BsMEJNT096akp3IiwiaWF0IjoxNzM1NjE1MDc1LCJleHAiOjE3MzU3MDE0NzUsIm5iZiI6MTczNTYxNTAxNSwic3ViIjoieXVueWEiLCJpc3MiOiJyYW5rIiwiYXVkIjoic2VsbGVyU3BhY2UiLCJpZCI6NDY5MjQsInBpIjpudWxsLCJubiI6IumYs-mYsyIsInN5cyI6IlNTX0NOIiwiZWQiOiJOIiwicGhuIjoiMTczNjAwODY3NjkiLCJlbSI6IjUwNDY5OTI1N0BxcS5jb20iLCJtbCI6IlYiLCJlbmQiOjE3NjMyNjMwNzU0MTV9.WHul4qJWl5nHJ-tpMfUtVtBRArqXICy2lWK__kh3-UmpwNLu1K5tRHPne96NI1I2p2xDdaa0SwMQdPf__w7bweHooyQxzDqxX0yzw77WKkm1FRD1FS2lsui5s0mc6B7_7Pg2hoq66sr5KVONfVkmXBofQxLW1o3cST6obA9nwaH3__5Zbbhq6OHWNiPcPvCVdK9sp9lcv8Vu_t_CPVVAajKRgEoRpvYyIHr1AiUc08Kgn9DEn7gvnmJY5M3JZhH4BJUsEZTah9Tfo-Nz1mekok7nalKnUBoZaeW_PgBKGKd_2wEolMb0x9M-3obKDuvrB4aaEb5Yd_ClPHwUxS--6w",
    "ao_lo_to_n": "5762765371od93uOgn3+e3JxbtLuwjQjp1NB35zBEkeLbRmHjKawb1J7yw06nVDdhShUPZrsRus/W0HFxtU/ClpVn3m4HET8X49cwNcnY/N+Zt695NtGw=",
    "JSESSIONID": "F74B7988B7D7EFA381077E48EB277AD4",
    "Hm_lpvt_e0dfc78949a2d7c553713cb5c573a486": "1735615079",
    "_ga_38NCVF2XST": "GS1.1.1735614456.3.1.1735615089.38.0.1090534564",
    "_ga_CN0F80S6GL": "GS1.1.1735614604.1.1.1735615100.0.0.0"
}
name_list=[]
for p in range(3, 100):
    print(f'正在爬取第{p}页')
    url = "https://www.sellersprite.com/v3/api/product-research"
    data = {
        "market": "US",
        "page": p,
        "size": 50,
        "symbolFlag": True,
        "monthName": "bsr_sales_nearly",
        "selectType": "2",
        "filterSub": False,
        "weightUnit": "g",
        "order": {
            "field": "total_units",
            "desc": True
        },
        "productTags": [
            "BestSeller"
        ],
        "nodeIdPaths": [
            "3760911:19323855011",
            "3760911:18066620011",
            "3760911:19219848011",
            "3760911:17038387011",
            "3760911:23946846011",
            "3760911:51570011",
            "3760911:17242866011",
            "3760911:11056591",
            "3760911:11057241",
            "3760911:98174186011",
            "3760911:11058281",
            "3760911:10079992011",
            "3760911:3777891",
            "3760911:14760453011",
            "3760911:3778591",
            "3760911:11060451",
            "3760911:8797459011",
            "172282:172541",
            "172282:21608214011:21608216011",
            "172282:21608214011:10063711011",
            "172282:21608214011:18007817011",
            "172282:172623",
            "172282:300334",
            "1055398:3610841:2422430011",
            "1055398:3610841:2422451011",
            "1055398:3610841:2423187011",
            "1055398:3610841:16175642011",
            "3375251:2614635011",
            "3375251:706814011:11443874011"
        ],
        "sellerTypes": [
            "FBM",
            "FBA"
        ],
        "dimensionTypeList": [],
        "sellerNationList": [
            "CN"
        ]
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data).json()

    for i in response['data']['items']:
        if i['sellerDto']['businessName'] not in name_list:
            name_list.append(i['sellerDto']['businessName'])
            # print(i['sellerName'])
            search_result=天眼查.get_info(i['sellerDto']['businessName'])
            # print(search_result)
            if(search_result!={}):
                for t in search_result:
                    format_dict={
                        'company_name':i['sellerDto']['businessName'],
                        '天眼查|企业昵称': search_result[t]['天眼查|企业昵称'],
                        '卖家精灵|地址':i['sellerDto']['businessAddress'],
                        '天眼查|联系地址':search_result[t]['天眼查|联系地址'],
                        'phoneList':search_result[t]['phoneList'],
                        '品类': i['nodeLabelPathLocale'],
                    }
                    print(format_dict)

                    csv_writer.writerow(format_dict)
                    time.sleep(5)
    print(len(response['data']['items']))