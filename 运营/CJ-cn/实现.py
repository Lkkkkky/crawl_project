'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/1/24 11:33
       @Desc     : 
=========================================================   
'''
import requests
import re
import 天眼查
from loguru import logger
import csv


f=open('company.csv','a+',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['url','company_name','connect_phone','good_count','good_price','company_address'])
# csv_writer.writeheader()

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://cjdropshipping.cn/global-warehouses?startSellPrice=0&startWarehouseInventory=1&countryCode=US&closeFilter=false&searchValue=&endWarehouseInventory=&pageNum=1&pageSize=60&verifiedWarehouse=1",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Microsoft Edge\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
}
cookies = {
    "csrfToken": "OMtzHUM3fGKJGe5jByR61enR",
    "lng": "zh",
    "language": "en|zh-CN",
    "googtrans": "/en/zh-CN",
    "_ati": "2448290605886",
    "_gcl_au": "1.1.670538121.1737689126",
    "_clck": "zv8uu%7C2%7Cfsu%7C0%7C1850",
    "anonymousToken": "e79140db2252201fae32e66d86c445088fae76c16fe24833f65e56ca7eb60680",
    "loginName": "amluZzMzMzM=",
    "token": "VVNSQENKMzg4MTA5NkBDTjo5NzU5ODQyMjZiYzM0MGJmOTZkZWEyNWJiYjYyYzJlZTE=",
    "name": "6ZOg6ZizIOadjg==",
    "firstName": "6ZOg6Ziz",
    "lastName": "5p2O",
    "email": "amluZzM2NjY2QDE2My5jb20=",
    "phone": "ODYtMTc4MTk0NjE5ODQ=",
    "relateSalesman": "QW5keSBDaG91",
    "salesmanId": "Mg==",
    "cjLoginName": "jing3333",
    "accessToken": "USR@CJ3881096@CN:eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJDSjM4ODEwOTYsZmFsc2UiLCJpbmZvIjp7InVzZXJJZCI6IjE4ODI2MzA5NDc1MTg4MTYyNTYiLCJ0b0NqRXJwSWQiOm51bGwsInRvQ2pGbG93ZXJOYW1lIjpudWxsLCJpbnRlcm5hbEVtcGxveWVlSWQiOm51bGwsImludGVybmFsRW1wbG95ZWVOYW1lIjpudWxsLCJzdWJVc2VySWQiOm51bGwsImNvZFN0YXR1cyI6bnVsbCwic3lzdGVtIjoiQ04iLCJwbGF0Zm9ybSI6MTh9LCJpYXQiOjE3Mzc2ODkxNzAsImV4cCI6MTc2ODc5MzE3MH0.Qf8hDlXm0MUByB_OTz5krpUnUJmvj2pJAro3fiONLcI",
    "cjLoginToken": "USR@CJ3881096@CN:975984226bc340bf96dea25bbb62c2ee1",
    "vip": "0",
    "userId": "MTg4MjYzMDk0NzUxODgxNjI1Ng==",
    "avatar": "https://cc-west-usa.oss-us-west-1.aliyuncs.com/ba627238-87d7-41a9-86f1-960b4cc07ebf.png",
    "emailVerifyStatus": "3",
    "isFirstLogin": "0",
    "loginTime": "1737689172102",
    "memberLevelTagType": "Free",
    "plusExpirationTime": "1737689172102",
    "num": "CJ3881096",
    "moneyLevelType": "1",
    "SHOWMESSAGE": "NsK",
    "_ga_SXFZSX9SSV": "GS1.1.1737689126.1.1.1737689172.14.0.1617679913",
    "_gid": "GA1.2.693285855.1737689178",
    "_ga": "GA1.1.1407585401.1737689128",
    "_ga_LNWM1Y68DD": "GS1.2.1737689178.1.0.1737689180.0.0.0",
    "currency": "currency%253DUSD%253BNAME%253D%25E7%25BE%258E%25E5%2585%2583%253BID%253DCN%253Bsymbol%253D%2524%253Brate%253D1",
    "temp-agent-flag": "1",
    "_clsk": "1kl64nt%7C1737689208167%7C4%7C1%7Cl.clarity.ms%2Fcollect",
    "_uetsid": "dc63ad50da0211ef881a795753b5b1a9",
    "_uetvid": "dc63c700da0211ef897847c26dee3015",
    "_ga_2FHGJ78Y24": "GS1.1.1737689133.1.1.1737689426.0.0.0",
    "_ga_S2Q09M5ZGM": "GS1.1.1737689133.1.1.1737689426.0.0.0"
}
company_name_list = []
def get_company_info(id_list):

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://cjdropshipping.cn/global-warehouses?startSellPrice=0&startWarehouseInventory=1&countryCode=US&closeFilter=false&searchValue=&endWarehouseInventory=&pageNum=1&pageSize=60&verifiedWarehouse=1",
        "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Microsoft Edge\";v=\"132\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
    }
    cookies = {
        "csrfToken": "OMtzHUM3fGKJGe5jByR61enR",
        "lng": "zh",
        "language": "en|zh-CN",
        "googtrans": "/en/zh-CN",
        "_ati": "2448290605886",
        "_gcl_au": "1.1.670538121.1737689126",
        "_clck": "zv8uu%7C2%7Cfsu%7C0%7C1850",
        "anonymousToken": "e79140db2252201fae32e66d86c445088fae76c16fe24833f65e56ca7eb60680",
        "loginName": "amluZzMzMzM=",
        "token": "VVNSQENKMzg4MTA5NkBDTjo5NzU5ODQyMjZiYzM0MGJmOTZkZWEyNWJiYjYyYzJlZTE=",
        "name": "6ZOg6ZizIOadjg==",
        "firstName": "6ZOg6Ziz",
        "lastName": "5p2O",
        "email": "amluZzM2NjY2QDE2My5jb20=",
        "phone": "ODYtMTc4MTk0NjE5ODQ=",
        "relateSalesman": "QW5keSBDaG91",
        "salesmanId": "Mg==",
        "cjLoginName": "jing3333",
        "accessToken": "USR@CJ3881096@CN:eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJDSjM4ODEwOTYsZmFsc2UiLCJpbmZvIjp7InVzZXJJZCI6IjE4ODI2MzA5NDc1MTg4MTYyNTYiLCJ0b0NqRXJwSWQiOm51bGwsInRvQ2pGbG93ZXJOYW1lIjpudWxsLCJpbnRlcm5hbEVtcGxveWVlSWQiOm51bGwsImludGVybmFsRW1wbG95ZWVOYW1lIjpudWxsLCJzdWJVc2VySWQiOm51bGwsImNvZFN0YXR1cyI6bnVsbCwic3lzdGVtIjoiQ04iLCJwbGF0Zm9ybSI6MTh9LCJpYXQiOjE3Mzc2ODkxNzAsImV4cCI6MTc2ODc5MzE3MH0.Qf8hDlXm0MUByB_OTz5krpUnUJmvj2pJAro3fiONLcI",
        "cjLoginToken": "USR@CJ3881096@CN:975984226bc340bf96dea25bbb62c2ee1",
        "vip": "0",
        "userId": "MTg4MjYzMDk0NzUxODgxNjI1Ng==",
        "avatar": "https://cc-west-usa.oss-us-west-1.aliyuncs.com/ba627238-87d7-41a9-86f1-960b4cc07ebf.png",
        "emailVerifyStatus": "3",
        "isFirstLogin": "0",
        "loginTime": "1737689172102",
        "memberLevelTagType": "Free",
        "plusExpirationTime": "1737689172102",
        "num": "CJ3881096",
        "moneyLevelType": "1",
        "SHOWMESSAGE": "NsK",
        "_ga_SXFZSX9SSV": "GS1.1.1737689126.1.1.1737689172.14.0.1617679913",
        "_gid": "GA1.2.693285855.1737689178",
        "_ga": "GA1.1.1407585401.1737689128",
        "_ga_LNWM1Y68DD": "GS1.2.1737689178.1.0.1737689180.0.0.0",
        "currency": "currency%253DUSD%253BNAME%253D%25E7%25BE%258E%25E5%2585%2583%253BID%253DCN%253Bsymbol%253D%2524%253Brate%253D1",
        "temp-agent-flag": "1",
        "_clsk": "1kl64nt%7C1737689208167%7C4%7C1%7Cl.clarity.ms%2Fcollect",
        "_uetsid": "dc63ad50da0211ef881a795753b5b1a9",
        "_uetvid": "dc63c700da0211ef897847c26dee3015",
        "_ga_2FHGJ78Y24": "GS1.1.1737689133.1.1.1737689426.0.0.0",
        "_ga_S2Q09M5ZGM": "GS1.1.1737689133.1.1.1737689426.0.0.0"
    }
    for id in id_list:
        url = f"https://www.cjdropshipping.cn/product/1600-ml-cooling-water-kettle-tea-pot-coffee-pot-with-4-cups-large-capacity-water-kettle-set-p-{id}.html"
        response = requests.get(url, headers=headers, cookies=cookies)
        # print(response.text)
        try:
            company_name=re.findall("\"supplierName\":\"(.*?)\"",response.text)[0]
            good_count=re.findall("\"totalInventory\":(.*?),",response.text)[0]
            good_price=re.findall("\"sellPrice\":\"(.*?)\"",response.text)[0]
        except Exception as e:
            company_name=''
            good_count=''
            good_price=''
        if (company_name!=''):
            print(company_name)
            if (company_name not in company_name_list):
                try:
                    company_address,connect_phone=天眼查.get_info(company_name)
                except Exception as e:
                    connect_phone='暂无'
                    company_address='暂无'
                format_dict = {
                    "url":url,
                    "company_name": company_name,
                    "connect_phone":connect_phone,
                    "good_count": good_count,
                    "good_price": good_price,
                    "company_address":company_address
                }
                print('写入',format_dict)
                csv_writer.writerow(format_dict)
                company_name_list.append(company_name)
                print(company_name_list)
for i in range(55,100):
    id_list = []
    url = "https://cjdropshipping.cn/global-warehouses"
    params = {
        "startSellPrice": "0",
        "startWarehouseInventory": "1",
        "countryCode": "US",
        "closeFilter": "false",
        "searchValue": "",
        "endWarehouseInventory": "",
        "pageNum": str(i),
        "pageSize": "60",
        "verifiedWarehouse": ""
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    logger.info(f'正在爬取第{i}页的内容')
    pattern = r'"id":\s*"([^"]+)",\s*"nameEn":'
    # 匹配所有符合条件的 id 和 className
    new_id_list = re.findall(pattern, response.text)
    id_list.extend(new_id_list)
    print(id_list)
    get_company_info(id_list)
    print(len(id_list))

# get_company_name('1849394281921269760')
# print(len(id_list))

