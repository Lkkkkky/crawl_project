'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/25 15:15
       @Desc     : 
=========================================================   
'''
import time


from DrissionPage import Chromium

browser = Chromium(5678)
url = 'https://www.globalsources.com/searchList/products?keyWord=make%20up&pageNum=1'
main_tab=browser.new_tab(url)
company_list_eles=main_tab.eles('xpath://div[@class="name o2o-name"]')
for company in company_list_eles[22:40]:
    new_tab=company.click.for_new_tab()
    new_tab.listen.start('supplier/v2/home/category-top')
    time.sleep(5)
    ExportSite=new_tab.eles('xpath://div[@class="item-content text-one-omitted"]/span')[1].text
    print(ExportSite)
    hotsalegoods=[]  #热销商品
    if "America" in ExportSite:
        for hotsalegood in new_tab.listen.wait().response.body['data']['groupList']:
            hotsalegoods.append(hotsalegood['groupName'])

        new_tab.ele('xpath://div[@class="nav-btm-box"]/div/div/ul/li[5]/div').click()
        try:
            new_tab.ele('xpath://div[@class="sign-in-btn"]').click()
            new_tab.ele('xpath://button[@class="sure-btn ant-btn ant-btn-primary"]').click()
        except Exception as e:
            print("已交换过联系方式")
        print(new_tab.ele('xpath://div[@class="show-value"]/div[2]').text)
    print(hotsalegoods)
    browser.close_tabs(new_tab)





