'''
=========================================================    
       @File     : GIGA.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/9 15:40
       @Desc     : 
=========================================================   
'''
import requests
import json


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "ori-status-in-response": "code",
    "origin": "https://www.gigab2b.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.gigab2b.com/index.php?route=product/search/advancedFilter&product_category_id=10209&seller_type=onsite&origin_place_code=USA&skip_has_wishlist=true&skip_has_downloaded=true&skip_has_purchased=true",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "x-csrf-token": "qxkmbcSKhbrc5rj5IgzjR5nzYwbUSCi3JtptVAVq",
    "x-gmd-device-id": "1283195e-4443-4fb4-978b-244df1097940",
    "x-gmd-page-url": "https://www.gigab2b.com/index.php?route=product/search/advancedFilter&product_category_id=10209&seller_type=onsite&origin_place_code=USA&skip_has_wishlist=true&skip_has_downloaded=true&skip_has_purchased=true",
    "x-gmd-referer-url": "https://www.gigab2b.com/index.php?route=product/search/advancedFilter&product_category_id=10209&seller_type=onsite&origin_place_code=USA&skip_has_wishlist=true&skip_has_downloaded=true&skip_has_purchased=true",
    "x-gmd-screen": "1920x1080",
    "x-requested-with": "XMLHttpRequest, XMLHttpRequest"
}
cookies = {
    "country": "USA",
    "currency": "USD",
    "gmd_device_id": "1283195e-4443-4fb4-978b-244df1097940",
    "_ga": "GA1.1.408575259.1733361903",
    "_gcl_au": "1.1.1151540469.1733361903",
    "_pk_id.2.185c": "a2b8705262873a34.1733361904.",
    "hubspotutk": "e0ac6d6ae1ea998f165da8110cf1f836",
    "__hs_opt_out": "no",
    "__hs_initial_opt_in": "true",
    "_ayo": "531986d8ced8ec0a815a681ec7505a3d",
    "OCSESSID": "2447fe134386dbe5659626e3e1",
    "_pk_ses.2.185c": "1",
    "__hstc": "114550104.e0ac6d6ae1ea998f165da8110cf1f836.1733361999612.1733361999613.1733728432742.2",
    "__hssrc": "1",
    "tfstk": "fv5ZB8toW5FaNCVjGFRqTa4M1tA9ZCq77stXoZbD5hxi1ficLgjNfPevnKWFmMp6jO_Xuj79AnsXGsWKgaQA1PdbWCQ9MIq7V71VWNdvx_1q2sRntUTYGFDMmRZkOvE7V7NID0E9Pus6kvuE8EKHSEcmiy-H5FADodA08HY2yxmGmib38FTWSnxiIe0HyHxDidjmtWcm8NbmTU9gyxsgvxlzEdtlShb1W6c6HAIBY3KFBF7epNDoijfe7d5vbHcrid6cyLC1rSlp1aWHtE5Yrx-2Utf6t1q3ZppctMYhfrMv8t7cwCdro5be_hJlgMF4zgbFoT9FOzVJ_CxGhCQjzl_F_G_OTZgmKCR1LL5wZ7nMc9_PgE5YDWSPoaBDLsoN4uov-Pq1MOom3dYp83aU8q4IAMoBcyptHxpHwe-75FMxHdYp83aU8xHvKQLeVPT1.",
    "is_partner": "0",
    "login_flag": "",
    "_fbp": "fb.1.1733729031869.450488541383874844",
    "acw_tc": "ac11000117337321728116043e01197e3ab45644ce4c2c9a5102294b3b1969",
    "acw_sc__v2": "6756a79409e68c4f89aa12b8ee5f0af1b1a0d421",
    "__hssc": "114550104.58.1733728432742",
    "SERVERID": "66839549c43026f0ffd947819a6794bc|1733732260|1733728429",
    "SERVERCORSID": "66839549c43026f0ffd947819a6794bc|1733732260|1733728429",
    "_ga_39N4BF4XSG": "GS1.1.1733728431.3.1.1733732261.0.0.0"
}
url = "https://www.gigab2b.com/index.php"
params = {
    "route": "/product/list/list"
}
data = {
    "product_ids": [
        526543,
        526198,
        805484,
        828191,
        526163,
        526547,
        828192,
        828193,
        526167,
        526170,
        828194,
        828196,
        526171,
        526172,
        526180,
        526181,
        526182,
        526183,
        526189,
        526199,
        526207,
        526208,
        526544,
        526548,
        526551,
        526552,
        526553,
        526558,
        526162,
        526164,
        526165,
        526169,
        526178,
        526185,
        526187,
        526192,
        526201,
        526206,
        526555,
        526557,
        526559,
        526560,
        526561,
        526168,
        526174,
        526177,
        526179,
        526202,
        526542,
        526546,
        526549,
        526554,
        526166,
        526173,
        526176,
        526186,
        526190,
        526209,
        526550,
        526556,
        526184,
        526191,
        526203,
        526545,
        526175,
        526205
    ],
    "with_seller": True,
    "with_wishlist": True,
    "type": "grid"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
res_json=json.loads(response.text)
good_list=res_json['data']
for i in good_list:
    seller_id=i['other']['seller_id']
    good_name=i['product']['name']
    store_name=i['seller']['store_name']
print(response.text)
print(response)