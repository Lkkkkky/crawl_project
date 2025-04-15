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
session=requests.session()

def get_salt_execution():

    url = "https://authserver.gdut.edu.cn/authserver/login"
    response = session.post(url,headers=headers)
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
    response = session.post(url,headers=headers,params=params, data=data)


    return response.cookies.get_dict().get('JSESSIONID')


def get_subject_info(JSESSIONID):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "$Referer": "https://jxfw.gdut.edu.cn/xsgrkbcx\\u0021getXsgrbkList.action",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "cookies": f'JSESSIONID={JSESSIONID}',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "JSESSIONID": JSESSIONID
    }
    url = "https://jxfw.gdut.edu.cn/xsgrkbcx!xsAllKbList.action"
    params = {
        "xnxqdm": "202301"
    }
    response = session.get(url,headers=headers,params=params,cookies=cookies)

    print(response.text)
    print(session.cookies)
    # print(response)



salt,execution=get_salt_execution()
JSESSIONID=get_session(salt,execution)
print(JSESSIONID)
get_subject_info(JSESSIONID)