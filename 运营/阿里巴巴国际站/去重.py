'''
=========================================================    
       @File     : 去重.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/17 11:49
       @Desc     : 
=========================================================   
'''
import pandas as pd
df = pd.read_csv('company.csv')
df_deduplicated = df.drop_duplicates( subset=['companyName'])
# 保存去重后的 CSV 文件
df_deduplicated.to_csv('alibaba.csv', index=False,encoding='utf-8')