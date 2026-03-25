import requests
import time
import hashlib


headers = {
    "Host": "api.union.vip.com",
    "Authorization": "OAuth api_sign=83b91e0d6e05c471008e95efa8e6f8431e1441db",
    "User-Agent": "{\"appversion\":\"7.01.0\",\"platform\":\"android\",\"webTForm\":\"okhttp\",\"originid\":\"\"}",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "400",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}
url = "https://api.union.vip.com/vsp/share/history/goodsList"
data = {
    "api_key": "8dc6608ab8c84820bb2a220df4d9961e",
    "appName": "weixiangke_android",
    "appVersion": "7.01.0",
    "deviceToken": "f10b69e2-7565-300a-9650-54c644a4dab8",
    "fdc_area_id": "104104101",
    "marsCid": "494eddc9-21f8-3ea6-bc0f-b9e45e355d80",
    "mars_cid": "494eddc9-21f8-3ea6-bc0f-b9e45e355d80",
    "pageNo": "1",
    "pageSize": "14",
    "phone_model": "m2012k11ac",
    "sd_tuijian": "0",
    "timestamp": str(int(time.time())),
    "ucode": "dqek4bdm",
    "userToken": "da29578381da58ac2af124ade05c0fba",
    "warehouse": "VIP_NH"
}
def calc_authorization(params: dict) -> str:
    def sha1(s: str) -> str:
        return hashlib.sha1(s.encode("utf8")).hexdigest()
    _salt = "326ee2ac14bf485897223c664e285a0e&a2c359b80482547446e4c6efce15b538"
    sorted_keys = sorted(params.keys())
    value_parts = []
    for k in sorted_keys:
        value_parts.append(str(params[k]))
    values_string = "".join(value_parts)
    params_string = f"{_salt}{values_string}"
    print(f"待加密字符串: {params_string}")
    sign1 = sha1(params_string)
    return f"OAuth api_sign={sign1}"
headers["Authorization"] = calc_authorization(data)
print(headers["Authorization"])

response = requests.post(url, headers=headers, data=data, verify=False)

print(response.text)
print(response)
