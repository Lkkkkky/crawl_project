'''
=========================================================
       @File     : CJ.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/4 14:37
       @Desc     :
=========================================================
'''
import requests
import re
import csv
import 企查查实现
from loguru import logger
f=open('company.csv','w',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['url','company_name','connect_phone','good_count','good_price','company_address'])
csv_writer.writeheader()

def get_list():
    for i in range(44):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "referer": "https://www.cjdropshipping.com/list/wholesale-all-categories-l-all.html?pageNum=1&from=US&startSellPrice=&endSellPrice=&feildType=0&isAsc=0",
            "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
        cookies = {
            "csrfToken": "ri2WaP3IgKOxEujIlsanzbKv",
            "lng": "zh",
            "language": "en|zh-CN",
            "currency": "currency%253DUSD%253BNAME%253D%25E7%25BE%258E%25E5%2585%2583%253BID%253DCN%253Bsymbol%253D%2524%253Brate%253D1",
            "temp-agent-flag": "1",
            "country": "AF",
            "hasYindao": "1",
            "anonymousToken": "5851c366296e9d2d0a7321c4acf915c099f4bf3d9e7caf0e5aeee3b2a0a0d50c",
            "cookieyes-consent": "consentid:UmtXc0hodzM4VVBydVMxZE4wTUVVVUw5Uk95ck5lMWM,consent:no,action:,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no,other:no",
            "SHOWMESSAGE": "Ns",
            "loginName": "amluZzM=",
            "token": "VVNSQENKMzc1MjkzMEBDSjphMzI0NWM4ODk0Yzk0NTMwOWNhMTVhYjkxYTZiYjk1NjE=",
            "name": "bCBreQ==",
            "firstName": "bA==",
            "lastName": "a3k=",
            "email": "MTE1ODM1NjAwMUBxcS5jb20=",
            "phone": "ODYtMTc4OTY2ODY4MzE=",
            "relateSalesman": "QW5keSBDaG91",
            "salesmanId": "Mg==",
            "cjLoginName": "jing3",
            "accessToken": "USR@CJ3752930@CJ:eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJDSjM3NTI5MzAsZmFsc2UiLCJpbmZvIjp7InVzZXJJZCI6IjE4NjQxOTY2NTg5MjIwMDQ0ODAiLCJ0b0NqRXJwSWQiOm51bGwsInRvQ2pGbG93ZXJOYW1lIjpudWxsLCJpbnRlcm5hbEVtcGxveWVlSWQiOm51bGwsImludGVybmFsRW1wbG95ZWVOYW1lIjpudWxsLCJzdWJVc2VySWQiOm51bGwsImNvZFN0YXR1cyI6bnVsbCwic3lzdGVtIjoiQ0oiLCJwbGF0Zm9ybSI6Mn0sImlhdCI6MTczMzI5NTAzOCwiZXhwIjoxNzY0Mzk5MDM4fQ.s13hHPdf-vBpezY43ppilLesmIzF4Is7LRI6_HWHyUU",
            "cjLoginToken": "USR@CJ3752930@CJ:a3245c8894c945309ca15ab91a6bb9561",
            "vip": "0",
            "userId": "MTg2NDE5NjY1ODkyMjAwNDQ4MA==",
            "avatar": "https://cc-west-usa.oss-us-west-1.aliyuncs.com/ba627238-87d7-41a9-86f1-960b4cc07ebf.png",
            "isFirstLogin": "0",
            "loginTime": "1733295039859",
            "memberLevelTagType": "Free",
            "plusExpirationTime": "1733295039859",
            "num": "CJ3752930",
            "moneyLevelType": "1",
            "specifyVisible": "1",
            "JSESSIONID": "E95450E0836AB3272401675DFDBFE309",
            "recommendSKU": "[]",
            "recommendSKU.sig": "95lW94ENGZ7lqKo9LL_P7RYnGZyLS6e-nUDLw4USPQ8",
            "_ati": "4317530739591",
            "emailVerifyStatus": "1"
        }
        url = "https://www.cjdropshipping.com/list/wholesale-all-categories-l-all.html"
        params = {
            "pageNum": str(i),
            "from": "US",
            "startSellPrice": "",
            "endSellPrice": "",
            "feildType": "1",
            "isAsc": "0"
        }
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        pattern = r'"id":\s*"([^"]+)",\s*"nameEn":'
        # 匹配所有符合条件的 id 和 className
        new_id_list = re.findall(pattern, response.text)
        id_list.extend(new_id_list)
        print(id_list)
