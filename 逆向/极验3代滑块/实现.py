import json
import time
from PIL import Image
import ddddocr
import requests
import re
import random
import execjs

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.geetest.com/demo/slide-float.html",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}

def handle_response_to_json(respText):
    start_index = respText.find('(')
    end_index = respText.rfind(')')
    json_data = json.loads(respText[start_index + 1:end_index])
    return json_data
def get_challenge_gt():

        url = "https://www.geetest.com/demo/gt/register-slide"
        params = {
            "t": int(time.time()*1000)
        }
        response = requests.get(url,headers=headers,params=params)
        res=response.json()
        cha=res['challenge']
        gt=res['gt']
        # print(response.text)
        return cha,gt
# 两个cookies要带上
def get_GeeTestUser_cookie(gt):
    url = "https://apiv6.geetest.com/gettype.php"
    params = {
        "gt": gt,
        # "callback": "geetest_1727091479438"
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    cok=response.cookies.get_dict()
    GeeTestUser=cok['GeeTestUser']
    # print('GeeTestUser----->'+GeeTestUser)
    return GeeTestUser
def get_GeeTestAjaxUser_cookie(GeeTestUser,gt,cha):
    cookies = {
        "GeeTestUser": GeeTestUser
    }
    url = "https://apiv6.geetest.com/ajax.php"
    params = {
        "gt": gt,
        "challenge": cha,
        "lang": "zh-cn",
        "pt": "0",
        "client_type": "web"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    cok=response.cookies.get_dict()
    GeeTestAjaxUser=cok['GeeTestAjaxUser']
    return  GeeTestAjaxUser
def get_newchallenge_c_s_image(cha,gt,GTU,GTA):
    cookies = {
        "GeeTestUser": GTU,
        "GeeTestAjaxUser": GTA
    }
    url = f"https://apiv6.geetest.com/get.php?is_next=true&type=slide3&gt={gt}&challenge={cha}&lang=zh-cn&https=true&protocol=https%3A%2F%2F&offline=false&product=embed&api_server=apiv6.geetest.com&isPC=true&autoReset=true&width=100%25&callback=geetest_1727091489509"
    response = requests.get(url,headers=headers,cookies=cookies)
    res=response.text
    # print(res)
    js_res=handle_response_to_json(res)

    newcha=re.findall("challenge\": \"(.*?)\"",res)[0]
    bg=re.findall("bg\": \"(.*?)\"",res)[0]
    fullbg=re.findall("fullbg\": \"(.*?)\"",res)[0]
    c=js_res['c']

    # print(c)
    s=re.findall("\"s\": \"(.*?)\"",res)[0]
    # print(s)
    # slice=re.findall("slice\": \"(.*?)\"",res)[0]
    return newcha,bg,fullbg,c,s
# 底图还原
def fix_image(img_list):

    for index,img in enumerate(img_list):
        im=Image.open(img)
        new_img=Image.new("RGB",(260,160))
        r=160
        Ut=[
            39,
            38,
            48,
            49,
            41,
            40,
            46,
            47,
            35,
            34,
            50,
            51,
            33,
            32,
            28,
            29,
            27,
            26,
            36,
            37,
            31,
            30,
            44,
            45,
            43,
            42,
            12,
            13,
            23,
            22,
            14,
            15,
            21,
            20,
            8,
            9,
            25,
            24,
            6,
            7,
            3,
            2,
            0,
            1,
            11,
            10,
            4,
            5,
            19,
            18,
            16,
            17
        ]
        for _ in range(len(Ut)):
            a = r / 2,
            c = Ut[_] % 26 * 12 + 1
            u = 80 if 25 < Ut[_] else 0
            l = im.crop(box=(c, u, c+10, u+80))
            new_img.paste(l,box=(_ % 26 * 10,80 if _ >25 else 0))
        if index ==0:
            new_img.save("./背景缺口图.jpg")
            bgimage=new_img
        else:
            new_img.save("./背景完整图.jpg")
            fullimage=new_img
    return bgimage,fullimage
#识别滑块距离  用缺口底图和完整地图   无需拼图图片
def get_distance(target_byte,full_byte):
    slide=ddddocr.DdddOcr(show_ad=False)
    with open('背景缺口图.jpg','rb') as f:
        target_byte=f.read()
    with open('背景完整图.jpg','rb') as f:
        full_byte=f.read()
    dis=slide.slide_comparison(target_byte,full_byte)
    # print(dis)
    return dis['target'][0]

def __ease_out_expo(sep):
    """
    缓动函数 easeOutExpo
    参考：https://easings.net/zh-cn#easeOutExpo
    """
    if sep == 1:
        return 1
    else:
        return 1 - pow(2, -10 * sep)

def get_slide_track(distance):
    """
    根据滑动距离生成滑动轨迹
    :param distance: 需要滑动的距离
    :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
        x: 已滑动的横向距离
        y: 已滑动的纵向距离, 除起点外, 均为0
        t: 滑动过程消耗的时间, 单位: 毫秒
    """

    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        [random.randint(-50, -10), random.randint(-50, -10), 0],
        [0, 0, 0],
    ]
    # 共记录count次滑块位置信息
    count = 30 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # 滑动过程消耗的时间
        t += random.randint(10, 20)
        if x == _x:
            continue
        slide_track.append([x, _y, t])
        _x = x
    slide_track.append(slide_track[-1])
    return slide_track

def vertify(gt,newcha,w,GTU,GTA):
    cookies = {
        "GeeTestUser": GTU,
        "GeeTestAjaxUser": GTA
    }
    url = "https://apiv6.geetest.com/ajax.php"
    params = {
        "gt": gt,
        "challenge": newcha,
        "lang": "zh-cn",
        "%24_BCN": "0",
        "client_type": "web",
        "w": w,
        "callback": "geetest_1727115859460"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(response.text)
    print(response)

def final():
    cha,gt=get_challenge_gt()
    GTU=get_GeeTestUser_cookie(gt)
    GTA=get_GeeTestAjaxUser_cookie(GTU,gt,cha)
    newcha,bg,fullbg,c,s=get_newchallenge_c_s_image(cha,gt,GTU,GTA)     # 获取滑块相关图片
    with open('未还原缺口背景图.jpg','wb') as f:
        f.write(requests.get(f'https://static.geetest.com/{bg}',headers=headers).content)
    with open('未还原背景图.jpg','wb') as f:
        f.write(requests.get(f'https://static.geetest.com/{fullbg}',headers=headers).content)
    # slice_image=requests.get(f'https://static.geetest.com/{slice}',headers=headers).content
    # with open('滑块图.jpg','wb') as f:
    #     f.write(slice_image)
    img_list=['未还原缺口背景图.jpg','未还原背景图.jpg']
    bgimage,fullimage=fix_image(img_list)
    dis=get_distance(bgimage,fullimage)
    trace=get_slide_track(dis)
    # print(trace)
    w=execjs.compile(open('js.js','r',encoding='utf-8').read()).call('get_w',trace,c,s,gt,newcha)
    # print(w)
    vertify(gt,newcha,w,GTU,GTA)


for i in range(20):
    final()
    time.sleep(1)