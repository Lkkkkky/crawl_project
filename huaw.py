from idlelib.iomenu import encoding

import requests
import execjs

ret=execjs.compile(open('enc.js','r',encoding='utf-8').read()).call('enc')

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI1MGE4MDE2NTA1NzU1NWNiNzBmZTJkNjZjZDUxYzg5YWJkOGYxZjk1N2QzMWM1MzZlODdjMjdiZmIyMjRiM2RmMGM3NTI0ODBjZjVlNjIxNTM5OGMzNmNjOTBjYmEwNzMyNTkxMjVhMTM3NTZjNmY2Y2E5ODAxNjJkOWNiMGY2NWNjYjFhZTRhMDVlYTMyMzcxZGZlZWY4YThkZWE2MGRjMzc2NTRkNWY2N2I2ZmFjNWQ2MGVlMzRiNjRlMGNiNjUzM2ViODQ2ZWRiNDU1NTM5ZTIzNDNiMzYyNGYxOTQ4ZDdkYThlY2FkNWQ0ZjkxMGY2ZTUwMDNmZDhkZGRlNTA3YjlhM2Q4YzkzOTNlODAxYmRmYWJlNzMwYTI5MTNlZDMyYzYwYWQ0ZWYzOTVkNTFiYjJlZDgzNDVkZDBiYzE3NDUwYmU5YWNlYjQ3OGI1ZWY4Y2ZhY2QyOGIwMjRiYzY4NjYyMTdjMWUzNzgzMTdiZWU5YWUxODg1NGQ0MTAzOTQ5ZTA2Njk4NTJlZTZiMjU2OWE1YzBjYzg1MmRhM2NjMyIsImV4cCI6MTc0MjYzMTA5Mn0.Pe97fN4q5RqvQTJpNmfZu4FeA7cu_o5OiP0G9wnthFEmOtLDpqONGximSVMXlJfxy8odEh9idgHmoHM5XoKoyw",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-type": "application/json",
    "Origin": "https://issue.4008117117.com",
    "Pragma": "no-cache",
    # "Referer": "https://issue.4008117117.com/pages/authentication/authentication?returnUrl=https%3A%2F%2Fissue.4008117117.com%2F%3F%26token%3D%2522eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiJhNTA4NjMxNTVkNWQwYmUyYmVmZTYxNDBhMTU1ZTc5OWQxODdjOGU1Mzg3ZWQ5ZmM0MDhkNGQ1NzEzZDllYWRlIiwibmJmIjoxNzQyNTQ0Njg5LCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDUxMzY2ODksImlhdCI6MTc0MjU0NDY4OX0.yPohQGrRVGBB8C1wCFFWKiMv2-y7p-XwYgzw4-1n_BQ%2522%26fromType%3Dguangming",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
    "X-Requested-With": "com.brightdairy.personal"
}
cookies = {
    "JSESSIONID": "3A2F6DDE23C8BACCE18E33325950EB07",
    "guestId": "dedc56a9-ccb2-4249-acb3-b8b07be9e356",
    "guestId.sig": "W_EO7HqfB7I0zU14SFExSOjX43Y",
    "Hm_lvt_6a5f1ed482525d435338c545ad0e23b4": "1742383611,1742383652",
    "HMACCOUNT": "DDC3E44D29B30C7E",
    "acw_tc": "ac11000117425445324766049e00d2845e4642bd8e112e1f099f41e938d0ea",
    "tenantId": "1",
    "draco_local": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsb2dpbiIsInBhdGgiOiIvIiwidG9rZW5LZXkiOiJhNTA4NjMxNTVkNWQwYmUyYmVmZTYxNDBhMTU1ZTc5OWQxODdjOGU1Mzg3ZWQ5ZmM0MDhkNGQ1NzEzZDllYWRlIiwibmJmIjoxNzQyNTQ0Njg5LCJkb21haW4iOiI0MDA4MTE3MTE3LmNvbSIsImlzcyI6ImRyYWNvIiwidGVuYW50SWQiOjEsImV4cGlyZV90aW1lIjoyNTkyMDAwLCJleHAiOjE3NDUxMzY2ODksImlhdCI6MTc0MjU0NDY4OX0.yPohQGrRVGBB8C1wCFFWKiMv2-y7p-XwYgzw4-1n_BQ",
    "Hm_lpvt_6a5f1ed482525d435338c545ad0e23b4": "1742544699"
}
url = "https://issue.4008117117.com/casting/authentication/realName"
data = {
    ret: "="
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)