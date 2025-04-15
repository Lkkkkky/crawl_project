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


browse=Chromium(5678)

main_tab=browse.new_tab('https://www.jd.com/')

input=main_tab.ele('xpath://input[@id="key"]').input('电脑')#搜索内容
main_tab('xpath://*[@id="search"]/div/div[2]/button').click()
time.sleep(2)

main_tab.scroll.down(10000)#下拉,加载完整列表
time.sleep(5)
search_result=main_tab.eles('t:li@@class=gl-item')#获取搜索结果
detail_tab=search_result[8].ele('t:a').click.for_new_tab()

detail_tab.ele('@data-anchor=#comment').click()
time.sleep(2)
for page in range(30):
    for i in detail_tab.eles('t:div@@class=comment-item'):
        print(i('.comment-con').text)
    detail_tab.ele('t:a@href=#comment').click()
    time.sleep(2)

# for result in search_result:
#     print(result)
