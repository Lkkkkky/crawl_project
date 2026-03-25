import requests
import time
import json
import os
import hashlib
import random
from loguru import logger

# requests.get('https://api.day.app/YToREckaeQXotQJPrn7MWa/已上架?url=vipshop://showWebview?url=https://t.vip.com/hsbpB3Uqzk9')

SALT = "326ee2ac14bf485897223c664e285a0e&a2c359b80482547446e4c6efce15b538"

def sha1(s: str) -> str:
    return hashlib.sha1(s.encode("utf8")).hexdigest()
def get_api_sign(params):
    """计算 api_sign 签名，严格按照 test.py 的算法"""
    # 1. 按照 key 排序 (包含所有参数)
    sorted_keys = sorted(params.keys())
    
    # 2. 拼接所有 value
    values_string = "".join([str(params[k]) for k in sorted_keys])
    
    # 3. 构造最终加密字符串: salt + values
    params_string = f"{SALT}{values_string}"
    
    # 4. 单次 SHA1 哈希
    sign1 = sha1(params_string)
    
    # 5. 返回完整格式
    return f"OAuth api_sign={sign1}"


headers = {
    "Authorization": "OAuth api_sign=78527c878e57f260b79352e60dc676b040b83698",
    "User-Agent": "{\"appversion\":\"7.01.0\",\"platform\":\"android\",\"webTForm\":\"okhttp\",\"originid\":\"\"}",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "571",
    "Host": "api.union.vip.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}
url = "https://api.union.vip.com/vsp/goods/queryGoodsShareInfo"
data = {
    "adCode": "hisGoods",
    "api_key": "8dc6608ab8c84820bb2a220df4d9961e",
    "appName": "weixiangke_android",
    "appVersion": "7.01.0",
    "deviceToken": "f10b69e2-7565-300a-9650-54c644a4dab8",
    "fdc_area_id": "104104101",
    "giftCouponId": "",
    "goodsId": "6921172663483581531",
    "landUrl": "https://m.vip.com/product-1710613307-6921172663483581531.html",
    "marsCid": "494eddc9-21f8-3ea6-bc0f-b9e45e355d80",
    "mars_cid": "494eddc9-21f8-3ea6-bc0f-b9e45e355d80",
    "phone_model": "m2012k11ac",
    "queryGiftCoupon": "0",
    "queryWxQRCode": "0",
    "sd_tuijian": "0",
    "sharePanelOptSwitch": "0",
    "timestamp": str(int(time.time())),
    "ucode": "dqek4bdm",
    "userToken": "da29578381da58ac2af124ade05c0fba",
    "warehouse": "VIP_NH"
}
get_api_sign(data)
dynamic_sign = get_api_sign(data)
headers["Authorization"] = dynamic_sign
response = requests.post(url, headers=headers, data=data)

def extract_share_info(response_text):
    """
    从 API 响应中提取商品口令(onlyCommand)
    返回格式: 唯口令内容
    """
    try:
        res_json = json.loads(response_text)
        # 唯品会 API 返回的 code 可能是 200，也可能是 '200' 字符串，或者通过 msg 判断
        if res_json.get('code') in [200, '200'] or res_json.get('msg') == 'success':
            data_obj = res_json.get('data', {})
            # 尝试从不同的可能结构中提取 onlyCommand
            
            # 常见结构 1：直接在 data 下
            if 'onlyCommand' in data_obj:
                return data_obj.get('onlyCommand')
            
            # 常见结构 2：在 shareInfo 字典下
            share_info = data_obj.get('shareInfo', {})
            if 'onlyCommand' in share_info:
                return share_info.get('onlyCommand')
                
            # 常见结构 3：在 commandInfo 字典下
            command_info = data_obj.get('commandInfo', {})
            if 'onlyCommand' in command_info:
                return command_info.get('onlyCommand')
                
            return "未找到口令字段"
        else:
            return f"请求失败，状态码或业务码异常: {res_json.get('msg', '')}"
    except json.JSONDecodeError:
        return "解析JSON失败"
    except Exception as e:
        return f"提取出错: {str(e)}"

# 测试提取函数
share_command = extract_share_info(response.text)
print(f"提取到的唯口令: {share_command}")





