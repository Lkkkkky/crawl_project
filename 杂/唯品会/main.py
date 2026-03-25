import requests
import time
import json
import os
import hashlib
import random
from loguru import logger

# 禁用 HTTPS 警告（因为 verify=False）
requests.packages.urllib3.disable_warnings()

CACHE_FILE = "commission_cache.json"
LAST_HEARTBEAT_TIME = 0 # 记录上次推送全量列表的时间

# 不监控的商品ID列表 (字符串格式)
EXCLUDED_GOODS_IDS = [
    "6920962187441807504",
    "6921439510821923025",
    "6921661304706772753",
    "6919021290616170513",
    "6919021290549000209",
    "6921864134839482135", # 示例ID，请替换为实际不需要监控的商品ID
]

# 参考 test.py 的签名算法
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
    "Host": "api.union.vip.com",
    "Authorization": "", # 动态生成
    "User-Agent": "{\"appversion\":\"7.01.0\",\"platform\":\"android\",\"webTForm\":\"okhttp\",\"originid\":\"\"}",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "400", # 保持与 test.py 一致
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
    "timestamp": str(int(time.time())), # 动态生成
    "ucode": "dqek4bdm",
    "userToken": "da29578381da58ac2af124ade05c0fba",
    "warehouse": "VIP_NH"
}

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=4)

def get_padded_str(s, width):
    extra_width = sum(1 for char in s if ord(char) > 255)
    return s + ' ' * (width - len(s) - extra_width)

def extract_share_info(response_text):
    """
    从 API 响应中提取商品口令(onlyCommand)
    返回格式: 唯口令内容
    """
    try:
        res_json = json.loads(response_text)
        if res_json.get('code') in [200, '200'] or res_json.get('msg') == 'success':
            data_obj = res_json.get('data', {})
            if 'onlyCommand' in data_obj:
                return data_obj.get('onlyCommand')
            share_info = data_obj.get('shareInfo', {})
            if 'onlyCommand' in share_info:
                return share_info.get('onlyCommand')
            command_info = data_obj.get('commandInfo', {})
            if 'onlyCommand' in command_info:
                return command_info.get('onlyCommand')
            return "未找到口令"
        else:
            return "提取口令失败"
    except Exception:
        return "解析口令失败"

