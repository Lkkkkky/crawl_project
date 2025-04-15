'''
=========================================================    
       @File     : 获取商品链接.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/12 11:28
       @Desc     : 
=========================================================   
'''
from DrissionPage import Chromium
from loguru import logger

goods_url_list=[]

browse=Chromium(5678)

main_tab=browse.new_tab('https://www.temu.com/-white-m-634418216360063.html?is_back=1&refer_page_name=mall&refer_page_id=10040_1733973571180_xxdjyoki85&refer_page_sn=10040&_x_sessn_id=z1jm4984gw&filter_items=2%3A0')
eles=main_tab.eles('@class:_2Tl9qLr1 _1ak1dai3')[0:24]
for i in eles:
    goods_url_list.append(i.attr('href'))

print(goods_url_list)