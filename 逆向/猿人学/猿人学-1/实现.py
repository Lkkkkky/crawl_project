import requests
import execjs
import json
# js引入模块
import execjs, json
# 请求模块
import requests
# 日志模块
from loguru import logger

# with open(r'js.js', encoding='utf-8', mode='r') as f:
#     JsData = f.read()
# psd = execjs.compile(JsData).call('getM')
# m = psd.replace('|', '%E4%B8%A8')
# m1 = m.replace(' ', "")
# print(m1)
# lst = []
# for i in range(1, 6):
#     base_url = 'http://match.yuanrenxue.com/api/match/1?page={}&m={}'.format(i, m1)
#     headers = {
#                   'user-agent': 'yuanrenxue.project',
#                   'x-requested-with': 'XMLHttpRequest',
#                   'cookie': 'sessionid=nu7n7p0552x6ahi5kmllps85ifktyqga; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1726746199; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1726746162,1726768919; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1726768919; HMACCOUNT=70DAAD6496FF2F56',
#
#     }
#     response = requests.get(base_url, headers=headers)
#     json_data = response.json()['data']
#     for data in json_data:
#         lst.append(data['value'])
# sum = 0
# for i in lst:
#     sum += int(i)
# print(sum / len(lst))


headers = {

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    'cookie': 'sessionid=nu7n7p0552x6ahi5kmllps85ifktyqga; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1726746199; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1726746162,1726768919; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1726768919; HMACCOUNT=70DAAD6496FF2F56',
}
cookies = {
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1726746162",
    "HMACCOUNT": "70DAAD6496FF2F56",
    "tk": "-335598377529947670",
    "sessionid": "nu7n7p0552x6ahi5kmllps85ifktyqga",
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1726746199",
    "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1726746199",
    "qpfccr": "true",
    "no-alert3": "true",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1726750132"
}

arr=[]

def get_ans(page):
    psd=execjs.compile(open('js.js','r',encoding='utf-8').read()).call('getM')
    m = psd.replace('|', '%E4%B8%A8')
    m1 = m.replace(' ', "")
    url = f"https://match.yuanrenxue.cn/api/match/1?page={page}&m={m1}"
    print(m1)
    response = requests.get(url, headers=headers)
    print(response.text)
    print(response)
    res=response.json()
    price=res['data']
    sum=0
    for index in price:
        arr.append(index['value'])
sum=0

for i in range(1,6):
    get_ans(i)
for i in arr:
    sum+=int(i)

print(sum / len(arr))