'''
=========================================================    
       @File     : 西之月高销量.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/3/4 12:00
       @Desc     : 
=========================================================   
'''
import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3dlc3Rtb250aC5jb20vc2hvcF9hcGkvbG9naW4iLCJpYXQiOjE3NDEwNjA2NDgsIm5iZiI6MTc0MTA2MDY0OCwianRpIjoiVDd1c21Va1ZGbVVvVVRvYSIsInN1YiI6IjE5MjIyIiwicHJ2IjoiYWZhNjAxYjY3NmMxOTM4MGNjODBiY2RhZmY5NTMyMTZjY2I1Y2UxYyJ9.jPbmdT0YNbwSsiGZG7oV3CPrVr4x6L19vJLtrzdqC2I",
    "cache-control": "no-cache",
    "locale": "zh_cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://westmonth.com/products/all",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "x-xsrf-token": "eyJpdiI6Ikp1M0drZ25mdG5KSGxtbnQ2bXIzVHc9PSIsInZhbHVlIjoiYXdIMnN4alVwVnFZR2duL2w0ZXlvd0dNcFo4c1hxTTFXNDNiaVEwYWNISmJrYnpKZkJiZDdDVnMzWmh2Zk5GRXVYR25kRGNDbkJrcUJvajdXWEE0aHY4TGVYT0NCbWxZa3g0c0kxa2lsT0NDQ25tdi9SODVnV1h6VFpGQS91NlEiLCJtYWMiOiJhYjVhNTk2MWI0NTk0NjlkZDgyNzkwMGYzNmVmNTYwMmNkZjA4ZDJhN2JhZjBmYjY2YzYwMGNiOWRmZDY0NjkxIiwidGFnIjoiIn0="
}
url = "https://westmonth.com/shop_api/products/load_list"
params = {
    "locale": "zh_cn",
    "delivery_region_id": "3",
    "brandId": "",
    "depot": "",
    "categoryId": "0",
    "newtime": "",
    "certificateId": "0",
    "sort_field": "2",
    "sort_mode": "2",
    "onlyShow": "1",
    "page": "2",
    "pagesize": "1000",
    "indistinct": ""
}
response = requests.get(url, headers=headers, params=params)
for i in response.json()['data']['data']:
    print(i['product_id'])
