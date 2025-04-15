#!/usr/bin/python
#coding=utf-8
# ���û�ֻ��Ҫ�滻14�к�15�е�orderno��secret��������

import sys
import time
import hashlib
import requests

_version = sys.version_info

is_python3 = (_version[0] == 3)

# �������Ļ�ȡorderno��secret
orderno = "GL202407171002005Cw0dXVa"
secret = "b6840f11b6ca4cb1bf1e6e022eea51f9"
ip = "www.xiongmaodaili.com/"
#���������˿�
port = "8088"
#��̬������Ʒ��������Ϊdtbf.xiongmaodaili.com:8089
#��̬������Ʒ�轫��������Ϊdtan.xiongmaodaili.com:8088

ip_port = ip + ":" + port

timestamp = str(int(time.time()))                # ����ʱ���
txt = ""
txt = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

if is_python3:
    txt = txt.encode()

md5_string = hashlib.md5(txt).hexdigest()                 # ����sign
sign = md5_string.upper()                              # ת���ɴ�д
print(sign)
auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp + "&change=true"

print(auth)
proxy = {"http":"http://" + ip_port, "https": "http://" + ip_port}
print(proxy)
headers = {"Proxy-Authorization": auth,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
#������ش���"��֤ʧ�ܣ�û�д�����ȷ������ͷ"��ʹ�� 'Xiongmao-Proxy-Authorization'�������ͷ��֤
#headers = {"Xiongmao-Proxy-Authorization": auth, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
#r = requests.get("http://2021.ip138.com", headers=headers, proxies=proxy, verify=False,allow_redirects=False)
#r = requests.get("https://api.ip.la", headers=headers, proxies=proxy, verify=False,allow_redirects=False)
print(headers)
#httpЭ������Լ�⣬ÿ����һ�η��صĽ����һ��IP��Ϊ�����ɹ�
r = requests.get("http://2022.ip138.com", headers=headers, proxies=proxy, verify=False,allow_redirects=False)
#httpsЭ������Լ�⣬ÿ����һ�η��صĽ����һ��IP��Ϊ�����ɹ�
#r = requests.get("https://ip.cn/",headers=headers,proxies=proxy,verify=False,allow_redirects=False)
print(r.encoding)
print(r.apparent_encoding)
#httpЭ����Բ��ô����ı���
r.encoding = 'gb2312'
#httpsЭ����Բ��ô����ı���
#r.encoding = 'utf-8'
print(r.encoding)
print(r.status_code)
print(r.text)
print(str(r.elapsed.total_seconds())+"    秒")