import requests


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhYTc1NTRiYWEyNDNkODA3MjY5NWU3OTUxMGQxNjVkZDM2YWIxMGJiNjkzNjUzNmI2NmJlNjExMWQ1YzU0MDYyMzgyNThhNWFlMzkzOTlkMmVmNThiZGQ3OGU2ZDAwY2M0Yzk1YjhjYTUyOGRkY2U3ODRlMzgxN2M3OTA1MzBmZjYxNDYzNjVkODE4OTg1NmE3ZWE1MGU3MjBiOGUyNzMzMzU1MjQzMzU1NzIwMGQwZTE5MjA1ZTZmNTc4ZDRhZjExNDllZTBlMTA2MGMxYTQzOWI0MDM4NDE2ZTAxMWZhNDg3NDBlMzE3NDMwZTIyNjdhODRmZTliNzNlYTE1Nzg5ZWY5NjlmMmNmN2Q5NWEzMDI3NGM2ODdjMjlkZjVkM2Y5NjMwZWMyZjc4MTQ3NGYzMjk3ZGRjOWYyNWNkNDJhNTljMDFmMWI3NGFiNDhmNzNmZGRkNmU4NTBjNWQ4Mjk2NGY3MzlmMzIyNDZkZGVkYmJkNDRmMGI0OTg2MGZjZDQ5MTA0ZDViNWExNzIwMjQ2NzVkZGYyNzJiNmUwM2FmNDdjOTRhY2U5ZWQ2ZTE1NThjMjdjMTQyYzMzMTZkMTVlYjMyOGE1NjkxOGZmNWIzM2RjZTM0NzA0ODEzOTU4OTMiLCJleHAiOjE3NDgzNDcxMTR9.UGdVyfKpGREEnV4ChJC9vRoNBQS_slfNz1icL3ltuIQIgSIGy__DZkiMyGTds2my4Wot0wltbi0Q44Z1kCbmXg",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://issue.4008117117.com/pages/collectionDetail/collectionBuy?id=41&returnURL=https%3A%2F%2Fissue.4008117117.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
    "X-Requested-With": "com.brightdairy.personal"
}
cookies = {
    "JSESSIONID": "A08CE8CF4AE4E47F4CEF089EA833FFEE",
    "Hm_lvt_6a5f1ed482525d435338c545ad0e23b4": "1745857020",
    "tenantId": "1",
    "guestId": "75b3b1f5-d66e-418d-8e83-b08c4f2da97b",
    "guestId.sig": "Npmj28BgzdymOACgDqdiKTiuOZM",
    "HMACCOUNT": "9E0B7A3C517FA2EB",
    "draco_local": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiJmNmJlMzExYTJhMDE0ODE3M2E4ZDg4ZDI5NGYyZTU1ZmVkMWJmNzJkMzI2MGVjNmJiM2YxMjg4YTA1ZmUzMTU4IiwibmJmIjoxNzQ4MjYwNzEzLCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NTA4NTI3MTMsImlhdCI6MTc0ODI2MDcxM30.7znLcsjJGwc5zdE61OBAvrYNPWXUc4Y0J2GIf2Qubao",
    "acw_tc": "0a47314717482607133915223e006d4cd698c959a8b638c5ef7ef40e2db282",
    "Hm_lpvt_6a5f1ed482525d435338c545ad0e23b4": "1748260723"
}
url = "https://issue.4008117117.com/casting/collection/reservation/57"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)