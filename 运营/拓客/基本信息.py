'''
=========================================================    
       @File     : 基本信息.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/5 14:08
       @Desc     : 
=========================================================   
'''
import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "product-type": "25",
    "referer": "https://logistics.tungee.com/enterprise-details/57ca06b399326598/foreign-trade/factory?isOpenFrame=true",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "_co_i": "6437da3f6eceb92bef8936bd",
    "__wpkreporterwid_": "78b6ad7d-f2df-404c-15c0-6ecd7dade2af",
    "__last_enter_version": "logistics",
    "Hm_lvt_d6df51ae5ec3a1b64d27905896d77ba5": "1733370746",
    "HMACCOUNT": "4D4F61CE5656C745",
    "DISTINCT_ID": "15d2985a-e39f-45a2-a43e-58fc331c491d",
    "tg_referrer_source": "https%3A%2F%2Fuser.tungee.com%2F",
    "SecurityCenterDuId": "IlpNZVQ4ZHlwUVhIRTIrbCtGek0wR0FjPSI.GjLNSg._5cxZpsXzm3HscC5GR8LwHDZmxI",
    "acw_tc": "9cdd1a6e6d324bd2d99dd82a9eb27c77d2c3bc7a7608969da9e20c26a19fa7df",
    "Hm_lpvt_d6df51ae5ec3a1b64d27905896d77ba5": "1733378284",
    "accountCenterSessionId": ".eJwlj01PhEAQRP_LnPcwX80M3PTsQlQ8sBfSPd3jiismwErE-N9FPVZV8vLqS_UvrCplXQRItkQJhS-QQvKeUhT0UbPllB2S9wwgUQfnc3ZOsOAMkbzRPmjgJKSdDpETQxnQGrQUUzDZBRvZJU7WU4EQgD2bCKXV8rsayKTVQaUzjqNcdplVaM-jCPczfki_vPdMqsp4meWg5j_hpn3Wp-F26Gy31NvDW_Oodb09ubv2dW3a--Vou89jexrq7Watbed2YJ8nmc-qWqbrjrnOMv1_LwIYRwk5YekNRAbaKwfq-weCoVUx.GjLSbA.fWTXI_WdhIbG_CjYJp8RR6nIXPw",
    "CGISessionId": "eyJzaWQiOiJPVGcwWmpCalkyWXROelJtT1MwME56VTNMVGt3T1RRdE0yWXlNVFpqTnpBd04yWTMiLCJjaGFubmVsIjoid2ViIiwiX2ZyZXNoIjpmYWxzZX0.Z1FA7Q.dgcKVf84w4GufQV20toANULMNeg"
}
url = "https://logistics.tungee.com/cgi/logistics/api/enterprise/info/basic"
params = {
    "enterprise_id": "57ca06b399326598",
    "multi_version_type": "logistics"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)