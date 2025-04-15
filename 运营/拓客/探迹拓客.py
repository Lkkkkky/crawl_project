'''
=========================================================    
       @File     : 探迹拓客.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/5 12:10
       @Desc     : 
=========================================================   
'''
import json
import requests
import csv
from loguru import logger
import 联系方式

f=open('company.csv','w',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['company_name','address','url','phone','site','company_id','CategoriesShow','SalesLevel'])
csv_writer.writeheader()
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    # "content-type": "multipart/form-data",
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
    "__wpkreporterwid_": "ee5d56d2-b1c7-455b-bc24-66f19af36550",
    "tg_referrer_source": "https%3A%2F%2Fuser.tungee.com%2F",
    "SecurityCenterDuId": "IlpNZVQ4ZHlwUVhIRTIrbCtGek0wSkJFPSI.GjLhig.dA9H9LhqWVB-YKt4FdfGKGOdub8",
    "__last_enter_version": "logistics",
    "_co_i": "6437da3f6eceb92bef8936bd",
    "acw_tc": "ff2c23398762a0242e03f1ed7ee554ca1717bcad17797f46f428a648362a66d8",
    "Hm_lpvt_d6df51ae5ec3a1b64d27905896d77ba5": "1733385655",
    "CGISessionId": "eyJzaWQiOiJOalpqWlRjNU5XWXRZMk13TnkwME9EZG1MVGhtWkRVdE5XUXhNRFZsTW1ObU56bGsiLCJjaGFubmVsIjoid2ViIiwiX2ZyZXNoIjpmYWxzZX0.Z1Fdtw.SU4P-qo8JCFXIXZuxBHmGVq9K_U",
    "accountCenterSessionId": ".eJwlj0trwzAQhP-LzjmsHivZPvtYqxTShvhiVtIKJ7VdsJ2mD_rfK9rTMDAfM_MthksSjcCKbBWcBWeUM6Y2RnNwrJEJskYLbLSNRmYjo0MoWSRjikqQwJy11NbVjkLOygaFSKQgyVhSwQRHqIJLmmKSCWustEqVUYC5tKmkgMRBxJGWhacy5s6h-O1vmL_21_4Y0Z_O-1l1d_8J8Nim-eE4zn37vPvT00fXvkzd7Gf_Nb0WcGFOw0bvPOxvQwqiyTRtfBC3jdf_t9ahRACyHDnUKkCsgo05FXjIK2-jaPb1xj-_tVhUrA.GjLvNw.-rR-N4xB4B9eEWalyYpWFu9i8mQ"
}
url = "https://logistics.tungee.com/cgi/logistics-data/api/logistics-amazon/search"
start='100'
end='150'
data = {
    'mode': 0,
    'begin': 1,
    'end': 200,
    'filter': '{"deliveryMethod":"含自发货","amazon_stations":["美国站"]}'
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)
res_json=json.loads(response.text)
company_list=res_json['data']['items']
for index in company_list:
    # 品类
    cate_arr = []
    categoriesList=index['entAmazonGoodsCategoriesShow']#品类
    for i in categoriesList:
       cate_arr.append(i['showSecondClassify'])
    #站点
    site_arr = []
    siteList=index['entAmazonSiteInfo']
    for i in siteList:
       site_arr.append(i['site'])
    try:
        id = str(index.get('_id'))
        # list(id)
        # print(id[0])
        url='https://logistics.tungee.com/enterprise-details/'+id+'/enterprise-information/basic-information'
        phone=联系方式.get_phone(index['lead']['enterprise_name'],id)
        dict={
        'company_name': index['lead']['enterprise_name'],#公司名称
        "address":index['address.value'],#地址
        'url':url,
        'phone':phone,
        'site':','.join(site_arr),#站点
        'company_id':index['_id'],#公司id
        'CategoriesShow':','.join(cate_arr),#类目
        'SalesLevel':index['entAmazonSalesLevel']#销量情况
        }
        csv_writer.writerow(dict)
        print(dict)
    except Exception as e:
        logger.error(e)
# print(response.text)