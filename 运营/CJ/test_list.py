'''
=========================================================    
       @File     : test_list.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/4 16:27
       @Desc     : 
=========================================================   
'''
import requests
import re

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.cjdropshipping.com/list/wholesale-all-categories-l-all.html?pageNum=43&from=US&startSellPrice=&endSellPrice=&feildType=1&isAsc=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
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
    "cookieyes-consent": "consentid:UmtXc0hodzM4VVBydVMxZE4wTUVVVUw5Uk95ck5lMWM,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes",
    "_clsk": "dl55bz%7C1733298400260%7C5%7C1%7Ch.clarity.ms%2Fcollect",
    "_uetsid": "09e299d0b20f11efbe6ddfa6c45b51ac",
    "_uetvid": "09e2c7f0b20f11ef86be8bab384ad523",
    "_gat_gtag_UA_88409817_1": "1",
    "_ga": "GA1.1.1849155638.1733295415",
    "_ga_SXFZSX9SSV": "GS1.1.1733295414.1.1.1733298530.53.0.459606264",
    "_ga_S2Q09M5ZGM": "GS1.1.1733295415.1.1.1733298530.0.0.0",
    "_ga_2FHGJ78Y24": "GS1.1.1733295415.1.1.1733298530.0.0.0"
}
url = "https://www.cjdropshipping.com/list/wholesale-all-categories-l-all.html"
params = {
    "pageNum": "43",
    "from": "US",
    "startSellPrice": "",
    "endSellPrice": "",
    "feildType": "1",
    "isAsc": "0"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
pattern = r'"id":\s*"([^"]+)",\s*"nameEn":'

# 匹配所有符合条件的 id 和 className
matches = re.findall(pattern, response.text)
print(matches)
# print(response.text)
# print(response)