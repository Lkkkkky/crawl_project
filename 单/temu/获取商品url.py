import requests
import json


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "anti-content": '0aqWtxUkM_Ve0PrPC40EEXHP7DB6RYp1N4vJgyVikjARp7eyoFl15qr0KnKJfM6MmMXvxQXFUnNNa1GpfLxs8N9pH_xHBnN0DprQnbYJV0po_aCBANukhecXOUtdgFjnlmlqpahLWlKeTKT-QYSLBmITNXnnt-UTclNP08lexod_59iSWnPyygVXd8mICgKuafYjGTnLj5867785nVKGpFKccXEXqNojqctYpJzpNrTjeWbPHbKcmVy1ywoKqwJxxbI-tjDDDoIDISIDGkIDDSIDImIkG0IkGPB-ujlXuSPdrgcXvbcecZzrL6oyn4fVNl0Yc0gycXpalYujld4yn09YsYEylYeqnYpqldvyn0PnI02PWPRXyc4eMzMkABENK1NJfqIYtqu_6jdTwnsUC0notdNNMPsox9swani98OsKP4k5mz4ZkMt1KtUwvsQDSZIFSAM5mL1OmMWOkM4ZHA65GRTUFtQkSDIVScIuSDR1KtY_-sRmIIRKmBZSVgPGVwS15v7kvGjlBZgsQw7_15LtF7e1-_Bs94xkExeOP-TCgzKcSlIWX-6ee1H5MiqWEe6ypKS5BPljavpYHFBx_3BGWLz8vg7Xh-Q5mrD2cMQLmD8Gb7JnvrQDAnyhn999Qx_oRDgIke5f',
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.temu.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.temu.com/search_result.html?search_key=%E9%A6%99%E6%B0%B4&search_method=user",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "x-document-referer": "https://www.temu.com/?_x_sessn_id=liodzpnuj5&refer_page_name=bgn_verification&refer_page_id=10017_1732692025523_tstaqgnxnv&refer_page_sn=10017&is_back=1",
    # "x-phan-data": "0aeJx7xMxiYPiIuSja0NzYyMzSyNTMyNjQUAfOMzazMEfwTAzNLBE8M1NL41gA-fEOjA"
}
cookies = {
    "_bee": "HlFHeIOIgI3EevAiFX0tQ5xCQk0Qhap8",
    "njrpl": "HlFHeIOIgI3EevAiFX0tQ5xCQk0Qhap8",
    "dilx": "ngO7OssYeYE21xvkE8OKL",
    "hfsc": "L3yJeo8w7D/815PFfg==",
    "region": "211",
    "language": "zh-Hans",
    "currency": "USD",
    "api_uid": "Cm0sH2dGykR8DgBaM+0kAg==",
    "__cf_bm": "cghKiTzgzSzksPHPmJEwX_OGWoMCy6fAhox.WMXFxO8-1732692549-1.0.1.1-VdES8yo8TZepcQUwH0PiJbcX_Avz0o0KVBRraZaKDl.1.imQUCU5DtK6qs8GD4aMFGdzcpKglvzMlM0LFvsL1Q",
    "timezone": "Asia%2FShanghai",
    "webp": "1",
    "_nano_fp": "XpmqX5EbX5dyXpdyX9_VS4L_xUkCeWwHqdEdMcwk",
    "_ttc": "3.eVyyRHYCsTFB.1764228551"
}
url = "https://www.temu.com/api/poppy/v1/search"
params = {
    "scene": "search"
}
data = {
    "scene": "search",
    "pageSn": 10009,
    "offset": 0,
    "listId": "dd247567f693458fa91b9f2de4e172ba",
    "pageSize": 120,
    "query": "香水",
    "filterItems": "",
    "searchMethod": "user",
    "disableCorrect": False
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data,proxies= {
        "http": "http://xmdl2e65:xmdlb825@58.220.27.212:46408",
        "https": "http://xmdl2e65:xmdlb825@58.220.27.212:46408"
    })

print(response.text)
print(response)