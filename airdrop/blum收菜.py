'''
=========================================================    
       @File     : blum收菜.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/1/15 19:14
       @Desc     : 
=========================================================   
'''
import requests

headers = {
'Host': 'game-domain.blum.codes',
'Connection': 'keep-alive',
'Content-Length': '0',
'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJoYXNfZ3Vlc3QiOmZhbHNlLCJ0eXBlIjoiQUNDRVNTIiwiaXNzIjoiYmx1bSIsInN1YiI6ImJmY2U1ODUxLThmN2ItNDUzMC1iZDRmLWRmMTQzYTZlOWE0MyIsImV4cCI6MTczNjkxMTc4MSwiaWF0IjoxNzM2OTA4MTgxfQ.BAsrvEoOwZgpUyC9OJYdW8pc1RrtLD6Vpd1PQbUXXlg',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
'Accept': 'application/json, text/plain, */*',
'Origin': 'https://telegram.blum.codes',
'Sec-Fetch-Site': 'same-site',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}
url='https://game-domain.blum.codes/api/v2/daily-reward'
response = requests.get(url, headers=headers)
print(response.text)
