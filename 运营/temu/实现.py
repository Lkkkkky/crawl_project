'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/17 14:34
       @Desc     : 
=========================================================   
'''
import requests



# session=requests.session()
# session.trust_env=False

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.temu.com/?_x_sessn_id=pt796ywkdf&refer_page_name=bgn_verification&refer_page_id=10017_1734416706642_n70ys0bjkw&refer_page_sn=10017&is_back=1",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "service-worker-navigation-preload": "2",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "api_uid": "CmycSWdFUbcoEwBKwZGGAg==",
    "timezone": "Asia%2FShanghai",
    "webp": "1",
    "_nano_fp": "XpmqX5dbn5gynqmoXT_VWzdVsrFIeWzzwiKsXWuY",
    "_bee": "ZY6Z2bKQvjI0dlMqYj64mYpkNV5vrdOd",
    "njrpl": "ZY6Z2bKQvjI0dlMqYj64mYpkNV5vrdOd",
    "dilx": "sz0UPc-iyyNeGI_ae_y7M",
    "hfsc": "L3yJeow57z/91pHKfQ==",
    "region": "211",
    "currency": "USD",
    "g_state": "{\"i_l\":0}",
    "_u_pa": "%7B%22nrpt_211%22%3A0%7D",
    "language": "en",
    "_hal_tag": "APcSbUucXHiv8V/o1ZcOYTPQh3WMup3ZV1/Q9d4ubYlf8sZQMJKPFmgP7VEPMGrAWQ==",
    "AccessToken": "6BMU3UUSDIDKLX5F634XWUJUAEHVLDSOVB6ZTJTXEDJRUDEW7IMQ0110d3374394",
    "user_uin": "BB5YALAEHUYP56KGEEY77Y67WEOLLATEHD4YHQBV",
    "isLogin": "1734416700624",
    "verifyAuthToken": "5bMGnwXcrLmmAxGC7Q2yJg59c38882b8d66ede8",
    "_ttc": "3.CXSrnp92gjBC.1765952707",
    "__cf_bm": "51pJNtmmf0qQBiWhXnZH2iYmUGYeqAT6oF1kpJqjqzw-1734418318-1.0.1.1-kWnXePmSf0alkV1OKMl0CNf9U97diH4iCcW_o1jViMzeL3GptJ9Z_jBeHag7x3A94y.d2qdhufsJPFyOx70_gA"
}
url = "https://www.temu.com/air-quality-o3-6841.html"
params = {
    "opt_level": "2",
    "title": "Air Quality",
    "_x_enter_scene_type": "cate_tab",
    "leaf_type": "bro",
    "show_search_type": "3",
    "refer_page_el_sn": "200055",
    "_x_sessn_id": "pt796ywkdf",
    "refer_page_name": "home",
    "refer_page_id": "10005_1734416713461_j4krs0oamz",
    "refer_page_sn": "10005",
    "filter_items": "400:1|0:1",
    "is_back": "1"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)