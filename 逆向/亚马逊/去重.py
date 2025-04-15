'''
=========================================================    
       @File     : 去重.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/28 22:30
       @Desc     : 
=========================================================   
'''
import pandas as pd
df = pd.read_csv('song.csv')
df_deduplicated = df.drop_duplicates( subset=['name'])
# 保存去重后的 CSV 文件
df_deduplicated.to_csv('out.csv', index=False,encoding='utf-8')