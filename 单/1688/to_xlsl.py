'''
=========================================================    
       @File     : to_xlsl.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/26 11:55
       @Desc     : 
=========================================================   
'''
import pandas
r = pandas.read_csv('company.csv')
r.to_excel('company_.xlsx')
