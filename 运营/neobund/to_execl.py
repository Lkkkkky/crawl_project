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
f=pd.read_csv('去重_neobund_with_phone.csv')
f.to_excel('去重neobund_with_phone.xlsx')