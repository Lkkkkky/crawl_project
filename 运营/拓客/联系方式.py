'''
=========================================================    
       @File     : 联系方式.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/5 13:59
       @Desc     : 
=========================================================   
'''
import json

import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "product-type": "25",
    "referer": "https://logistics.tungee.com/enterprise-details/57ca06b399326598/contacts?isOpenFrame=true",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
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
def get_phone(cname,key):
    url = "https://logistics.tungee.com/cgi/logistics-common/api/lead/contacts"
    params = {
        "enterprise_id": key,
        "type": "company",
        "multi_version_type": "logistics"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    res_json = json.loads(response.text)
    for i in  res_json['contacts']:
        if ('*' not in i['contact_label']):
            print(cname, '---->', i['contact_label'])
            return i['contact_label']

    print('无')

