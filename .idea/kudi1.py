import requests
import time
def generate_13_digit_timestamp():
    # 获取当前时间的秒数和微秒数
    current_time = time.time()
    seconds = int(current_time)  # 秒数部分
    milliseconds = int((current_time - seconds) * 1000)  # 毫秒数部分，取0到999的整数部分

    # 组合成13位时间戳（前10位是秒，后3位是毫秒）
    timestamp = int(f"{seconds}{milliseconds:03d}")

    return timestamp

# 生成并打印13位时间戳
timestamp=generate_13_digit_timestamp()
print(timestamp)
timestampstr=str(timestamp)
token1='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJpc05ld01lbWJlclwiOmZhbHNlLFwibWVtYmVySWRcIjoyNTc5MjM2OTAyMCxcIm1lbWJlck5vXCI6XCIyNTc5MjM2OTAyMFwiLFwibWVtYmVyVHlwZVwiOjAsXCJtb2JpbGVcIjpcIjE3ODE5NDYxOTg0XCIsXCJvcGVuSWRcIjpcIm9ROVpWNU1LVXI5eHFhRWZvbzJMUzRyUnh0LTRcIixcInRlcm1pbmFsVHlwZVwiOlwiOTAxXCIsXCJ1bmlvbklkXCI6XCJvMlNfTDUxZ2NlYTU1dWY2MDhFRFNZWFN1VFpNXCJ9IiwiaXNzIjoiaXNzdWUiLCJleHAiOjE3MjI5OTcwNjUsImlhdCI6MTcyMDQwNTA2NX0.Yyj4FRmGP2QYMbVApq2XJ0UFLo-Q-gllPdFJzkXB3r4'
cookies = {
    'sajssdk_2015_cross_new_user': '1',
    'HWWAFSESTIME': '1720405058009',
    'HWWAFSESID': '4eaefd063f7afc4520',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2225792369020%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwOTAyMWYxNDcwLTBiNTZmMmRkY2JlMzEwOC02ZDNjMWYyYy0yMDczNjAwLTE5MDkwMjFmMTRiMzllIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D',
}

headers = {
    'Host': 'ma.cotticoffee.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '152',
    'version': 'v1',
    'split_timestamp': '0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/9185',
    'Content-Type': 'application/json',
    'timestamp': timestampstr,
    'brandMdCode': '20200000006',
    'api-version': 'v1',
    'token': token1,
    'sign': '9EAABCC98439B55E210A4E98605260E6',
    'appKey': '2YAhmad694MnzqmcPQ5X6TJ6EoSx6sYx',
    'Accept': '*/*',
    'Origin': 'http://m.cotticoffee.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'http://m.cotticoffee.com/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': 'sajssdk_2015_cross_new_user=1; HWWAFSESTIME=1720405058009; HWWAFSESID=4eaefd063f7afc4520; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2225792369020%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwOTAyMWYxNDcwLTBiNTZmMmRkY2JlMzEwOC02ZDNjMWYyYy0yMDczNjAwLTE5MDkwMjFmMTRiMzllIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D',
}

json_data = {
    'activityNo': 'NAkaizWulk7I2rUkS7piRPd1xJ-dcZrhy2fQ8L2avL8',
    'mobile': '17819461984',
    'comeFrom': '4',
    'openid': None,
    'blackBox': 'oWPHe17204050828ZFUpoJNS8c',
}

response = requests.post(
    'http://ma.cotticoffee.com/cotti-capi/universal/coupon/receiveLaunchRewardH5',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
)
res=response.text
print(res)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"activityNo":"NAkaizWulk7I2rUkS7piRPd1xJ-dcZrhy2fQ8L2avL8","mobile":"17819461984","comeFrom":"4","openid":null,"blackBox":"oWPHe17204050828ZFUpoJNS8c"}'
#response = requests.post(
#    'https://ma.cotticoffee.com/cotti-capi/universal/coupon/receiveLaunchRewardH5',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#    verify=False,
#)