def get_share_command(goods_id, brand_id):
    """请求商品唯口令"""
    url = "https://api.union.vip.com/vsp/goods/queryGoodsShareInfo"
    land_url = f"https://m.vip.com/product-{brand_id}-{goods_id}.html"
    data = {
        "adCode": "hisGoods",
        "api_key": "8dc6608ab8c84820bb2a220df4d9961e",
        "appName": "weixiangke_android",
        "appVersion": "7.01.0",
        "deviceToken": "f10b69e2-7565-300a-9650-54c644a4dab8",
        "fdc_area_id": "104104101",
        "giftCouponId": "",
        "goodsId": str(goods_id),
        "landUrl": land_url,
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
    
    headers = {
        "User-Agent": "{\"appversion\":\"7.01.0\",\"platform\":\"android\",\"webTForm\":\"okhttp\",\"originid\":\"\"}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "api.union.vip.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    
    dynamic_sign = get_api_sign(data)
    headers["Authorization"] = dynamic_sign
    
    try:
        response = requests.post(url, headers=headers, data=data, verify=False, timeout=10)
        if response.status_code == 200:
            return extract_share_info(response.text)
    except Exception as e:
        logger.error(f"提取唯口令请求异常: {e}")
    return "无口令"

def check_commission():
    global LAST_HEARTBEAT_TIME
    try:
        # 1. 动态生成当前时间戳并更新 data
        current_ts = str(int(time.time()))
        data["timestamp"] = current_ts
        
        # 2. 计算动态 api_sign 并更新 headers
        dynamic_sign = get_api_sign(data)
        headers["Authorization"] = dynamic_sign
        response = requests.post(url, headers=headers, data=data, verify=False, timeout=10)
        if response.status_code == 200:
            res_json = response.json()
            data_obj = res_json.get('data') or {}
            goods_list = data_obj.get('goodsList', [])
            
            if not goods_list:
                logger.warning("未获取到商品数据，请检查响应内容。")
                print("服务器响应内容:", response.text)
                return
            
            cache = load_cache()
            has_changed = False
            seen_names = set() # 用于记录本次检测中已经处理过的商品名称
            
            # 记录所有商品的消息列表（用于定时推送全量）
            all_goods_messages = []
            # 记录变动的消息列表
            change_messages = []

            print(f"\n[{time.strftime('%H:%M:%S')}] 当前商品监控中...")
            print(f"{get_padded_str('商品名称', 50)} | {'佣金比例':<10} | {'上架状态':<10}")
            print("-" * 80)

            for goods in goods_list:
                goods_id = str(goods.get('goodsId'))
                
                # 过滤不监控的商品
                if goods_id in EXCLUDED_GOODS_IDS:
                    continue

                name = goods.get('name', '未知商品')
                current_ratio = str(goods.get('commissionRatio', '0'))
                
                # 获取商品链接 (尝试获取 url 字段，如果不存在则尝试拼接)
                # 假设商品链接可能是 goods.get('url') 或需要根据 goodsId 拼接
                # 根据常见模式，尝试获取 url 字段
                goods_url = goods.get('url', '')
                if not goods_url:
                     # 备用方案：尝试拼接唯品会商品详情页
                     goods_url = f"https://detail.vip.com/detail-{goods.get('brandId', '0')}-{goods_id}.html"

                # 获取上架状态
                is_offline = goods.get('isOffline', False)
                status_name = goods.get('statusName') or ("在架" if not is_offline else "已下架")
                
                # 获取商品 brandId，用于拼接和获取口令
                brand_id = goods.get('brandId', '0')
                
                # 尝试从缓存中获取口令，若无则请求提取
                if goods_id in cache and cache[goods_id].get('share_command') and cache[goods_id].get('share_command') not in ["无口令", "未找到口令", "提取口令失败", "解析口令失败"]:
                    share_command = cache[goods_id].get('share_command')
                else:
                    share_command = get_share_command(goods_id, brand_id)
                    time.sleep(0.5) # 防止请求过快
                
                # 如果该名称在本次检测中已经处理过，则跳过
                if name in seen_names:
                    continue
                seen_names.add(name)
                
                # 记录商品信息用于全量推送
                all_goods_messages.append(f"【{status_name}】{name} | 佣金: {current_ratio}% | 链接: {goods_url} | {share_command}")

                # 打印当前数据（终端保持打印，方便本地查看）
                print(f"{get_padded_str(name, 50)} | {current_ratio:<10}% | [{status_name}] |  {share_command} | {goods_url}")

                # 检查缓存中是否存在且比例或状态是否变化
                if goods_id in cache:
                    old_ratio = cache[goods_id].get('ratio')
                    old_status = cache[goods_id].get('status')
                    
                    item_changed = False
                    change_detail = []
                    
                    # 佣金比例变动
                    if old_ratio != current_ratio:
                        change_detail.append(f"佣金: {old_ratio}% -> {current_ratio}%")
                        item_changed = True
                    
                    # 上架状态变动
                    if old_status != status_name:
                        change_detail.append(f"状态: {old_status} -> {status_name}")
                        item_changed = True
                    
                    if item_changed:
                        msg = f"{name}: {' | '.join(change_detail)} | 提取到的唯口令: {share_command}"
                        print(f"检测到变动: {name}")
                        logger.info(msg.replace("<br>", " "))
                        change_messages.append(msg)
                        has_changed = True
                
                # 新发现的商品且状态为"有机会"，也加入推送
                elif "有机会" in status_name:
                    msg = f"新发现: {name} | 状态: {status_name} | 佣金: {current_ratio}% | 提取到的唯口令: {share_command} | 链接: {goods_url}"
                    print(f"检测到新品(有机会): {name}")
                    logger.info(msg)
                    change_messages.append(msg)
                    has_changed = True
                
                # 更新当前数据到缓存对象
                cache[goods_id] = {
                    "name": name,
                    "ratio": current_ratio,
                    "status": status_name,
                    "share_command": share_command
                }
            
            # 逻辑 1：如果有变动，立即推送变动的商品信息
            if change_messages:
                send_wechat("-----------------".join(change_messages), title="商品变动提醒")

            # 逻辑 2：每间隔 2 小时推送一次全量列表（Heartbeat）
            current_time = time.time()
            if (current_time - LAST_HEARTBEAT_TIME) >= 7200: # 7200秒 = 2小时
                heartbeat_msg = f"### 📋        当前监控商品清单 ({time.strftime('%H:%M:%S')}):------" + "".join(all_goods_messages)
                # send_wechat(heartbeat_msg, title="监控正常运行中")
                LAST_HEARTBEAT_TIME = current_time

            if has_changed or not os.path.exists(CACHE_FILE):
                save_cache(cache)
                
        else:
            logger.error(f"请求失败，状态码: {response.status_code}")
    except Exception as e:
        logger.error(f"检测出错: {e}")

def send_wechat(msg, title="商品监控提醒"): #微信推送
    url = 'https://xizhi.qqoq.net/XZ3a4f3a59ab6b0ddc999dbd3bf1867455.channel'
    data = {
        "title": title,
        "content": msg,
    }
    try:
        r = requests.post(url, json=data, timeout=15)
        logger.info(f"推送成功 [{title}]: {r.text}")
    except Exception as e:
        logger.error(f"推送失败: {e}")

if __name__ == "__main__":
    logger.info("启动佣金监控任务，每60秒检测一次...")
    # 首次运行先填充缓存
    check_commission()
    
    while True:
        time.sleep(random.randint(10, 15))
        check_commission()