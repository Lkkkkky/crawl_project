'''
=========================================================    
       @File     : 天眼查.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/31 09:37
       @Desc     : 
=========================================================   
'''
import time
import csv
import requests
import re
import json



headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.tianyancha.com/nsearch?key=Ke%20Liu",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Microsoft Edge\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "TYCID": "fb562c70733e11efaf3d9f3cb0cb3e6b",
    "CUID": "896180ecfaa6240e13f9370db34653eb",
    "ssuid": "3183649984",
    "_ga": "GA1.2.332962379.1726389985",
    "jsid": "SEO-BING-ALL-SY-000001",
    "HWWAFSESID": "a273d1720642cd40be0",
    "HWWAFSESTIME": "1737705818500",
    "csrfToken": "vvVV2DBUmh3jXTG8LHG9mG0s",
    "bannerFlag": "true",
    "Hm_lvt_e92c8d65d92d534b0fc290df538b4758": "1735607643,1735781416,1737705825",
    "HMACCOUNT": "4D4F61CE5656C745",
    "_gid": "GA1.2.1733773011.1737705826",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22304530888%22%2C%22first_id%22%3A%22191f4dc9b07a67-03908a380bcc96e-4c657b58-2073600-191f4dc9b08541%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxZjRkYzliMDdhNjctMDM5MDhhMzgwYmNjOTZlLTRjNjU3YjU4LTIwNzM2MDAtMTkxZjRkYzliMDg1NDEiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIzMDQ1MzA4ODgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22304530888%22%7D%2C%22%24device_id%22%3A%22191f4dc9b07a67-03908a380bcc96e-4c657b58-2073600-191f4dc9b08541%22%7D",
    "tyc-user-info": "{%22state%22:%224%22%2C%22vipManager%22:%220%22%2C%22mobile%22:%2213437891003%22%2C%22userId%22:%22304530888%22%2C%22isExpired%22:%220%22}",
    "tyc-user-info-save-time": "1737705855125",
    "auth_token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzQzNzg5MTAwMyIsImlhdCI6MTczNzcwNTg1MywiZXhwIjoxNzQwMjk3ODUzfQ.FshaGbf44bkFN6is1aywrh9EgJWF0wk0mFLHtHSfRmiaJdChZUkGXFGQdwFBqC50QYbD4xqq3MUqFDkZvNdPGg",
    "tyc-user-phone": "%255B%252213437891003%2522%255D",
    "searchSessionId": "1737705862.75306545",
    "Hm_lpvt_e92c8d65d92d534b0fc290df538b4758": "1737705867"
}

url = "https://www.tianyancha.com/nsearch"
def get_info(keyword):
    params = {
        "key": keyword
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    res=re.findall("<script id=\"__NEXT_DATA__\" type=\"application/json\">(.*?)</script>",response.text)[0]
    res_json=json.loads(res)
    # print(response.text)
    companyList=res_json['props']['pageProps']['dehydratedState']['queries'][2]['state']['data']['data']['companyList']
    for i in companyList:

        loc = i.get('regLocation')
        phonelist = i.get('phoneList')


        return loc,phonelist




    # print(res_json.get('props.pageProps.dehydratedState.queries[2].state.data.data.companyList'))

