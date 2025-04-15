'''
=========================================================    
       @File     : run.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/10/27 21:04
       @Desc     : 
=========================================================   
'''
from scrapy.cmdline import execute

if __name__ == '__main__':
    execute('scrapy crawl youxi'.split())