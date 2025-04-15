'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/8 16:56
       @Desc     : 
=========================================================   
'''
import requests
import execjs
import json
import ddddocr
from loguru import logger
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.yunpian.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "_gid": "GA1.2.1333751231.1730913123",
    "MEIQIA_TRACK_ID": "2oU981mnGGTpsbco2aX8jKASPIM",
    "MEIQIA_VISIT_ID": "2oU97vNLbat8vly3FUArGPcIr52",
    "Hm_lvt_70eec7aeabdef9224878ecbafcc9bf6a": "1730913123,1731004116,1731054885",
    "HMACCOUNT": "4D4F61CE5656C745",
    "__wksid": "n-937CBFCB1980475EB1C5E471DBCCE2C1",
    "_ga_ESVMH6YSPX": "GS1.1.1731054883.4.1.1731055362.0.0.0",
    "Hm_lpvt_70eec7aeabdef9224878ecbafcc9bf6a": "1731055367",
    "_ga_B8H0JYR4RL": "GS1.1.1731054885.5.1.1731055370.44.0.0",
    "_ga": "GA1.1.405273468.1730913122"
}


def get_image():
    url = "https://captcha.yunpian.com/v1/jsonp/captcha/get"
    params = {
        "cb": "cf3gk91i0v",
        "i": "Hcr5S7shboMl63oshUxl3orTR3m+54pNzs63sZVITWt8uWE+meqSf/eYkcoXSbbbxMvoVDf58bE7UxLXUWXBhmjHI+qDXG6t2eTLvItGzyX3KiEglShoXXy4szVJ/SwxJvbULQx31NtwbKjCTV76yzdbMB6G2CrHZecQZGpyOUHQnKhyU4me1Gdpe2dyqtBcGrA1+GHzdWxEMUCoM3r7tBzOlXmNnway48BDcIakzbdUBJU2k5WDS4iWwcAPrdEHut+bIF19TU5yZ/Jy/V5lFwfdkcWTQUOIGJ67rI5nANgzAIrz32N8IdQVgI5yzawNIa6HeOGvpFnJgAOKiSZ93XHWJ4Up+v1oBY7cdyvwLuGC6mKocAyDrNZAvZkS2gL8MOB2lXxW5KF3QLYdxiRLhEZX0+unPLzwu7rJe4Zhy1CrC69pkRdOq3Voap8vfVPnjk2jNEaU33u1vkw8CKnAQhnlOD/rSPH42ozV3CFlIAsBEodw+4daB4bHiIZNxbivI0OnvtRWm/LHKdjdkIk1pl3MCdO2IBjHe0/ZWcDEZWnE/bVm/i+j6xqdjEvl4++Eu0/rB1uN0zXYJIpdboRLVSQ5zUMO/ldNVbhck45K4FO+LLkFTPQt3AJCuOUFX15945OIfL8LZPMl7aMmUr4bna7zlJ8To+C5fkqru1LkycVCt4kQydAQwFHq8gfKFndczSIvgE0jiJMkKbcJH/59PftcYls1Qa4nVaMmTPY39KwwKYgDz03q15CP040M9HhVxlEDAE4TxcsQ1//B4d1AhPTQggjNquFWhbvZ//OK+J1mkH0PgrBTwfegdD0rVcyyYAHp+OIm3NhBFz0LRLLjOqD6N+xv14mGw3xfkrcFd6ndgYt36nlqcdAa+EnpTzs4",
        "k": "Kqd8jj43p8LBWTXrZ9a/w3Jz9Z01X2epQyjht83kYl/N+CEClYwaY2XUuc2FaaQt8QGHK0shdxGgRv6luXG132t252Rp9Nz47QKm6NTwuRtOtodmPolBiSCVNc9POUsNQJ7rxfoLMEQtKETdOJt8jcELygPjZbJprcqt2ZG0P/4=",
        # "token": "0759be7c8e134ccaaab1572d1d49af92",
        "captchaId": "974cd565f11545b6a5006d10dc324281"
    }

    arr = execjs.compile(open('js.js', 'r', encoding='utf-8').read()).call('get_image')

    params['cb'] = arr[0]
    params['i'] = arr[1]
    params['k'] = arr[2]
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    res = response.text.replace('ypjsonp(', '').replace(')', '')
    json_res = json.loads(res)
    bg_image_href = json_res["data"]['bg']
    slide_image_href = json_res["data"]['front']
    token=json_res["data"]['token']
    # print(token)
    return bg_image_href, slide_image_href,token


def get_dis(background_link, slide_link):
    slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    with requests.get(slide_link, stream=True) as r:
        with open('slide_image.jpg', 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
    with requests.get(background_link, stream=True) as r:
        with open('background_image.jpg', 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
    slide_image = requests.get(slide_link, headers=headers).content

    background_image = requests.get(background_link, headers=headers).content

    distance = slide.slide_match(slide_image, background_image).get('target')[0]
    # 对距离识别进行优化
    distance=int((distance+20)*(304/480))

    print(f'识别成功！滑动距离为{distance}px')
    return distance


def vertify(distance,token):
    arr = execjs.compile(open('js.js', 'r', encoding='utf-8').read()).call('vertify', distance)
    # print(arr)
    url = "https://captcha.yunpian.com/v1/jsonp/captcha/verify"
    params = {
        "token": token,
        "captchaId": "974cd565f11545b6a5006d10dc324281",
        'cb': arr[0],
        'i': arr[1],
        'k': arr[2]}
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    logger.info(response.text)


for i in range(20):
    bg_image_href, slide_image_href,token = get_image()

    distance = get_dis(bg_image_href, slide_image_href)
    vertify(distance,token)
