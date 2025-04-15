'''
=========================================================    
       @File     : 运费.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/28 14:55
       @Desc     : 
=========================================================   
'''
import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Cbs-Token": "cbs:token:db8c883203fed15ff74f173e73373ae1",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Cvt": "a32b3baf-a095-4158-babc-25997bf17d15",
    "Origin": "https://shop.dropwiz.net",
    "Pragma": "no-cache",
    "Referer": "https://shop.dropwiz.net/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://api.dropwiz.net/openapi/goods/detail/PQQHLNC57"
response = requests.post(url, headers=headers)

print(response.text)
print(response)