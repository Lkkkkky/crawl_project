import requests
res=requests.get('http://127.0.0.1:1234/ss',params='2')
print(res.text)
