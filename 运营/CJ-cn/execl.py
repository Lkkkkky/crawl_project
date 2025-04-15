'''
=========================================================    
       @File     : execl.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/10 11:16
       @Desc     : 
=========================================================   
'''
'''
=========================================================    
       @File     : execl.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/31 10:55
       @Desc     : 
=========================================================   
'''
import pandas as pd
f=pd.read_csv('company.csv')
import pandas as pd

# 读取CSV文件


# 假设要根据 'column_name' 列进行排序
# 升序排列
df_sorted = f.sort_values(by='company_name', ascending=True)

# 降序排列
# df_sorted = df.sort_values(by='column_name', ascending=False)

# 保存排序后的CSV文件

df_sorted.to_excel('company.xlsx',index=False)