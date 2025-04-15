import requests
import json


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "check_value": "3a849b97b182c1d6698ae75124450f5e92bcdb11c968633ed3f58b88ef9b4312",
    "content-type": "application/json",
    "hide_head": "0",
    "mer_cust_id": "6666000137842973",
    "origin": "https://hfpay.cloudpnr.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://hfpay.cloudpnr.com/h5/pages/cashier/index?uuid=hfpwallet6666000137842973pay9b42bb10-a124-4863-9f00-f16647feb7e8",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/133.0.0.0",
    "uuid": "hfpwallet6666000137842973pay9b42bb10-a124-4863-9f00-f16647feb7e8"
}
url = "https://hfpay.cloudpnr.com/api/hfpwalleth5/queryCashDeskInfo"
data = {}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)