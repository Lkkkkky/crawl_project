
import sys
import time
import hashlib
import requests
import json
from lxml import etree

_version = sys.version_info

is_python3 = (_version[0] == 3)

r = requests.get("http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=b6840f11b6ca4cb1bf1e6e022eea51f9&orderNo=GL202407171002005Cw0dXVa&count=10&isTxt=0&proxyType=1&returnAccount=1", verify=False, allow_redirects=False)
r.encoding='utf8'
print(r.status_code)
print(r.text)
o = json.loads(r.text)
if o['code'] == "0" :
    for obj in o['obj']:
        ip = obj.get('ip')
        port = obj.get('port')
        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": ip,
            "port": port,
            # 代理认证的用户名
            "user": obj.get('account'),
            # 代理认证的密码
            "pass": obj.get('password'),
        }
        proxy = {"http": proxyMeta, "https": proxyMeta}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"}
        r = requests.get("https://2023.ip138.com", headers=headers, proxies=proxy, verify=False, allow_redirects=False)
        r.encoding = 'utf8'
        print(r.status_code)
        print(r.text)
        if r.status_code == 302 or r.status_code == 301:
            loc = r.headers['Location']
            print(loc)
            r = requests.get(loc, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
            r.encoding = 'utf8'
            print(r.status_code)
            print(r.text)