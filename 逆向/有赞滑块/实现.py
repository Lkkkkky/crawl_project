import requests
import json
import execjs
import re
import ddddocr

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://account.youzan.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://account.youzan.com/login",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
cookies = {
    "KDTSESSIONID": "YZ1285252293205643264YZTa79Muvv",
    "KEYWORD_ID": "610808449814",
    "yz_log_ftime": "1726469628157",
    "yz_log_uuid": "70c2d7d4-4e0a-31bf-1bba-8709f5e28116",
    "trace_sdk_context_from_source": "baidu_sem_wsc_001",
    "yz_log_seqb": "1726469628162",
    "Hm_lvt_7bec91b798a11b6f175b22039b5e7bdd": "1726469629",
    "HMACCOUNT": "0E7D89894D8D5CB3",
    "_clck": "18dyd5a%7C2%7Cfp8%7C0%7C1720",
    "nobody_sign": "YZ1285252293205643264YZTa79Muvv",
    "Hm_lpvt_7bec91b798a11b6f175b22039b5e7bdd": "1726469645",
    "_clsk": "1wk27di%7C1726469646475%7C2%7C1%7Cx.clarity.ms%2Fcollect",
    "ec": "D5cgJ8PP-1726469648137-f3c947e1a6847-173252168",
    "yz_fp_hash": "eafded7164b0e33f91afb5bbb0feba35",
    "_efmdata": "cFqkTOnIfXueNEBeKNTDBMobkxJFOTd2coxTp5ppx25SRFLs%2BsJQDQ%2B%2BKrHMbvDr7XX3gFtJahaxE1i0Ys1TZq2fUMhG0o1fFlNgncjMfcY%3D",
    "_exid": "msWtIiRUP5smV7rbtfdne5p6xpANpl3CbTf95frkfyDNqDzK4q0Xaa5ifzh2JChzISvQwZPbqpoT2ToxRiIx5Q%3D%3D",
    "dfp": "09a9dbae092c7324588d20407d83a130bcc0bb3e",
    "acw_tc": "c85610e8ae40c94d12d6b11f96bd5eec45a83a433e6dad0974b8fbc38a70eb9c",
    "captcha_sid": "YZ1285252397648293888YZxailtvs4",
    "_kdt_id_": "371189",
    "yz_log_seqn": "27"
}


def getimage():
    url = "https://passport.youzan.com/api/captcha/get-behavior-captcha-token-v2.json"
    params = {
        "bizType": "3",
        "version": "1.0"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    res = json.loads(response.text)
    token = res['data']['token']
    rdstr = res['data']['randomStr']
    params1 = {
        "captchaType": 1,
        "token": token
    }
    response = requests.get('https://passport.youzan.com/api/captcha/get-behavior-captcha-data.json', headers=headers,
                            cookies=cookies, params=params1)
    res = json.loads(response.text)
    bigUrl = res['data']['captchaObtainInfoResult']['bigUrl']
    smallUrl = res['data']['captchaObtainInfoResult']['smallUrl']
    cy = res['data']['captchaObtainInfoResult']['cy']
    print(bigUrl, smallUrl)
    return bigUrl, smallUrl, rdstr, cy,token

def getdistance(background_link, slide_link):
    slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    slide_image = requests.get(slide_link, headers=headers).content
    background_image = requests.get(background_link, headers=headers).content
    distance = slide.slide_match(slide_image, background_image).get('target')[0]
    print(f'识别成功！滑动距离为{distance}px')

    return distance

def get_userBehaviorData(rdstr, dis, _cy):
    # dis=int(dis)
    # _cy=int(_cy)
    # rrr=
    return execjs.compile(open('滑块.js', 'r', encoding='utf-8').read()).call('get_key_iv', rdstr, dis, _cy)

def vertify(token,userBD):
    url = "https://passport.youzan.com/api/captcha/check-behavior-captcha-data.json"
    data = {"token": token,
            "bizType": 3,
            "bizData": "",
            "captchaType": 1,
            "userBehaviorData":userBD
            }
    data=json.dumps(data,separators=(',',':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    print(response.text)
    print(response)

def sengmsg(token):
    url = "https://account.youzan.com/api/captcha/sms/send.json"
    params = {
        "ticket": token,
        "mobile": "17819461984",
        "countryCode": "+86",
        "behaviorBizType": "3",
        "platform": "pc",
        "subFrom": "uic_login_without_password",
        "biz": "uic_login_without_password",
        "csrf_token": "74151223197220573190396295066319306224119075969908506681039406214553375412330"
        }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(response.text)
    print(response)

def final():
    bg_link, sd_link, rdstr, cy,token = getimage()
    dis = getdistance(bg_link, sd_link)
    userBD = get_userBehaviorData(rdstr, dis / 2, cy / 2)
    print(userBD)
    vertify(token,userBD)
    # 过验证才发码 拿下
    sengmsg(token)

final()
