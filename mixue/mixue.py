import threading

import execjs
import requests
import time
import hashlib
import warnings
import urllib.parse
import json
from urllib.parse import quote_plus
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

warnings.filterwarnings("ignore")

with open('js加密.js', 'r', encoding='UTF-8') as f: #算法1
    js = execjs.compile(f.read())

tk1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eG1pbmlfMTgxNzQ1NDQxNTExNzE5MzIxOCIsImlhdCI6MTcyMjcxODYwN30.682BUXnt3jltAaTHGN9A5f6rDcjMHsLfvPn3n_3OTeHV-NGjWgv4wF1rmpg7GPXYgsYfmrT56BcNGABjv8HnAQ"
tk2='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eG1pbmlfMTgxNzQ3NjEyNTE0OTI1MzYzMyIsImlhdCI6MTcyMzIwODEyNH0.hGP3JOkfgei9-ZSXw8w_H1CyCr78zHghT0-zI_XNp-3szRKYKD0ABa3RkkDULyfImuGkmgv_eX-ywP3qGFrUyg'
tk_h='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eG1pbmlfMTQ0ODk3NTY3ODgzMzQ0NjkxMyIsImlhdCI6MTcyMjA1NjQ0NH0.KuUb4SEzxyjgVvOJu05r7Fk9MqNMs1_JobFfxqKYenEwoDf5l9Sx3sb-3ah59xE_ZmfziZw2BM3sbsuFul_CYQ'
# def generate_sign(secretword,timestamp):
#     # 构造字符串marketingId=1816854086004391938&round=18:00&s=2&secretword=7&stamp=1722248190033c274bac6493544b89d9c4f9d8d542b84
#     marketingId = '1816854086004391938'
#     s = '2'
#     stamp = timestamp
#     sign_str = f'marketingId={marketingId}&round={round}&s={s}&secretword={secretword}&stamp={stamp}c274bac6493544b89d9c4f9d8d542b84'
#     sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
#     print(sign_str)
#     return sign

# 毫秒级时间戳
def get_timestamp():
    # 获取当前时间的秒数和微秒数
    current_time = time.time()
    seconds = int(current_time)  # 秒数部分
    milliseconds = int((current_time - seconds) * 1000)  # 毫秒数部分，取0到999的整数部分

    # 组合成13位时间戳（前10位是秒，后3位是毫秒）
    timestamp = int(f"{seconds}{milliseconds:03d}")

    return timestamp
def send_request(round:str,keyword:str,tk):
    t = int(time.time() * 1000)
    headers = {
        "Host": "mxsa.mxbc.net",
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://mxsa-h5.mxbc.net",
        "Accept-Encoding": "gzip, deflate, br",
        'Access-Token': tk,
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/WIFI Language/zh_CN miniProgram/wx7696c66d2245d107",
        "Referer": "https://mxsa-h5.mxbc.net/",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9"
    }
    data = {
        "marketingId": "1816854086004391938",
        "round": round,
        "s": 2,
        "secretword": keyword,
        "sign": "",
        "stamp": t
    }
    sig=[]
    for k in data.keys():
        if k == "sign": continue
        sig.append(k+"="+str(data[k]))
    sig="&".join(sig)+"c274bac6493544b89d9c4f9d8d542b84"
    #md5计算sign
    data["sign"] = md5(sig)

    copy_data = {
        "marketingId": data["marketingId"],
        "round": data["round"],
        "secretword": data["secretword"],
        "sign": data["sign"],
        "s": data["s"],
        "stamp": data["stamp"]
    }
    params = {}
    N = json.dumps(copy_data, ensure_ascii=False)
        # .replace(" ", "")
    print(N)
    type_ = js.call("R_type", N)
    params["type__1286"] = type_["type__1286"]
    try:
        response = requests.post('https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm', headers=headers, params=params,data=N.encode(), timeout=1)
        print(response.request.headers)
        print(response.request.url)
        print(response.text)
        response.close()
        return response
    except:
        return 0

def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()


def getit(round:str,secretword:str,tk):
    while True:
        settime='2024-08-10 18:00:00'
        tt=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if tt>settime :
            s = send_request(round, secretword,tk)
            if s.status_code == 405:
                print(s.text)
                # time.sleep(2)
                continue
            if s.status_code == 200:
                requests.get(f'http://47.236.198.227:8080/fhFfdJTuxzwbWPky6Tw9u5/蜜雪/{s.text}')
                print(s.text)
                break

# def url_encode(type) :
#
#         encode_value = quote_plus(type)
#         encode_value = encode_value.replace('+', '%20')
#         encode_value = encode_value.replace('/', '%2F')
#         return encode_value

if __name__ == '__main__':
    round = '17:00' #todo 自己改
    keyword = "茉莉奶绿销量突破5000万杯"
    inttimestam=get_timestamp()
    timestamp = str(inttimestam)
    t1 = threading.Thread(target=getit,args=(round,keyword,tk_h,))
    time.sleep(1)
    t2 = threading.Thread(target=getit,args=(round,keyword,tk2,))
    t1.start()
    t2.start()


    # to_be_encode1='https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm{"marketingId":"1816854086004391938","round":"15:00","secretword":"75896","sign":"75e468283b707411a49319a9eebef723","s":2,"stamp":1722411866390}'


    # to_be_encode2='{"marketingId":"1816854086004391938","round":"20:00","secretword":"1","sign":"d64dd63ab0ba741cd6c56b46d66af313","s":2,"stamp":1722862742773}'
    # type = context.call("R_type",to_be_encode)
    # print(f'算法1type为{type["type__1286"]}')


    # type1=urllib.parse.quote(type)
    # type2=str.replace(type1,'/','%2F')
# for i in range(30):
#     timestamp = get_timestamp()
#     send_request(secretword,timestamp)
#     time.sleep(0.8)