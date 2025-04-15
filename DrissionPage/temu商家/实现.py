'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/17 15:02
       @Desc     : 
=========================================================   
'''
import traceback

'''
=========================================================    
       @File     : main.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/10 17:49
       @Desc     : 
=========================================================   
'''
from DrissionPage import Chromium,ChromiumOptions
import time
import requests
from loguru import logger
import  csv
import 企查查实现

f=open('company.csv','a+',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['url','company_name','name','phone','address'])
csv_writer.writeheader()
session = requests.Session()
session.trust_env=False
attr_list=[]
img_url_list=[]
co=ChromiumOptions()
# co.headless()
co.incognito(on_off=True)
browse=Chromium(co)
main_tab=browse.new_tab('https://www.temu.com/makeup-o3-26.html?opt_level=2&title=Makeup&_x_enter_scene_type=cate_tab&leaf_type=bro&show_search_type=3&refer_page_el_sn=200055&_x_sessn_id=v8j49gfb1l&refer_page_name=category&refer_page_id=10012_1734419442522_734jggjszk&refer_page_sn=10012&filter_items=400%3A1%7C0%3A1&is_back=1')
good_list_eles=main_tab.eles("xpath://h2[@class='_2BvQbnbN']")
print(good_list_eles)
try:
    new_tab=good_list_eles[0].click.for_new_tab()
    logger.info(f"打开第一个商品链接")
    new_tab.ele("t:div@class=_373TxnaS").click()#打开店铺页面
    logger.info(f"打开第一个商品的店铺链接")

except Exception as e:
    logger.error(e)
    logger.info("等待验证")
    time.sleep(60)

new_tab.ele("t:h1@class:PX7EseE2 _2DshZJ_y").click()  # 加载公司名称
company_name = new_tab.ele("t:p@class=_3dYV5Hya").text
logger.info("公司信息获取成功---->"+company_name)
# name, phone, address = 企查查实现.get_phone(company_name)
name=''
phone=''
address=''

format_dict={
    "url":new_tab.url,
    "company_name":company_name,
    "name": name,
    "phone": phone,
    "address": address
}
csv_writer.writerow(format_dict)
time.sleep(2)
new_tab.close()
