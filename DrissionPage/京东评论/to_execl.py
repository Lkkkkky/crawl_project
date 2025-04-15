'''
=========================================================    
       @File     : to_execl.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/6 17:45
       @Desc     : 
=========================================================   
'''
import pandas
pd=pandas.read_csv('comment.csv')
pd.to_excel('comment.xlsx')
