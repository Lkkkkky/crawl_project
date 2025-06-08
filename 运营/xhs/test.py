import requests
import json


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.xiaohongshu.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.xiaohongshu.com/",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "x-b3-traceid": "26c346cb22dd3e8a",
    "x-mns": "awkbKBECce0aIIgTL1GdMtWti4TTKePYWNLKuo1o4gHem7pdvTff9ea4Y3xX8fM6Jk665/vDFIGt+599I7NNQtN7Fy1X64OtKOZf99QbhbooytIbjC99WIYe0Q7Jvg3RoioP3p9J16wn30hlPveLnIojg2PWgf1u4RujgvpX2Q9kkhYfEPMhYf3OQNbNJNdcjPeMXPIcInxYgYtb8pova5i5lSfX62MpaegCSFoRaZgEt1ah3Cu++G7TgLt7EPgcKMKw7hyZouutdjYGPtDREFDOHiiCIxMNfwF4BmSaT+S4fLezb+M7ZNkbp1KxJ3SuczYv6y4h0XCY365CBZz0al+hbKeKJmwkgR2+DxgWdBPgwPiy31hSjPhtmc40wH/JTJQ+1yHfnfDSBDf5EG4CaYFnPHi74CP1IHD2m8XdiZGDWi6NOtuJCfaMELee9QTIicl4Ku2icfNbaix1ZMzZ2leOgltx9dfB/kFm13YGfj5g/vZbde+MDopuQR2k",
    "x-s": "XYW_eyJzaWduU3ZuIjoiNTYiLCJzaWduVHlwZSI6IngyIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6ImFkZDcyY2U4NWMyZWU2NDAxMDg0NWVjZDQ2MDRkZjc4MDZmZjAxYTlhYTE3NTIyYTM4ZDljZjQxN2VmYTNmMWEyNmRjY2ZlZGQwYzc0ZjljMmVhMDQ0ZTRjMmQyNTg3NDJjN2Y3YmUyZDU2ZmZhNTQyYTY2NTYxZjRhMjczZmFjZjZhY2Q2ZTIxNzhkNDVhZDMxMzZkNzlkYTM5OTNlMDQ2M2RlNmRlZmRjNzZmZjExMGM0YThhYjQ2ZTZmZGI5NGE2ZjllMDg5MzQ4NWM2OWRmZDM5NjM1M2E0OTQ3NzMzZGI3OGZlM2QwNzJiODZlYjMyZTUzMzcwN2Y2M2IwMzRiZDI4NGQ2NGI0ZWJjMDkyMDk0MWRiMzhjMjQ0MzZkYjgxMDJiZGYwZmQ5ODAwN2QyNjBlZTM4Y2EzYjViYjM5YWNjZmI3ZmE1OTMyNmMzOWI5NjYzNWMxY2I3ODUzY2RlMGZkMTk5NzBjNjg3OTlhODRhNmNkODRmOTAyYWNlODVmNDZkMDcwNzBhNDM1MjIxNWY4NzQxZjA3NmU4ZWI1In0=",
    "x-s-common": "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",
    "x-t": "1746902077909",
    "x-xray-traceid": "cb5dbd27e836f2bf30b87784f888bc31"
}
cookies = {
    "abRequestId": "dd0419ac-d5ac-516d-bfae-e371522dad21",
    "a1": "1951c0033d4gzy900uedtkrj977h5fcsnqmtgeica50000857898",
    "webId": "92bc1c6492cff53edeb04d845b78d6cf",
    "gid": "yj2yS884qWIyyj2yS88qqAd3f4kuvj887df96S0TFVjWW928x2iSMk888Y2WYjY8j0YyyqKJ",
    "x-user-id-creator.xiaohongshu.com": "65c1c8480000000016002321",
    "customerClientId": "014013214631522",
    "xsecappid": "xhs-pc-web",
    "web_session": "040069b590abc3569b445a34283a4b42290c5e",
    "webBuild": "4.62.3",
    "unread": "{%22ub%22:%22681ec571000000002301e630%22%2C%22ue%22:%22681f396a000000002301e5c9%22%2C%22uc%22:24}",
    "loadts": "1746900942373",
    "acw_tc": "0a4a31c217469010054232727e91f8a88424d520282fb2f290dfd9008b43ca",
    "websectiga": "cf46039d1971c7b9a650d87269f31ac8fe3bf71d61ebf9d9a0a87efb414b816c",
    "sec_poison_id": "c54adf01-713c-43c8-a35e-948b65da50e9"
}
url = "https://edith.xiaohongshu.com/api/sns/web/v1/search/notes"
data = {
    "keyword": "熊猫",
    "page": 1,
    "page_size": 20,
    "search_id": "2es8cm1s61sag2qwz7koe",
    "sort": "general",
    "note_type": 0,
    "ext_flags": [],
    "geo": "",
    "image_formats": [
        "jpg",
        "webp",
        "avif"
    ]
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)