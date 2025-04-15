'''
=========================================================    
       @File     : address.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/26 10:50
       @Desc     : 
=========================================================   
'''
import json

import requests
import hashlib



def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://sale.1688.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "4921a5565977fe903f3957f08fcb0107_1732592759270",
    "_m_h5_tk_enc": "7332d2de16aebcfb0133c585ed1f1c9e",
    "cna": "VxbMHxwaJCYCAbfsE96tvqbx",
    "xlly_s": "1",
    "cookie1": "U7kCem%2FLBWmXIqt07nPeXOgRpk%2F0MRabtVEeHmvwZtY%3D",
    "cookie2": "198d92feab839b20ab666f0539f80bb5",
    "cookie17": "UUpgQy0KpNd3GoIQ3g%3D%3D",
    "sgcookie": "E100Hm8SFALw%2FNzkwMNbedatEjI6qSwNjuEfTgrjt34WYTDi21aiA1Nl4%2B2U3EbbthseDXfcriK5wJ%2FbIhNjoW%2BSMQX8%2BIMAv450fFj7vr5HwHg%3D",
    "t": "3ee973d5b98de23e1476035588ef4c4c",
    "_tb_token_": "587e989fb7759",
    "sg": "68d",
    "csg": "3b30c807",
    "lid": "tb0794515046",
    "unb": "2215447194428",
    "uc4": "nk4=0%40FY4O7o5J9UxMoQfLR7DudvFY2wdtLnI%3D&id4=0%40U2gqzJtMDo8gL5hWPzkrZGufLn0LFwXv",
    "_nk_": "tb0794515046",
    "__cn_logon__": "true",
    "__cn_logon_id__": "tb0794515046",
    "ali_apache_track": "c_mid=b2b-2215447194428b1a46|c_lid=tb0794515046|c_ms=1",
    "ali_apache_tracktmp": "c_w_signed=Y",
    "last_mid": "b2b-2215447194428b1a46",
    "_csrf_token": "1732585677710",
    "leftMenuLastMode": "EXPEND",
    "leftMenuModeTip": "shown",
    "keywordsHistory": "%E9%A6%99%E6%B0%B4",
    "isg": "BMLCuSt9Edieqw2EFBHz0xlfE8gkk8atZ8pMgwzb7jXgX2LZ9CMWvUicD1sjDz5F",
    "tfstk": "fU2icpZRN5l_cudnx6k1gzKfXifLfhMb3rpxkx3VT2uCflhY0vREfcl4BAET-Z4Y0q3Z_m-eY2E4BfrO1mJ0mPjsHVHwii4UVfSsWVpm0ouQMxH9BJ008yUmGGgxuq4Y05IdeTE_fxM4oaBRenZgv1yiuEHVYoZXyaQRe9E_fxMVyPIZ0gvnc2oZbKuVxkuIDKkq7j8eT0uE3qzq_2-E40Rq0mRNLMmj8qkq3vO63424dJ7TAkKiCypQnccirK3HnKjxjf0zb2bPzJXqs4rZ-K7SQj2jo2wPJ6qQT5ztArXl-xaQgro08e7x1oP3-c4OrEgYClemWlfN5kDESPlgtgRsxkegmSlhbOrnIVc8Ky-v1AV45-c_sns7YAzQN4GNOwi3B8hmPXYF7kEn7bV0Ww9qW7qU-bepJLHbRSzqmy8G4vAeaCB2hDSYKIOj_DinyZKBsaqG0RaGxMA51foIXaIhxIOj_DinyMjHN1GZAcQR."
}
url = "https://h5api.m.1688.com/h5/mtop.mbox.fc.common.gateway/2.0/"
my_token=cookies['_m_h5_tk'][0:32]
data_c="{\"fcGroup\":\"cbu-seller-fc\",\"fcName\":\"factory-card-common-fn\",\"serviceName\":\"factoryCoreInfoService\",\"params\":\"{\\\"memberId\\\":\\\"b2b-3603363763227c6\\\",\\\"extendParam\\\":{\\\"query\\\":\\\"\\\",\\\"trafficSource\\\":\\\"factory_card@detail_pc\\\"}}\"}"
params = {
    "jsv": "2.6.1",
    "appKey": "12574478",
    "t": "1732589228863",
    "sign": md5(my_token+ "&" + '1732589228863' + "&" + '12574478' + "&" +data_c),
    "v": "2.0",
    "type": "jsonp",
    "isSec": "0",
    "timeout": "5000",
    "api": "mtop.mbox.fc.common.gateway",
    "jsonpIncPrefix": "mboxfc",
    "dataType": "jsonp",
    "callback": "mtopjsonpmboxfc1",
    "data": "{\"fcGroup\":\"cbu-seller-fc\",\"fcName\":\"factory-card-common-fn\",\"serviceName\":\"factoryCoreInfoService\",\"params\":\"{\\\"memberId\\\":\\\"b2b-3603363763227c6\\\",\\\"extendParam\\\":{\\\"query\\\":\\\"\\\",\\\"trafficSource\\\":\\\"factory_card@detail_pc\\\"}}\"}"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
res=response.text.replace('mtopjsonpmboxfc1(','').replace(')','')
res_json=json.loads(res)
print(res_json['data']['result']['factoryDetailedAddress'])