# print(id_list)
def get_company_info(id_list):
    company_name_list = []
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "csrfToken": "ri2WaP3IgKOxEujIlsanzbKv",
        "lng": "zh",
        "language": "en|zh-CN",
        "currency": "currency%253DUSD%253BNAME%253D%25E7%25BE%258E%25E5%2585%2583%253BID%253DCN%253Bsymbol%253D%2524%253Brate%253D1",
        "temp-agent-flag": "1",
        "country": "AF",
        "hasYindao": "1",
        "anonymousToken": "5851c366296e9d2d0a7321c4acf915c099f4bf3d9e7caf0e5aeee3b2a0a0d50c",
        "SHOWMESSAGE": "Ns",
        "loginName": "amluZzM=",
        "token": "VVNSQENKMzc1MjkzMEBDSjphMzI0NWM4ODk0Yzk0NTMwOWNhMTVhYjkxYTZiYjk1NjE=",
        "name": "bCBreQ==",
        "firstName": "bA==",
        "lastName": "a3k=",
        "email": "MTE1ODM1NjAwMUBxcS5jb20=",
        "phone": "ODYtMTc4OTY2ODY4MzE=",
        "relateSalesman": "QW5keSBDaG91",
        "salesmanId": "Mg==",
        "cjLoginName": "jing3",
        "accessToken": "USR@CJ3752930@CJ:eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJDSjM3NTI5MzAsZmFsc2UiLCJpbmZvIjp7InVzZXJJZCI6IjE4NjQxOTY2NTg5MjIwMDQ0ODAiLCJ0b0NqRXJwSWQiOm51bGwsInRvQ2pGbG93ZXJOYW1lIjpudWxsLCJpbnRlcm5hbEVtcGxveWVlSWQiOm51bGwsImludGVybmFsRW1wbG95ZWVOYW1lIjpudWxsLCJzdWJVc2VySWQiOm51bGwsImNvZFN0YXR1cyI6bnVsbCwic3lzdGVtIjoiQ0oiLCJwbGF0Zm9ybSI6Mn0sImlhdCI6MTczMzI5NTAzOCwiZXhwIjoxNzY0Mzk5MDM4fQ.s13hHPdf-vBpezY43ppilLesmIzF4Is7LRI6_HWHyUU",
        "cjLoginToken": "USR@CJ3752930@CJ:a3245c8894c945309ca15ab91a6bb9561",
        "vip": "0",
        "userId": "MTg2NDE5NjY1ODkyMjAwNDQ4MA==",
        "avatar": "https://cc-west-usa.oss-us-west-1.aliyuncs.com/ba627238-87d7-41a9-86f1-960b4cc07ebf.png",
        "isFirstLogin": "0",
        "loginTime": "1733295039859",
        "memberLevelTagType": "Free",
        "plusExpirationTime": "1733295039859",
        "num": "CJ3752930",
        "moneyLevelType": "1",
        "specifyVisible": "1",
        "JSESSIONID": "E95450E0836AB3272401675DFDBFE309",
        "recommendSKU": "[]",
        "recommendSKU.sig": "95lW94ENGZ7lqKo9LL_P7RYnGZyLS6e-nUDLw4USPQ8",
        "_ati": "4317530739591",
        "emailVerifyStatus": "1",
        "_gcl_au": "1.1.1934565651.1733296262",
        "_gid": "GA1.2.2135623342.1733296262",
        "googtrans": "/en/zh-CN",
        "_fbp": "fb.1.1733297357193.576004769781622645",
        "_clck": "1sj9h0x%7C2%7Cfrf%7C0%7C1799",
        "_uetsid": "09e299d0b20f11efbe6ddfa6c45b51ac",
        "_uetvid": "09e2c7f0b20f11ef86be8bab384ad523",
        "_ga_SXFZSX9SSV": "GS1.1.1733295414.1.1.1733297815.52.0.459606264",
        "cookieyes-consent": "consentid:UmtXc0hodzM4VVBydVMxZE4wTUVVVUw5Uk95ck5lMWM,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes",
        "_ga_2FHGJ78Y24": "GS1.1.1733295415.1.1.1733297828.0.0.0",
        "_ga_S2Q09M5ZGM": "GS1.1.1733295415.1.1.1733297828.0.0.0",
        "_ga": "GA1.2.1849155638.1733295415",
        "_gat_gtag_UA_88409817_1": "1"
    }
    for id in id_list:
        url = f"https://www.cjdropshipping.com/product/1600-ml-cooling-water-kettle-tea-pot-coffee-pot-with-4-cups-large-capacity-water-kettle-set-p-{id}.html"
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
                connect_phone,company_address=企查查实现.get_phone(company_name)
                format_dict = {
                    "url":url,
                    "company_name": company_name,
                    "connect_phone": connect_phone,
                    "good_count": good_count,
                    "good_price": good_price,
                    "company_address": company_address
                }
                print('写入',format_dict)
                csv_writer.writerow(format_dict)
                company_name_list.append(company_name)
                print(company_name_list)
# get_company_name('1849394281921269760')
# print(len(id_list))
id_list=[]
get_list()
get_company_info(id_list)
