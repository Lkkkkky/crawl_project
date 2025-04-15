# import requests
# import execjs
# import  json
# m=execjs.compile(open('魔改md5.js','r',encoding='utf-8').read()).call('getM')
# m=m.replace(' ','')
# print(m)
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
#
# }
#
# cookies={
#     "sessionid":'czxp2psikqzgzybkh4dhae11at6jccn4',
#     " m": m
# }
#
# print(headers)
# page=1
#
#
#
#
# url = f"https://match.yuanrenxue.cn/api/match/2?page={page}"
#
# response = requests.get(url, headers=headers)
#
# print(response.text)
# print(response)



import requests
import execjs


url = 'https://match.yuanrenxue.cn/api/match/2?page=%s'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}
cookies = {}
cookies['seesionid'] = 'czxp2psikqzgzybkh4dhae11at6jccn4'
js_code = open('魔改md5.js', 'r', encoding='utf-8').read()
js_compile = execjs.compile(js_code)
result = 0
for i in range(1, 6):
    cookie_m = js_compile.call('run')
    cookies['m'] = cookie_m
    response = requests.get(url%i, headers=headers, cookies=cookies)
    print(response.text)
    json_data = response.json()
    for dic in json_data.get('data'):
        result += dic.get('value')
print(result)	# 最终结果为:248974
