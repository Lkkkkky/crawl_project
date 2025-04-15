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
f=pd.read_csv('天眼查.csv')
f.to_excel('天眼查.xlsx')