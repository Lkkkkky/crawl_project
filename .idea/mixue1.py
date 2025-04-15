import time
import sys
import time
import hashlib
import requests
import json
import urllib3
import random
import threading
import execjs
from lxml import etree
from fake_useragent import UserAgent
urllib3.disable_warnings()

ua = UserAgent()

# 获取随机用户代理字符串


#  print(r.text)
def generate_13_digit_timestamp():
    # 获取当前时间的秒数和微秒数
    current_time = time.time()
    seconds = int(current_time)  # 秒数部分
    milliseconds = int((current_time - seconds) * 1000)  # 毫秒数部分，取0到999的整数部分

    # 组合成13位时间戳（前10位是秒，后3位是毫秒）
    timestamp = int(f"{seconds}{milliseconds:03d}")

    return timestamp


def get_proxy():
    proxyy = { "https":'' }
    _version = sys.version_info
    is_python3 = (_version[0] == 3)
    r = requests.get("http://pandavip.xiongmaodaili.com/xiongmao-web/apiPlus/vgl?secret=b6840f11b6ca4cb1bf1e6e022eea51f9&orderNo=VGL20240730141017TGnJuqAR&count=10&isTxt=0&proxyType=1&validTime=0&removal=1&cityIds=&returnAccount=2", verify=False, allow_redirects=False)
    r.encoding='utf8'
    #print(r.status_code)
    #print(r.text)
    resp_dict = json.loads(r.text)
    resp_dict_list=resp_dict.get('obj')
    # if resp_dict['code'] == "0" :
    #     for resp_dict_list in resp_dict['obj']:
    #         ip = resp_dict_list.get('ip')
    #         port = resp_dict_list.get('port')
    #         # proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    #         #     "host": ip,
    #         #     "port": port,
    #         #     # 代理认证的用户名
    #         #     "user": resp_dict_list.get('account'),
    #         #     # 代理认证的密码
    #         #     "pass": resp_dict_list.get('password'),
    #         # }
    #         # proxy = {"http": proxyMeta, "https": proxyMeta}
    print(resp_dict_list)
    return resp_dict_list

def bug(ip):
    timee=1722259666740

    timestr=str(timee)
    proxy = {"http": ip, "https": ip}
    headers = {
        'Host': 'mxsa.mxbc.net',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://mxsa-h5.mxbc.net',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Access-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eG1pbmlfMTgxNzQ1NDQxNTExNzE5MzIxOCIsImlhdCI6MTcyMjE0OTg3M30.M-DPMlk0Yv0xELjztQCRQvPKM1RfnHg409EXq2QC0VNNMF-rMhPfs5rT4eAzFCp00D52TjnNjVmV-fSaDefb-w',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent':ua.random,
        'Referer': 'https://mxsa-h5.mxbc.net/',
        # 'Content-Length': '164',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',}
    json_data = {
        "secretword" : "茉莉奶绿销量突破500万杯",
        "sign" : "dd210796a498b77fb3918f5a8d1fd693",
        "marketingId" : "1816854086004391938",
        "round" : "14:00",
        "s" : 2,
        "stamp" : 1722329722748
    }
    # print(ua.random)
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),end=' ')
    while True:
        # 生成并打印13位时间戳

        # print(timestamp)

        time.sleep(5)
        r = requests.post("https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm", headers=headers, json=json_data, proxies=proxy, verify=False, allow_redirects=False)
        r.encoding = 'utf8'
        print(r.text,end='')
        print(proxy)
        print("当前线程信息", threading.current_thread())




if __name__== '__main__':
    while True:
        settime='2024-07-30 14:00:00'
        tt=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if tt>settime :
            proxy_dict_list=get_proxy()
            threads=[]
            i=0
            pro=[0 for i in range(20)]
            for ip_dict in proxy_dict_list:
                ip = ip_dict.get('ip')
                port = ip_dict.get('port')
                proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
                    "host": ip,
                    "port": port,
                    # 代理认证的用户名
                    "user": ip_dict.get('account'),
                    # 代理认证的密码
                    "pass": ip_dict.get('password'),
                }
                ip=proxyMeta
                # proxy = {"http": proxyMeta, "https": proxyMeta}
                pro[i]=ip
                t = threading.Thread(target=bug,args=(pro[i],))
                t.name='线程%d' % i
                t.start()
                threads.append(t)
                print(t.name)
                time.sleep(6)
                i+=1




    # threads=[]
    #     ip=proxy_dict.get('http')




# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"marketingId":"1816854086004391938","round":"11:00","secretword":"年度重磅 新品免单","sign":"ee0d52239f311b5dbd63c5a1fce1a974","s":2,"stamp":1722259666740}'.encode()
#response = requests.post('https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm', headers=headers, data=data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"marketingId":"1816854086004391938","round":"20:00","secretword":"zjjw","sign":"f6bfdc35f8e1cab6c76293444e511bba","s":2,"stamp":1722084674302}'
#response = requests.post('https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm', headers=headers, data=data)
