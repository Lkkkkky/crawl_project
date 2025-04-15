# https://user.wangxiao.cn/login?ur=http%3A%2F%2Fks.wangxiao.cn%2F

import json
import requests
import execjs
import ddddocr

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Content-Type": "application/json;charset=UTF-8",
    "EagleEye-SessionID": "k6mkp1yq8U6uCbs93cps8RL74k7s",
    "EagleEye-TraceID": "962f02791726725139850101581d1d",
    "EagleEye-pAppName": "ihuy5j2ab7@7cd9bc63da81d1d",
    "Origin": "https://user.wangxiao.cn",
    "Pragma": "no-cache",
    "Referer": "https://user.wangxiao.cn/login?ur=http%3A%2F%2Fks.wangxiao.cn%2F",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    'sessionid':'1726723830418',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "source": "pc",
    "token;": ""
}

session=requests.session()
session.headers=headers
session.get('https://user.wangxiao.cn/login?ur=http%3A%2F%2Fks.wangxiao.cn%2F')

def get_time():
    res=session.post('https://user.wangxiao.cn/apis//common/getTime').json()
    timestamp=res['data']
    print(timestamp)
    return timestamp

def get_v_image():
    res=session.post('https://user.wangxiao.cn/apis//common/getImageCaptcha').json()
    image=res['data']
    image=image.split('data:image/png;base64,')[1]

    ocr=ddddocr.DdddOcr(det=False,show_ad=False)
    code=ocr.classification(image)
    print(code)
    return code


def login(encpass,code):
    data= {
        "userName": "1158356001@qq.com",
        "password": encpass,
        "imageCaptchaCode": code
    }
    data=json.dumps(data,separators=(',',':'))
    res=session.post('https://user.wangxiao.cn/apis//login/passwordLogin',data=data).json()
    print(res)
def final():    
    code=get_v_image()
    time=get_time()
    encpass=execjs.compile(open('enc_pass.js','r',encoding='utf-8').read()).call('enc','111222',time)
    login(encpass,code)

final()