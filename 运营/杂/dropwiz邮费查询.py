'''
=========================================================    
       @File     : dropwiz邮费查询.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/28 18:40
       @Desc     : 
=========================================================   
'''

import pandas as pd
import time
import csv
import requests
import re
import json




# 读取货盘表
file_path = "商城货盘数据-请点击刷新手动刷新数据1_2025_02_27.xlsx"
df = pd.read_excel(file_path)

# 假设第一列是货物ID，API接口需要货物ID作为参数
# 假设API接口返回的运费在响应的 'shipping_cost' 字段中

# 定义API接口的URL

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Cbs-Token": "cbs:token:db8c883203fed15ff74f173e73373ae1",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Cvt": "a32b3baf-a095-4158-babc-25997bf17d15",
    "Origin": "https://shop.dropwiz.net",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
# 创建一个新的列来存储运费
df['运费'] = None

# 遍历每一行，调用API接口获取运费
for index, row in df.iterrows():
    try:

        cargo_id = row[0]  # 假设第一列是货物ID
        response = requests.post(f"https://api.dropwiz.net/openapi/goods/detail/{cargo_id}",headers=headers,timeout=10)

        if response.status_code == 200:
            shipping_cost = response.json()['data']['shippingTemplate']['details'][0]['items'][0]['price']
            df.at[index, '运费'] = shipping_cost
            print(f'{index}插入成功')
        else:
            print(f"Failed to get shipping cost for cargo ID {cargo_id}")
    except:
        ""
    output_file_path = "货盘表_带运费.xlsx"
    df.to_excel(output_file_path, index=False)

    print(f"运费已成功填入货盘表，并保存为：{output_file_path}")
# 保存修改后的货盘表




