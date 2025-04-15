import requests
import execjs
import hashlib
import time
import re
import json
import subprocess
def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()
t = int(time.time() * 1000)
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://item.jd.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://item.jd.com/",
    "sec-ch-ua": "'Chromium';v='130', 'Google Chrome';v='130', 'Not?A_Brand';v='99'",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "'Windows'",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "x-referer-page": "https://item.jd.com/100026836156.html",
    "x-rp-client": "h5_1.0.0"
}
cookies = {
    "__jdu": "369041817",
    "shshshfpa": "0315a5f6-560b-3b6f-4a4f-e530675a58cd-1728735584",
    "shshshfpx": "0315a5f6-560b-3b6f-4a4f-e530675a58cd-1728735584",
    "_pst": "jd_MhNyBaXRXFnl",
    "unick": "lkyyyyyyyyyyy",
    "pin": "jd_MhNyBaXRXFnl",
    "_tp": "LckDemJZ9vjD7CXeUJhnPA%3D%3D",
    "areaId": "19",
    "ipLoc-djd": "19-1601-50258-129167",
    "PCSYCityID": "CN_440000_440100_0",
    "unpl": "JF8EAJdnNSttURtXARxVSRoVHwldWwhcHkQAOzMEAw9ZSF0MTFcfF0R7XlVdWBRLFx9uZRRXXlNLUg4fBCsSEXteU11bD00VB2xXVgQFDQ8WUUtBSUt-S1tXV1QOSh4AbGYDZG1bS2QFGjIZFRhKWFRXXQ57FjNoVzVkWVhOVg0rAysTIAkJCFtbDkMWAyJlAlxcXUtdBR0yGiIT",
    "thor": "1F63723E3B0B854D9454AB8BE6A4EAB5D6AE0AE74007F05D682072A2346EEFEA1028B934EFF944249F950729B9C04FFE172EEEFE9ED3052C5EE9852B1938C952C4992600D615315EE8945472C59074F097A63F8E8E2D3C7287D5FC8700796225037D3212DAF381EADDBDEE098648A38579DE37A038F1D77B8954BD21A71EC9B47A375E80F292B680AC9C1BB1E192E92570899DBCBA0DE2B5BBC8A904CD1A4027",
    "pinId": "8iMjBrpr1TnSWYxYoJoW6g",
    "3AB9D23F7A4B3C9B": "IP7ZOEW6HMAOR2YF23KYRWMTUEY6WE6YJCO4HO45KAOUDW75RJ6AXP3E73LX34Z3DYL6ZVYZKZQ2OLMLEB35CY63C4",
    "__jdv": "76161171|baidu|-|organic|notset|1730648921764",
    "mt_xid": "V2_52007VwEVWlxdUlMfTykJB2EKEwcKUE5fSxpOQABhAhpOVQxRDgMeGQ9XZQQUUwkLB1wvShhfAHsDEk5cWkNZHUIcVQ5iBSJQbVhiUxpNHV0GZgoWVl1ZUVMZShxdDVcGE1tb",
    "__jdc": "181111935",
    "__jda": "181111935.369041817.1728735580.1730648922.1730654544.12",
    "3AB9D23F7A4B3CSS": "jdd03IP7ZOEW6HMAOR2YF23KYRWMTUEY6WE6YJCO4HO45KAOUDW75RJ6AXP3E73LX34Z3DYL6ZVYZKZQ2OLMLEB35CY63C4AAAAMS6M6QMJAAAAAADMPRHKVG5CGRGIX",
    "flash": "3_aSpwJOixmkVrR6d2kFqDhLTBKiY-Os70RsE7-ire1yjSpcOL2nyUd5Pw-pKdms444baebC03UBQHLzimzKsQvxg8b8RBu39yNgkZPnnQ7Ljd_LBPFNgQjXwF1EQi31DLrsJ2BGyVVWbKj6Hskw4mFbtbsNN3BILaJets2DcKoZ59pq**",
    "shshshfpb": "BApXSogrv9vdA4wvmpEzV2_iGjEfcnOkXBmoyUqts9xJ1MthSF4G2"
}
url = "https://api.m.jd.com/"
params = {
    "appid": "item-v3",
    "functionId": "pctradesoa_diviner",
    "client": "pc",
    "clientVersion": "1.0.0",
    "t": str(t),
    "body": '{"lid":19,"lim":15,"ec":"utf-8","uuid":"369041817","p":902029,"sku":100026836156,"ck":"pin,ipLocation,atw,aview","pin":"","c1":15901,"c2":15902,"c3":15908,"securityToken":"BApXSW3D19vdA4wvmpEzV2_iGjEfcnOkXBmoyUqts9xJ1MthSF4G2","clientChannel":"3","clientPageId":"item.jd.com"}',
    "h5st": "20241104144053338;yhhyevevirzk9149;fb5df;tk03waea71bb618nZ0uI7MfcntcsxOR4yz5tKE8FxqRD8rmGy0V6You0BoJGE94yFRf_oo7QiOJI2PKI5b0VQcnbA_Y7;9eb4b50f2e780a7433c878fc544c1303;4.9;1730702453338;of7ruCLjzzZf9rIjLDIj6XETJrpjh7JjybYfy-FN5GFOGSUSyKlRyipjxjpPFipjLDrgzrJdJz1TIipjLDrgJrIf6XVd1b4e2PYezLoS4flf2bVf3nlf3TFTzfVd5T4eJrJdJrEa-OFTGOEjLrJp-jpe7PYSHKYeIWlf1roeJaleJq4e2XYd3fVS5X1ezHIS4jpjxj5PKSEQKeFjLrJp-jZf9HIg3T0UG6VRFuWeDipjxjJOJrpjh7JjeanO3q4ZKaVYlCndJrJdJ31QHyVT5ipjLDrgJj4f9G1WJrJdJTlPJrpjh7ZMLrJp7rJdJLYOJipjLrpjh7JjJrJdJPYOJipjLrpjh7pf3rJdJTYOJipjLrpjh7pfLDIj2XETJrpjLrJp-rojxjpe2iFjLrpjLDrgzLojxj5f2iFjLrpjLDrg63pjxjJf2iFjLrpjLDrgJHIg6zpfJrJdJnYOJipjLrpjh7pfLDIjAOEjLrpjLDrg2rJdJfkQJrpjLrJp-rojxjpQJrpjLrJp-rojxjpS0ipjLrpjh-kjxjpS9WlOzWFjLrJp-3kjLDLj-yFaTimVKiXNdKVYMaFRJrJdJjoPJrpjLrJpwqJdJrkPJrpjh7Jj3ToNL-oe1zVRUq5d7zpf6rpWdq5P0ulS9G1WJrJdJnVO4ipjLD7N;4f08d2798c6e885b2b0b811b4ff5c5c1",
    "x-api-eid-token": "jdd03IP7ZOEW6HMAOR2YF23KYRWMTUEY6WE6YJCO4HO45KAOUDW75RJ6AXP3E73LX34Z3DYL6ZVYZKZQ2OLMLEB35CY63C4AAAAMS6M6QMJAAAAAADMPRHKVG5CGRGIX",
    "loginType": "3",
    "uuid": "181111935.369041817.1728735580.1730648922.1730654544.12",
    "screen": "1920*991"
}

h5st = execjs.compile(open('fb5df.js', 'r', encoding='utf-8').read()).call('new1')
print(h5st,len(h5st))
params['h5st'] = h5st

response = requests.get(url, headers=headers, cookies=cookies, params=params)


print(response.text)
print(response)