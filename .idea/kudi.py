import requests
import time
import threading
def ohohoh():

    headers = {
        'Host': 'mxsa.mxbc.net',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://mxsa-h5.mxbc.net',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Access-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eG1pbmlfMTQ0OTM2OTU5MTYwOTc5NDU2MSIsImlhdCI6MTcyMjA2NjU3Nn0.jmF8X2FIbIOVUmo57jUc-syN1yK6nEb8zhY75YNP1OZMB1yE8-1wWGN8SGl_pR-xV1wtL-ODf3g6O6CJtSlQyA',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN miniProgram/wx7696c66d2245d107',
        'Referer': 'https://mxsa-h5.mxbc.net/',
        # 'Content-Length': '164',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    }

    json_data = {
        'marketingId': '1816854086004391938',
        'round': '17:00',
        'secretword': '170万杯茉莉奶绿免费喝',
        'sign': '73c7840561a676f5139d652f1ac4148b',
        's': 2,
        'stamp': 1722161971731,
    }
    while True:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),end=' ')
        response = requests.post('https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm', headers=headers, json=json_data)
        print(response.text)
        print("当前线程信息", threading.current_thread())
        print()
        time.sleep(2)
threads=[]
for i in range(2):
    t = threading.Thread(target=ohohoh)
    t.start()
    time.sleep(2)
    threads.append(t)


# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"marketingId":"1816854086004391938","round":"11:00","secretword":"年度重磅 新品免单","sign":"ee0d52239f311b5dbd63c5a1fce1a974","s":2,"stamp":1722259666740}'.encode()
#response = requests.post('https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm', headers=headers, data=data)