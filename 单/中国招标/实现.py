'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/4 21:12
       @Desc     : 
=========================================================   
'''
# https://www.chinabidding.cc/


import requests
import time

from lxml import etree
import pymysql
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.chinabidding.cc/info/lists/pid/9.html",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "AGL_USER_ID": "d0bc75ee-2a69-4eb8-b7bd-482634e2f585",
    "Qs_lvt_527898": "1730725795",
    "Hm_lvt_761bd819790da67359ef39f51efcaf00": "1730725795",
    "HMACCOUNT": "4D4F61CE5656C745",
    "Hm_lpvt_761bd819790da67359ef39f51efcaf00": "1730725818",
    "Qs_pv_527898": "2542342483081138700%2C1281806428816554000%2C3396033940048165400"
}
def get_info(page):
    url = "https://www.chinabidding.cc/info/lists/pid/9.html"
    for index in range(page):
        params = {
            "page":index,
            "pid": "9",
            "classid": "0"
        }
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        # print(response.text)
        # print(response)
        html = etree.HTML(response.text)
        infos = html.xpath('//*[@id="center_box"]/div[2]/div[1]/div[2]/ul/li')
        # print(infos)
        print(f'正在采集第{index+1}页')

        for info in infos:
            title = info.xpath('./a/text()')[0]
            date = info.xpath('./b/text()')[0]
            href = info.xpath('./a/@href')[0]
            sql = ('insert into notice (date,title,href) value (%s,%s,%s)')
            cursur.execute(sql, (date, title, href))
            print(date, title, href)
        time.sleep(2)

con=pymysql.connect( user='data', password="data",host='47.236.198.227',database='data')
con.connect()
cursur=con.cursor()





get_info(4)
con.commit()