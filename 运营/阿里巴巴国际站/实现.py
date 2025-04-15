'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/17 10:05
       @Desc     : 
=========================================================   
'''
import requests
import csv
import 企查查实现
import time
f=open('company.csv','a+',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['companyUrl','companyName','name','phone','address'])
# csv_writer.writeheader()
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "origin": "https://www.alibaba.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.alibaba.com/factory/index.html?spm=a2700.product_home_l0.home-tab.manufacturers",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "cbc": "T2gA2x0wmTvJMkHGf7E8c_gmSUks9xhRrKRq9JB6uIsooRsqDo9YYCAIVJCvCWe17Ec=",
    "umdata_": "T2gAmZia9kH1aJ0vErV8y5IsXCCxXD4f5vRKOD3GNbOlB_dt9VjPDTZYfzcColsiseg=",
    "cna": "4MLnH9hJawoCAct38XPO+DFJ",
    "ali_apache_id": "33.50.128.217.1734399201258.403775.7",
    "cookie2": "1640196e5fcbadf05dedcc15e5bd6275",
    "xlly_s": "1",
    "t": "42a731ec5bd375a74a471a625b16d8b8",
    "_tb_token_": "7e534e7066bed",
    "_samesite_flag_": "true",
    "_m_h5_tk": "700af12b3ba86a879ce3df0f3cd0208c_1734407171962",
    "_m_h5_tk_enc": "8ea37ba19a3b026b483e879b4a8b246d",
    "_lang": "zh_CN:GB18030",
    "ali_apache_tracktmp": "W_signed=Y",
    "ali_apache_track": "mt=2|mid=cn1574357083onsu",
    "xman_us_f": "x_locale=zh_CN&x_user=CN|ass|jjun|cnfm|284588481&no_popup_today=n&last_popup_time=1734399606483&x_l=1",
    "intl_common_forever": "HZotnqYjKD7cHRWT0ufSDeRa2XvI8U2mvkWG3R6pdFhH7GyVGEOWew==",
    "recommend_login": "email",
    "xman_f": "N15NvvPevjQVjmjEQjfbOHfu++8uZ6U/nCYyNZqF7ie6jcViDvlvCD5F13pRQFohxjy5w5gpd6KXjaun72Yx+t0oXKZfEpjLRt+UClH6vC30kHwU7wJUchWfqFozjJOZGdnNJIjzoQYOLSWoXeVPQl+4VtRFYifjlhxCaoj/mHw6LQ4MX59uY0XdQG2E48ub+lxqJaxB+aBXf+cKp01YOYC6JU6qxjjeQ7qjp1b2LmWr44+sH2aUnMMI22w66b8a+RU+EqgHpR6DaY8uwkFVL2mymg59MDALhpCe3jwUWeP3vA5NAyM7B88xkzeXlkjh3lcKw4k8gOJerkjXMvSYbZcB82G21561x4AGOCdJj90=",
    "acs_usuc_t": "acs_rt=5383b6f5fb734e2384393602d6d1d0f3",
    "intl_locale": "zh_CN",
    "xman_i": "aid=1990004753302",
    "sgcookie": "E100OXk3R0nKh+3y2sRfVNApaYm5wArld3QE+zhXRJjD4kGXFYZiLAeINxLVKH5e6vdcEp20E1o2nfjjTjcRnNtGlEtxxdag4RRr2B3kwF5QSh8=",
    "xman_t": "5+FAirZbVq5ox8LemEX6JEFXuhP8QJAMH37Ko1yAqEL/5pq+7q2tlH8DDSXzYiTD",
    "_ga": "GA1.1.2025389978.1734399932",
    "_fbp": "fb.1.1734399932005.93334164888283873",
    "_ym_uid": "173439993498654053",
    "_ym_d": "1734399934",
    "_ym_isad": "2",
    "_uetsid": "99c9e710bc1811ef854fe3bb6f11da34",
    "_uetvid": "99c9f4b0bc1811ef8b61ffede1312c84",
    "cto_bundle": "Xx-XdF91ZUltcHV1dHFBTURNTTExZDhlSiUyRlVkZzdqV1Y2QUtxTFc0MGpBME44NEJFVjJ3VzUyVjR6aDhnbmRPNTQyJTJGa2pCSzVvMEVDZGpUJTJGcUNDZ0VEZG1mVnZFb2ltZ2gzYXJVMEV2QnJ0VjBIT3BHZDNKcXVSa09WJTJCeENicWcxcmJtWUxTM1JVdEFEYXRGNHAzd1d2VFoydyUzRCUzRA",
    "_ga_RVSKK1KF5N": "GS1.1.1734399931.1.1.1734400009.60.0.0",
    "buyer_ship_to_info": "local_country=US",
    "sc_g_cfg_f": "sc_b_currency=USD&sc_b_locale=zh_CN&sc_b_site=US",
    "NWG": "NNW",
    "icbu_s_tag": "10_11",
    "JSESSIONID": "C5FF8A06542263B57EE88E242A9C458F",
    "ug_se_c": "organic_1734401067641",
    "isg": "BOrqS4pUecVMYPUpcPfBwLEvO1CMW261f4IUC3SilTxFp4hhXuzPxV2RM9O7V-ZN",
    "tfstk": "gZMsUHg9LNb_9E_njFKUR7YE3bebfq9rMiZxqmBNDReOkZn88h2q_I2bGqzEQPoaBswjk0Ua01y9hjgoPZPx3rkXcRDE_tzwS-ixz-TyzLJrjc2gHU8PLOLMqRqfXrEOuJnLb-ZO0iqurc20He5iReHZj43vEP3THHwLDoBTHSeYppU301UxkPFdJuZuHr3xkWnLDoWAM5UTp6U3D-Exk-KQpjWhVoO_SctUgA1x815Efy6AHvZpozo67trIKlaLPcH1jGx0f5a-XyTlEC1a9mVjniXbwchoou3OWEamdDHtw4LF_Ph7c0ljXdBLQAmtwSHJos37CqN-BWsACJmTRJZKen5u8vaZkANp4TN4pYP8BXRH7Sy_VqHi5i6xyDorIWDXPwUm_u2LcxxRGrNA49BzPlKRGMNlhkayAH1ci80VI0K6ZCC76kq_THtCWjVTxkayAH1ci5E3fW-BANhc."
}
for page in range(60,125):
    url = "https://insights.alibaba.com/openservice/gatewayService"
    params = {
        "endpoint": "pc",
        "pageSize": "12",
        "categoryIds": "0",
        "pageNo": str(page),
        "modelId": "10300"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    res_json=response.json()
    list=res_json["data"]["list"]
    for i in list:
        companyUrl=i["companyUrl"]
        companyName=i["companyName"]
        name,phone,address=企查查实现.get_phone(companyName)
        format_dict={
            "companyUrl":companyUrl,
            "companyName":companyName,
            "name":name,
            "phone":phone,
            "address":address
        }
        print(format_dict)

        csv_writer.writerow(format_dict)
        time.sleep(15)
