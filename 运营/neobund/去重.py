'''
=========================================================    
       @File     : 去重.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/21 16:25
       @Desc     : 
=========================================================   
'''
import pandas as pd
df = pd.read_csv('neobund_with_phone.csv')
df_deduplicated = df.drop_duplicates( subset=['商品链接'])
# 保存去重后的 CSV 文件
df_deduplicated.to_csv('去重_neobund_with_phone.csv', index=False,encoding='utf-8')