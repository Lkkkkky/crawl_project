'''
=========================================================    
       @File     : 实现.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/18 15:29
       @Desc     : 
=========================================================   
'''
import pandas as pd
import time
import csv
import requests
from lxml import  etree
import re
import json
import os

f=open('PMCID.csv','a+',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['PMID','PMCID'])


# 读取 Excel 文件
file_path = 'id.xlsx'  # 替换为你的 Excel 文件路径

df = pd.read_excel(file_path)


# 提取前 1000 行数据
first_1000_rows = df.head(100000)  # 方法 1：使用 head() 方法
# 或者
# first_1000_rows = df.iloc[:1000]  # 方法 2：使用切片操作

# 如果需要将数据转换为数组（例如提取某一列）
first_column_array = first_1000_rows.iloc[:, 0].values  # 提取第一列并转换为数组
print(first_column_array)
pdf_save_folder = 'pdf'

for id in first_column_array:
    try:
        response = requests.get(f'https://pubmed.ncbi.nlm.nih.gov/{id}/',timeout=10)
        res_html=etree.HTML(response.text)
        if res_html.xpath('//*[@data-ga-action="PMCID"]/text()'):
            PMCID=res_html.xpath('//*[@data-ga-action="PMCID"]/text()')[0]

            try:
                PMCID=PMCID.replace(r'\n','').strip()
            except :
                ''
            form_dict={
                'PMID':id,
                'PMCID':PMCID
            }

            csv_writer.writerow(form_dict)
            print(form_dict)
            pdf_name =str(id)
            save_path = os.path.join(pdf_save_folder, pdf_name)
            response=requests.get(f'https://pmc.ncbi.nlm.nih.gov/articles/{PMCID}/pdf/',timeout=10)
            if response.status_code == 200:
                # 将响应内容保存到文件中
                with open(pdf_save_folder, 'wb') as file:
                    file.write(response.content)
                print(f"PDF 文件已成功保存到 {pdf_save_folder}")
            else:
                print(f"下载失败，状态码: {response.status_code}")


    except Exception as e:
        print(e)