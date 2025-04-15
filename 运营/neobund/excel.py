'''
=========================================================    
       @File     : excel.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/11 15:16
       @Desc     : 
=========================================================   
'''
import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('neobund.xlsx')

# 提取第一部分字符串并创建新列
df['First Part'] = df['商品类目'].str.extract(r"\['([^']+)'")

# 保存结果到新的 Excel 文件
df.to_excel('output_file.xlsx', index=False)
