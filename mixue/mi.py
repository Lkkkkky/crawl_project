import warnings
import sys
import time
import hashlib
import requests
import json
import urllib3
import threading
import execjs
urllib3.disable_warnings()
warnings.filterwarnings("ignore")

with open('js加密.js', 'r', encoding='UTF-8') as f: #算法1
    js = execjs.compile(f.read())

round = '14:00' #todo 自己改

def generate_sign(secretword,timestamp):
    # 构造字符串marketingId=1816854086004391938&round=18:00&s=2&secretword=7&stamp=1722248190033c274bac6493544b89d9c4f9d8d542b84
    marketingId = '1816854086004391938'
    s = '2'
    stamp = timestamp
    sign_str = f'marketingId={marketingId}&round={round}&s={s}&secretword={secretword}&stamp={stamp}c274bac6493544b89d9c4f9d8d542b84'
    sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
    print(sign_str)
    return sign

# 毫秒级时间戳
def get_timestamp():
    # 获取当前时间的秒数和微秒数
    current_time = time.time()
    seconds = int(current_time)  # 秒数部分
    milliseconds = int((current_time - seconds) * 1000)  # 毫秒数部分，取0到999的整数部分

    # 组合成13位时间戳（前10位是秒，后3位是毫秒）
    timestamp = int(f"{seconds}{milliseconds:03d}")

    return timestamp
tk1='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eG1pbmlfMTgxNzQ1NDQxNTExNzE5MzIxOCIsImlhdCI6MTcyMjcxODYwN30.682BUXnt3jltAaTHGN9A5f6rDcjMHsLfvPn3n_3OTeHV-NGjWgv4wF1rmpg7GPXYgsYfmrT56BcNGABjv8HnAQ'
tk2='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eG1pbmlfMTQ0OTM2OTU5MTYwOTc5NDU2MSIsImlhdCI6MTcyMjA2NjU3Nn0.jmF8X2FIbIOVUmo57jUc-syN1yK6nEb8zhY75YNP1OZMB1yE8-1wWGN8SGl_pR-xV1wtL-ODf3g6O6CJtSlQyA'
def send_request(secretword,inttimestam,tk,ip):

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
        'round': round,
        'secretword': secretword,
        'sign': sign,
        's': 2,
        'stamp': inttimestam,
    }
    copy_data = {
        "marketingId": data["marketingId"],
        "round": data["round"],
        "secretword": data["secretword"],
        "sign": data["sign"],
        "s": data["s"],
        "stamp": data["stamp"]
    }
    proxy = {"http": ip, "https": ip}
    print(proxy)
    params = {}
    N = json.dumps(copy_data, ensure_ascii=False).replace(" ", "")
    type_ = js.call("R_type", N)
    params["type__1286"] = type_["type__1286"]
    response = requests.post('https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm', headers=headers, params=params,data=N.encode(),proxies=proxy, timeout=1)
    print(response.request.headers)
    print(response.request.url)
    print(response.request.body)
    print(response.text)
    response.close()



# def url_encode(type) :
#
#         encode_value = quote_plus(type)
#         encode_value = encode_value.replace('+', '%20')
#         encode_value = encode_value.replace('/', '%2F')
#         return encode_value

def get_proxy():
    proxyy = { "https":'' }
    _version = sys.version_info
    is_python3 = (_version[0] == 3)
    r = requests.get("http://pandavip.xiongmaodaili.com/xiongmao-web/apiPlus/vgl?secret=b6840f11b6ca4cb1bf1e6e022eea51f9&orderNo=VGL20240730141017TGnJuqAR&count=2&isTxt=0&proxyType=1&validTime=0&removal=1&cityIds=&returnAccount=2", verify=False, allow_redirects=False)
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
if __name__ == '__main__':

            secretword = "茉莉奶绿 奶香四溢"
            inttimestam=get_timestamp()
            timestamp = str(inttimestam)
            sign=generate_sign(secretword,timestamp)
            to_be_encode='{"marketingId":"1816854086004391938","round":"'+round+'","secretword":"'+secretword+'","sign":"'+sign+'","s":2,"stamp":'+timestamp+'}'
            print(to_be_encode)
            proxy_dict=get_proxy()
            pro=[0 for i in range(5)]
            i=0
            for ip_dict in proxy_dict:
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
                pro[i]=proxyMeta
                i+=1
            t1 = threading.Thread(target=send_request,args=(secretword,inttimestam,tk1,pro[0],))
            t2 = threading.Thread(target=send_request,args=(secretword,inttimestam,tk2,pro[1],))
            t1.start()
            t2.start()
