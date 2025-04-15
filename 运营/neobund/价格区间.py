'''
=========================================================    
       @File     : 价格区间.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/21 16:43
       @Desc     : 
=========================================================   
'''
import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('去重neobund_with_phone.xlsx')

# 定义函数，提取最小和最大价格
def extract_prices(price_range):
    if isinstance(price_range, str) and '-' in price_range:
        min_price, max_price = price_range.split('-')
        return float(min_price), float(max_price)
    else:
        return float(price_range), float(price_range)

# 应用函数，提取最小和最大价格
df[['最小价格', '最大价格']] = df['price'].apply(lambda x: pd.Series(extract_prices(x)))

# 保存结果到新的 Excel 文件
df.to_excel('价格区间_去重_neobund_with_phone.xlsx', index=False)

