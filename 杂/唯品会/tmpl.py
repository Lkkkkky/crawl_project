import requests
import time
import hashlib

data={
    "pageNo": "1",
    "pageSize": "14",
    "api_key": "8dc6608ab8c84820bb2a220df4d9961e",
    "appName": "weixiangke_android",
    "appVersion": "7.01.0",
    "deviceToken": "f10b69e2-7565-300a-9650-54c644a4dab8",
    "fdc_area_id": "104104101",
    "marsCid": "494eddc9-21f8-3ea6-bc0f-b9e45e355d80",
    "mars_cid": "494eddc9-21f8-3ea6-bc0f-b9e45e355d80",
    "phone_model": "m2012k11ac",
    "sd_tuijian": "0",
    "timestamp": "1773606477",
    "ucode": "dqek4bdm",
    "userToken": "da29578381da58ac2af124ade05c0fba",
    "warehouse": "VIP_NH"
}


def sha1(data: str) -> str:
    return hashlib.sha1(data.encode("utf8")).hexdigest()


def calc_api_sign(params: dict) -> str:
    _salt = "326ee2ac14bf485897223c664e285a0e"
    sorted_keys = sorted(params.keys())
    # 仅拼接所有的值 (移除之前手动插入的 '114')
    values_string =  "&".join(["{}={}".format(key, params[key]) for key in sorted(params.keys())])
    print(f"待加密字符串: {values_string}")
    return sha1(_salt + sha1(_salt + values_string))
print(calc_api_sign(data))