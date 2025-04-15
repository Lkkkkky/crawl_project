import requests
import re
import execjs
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://ticket.wisdommuseum.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ticket.wisdommuseum.cn/reservation/userOut/outSingle/loginSingle.do',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'token': 'a6539311-2c4e-43b4-bcfc-03c1b95d52f1',
    'telephone': '17819461984',
    'password': '00000000aB',
    'code': 'rfci',
    'radio': '',
}

response = requests.post(
    'https://ticket.wisdommuseum.cn/reservation/userOut/outSingle/toLoginSingle.do',
    headers=headers,
    data=data,
)
acw=response.cookies.get_dict()
re_text=re.sub('\s','',response.text)

arg1=re.findall("vararg1='(.*?)'",re_text)[0]
acw['acw_sc__v2']=execjs.compile(open('acw_sc__v2.js','r',encoding='utf-8').read()).call('get_acwv2',arg1)
print(acw)