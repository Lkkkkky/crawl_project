# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
from twisted.conch.insults.window import cursor
from wx.lib.masked import value
#
# con=pymysql.connect( user='data', password="data",host='47.236.198.227',database='data')
# con.connect()
# cursor=con.cursor()
# sql = 'insert into game_list (name) value (%s)'
# cursor.execute(sql, (item['name']))
# con.commit()

# 写入csv文件
class XiaoyouxiPipeline:
    # 实现单次开关文件
    def open_spider(self, spider):
        self.f= open ('data.csv','a',encoding='utf-8')
        print('打开文件')
    def close_spider(self, spider):
        self.f.close()
        print('关闭文件')
    def process_item(self, item, spider):

        print(item)
        self.f.write(item['name']+'\n')
        return item
# 写入数据库
class XiaoyouxiPipeline_MySql:
    # 实现单次开关文件
    def open_spider(self, spider):
        # 连接数据库
        self.con=pymysql.connect( user='data', password="data",host='47.236.198.227',database='data')
        self.con.connect()
        # 创建光标以输入sql指令
        self.cursor = self.con.cursor()
    def close_spider(self, spider):
        self.con.commit()
        self.con.close()
    def process_item(self, item, spider):
        sql = 'insert into game_list (name) value (%s)'
        self.cursor.execute(sql, (item['name']))
        self.con.commit()

        return item
