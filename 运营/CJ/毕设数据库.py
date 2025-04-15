import requests
import re
import json

# 目标 URL

import json

# 提供的 JSON 数据（注意这是一个字符串）
# data = """
# {
#     "pageSize": "60",
#     "pageNumber": "1",
#     "totalRecords": "53",
#     "totalPages": "1",
#     "content": [{
#         "productList": [{
#             "id": "1795412901558636544",
#             "nameEn": "25 New Cartoon Animal Dog Series Hole Shoes, Flower Shoes, Buckle Accessories, Cute Garden Shoes Decoration",
#             "sku": "CJNT2048128",
#             "isCollect": 0,
#             "listedNum": 24,
#             "bigImage": "https:\\u002F\\u002Fcf.cjdropshipping.com\\u002F4137483e-36c2-49da-b73d-d4a4e069f7c3.jpg",
#             "sellPrice": "7.26",
#             "nowPrice": null,
#             "authorityStatus": null,
#             "addMarkStatus": 1,
#             "isVedio": 0,
#             "productType": "5",
#             "isAut": null,
#             "categoryId": "D91A4505-6495-4DFD-9984-C8E728913127",
#             "threeCategoryName": null,
#             "twoCategoryId": null,
#             "twoCategoryName": null,
#             "oneCategoryId": null,
#             "oneCategoryName": null,
#             "directMinOrderNum": null,
#             "supplierName": null,
#             "zoneRecommendJson": null,
#             "createAt": null,
#             "setRecommendedTime": null,
#             "autStatus": "1",
#             "isList": 0,
#             "isAd": 0,
#             "activityId": null,
#             "isPersonalized": 0,
#             "saleStatus": null,
#             "syncListedProductStatus": null,
#             "videoList": [],
#             "deliveryCycle": null,
#             "warehouseInventoryNum": "500",
#             "discountPrice": null,
#             "discountPriceRate": null,
#             "myProduct": false,
#             "monthSold": null,
#             "currency": null,
#             "totalVerifiedInventory": null,
#             "totalUnVerifiedInventory": null,
#             "verifiedWarehouse": 2,
#             "image": "https:\\u002F\\u002Fcf.cjdropshipping.com\\u002F4137483e-36c2-49da-b73d-d4a4e069f7c3.jpg",
#             "listCount": 24,
#             "name": "25 New Cartoon Animal Dog Series Hole Shoes, Flower Shoes, Buckle Accessories, Cute Garden Shoes Decoration",
#             "originPrice": null,
#             "videoId": undefined,
#             "isPod": false,
#             "isFree": true,
#             "addedMyProduct": false
#         }]
#     }]
# }
# """
import requests

