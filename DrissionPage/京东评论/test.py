'''
=========================================================    
       @File     : main.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/6 15:08
       @Desc     :
=========================================================
'''
from DrissionPage import Chromium
from loguru import logger
import time
import csv

f=open('comment.csv','a+',encoding='utf-8',newline='')
csv_writer=csv.DictWriter(f,fieldnames=['comment'])
# csv_writer.writeheader()

browse=Chromium(5678)

main_tab=browse.new_tab('https://www.jd.com/')

input=main_tab.ele('xpath://input[@id="key"]').input('电脑')#搜索内容
main_tab('xpath://*[@id="search"]/div/div[2]/button').click()
time.sleep(2)

main_tab.scroll.down(10000)#下拉,加载完整列表
time.sleep(5)
search_result=main_tab.eles('t:li@@class=gl-item')#获取搜索结果
def get_detail_tab_list(search_result):
    detail_tab_list=[]
    for result in search_result:
        detail_tab = (result.ele('t:a'))#保存商品跳转链接元素
        detail_tab_list.append(detail_tab)

                    # .click.for_new_tab())
    return detail_tab_list

def get_comment(detail_tab_list):
    for detail_ele in detail_tab_list:
        detail_tab=detail_ele.click.for_new_tab()
        detail_tab.ele('@data-anchor=#comment').click() #打开新链接（搜索结果的商品）
        time.sleep(10)
        #开始爬取评论
        for index in range(5):#页数
            for i in detail_tab.eles('t:div@@class=comment-item'):
                print(i('.comment-con').text)
                dict={'comment':i('.comment-con').text}
                csv_writer.writerow(dict)
            if (detail_tab.ele('t:a@text()=下一页')):
                detail_tab.ele('t:a@text()=下一页').click()
                time.sleep(2)
        time.sleep(10)

detail_tab_list=get_detail_tab_list(search_result)
get_comment(detail_tab_list[0:15])



# for result in search_result:
#     print(result)
