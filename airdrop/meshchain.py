'''
=========================================================    
       @File     : meshchain.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/1/20 14:41
       @Desc     : 
=========================================================   
'''

def claim(tk,uid,email):
    import requests
    import json
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": tk,
        "content-type": "application/json",
        "origin": "chrome-extension://lobckpihghfknleknppdjnnncpcfpcgh",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "none",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    cookies = {
        "_ga": "GA1.1.618263239.1736927026",
        "_gcl_au": "1.1.368212989.1736927025.1332828803.1737335930.1737335936",
        "_ga_5PPR32GMM8": "GS1.1.1737337977.11.0.1737337977.60.0.0"
    }
    url = "https://api.meshchain.ai/meshmain/rewards/claim"
    data = {
        "unique_id": uid
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data).json()
    print(email + '---->', end='')
    try:

        print(response['total_reward'])

    except:
        print('登录状态失效')

claim("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4ME9LQVc5TksyQUsiLCJqdGkiOiI1M2MwMjFlYy1lN2NiLTQwMzgtYmQ2Yy05ZDQ5OThhMWUxNDQiLCJpYXQiOjE3MzczNTQzNjYsImV4cCI6MTczNzM1Nzk2Nn0.dU99QIDKcaLGEk2ZBXCXPgdSww97mjGS7agHx0OVucw","5307f4d01e2e66a7798a1433737073ab",'1158356001@qq.com')
claim("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJMTUM1UjJSMFRBNTkiLCJqdGkiOiJhYjUxODBjYi1kMWM0LTQ1ZmEtOWJjMC1mNjRjOWE0ZDUwODQiLCJpYXQiOjE3MzczNTQ1MzEsImV4cCI6MTczNzM1ODEzMX0.R7ag7kz6WTt_tF0IxT-3Dmoy89ONZgI1ZfYH6SHdzjA","ac6a7d419981fae7fb9106344d7cf02c",'jing36666@163.com')
claim("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzRDdNQjQwSVdVVkgiLCJqdGkiOiI2MDYxY2RjNi1hZTFlLTRkMDAtYWU5NS0wZmRhNDViYzc2YWIiLCJpYXQiOjE3MzczNTQ4MDQsImV4cCI6MTczNzM1ODQwNH0.HMawOqEHWJA2opVvN3bhvqEsyUaqYcmaCA7jlrlJLqg","1a9a4a5ba2b98ba271fdd7ae65c036ef",'1727699488@qq.com')
claim("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJHMUlKTlBBMVlGOUciLCJqdGkiOiIzMTIyOGY1MC05NDE3LTQxYzgtYjQ0Ny1iNDc4Mjk0NzAwNDUiLCJpYXQiOjE3MzczNTY0NzIsImV4cCI6MTczNzM2MDA3Mn0.VhVtiTo5_PfAHmEBmYOPa-tYvjf2wW7R4Ec4_PDxLIs","b94902b0a87cbc87f7ec20e1a27cd445",'jing36670@163.com')