'''
=========================================================    
       @File     : 格式清洗.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/11 17:18
       @Desc     : 
=========================================================   
'''
import pandas as pd
import time
import csv
import requests
import re
import json
# 读取 Excel 文件
file_path = '阿里国际-商品-20250208.xlsx'  # 替换为你的 Excel 文件路径

df = pd.read_excel(file_path)

def extract_cert_info(cert_data):
    try:
        # 将字符串转换为字典格式
        cert_json = json.loads(cert_data)

        # 获取 certName
        cert_name =list(set(item["certName"] for item in cert_json))  # 提取 certName


        cert_urls =[url for item in cert_json for url in item["certUrls"]]

        return cert_name, cert_urls
    except Exception as e:
        return "", ""  # 如果解析失败，返回空字符串


# 假设证书列的名称是 "证书"
df[['certName', 'certUrls']] = df['证书'].apply(lambda x: pd.Series(extract_cert_info(x)))

# 保存更新后的 DataFrame 到新的 Excel 文件
output_file_path = './updated_阿里国际-商品-20250208.xlsx'
df.to_excel(output_file_path, index=False)

