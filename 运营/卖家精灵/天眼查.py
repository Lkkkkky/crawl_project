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
    "Referer": "https://www.tianyancha.com/nsearch?key=%E7%89%9B%E5%95%8A",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "TYCID": "fb562c70733e11efaf3d9f3cb0cb3e6b",
    "CUID": "896180ecfaa6240e13f9370db34653eb",
    "ssuid": "3183649984",
    "_ga": "GA1.2.332962379.1726389985",
    "HWWAFSESID": "c1312cd44ad98513d0",
    "HWWAFSESTIME": "1735607638488",
    "csrfToken": "5edFXBvqnqKz_isf-y-Yirgv",
    "jsid": "SEO-BING-ALL-SY-000001",
    "Hm_lvt_e92c8d65d92d534b0fc290df538b4758": "1735607643",
    "HMACCOUNT": "4D4F61CE5656C745",
    "bannerFlag": "true",
    "searchSessionId": "1735635486.87302986",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%228312271%22%2C%22first_id%22%3A%22191f4dc9b07a67-03908a380bcc96e-4c657b58-2073600-191f4dc9b08541%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxZjRkYzliMDdhNjctMDM5MDhhMzgwYmNjOTZlLTRjNjU3YjU4LTIwNzM2MDAtMTkxZjRkYzliMDg1NDEiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI4MzEyMjcxIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%228312271%22%7D%2C%22%24device_id%22%3A%22191f4dc9b07a67-03908a380bcc96e-4c657b58-2073600-191f4dc9b08541%22%7D",
    "tyc-user-info": "%7B%22state%22%3A%223%22%2C%22vipManager%22%3A%220%22%2C%22mobile%22%3A%2218918278888%22%2C%22userId%22%3A%228312271%22%2C%22isExpired%22%3A%220%22%7D",
    "tyc-user-info-save-time": "1735635910005",
    "auth_token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODkxODI3ODg4OCIsImlhdCI6MTczNTYzNTkwOSwiZXhwIjoxNzM4MjI3OTA5fQ.1iNncC-V-ubu3XxWujHvw-ipIZoXe5ddZDswfhcM-PLHyz9x45PL7GgbtDvk7255fsOMtC-gJrAXzdQsWDEaFQ",
    "Hm_lpvt_e92c8d65d92d534b0fc290df538b4758": "1735635911"
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
    dict={}
    for index,i in enumerate(companyList):
        try:
            name=i.get('name').replace('<em>', '').replace('</em>', '')
            name = i.get('name')
            loc = i.get('regLocation')
            phonelist = i.get('phoneList')
            alias=i['multiMatchField'][0]['content'].replace('<em>', '').replace('</em>', '')
        except:
            name = ''
            loc = ''
            phonelist = ''
            alias='暂无'
        format_dict={
            index:{
            '天眼查|企业昵称':name,
            '天眼查|联系地址':loc,
            'phoneList':phonelist,
            # 'alias':alias,
        }
        }
        if format_dict[index]['天眼查|企业昵称'] != '':
            dict.update(format_dict)
            # print(format_dict)
    return dict

get_info('Jinjiang Siyi Trading Co., LTD')
    # print(res_json.get('props.pageProps.dehydratedState.queries[2].state.data.data.companyList'))

