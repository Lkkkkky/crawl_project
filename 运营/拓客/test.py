'''
=========================================================    
       @File     : test.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/5 15:00
       @Desc     : 
=========================================================   
'''
import requests

import json
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "multipart/form-data",
    "origin": "https://logistics.tungee.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://logistics.tungee.com/customer-group/amazon?mode=0&page=1&size=50&tab=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
cookies = {
    "DISTINCT_ID": "8b42af73-7b90-49e8-b9cb-60a6f32f2230",
    "Hm_lvt_d6df51ae5ec3a1b64d27905896d77ba5": "1733371195",
    "HMACCOUNT": "A24447EF7B46DD9D",
    "__last_enter_version": "logistics",
    "_co_i": "6437da3f6eceb92bef8936bd",
    "__wpkreporterwid_": "ee5d56d2-b1c7-455b-bc24-66f19af36550",
    "tg_referrer_source": "https%3A%2F%2Fuser.tungee.com%2F",
    "SecurityCenterDuId": "IlpNZVQ4ZHlwUVhIRTIrbCtGek0wSkJFPSI.GjLhig.dA9H9LhqWVB-YKt4FdfGKGOdub8",
    "acw_tc": "c39d74ce10961a172596aa929c56d7658bccb576ee591259d6a51d3199861a98",
    "Hm_lpvt_d6df51ae5ec3a1b64d27905896d77ba5": "1733382163",
    "accountCenterSessionId": ".eJwlj0trwzAQhP-LzjmsHivZPvtYqxTShvhiVtIKJ7VdsJ2mD_rfK9rTMDDDfPMthrzyNopmX298EMMliUZgRbYKzoIzyhlTG6M5ONbIBFmjBTbaRiOzkdEhlCySMUUlSGDOWmrrakchZ2WDQiRSkGQsqWCCI1TBJU0xyYQ1VlqlyijAXNZUUkDiIOJIy8JTgblzKH77A_PX_tofI_rTeT-r7u4_AR7bND8cx7lvn3d_evro2pepm_3sv6bXUlyY07DROw_725CCaDJNW3l623j9f2sdSgQgy5FDrQLEKtiYk_j5BY2yVKw.GjLhlw.4bgseE9hvfgQgrakYASHMAPqOzQ",
    "CGISessionId": "eyJzaWQiOiJOalpqWlRjNU5XWXRZMk13TnkwME9EZG1MVGhtWkRVdE5XUXhNRFZsTW1ObU56bGsiLCJjaGFubmVsIjoid2ViIiwiX2ZyZXNoIjpmYWxzZX0.Z1FQFw.YuFKOE0-lD3b_p8emAQUF0sbbvU"
}
url = "https://logistics.tungee.com/cgi/logistics-data/api/logistics-amazon/search"
data = {
    "------WebKitFormBoundarycb7B4iXqecfyKq9y\\r\nContent-Disposition: form-data; name": "\"mode\"\\r\n\\r\n0\\r\n------WebKitFormBoundarycb7B4iXqecfyKq9y\\r\nContent-Disposition: form-data; name=\"begin\"\\r\n\\r\n0\\r\n------WebKitFormBoundarycb7B4iXqecfyKq9y\\r\nContent-Disposition: form-data; name=\"end\"\\r\n\\r\n50\\r\n------WebKitFormBoundarycb7B4iXqecfyKq9y\\r\nContent-Disposition: form-data; name=\"filter\"\\r\n\\r\n{\"deliveryMethod\":\"含自发货\",\"amazon_stations\":[\"美国站\"]}\\r\n------WebKitFormBoundarycb7B4iXqecfyKq9y--\\r\n"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)
# res_json=json.loads(response.text)
# company_list=res_json['data']['items']
# for index in company_list:
#     categoriesList=index['entAmazonGoodsCategoriesShow']
#     cate_arr=[]
#     for i in categoriesList:
#        cate_arr.append(i['showSecondClassify'])
#     dict={
#     'company_name': index['lead']['enterprise_name'],#公司名称
#     "address":index['address.value'],#地址
#     'site':index['entAmazonSiteInfo'],#品类
#     'company_id':index['_id'],#公司id
#     'CategoriesShow':','.join(cate_arr),#类目
#     'SalesLevel':index['entAmazonSalesLevel']#销量情况
#     }
#     print(dict)

print(response.text)
print(response)