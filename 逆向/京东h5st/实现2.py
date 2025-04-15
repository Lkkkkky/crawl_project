'''
=========================================================    
       @File     : 实现2.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/10/13 14:32
       @Desc     : 
=========================================================   
'''
import requests
import hashlib
import time
import re
import json
import subprocess
t = int(time.time()*1000)
def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.jd.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
cookies = {
    "3AB9D23F7A4B3C9B": "IP7ZOEW6HMAOR2YF23KYRWMTUEY6WE6YJCO4HO45KAOUDW75RJ6AXP3E73LX34Z3DYL6ZVYZKZQ2OLMLEB35CY63C4",
    "__jdu": "369041817",
    "areaId": "19",
    "ipLoc-djd": "19-1601-0-0",
    "shshshfpa": "0315a5f6-560b-3b6f-4a4f-e530675a58cd-1728735584",
    "shshshfpx": "0315a5f6-560b-3b6f-4a4f-e530675a58cd-1728735584",
    "unpl": "JF8EAK1nNSttWxtdBR1VGEARH1wHW1UPSB8HaWYFVl9ZTlVWS1EYRkN7XlVdWBRLFh9vZRRUWFNKXQ4ZBCsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrABwaEU5dXV5bOEonBF9XNVBfWElRBysDKxMgCQkIWl4KShRObWANVVhYQlQDKwMrEQ",
    "__jda": "76161171.369041817.1728735580.1728735581.1728799722.2",
    "__jdc": "76161171",
    "shshshfpb": "BApXSqKSah_dA4wvmpEzV2_iGjEfcnOkXBmoyUqtp9xJ1MthSF4G2",
    "__jdb": "76161171.6.369041817|2.1728799722",
    "__jdv": "76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_2a817f2c0e0b49629570133040bab2eb|1728801047397",
    "3AB9D23F7A4B3CSS": "jdd03IP7ZOEW6HMAOR2YF23KYRWMTUEY6WE6YJCO4HO45KAOUDW75RJ6AXP3E73LX34Z3DYL6ZVYZKZQ2OLMLEB35CY63C4AAAAMSQSJHNKYAAAAACEFWZGT533TXR4X",
    "_gia_d": "1"
}
url = "https://api.m.jd.com/"
params = {
    "h5st": "20241013143057739;1bxors2dkddkkkf8;b5216;tk03wb2981c8618np7WXk04TYXkek0cmb0jNV_qXUHm828xW_UyNqTtmu2EdkHydR-Yw0p9FG-nqJuLi_D9rHliLNlRT;1c2f750d0884377d5d96c12e2c50715d;4.8;1728801057739;UOG3MOUIwpg8rFQ9rFwKjNf7eNAK0W0I0Wv90WUOMmUI2uzOoJg_0WUOMm0OmODKxxzJi6DJfCTIeGgKzVDJyRTJ1VTJwNQIzxzKg6zO2uzOm9S7vNA9fNUO2uWL0KjKxJAJiGwJwBw9fWDJj_AK1NQIjCQJdSDIyJzJ1BAK0W0I0K-_gdA_zNUO2uWL0OzLeeUJgZB9qxw93BT80W0I0_vO2W0UqO05hGC_BRBF_5x8HNUOcOE7nFw71NvO2W0UqO0KjeA8-NUOcO09mNUO2uWLZVUOMWTOcOUIhNwO2WUO2uWL0OUOcOkJhNwO2WUO2uWLkOTOcO0JhNwO2WUO2uWLmW0I0CD50NUO2WUOMmUK2uzOiCv_0WUO2W0Uq6jK2uzOjCv_0WUO2W0UqSDL2uzOkCv_0WUO2W0UqOUJoSzLmOUOcOEKhNwO2WUO2uWLmW0I0qg50WUO2W0UqCTOcOk6qNUO2WUOMmUK2uzOqNUO2WUOMmUK2uzOy5vO2WUO2um42uzOydA9i1-90WUOMmE3bV0I0WP60WUOMm0Oi_T42qTJgeA8-VkImeUKlWUBIVk6fZQ9oxgB0W0I0SA5jNUO2um4;e71c267fa2920d9e31735683871e8e96",
    "appid": "www-jd-com",
    "body": "{\"page\":2,\"pagesize\":25,\"area\":\"19_1601_0_0\",\"source\":\"pc-home\"}",
    "clientVersion": "1.0.0",
    "client": "pc",
    "functionId": "pc_home_feed",
    "t": str(t),
    "uuid": "76161171.369041817.1728735580.1728735581.1728799722.2",
    "loginType": "3",
    "x-api-eid-token": "jdd03IP7ZOEW6HMAOR2YF23KYRWMTUEY6WE6YJCO4HO45KAOUDW75RJ6AXP3E73LX34Z3DYL6ZVYZKZQ2OLMLEB35CY63C4AAAAMSQSC6O7IAAAAADXT567PWFRFZFEX",
    "callback": "jsonpMore2Goods",
    "_": "1728801057757"
}
data={
    "appid": "www-jd-com",
    "body": sha256(params['body']),
    "clientVersion": "1.0.0",
    "client": "pc",
    "functionId": "pc_home_feed",
    "t": t
}
result=subprocess.run(['node',r'E:\Program Files\Desktop\Jing3\逆向\京东h5st\11.2.js',json.dumps(data)],capture_output=True,text=True,encoding='utf-8')
print(result.stdout)
h5st=re.findall(r'\$\$(.*?)\$\$',result.stdout)[0]
print('h5st==',h5st)
# ddddd=re.findall(r'receive data-->(.*?)',result.stdout)[0]
# print(ddddd)
params['h5st']=h5st
print(params)
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)