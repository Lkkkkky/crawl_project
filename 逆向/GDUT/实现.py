import requests
import re
import execjs



from lxml import etree

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://authserver.gdut.edu.cn",
    "Pragma": "no-cache",
    "Referer": "https://authserver.gdut.edu.cn/authserver/login?service=https%3A%2F%2Fjxfw.gdut.edu.cn%2Fnew%2FssoLogin",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

# 定位到pwdEncryptSalt
cookies={}
def get_first_session():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://jxfw.gdut.edu.cn/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://jxfw.gdut.edu.cn/login!welcome.action"
    response = requests.get(url, headers=headers)
    first_JSESSIONID=response.cookies.get_dict().get("JSESSIONID")
    cookies['JSESSIONID']=first_JSESSIONID
    print(cookies)
    return first_JSESSIONID

def get_salt_execution():

    url = "https://authserver.gdut.edu.cn/authserver/login"
    response = requests.post(url, headers=headers ,cookies=cookies)
    html_res=etree.HTML(response.text)
    salt=html_res.xpath('//input[@id="pwdEncryptSalt"]/@value')[0]
    execution=html_res.xpath('//*[@id="execution"]/@value')[0]
    return salt,execution

def get_session(salt,execution):

    url = "https://authserver.gdut.edu.cn/authserver/login"
    params = {
        "service": "https://jxfw.gdut.edu.cn/new/ssoLogin"
    }
    enc_pass=execjs.compile(open('enc.js','r',encoding='utf-8').read()).call('enc_pass','20030531lky@',salt)
    data = {
        "username": "3121005299",
        "password": enc_pass,
        "captcha": "",
        "_eventId": "submit",
        "cllt": "userNameLogin",
        "dllt": "generalLogin",
        "lt": "",
        "execution": execution
    }
    response = requests.post(url, headers=headers, params=params, data=data)
    happyVoyage=response.cookies.get_dict().get('happyVoyage')
    CASTGC=response.cookies.get_dict().get('CASTGC')
    cookies['happyVoyage'] = happyVoyage
    cookies['CASTGC'] = CASTGC



def get_subject_info():
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://jxfw.gdut.edu.cn/xsbjkbcx!xskbList.action?xnxqdm=202302&bjdm=109939144&zc=12",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    url = "https://jxfw.gdut.edu.cn/xsbjkbcx!getKbRq.action"
    params = {
        "xnxqdm": "202302",
        "zc": "12",
        "bjdm": "109939144"
    }

    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(response.text)
    # print(response)

first_JSESSIONID=get_first_session()
#
salt,execution=get_salt_execution()
get_session(salt,execution)

get_subject_info()