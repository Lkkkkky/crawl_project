import requests

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

# 提供公钥字符串（PEM 格式）
public_key_pem = b"""
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDVe02v6Ras92CPVqBF/2ojERaF
DICLATLLgZscn8Z3C8Zj9w3H1p0+VW9ZBledYXVGCGrVD9ftjKhivILIhxKifwF9
LMWcKwAXmJjIH9vUcIku6T7E0qeDo/O4Xxnd1d2z8eKJgk23s9a9Ggf4zotqVw/p
1sUIPWc8MPQkpn64+QIDAQAB
-----END PUBLIC KEY-----
"""

# 加载公钥
public_key = serialization.load_pem_public_key(public_key_pem)

# 要加密的消息
admin    = b"17896686831"
passord = b"17896686831"

# 使用公钥加密
ciphertexta = public_key.encrypt(
    admin,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
ciphertextb = public_key.encrypt(
    passord,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
# print("Ciphertext:", ciphertext)

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://user.91160.com",
    "Pragma": "no-cache",
    "Referer": "https://user.91160.com/login.html",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "Hm_lvt_c4e8e5b919a5c12647962ea08462e63b": "1733996885",
    "HMACCOUNT": "C222DD6D62F25FA1",
    "_ga": "GA1.2.1941242203.1733996885",
    "_gid": "GA1.2.1684583721.1733996885",
    "ip_city": "sz",
    "__guid": "Rlb6A5675ab154f39363.06422166",
    "FISKCDDCC": "0401a8e7b0436f153118d26b82a738c6",
    "PHPSESSID": "taqr1o956mtmj7dfpfnpi0smp6",
    "__jsluid_s": "fc421a8ba24ea6a4ff8e19b7cad85a29",
    "no_dialog_times": "3",
    "access_hash": "1078e55f24f5e6fb40d85a38f0a6ba22BBADMiSa20250111180834",
    "_gat": "1",
    "DKLFFDKD": "%7B%22key%22%3A%2269ba62226ba06c6ee3cc6687f0cb5805%22%2C%22val%22%3A%22d14ec99c7a83102dc53d5727d747eb49%22%2C%22tm%22%3A1733998234%7D",
    "Hm_lpvt_c4e8e5b919a5c12647962ea08462e63b": "1733998236",
    "_ga_NYE4XMXXGY": "GS1.2.1733996885.1.1.1733998236.55.0.0"
}
url = "https://user.91160.com/login.html"
data = {
    "clientLoginUrl": "",
    "client_login_url": "",
    "username": ciphertexta,
    "password": ciphertextb,
    "target": "https://www.91160.com/",
    "error_num": "0",
    "checkcode": "",
    "tokens": "62afcf4835597ab62c7f6ab53930a395"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)
cookies2 = response.cookies.get_dict().get('access_hash')
print(response.text)
print(response)
print(cookies2)