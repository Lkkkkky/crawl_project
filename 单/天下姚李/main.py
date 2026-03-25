import requests



import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "origin": "https://js.cdn.ixunke.com",
    "priority": "u=1, i",
    "referer": "https://js.cdn.ixunke.com/",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Microsoft Edge\";v=\"145\", \"Chromium\";v=\"145\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
}
url = "https://yaoli.ixunke.cn/api/v1/question/sequence_practise_nestification"
params = {
    "app": "true",
    "token": "VTJGc2RHVmtYMS9xTDNGY3dHM3QwcXdieThRK1I4V2Y5YnR2WW8yTGVUeXRiWVhLZVRCMjRLWjQxdWFqVWZKaStsaHhDUHVNb3dMb1E4eVYzMW9WQnE4U2VTdGxoZEMxM2VoaExjOXdNQlU9IzE3NzMyODMxMTA3OTMtNjg4",
    "qBankId": "10230",
    "chapterId": "197978",
    "studentAnswer": "1"
}
response = requests.get(url, headers=headers, params=params)
# print(response.text)

res=response.json()['data']['questions']


for i in res:
    print(i['stem'].replace('</p>','').replace('<p>',''))
    print(i['answer'])
    print(i['analysis'].replace('</p>','').replace('<p>',''))
