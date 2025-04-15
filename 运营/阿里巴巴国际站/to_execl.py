'''
=========================================================    
       @File     : to_execl.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/11 13:33
       @Desc     : 
=========================================================   
'''
import pandas as pd
f=pd.read_csv('alibaba.csv')
f.to_excel('alibaba.xlsx')