import time
import sys
import time
import hashlib
import requests
import json
import urllib3
import random
import threading
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

def bug():
    timee=1722259666740
    timestr=str(timee)
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
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),end=' ')
    while True:
        # 生成并打印13位时间戳

        # print(timestamp)

        time.sleep(5)
        r = requests.post("https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm", headers=headers, json=json_data, verify=False, allow_redirects=False)
        r.encoding = 'utf8'
        print(r.text,end='')

        print("当前线程信息", threading.current_thread())




if __name__== '__main__':
    while True:
        settime='2024-07-30 14:00:00'
        tt=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if tt>settime :
          bug()







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
