import requests
import json



headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Cbs-Token": "cbs:token:0e3d536ba2d107418c23c962279a7997",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://www.dropwiz.net",
    "Pragma": "no-cache",
    "Referer": "https://www.dropwiz.net/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://api.dropwiz.net/openapi/goods/queryGoodsList"

page=5
no=0
for p in range(page):
    data = {
        "categoryId": None,
        "sortRules": [],
        "pageNo": p,
        "pageSize": 50,
        "searchWord": ""
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    res_json=json.loads(response.text)
    list=res_json['data']['list']
    for i in list:
        print(str(no)+'-->'+i['goodsName'])
        no+=1