def CJ_get_goods_info():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://www.cjdropshipping.com/search/boy.html",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }
    cookies = {
        "lng": "zh",
        "language": "en|zh-CN",
        "country": "AF",
        "hasYindao": "1",
        "cookieyes-consent": "consentid:c09FV3BGQ2J5cm5hdk5kSkx4U1UzeUlicHU0aTNCbzA,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes",
        "googtrans": "/en/zh-CN",
        "_ati": "8647380326590",
        "_ga_LNWM1Y68DD": "GS1.2.1733294097.1.0.1733294097.0.0.0",
        "_gcl_au": "1.1.907253351.1733293995.1071071093.1733294078.1733294111",
        "_fbp": "fb.1.1733309857366.797166116482729466",
        "_ga": "GA1.1.404617654.1733293989",
        "_tt_enable_cookie": "1",
        "_ttp": "sxkFDZMLnEYLdiPwz3UPcT-FO88.tt.1",
        "csrfToken": "O8nEymi1zPvL7IDr2A8MXScS",
        "currency": "currency%253DUSD%253BNAME%253D%25E7%25BE%258E%25E5%2585%2583%253BID%253DCN%253Bsymbol%253D%2524%253Brate%253D1",
        "temp-agent-flag": "1",
        "anonymousToken": "039645b686eac1a96a00c5684c379bb497d4201e35a667b5678cdd38562e9d2f",
        "_clck": "tp4n0q%7C2%7Cfsf%7C0%7C1799",
        "SHOWMESSAGE": "Ns",
        "loginName": "amluZzM=",
        "token": "VVNSQENKMzc1MjkzMEBDSjplMTRkYjA2MWYwMzQ0OWRhOWE4NzMwMjY5N2EyM2RhYzE=",
        "name": "bCBreQ==",
        "firstName": "bA==",
        "lastName": "a3k=",
        "email": "MTE1ODM1NjAwMUBxcS5jb20=",
        "phone": "ODYtMTc4OTY2ODY4MzE=",
        "relateSalesman": "V2FsdG9u",
        "salesmanId": "YjQ4Mjk5ODMzMzNlNGU3MjllZjBkMjgyNjk0MmNlN2I=",
        "cjLoginName": "jing3",
        "accessToken": "USR@CJ3752930@CJ:eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJDSjM3NTI5MzAsZmFsc2UiLCJpbmZvIjp7InVzZXJJZCI6IjE4NjQxOTY2NTg5MjIwMDQ0ODAiLCJ0b0NqRXJwSWQiOm51bGwsInRvQ2pGbG93ZXJOYW1lIjpudWxsLCJpbnRlcm5hbEVtcGxveWVlSWQiOm51bGwsImludGVybmFsRW1wbG95ZWVOYW1lIjpudWxsLCJzdWJVc2VySWQiOm51bGwsImNvZFN0YXR1cyI6bnVsbCwic3lzdGVtIjoiQ0oiLCJwbGF0Zm9ybSI6Mn0sImlhdCI6MTczNjQwNDI2NCwiZXhwIjoxNzY3NTA4MjY0fQ.Bj2AEgkhS97grsZ0r0_KfB1FcMWiCOZ5OlDPmSEozac",
        "cjLoginToken": "USR@CJ3752930@CJ:e14db061f03449da9a87302697a23dac1",
        "vip": "0",
        "userId": "MTg2NDE5NjY1ODkyMjAwNDQ4MA==",
        "avatar": "https://cc-west-usa.oss-us-west-1.aliyuncs.com/ba627238-87d7-41a9-86f1-960b4cc07ebf.png",
        "emailVerifyStatus": "1",
        "isFirstLogin": "0",
        "loginTime": "1736404266879",
        "memberLevelTagType": "Free",
        "plusExpirationTime": "1736404266879",
        "num": "CJ3752930",
        "moneyLevelType": "1",
        "specifyVisible": "1",
        "_clsk": "1yram32%7C1736404273964%7C5%7C1%7Ca.clarity.ms%2Fcollect",
        "recommendSKU": "[]",
        "recommendSKU.sig": "95lW94ENGZ7lqKo9LL_P7RYnGZyLS6e-nUDLw4USPQ8",
        "searchHit": "serviceDefaultSort:0",
        "searchHit.sig": "9I7Vq6x_eWGolXkpeggOci6EkuTQf88Wnv8OFABMBYc",
        "_ga_SXFZSX9SSV": "GS1.1.1736404148.8.1.1736404283.12.0.205556663",
        "_uetsid": "081d7640ce5311ef8332bf7337f6ea92",
        "_uetvid": "75d17160b20911ef9bcd131640f7417f",
        "_ga_2FHGJ78Y24": "GS1.1.1736404148.8.1.1736404283.0.0.0",
        "_ga_S2Q09M5ZGM": "GS1.1.1736404149.8.1.1736404283.0.0.0",
        "menuCollapsed": "true"
    }
    url = "https://www.cjdropshipping.com/search/boy.html"
    response = requests.get(url, headers=headers, cookies=cookies)

    data=re.findall('window.PRODUCTSRES=(.*?)\swindow.category=',response.text)[0]

    data = data.replace("undefined", "null")

    parsed_data = json.loads(data)  # 转换为字典
    # print(parsed_data)
    for i in parsed_data['content'][0]['productList']:
        good_id=i['id']
        good_url=f"https://www.cjdropshipping.com/product/1600-ml-cooling-water-kettle-tea-pot-coffee-pot-with-4-cups-large-capacity-water-kettle-set-p-{good_id}.html"
        insert_product(i['nameEn'], i['sellPrice'], good_url,'CJ')




