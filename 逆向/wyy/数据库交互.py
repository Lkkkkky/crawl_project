'''
=========================================================    
       @File     : 数据库交互.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/10/27 11:31
       @Desc     : 
=========================================================   
'''

# import pymysql
# from pyreadline3.release import authors
# from wx.lib.masked import value
#
# con=pymysql.connect( user='data', password="data",host='47.236.198.227',database='data',)
# con.connect()
# cursur=con.cursor()
# cursur.execute('select * from song_list')
# r=cursur.fetchall()
# print(r)
#
# sql=('insert into song_list (歌曲名,时长,作者,专辑) value (%s,%s,%s,%s)')
# name='aaa'
# time='4:30'
# author='小青'
# album='终于'
# cursur.execute(sql,(name,time,author,album))
# con.commit()


# import redis
#
# # conn=redis.ConnectionPool(host='localhost',db=0, password='jing33333', port=6379, decode_responses=True)
# conn=redis.Redis(host='47.236.198.227', port=6379,db=0, password='jing33333', charset='utf-8')
# r=conn.get('jing3')
# # r=conn.get('jing3')
# # print(r)

import redis  # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

r = redis.Redis(host='47.236.198.227', port=6379,password='jing33333',decode_responses=True)  # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r.set('jing3333', '7777')  # key是"foo" value是"bar" 将键值对存入redis缓存
print(r['name'])
print(r.get('jing3'))  # 取出键name对应的值
