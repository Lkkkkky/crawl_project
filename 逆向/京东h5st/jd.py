import time

import requests

import execjs

cookies = {
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://search.jd.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://search.jd.com/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-referer-page': 'https://search.jd.com/Search',
    'x-rp-client': 'h5_1.0.0',
}

params = {
    'appid': 'search-pc-java',
    'functionId': 'pc_search_s_new',
    'client': 'pc',
    'clientVersion': '1.0.0',
    't': '1730541689095',
    'body': '{"keyword":"手机","wq":"手机","pvid":"","isList":0,"page":"3","s":"56","click":"0","log_id":"","show_items":""}',
    'loginType': '3',
    'uuid': '',
    'area': '',
    'h5st': '',
    'x-api-eid-token': '',
}

time = str(int(time.time() * 1000))

# print(time)

params['t'] = time

with open('jd_10_25.js', 'r', encoding='utf-8') as f:
    js = f.read()

context = execjs.compile(js)
h5st = context.call('h5st', params['functionId'], time, params['body'], params['uuid'], params['area'])
# print(result)
params['h5st'] = h5st

response = requests.get('https://api.m.jd.com/', params=params, cookies=cookies, headers=headers)
print(response)
print(response.text)

