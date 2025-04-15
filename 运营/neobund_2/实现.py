'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/24 11:25
       @Desc     : 
=========================================================   
'''
import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.neobund.com/list?pn=Outdoor&kind=0&type=0",
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
    "_ga": "GA1.1.298371489.1733880376",
    "vuex": "{%22user%22:{%22userId%22:%2240aef0e19ef543e3b8edf5c3dfba88c3%22%2C%22nickName%22:%22jing336667@gmail.com%22%2C%22userAvatar%22:null%2C%22token%22:%22d1d652df-c8c0-4242-9afd-e0980750f91e%22%2C%22levelType%22:0%2C%22balance%22:0%2C%22unReadNotices%22:1%2C%22pageLoading%22:false%2C%22pageSize%22:10%2C%22payList%22:[]%2C%22tz%22:%22US%22%2C%22authTips%22:false%2C%22isOpenNbs%22:1%2C%22userEmail%22:null}}",
    "_ga_CP3T51ZM9M": "GS1.1.1735009847.7.1.1735010511.0.0.0",
    "JSESSIONID": "6933A42E8F3A294C90298773EF0F6D49"
}
url = "https://www.neobund.com/detail/2460"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)