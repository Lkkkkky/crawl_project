'''
=========================================================    
       @File     : trump.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/5 15:14
       @Desc     : 
=========================================================   
'''
import os
import json
import solana
from solders.keypair import Keypair
import requests


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://trump2.cc",

    "Referer": "https://trump2.cc/M7MS1",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Microsoft Edge\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://trump2.cc/index/index/post.html"
private_keys=[]
# 批量创建钱包并保存到文件
def create_solana_wallets(num_wallets):
    # 用来存放所有公钥
    public_keys = []

    # 文件路径

    # 清空文件内容（如果文件存在的话）


    for _ in range(num_wallets):
        # 创建钱包
        keypair = Keypair()

        # 获取私钥和公钥
        private_key = keypair.secret()
        public_key = keypair.pubkey()

        # 将私钥和公钥写入文件


        # 将公钥添加到数组中
        public_keys.append(str(public_key))
        private_keys.append(private_key)

    return public_keys

# 批量创建10个钱包
num_wallets = 666
public_keys = create_solana_wallets(num_wallets)

# 输出保存的公钥
print("公钥列表：")
for i,public_key in enumerate(public_keys):
    data = {
        "sharecode": "NJN99",
        "address": public_key
    }
    response = requests.post(url, headers=headers, data=data)
    private_keys_file = 'private_keys.txt'
    public_keys_file = 'public_keys.txt'

    with open(private_keys_file, 'a') as f:
        f.write(json.dumps(private_keys[i].hex()) + '\n')  # 将私钥以十六进制字符串保存

    with open(public_keys_file, 'a') as f:
        f.write(str(public_key) + '\n')  # 保存公钥
    print(response.text)
    print(response)
    # print(public_key,'--->邀请成功')

# 额外的：打印私钥文件的路径
print(f"私钥已保存到：{os.path.abspath('private_keys.txt')}")
print(f"公钥已保存到：{os.path.abspath('public_keys.txt')}")
