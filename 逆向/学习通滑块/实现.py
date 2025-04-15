import execjs
import requests
import json
import ddddocr
import re
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://v8.chaoxing.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "route": "d2738d9d28d2e628bdaefd634eed597a"
}
#获取参数
def get_params():
    js=execjs.compile(open('滑块.js','r',encoding='utf-8').read())
    global capkey
    capkey=js.call('get_captchaKey')
    print(capkey)
    global post_token
    post_token=js.call('get_token',capkey)
    print(post_token)
    global iv
    iv= js.call('get_iv')
    print(iv)
# 取滑块图
def getimage():
    url = "https://captcha.chaoxing.com/captcha/get/verification/image"
    params = {
        "callback": "cx_captcha_function",
        "captchaId": "qDG21VMg9qS5Rcok4cfpnHGnpf5LhcAv",
        "type": "slide",
        "version": "1.1.20",
        "captchaKey": capkey,
        "token": post_token,
        "referer": "https://v8.chaoxing.com/",
        "iv": iv,
        "_": "1726454218473"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    res=response.text.replace('cx_captcha_function(','').replace(')','')
    res_json=json.loads(res)
    get_token=res_json['token']
    background_link=res_json['imageVerificationVo']['shadeImage']
    slide_link=res_json['imageVerificationVo']['cutoutImage']

    return background_link,slide_link,get_token
#本地dddd库识别距离
def getdistance(background_link,slide_link):
    slide=ddddocr.DdddOcr(det=False,ocr=False,show_ad=False)
    slide_image=requests.get(slide_link,headers=headers).content
    background_image=requests.get(background_link,headers=headers).content
    distance=slide.slide_match(slide_image,background_image).get('target')[0]
    print(f'识别成功！滑动距离为{distance}px')
    return distance
#验证
def vertify(token,dis,iv):
    url = "https://captcha.chaoxing.com/captcha/check/verification/result"
    params = {
        "callback": "cx_captcha_function",
        "captchaId": "qDG21VMg9qS5Rcok4cfpnHGnpf5LhcAv",
        "type": "slide",
        "token": token,
        "textClickArr": "[{\"x\":"+str(dis)+"}]",
        "coordinate": "[]",
        "runEnv": "10",
        "version": "1.1.20",
        "t": "a",
        "iv": iv,
        "_": "1726458237565"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    res=response.text.replace('cx_captcha_function(','').replace(')','')
    # res_json=json.loads(res)
    validate=json.loads(json.loads(res)['extraData'])['validate']
    print(validate)
    return validate
#前置参数
def get_vpath():
    cookies = {
        # "route": "25bf9c9e377b1e1323ecaf5d3e51e190",
        # "V8_front": "87795B89E109AF8A8D6CCD618AF0339BE244430E71EDEBCA41096583A3A5636C9DF856DB764478302DA479651C48FE95E064178DBDEDD206106622DC11DB3E86FEB4939FF3A0F398A9E76A37BF846A4BE0D186AE73352642806020A80C33F6BC00F4D4440E51832818DC0EAE65C7DE80814B8FF9CCBB965217E9127C07C25EFF0138833F50C152E5E9BD782CB2E8989624DBC15263192245B5D5F31C7F18DDB8",
        # "createSiteSource": "num8",
        # "source": "num8",
        # "SESSIONID": "32C9D973634E90D4E5719C580D7291C9.v8"
    }
    url = "https://v8.chaoxing.com/"
    response = requests.get(url, headers=headers, cookies=cookies)
    res=response.text.replace(' ','')
    vpath=re.findall("vPath='(.*?)';",res)[0]
    return vpath
#登录
def login(vpath,validata,name,pwd):
    url = f"https://v8.chaoxing.com/users/dologinV2/{vpath}"
    data = {
        "source": "num8",
        "validata": validata,
        "uname":name,
        "pwd":pwd
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    print(response.text)
    print(response)
#主体
def final():
    get_params()
    back_link,slide_link,get_token=getimage()
    dis=getdistance(back_link,slide_link)
    validate=vertify(get_token,dis,iv)
    vpath=get_vpath()
    login(vpath,validate,'17819461984','20030531lky')
final()
#
