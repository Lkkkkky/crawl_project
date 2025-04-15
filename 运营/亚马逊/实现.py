from curl_cffi import requests
import json
import time
import re
import csv
import pandas as pd
from lxml import etree
headers = {
    "accept": "text/html,image/webp,*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "device-memory": "8",
    "downlink": "10",
    "dpr": "1",
    "ect": "4g",
    "origin": "https://www.amazon.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.amazon.com/-/zh/s?k=phone&page=6&language=zh&crid=IMVRWSKSO8X5&qid=1743584724&sprefix=%2Caps%2C290&xpid=LRsdSWdNkSPye&ref=sr_pg_6",
    "rtt": "250",
    "sec-ch-device-memory": "8",
    "sec-ch-dpr": "1",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-viewport-width": "1912",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "viewport-width": "1912",
    "x-amazon-rush-fingerprints": "AmazonRushAssetLoader:1202F8AA9B9E3A62A246BF3FA42812770110C222|AmazonRushFramework:2120192C7EB7263FB772CD294CC8AC09062D1B2D|AmazonRushRouter:2CCA57F4563CA787ECA85DBD7A3CA5CBC1744F4E",
    "x-amazon-s-fallback-url": "https://www.amazon.com/-/zh/s?k=phone&page=7&language=zh&crid=IMVRWSKSO8X5&qid=1743584740&sprefix=%2Caps%2C290&xpid=LRsdSWdNkSPye&ref=sr_pg_7",
    "x-amazon-s-mismatch-behavior": "FALLBACK",
    "x-amazon-s-swrs-version": "5429B58DEA87DF9D55A2B0F18B59072C,D41D8CD98F00B204E9800998ECF8427E",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "session-id": "143-7304992-7404309",
    "session-id-time": "2082787201l",
    "i18n-prefs": "USD",
    "ubid-main": "135-7265586-7432610",
    "lc-main": "zh_CN",
    "sp-cdn": "\"L5Z9:CN\"",
    "aws-target-data": "%7B%22support%22%3A%221%22%7D",
    "regStatus": "pre-register",
    "aws-target-visitor-id": "1739760556738-51869.42_0",
    "AMCV_7742037254C95E840A4C98A6%40AdobeOrg": "1585540135%7CMCIDTS%7C20180%7CMCMID%7C68110874936468907323610892830072390376%7CMCAAMLH-1744126754%7C11%7CMCAAMB-1744126754%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1743529154s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-20187%7CvVersion%7C4.4.0",
    "session-token": "jldHUQUQk0w8TRjI/mHUzF8vnaTt8d7PMaY9R0UAPagdURf9tArKudFL/+/bjQcY7YIX3ouVpv9KvUgvbDPFbH4ckpDUIfPJ+hjSzWiP9nW6wGbnDtW8M+hoImpLdiIv0FrUWWxC+mI/zEO0zefeOcVmt4D0xGH6GhwsK+v59TctiHD/d429rlqsbMPJTnKC5ozkenDl8i+kKJNsqzy25Ew6smpdcx8Gd4xjRdjjwv480+opJ2sffj4wnETRnF2Yeui9zOKaOoP+W5d7OiNu6AfSB5KE+HUt/HoIO7Tc3Ke0lKU0WbioAmOp2EHl0GqFqjqHCZfSW1oIRVS+vpSCOBS9gk1Rmzqs",
    "csm-hit": "tb:PVZXA1G1Q2K8W372ZSCD+sa-Q5JF2S5KYYJZJHWHD7V7-N9M436V9PKG974G69F7T|1743586827083&t:1743586827083&adb:adblk_no"
}
good_list=[]
# def good_info_1():
#
#    url = "https://www.amazon.com/s/query"
#    params = {
#       "crid": "IMVRWSKSO8X5",
#       "k": keyword,
#       "page": page,
#       "qid": "1743578110",
#       "ref": "sr_pg_4",
#       "sprefix": ",aps,290",
#       "xpid": "LRsdSWdNkSPye"
#    }
#    data = {
#       "page-content-type": "atf",
#       "prefetch-type": "rq",
#       "customer-action": "pagination"
#    }
#    data = json.dumps(data, separators=(',', ':'))
#    res = requests.post(url, headers=headers,cookies=cookies, params=params, data=data)
#
#    # print(res.text)
#
#    rrid=re.findall(r'"requestId" : "(.*?)"',res.text)[0]
#
#    prefetch_ajax_data=re.findall(r'"payload" : "(.*?)"',res.text)[0]
#
#    good_name=re.findall(r'h2 aria-label=\\"(.*?)\\"',res.text)
#    good_asin = re.findall(r'"asin" : "(.*?)"', res.text)  # 商品SKU
#
#    for i in good_name:
#       good_list.append(i)
#       print(i)
#    return rrid,prefetch_ajax_data
#
# def good_info_2(rrid,prefetch_ajax_data):
#    headers = {
#       "accept": "text/html,image/webp,*/*",
#       "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#       "cache-control": "no-cache",
#       "content-type": "application/json",
#       "device-memory": "8",
#       "downlink": "3.3",
#       "dpr": "1",
#       "ect": "4g",
#       "origin": "https://www.amazon.com",
#       "pragma": "no-cache",
#       "priority": "u=1, i",
#       "referer": "https://www.amazon.com/-/zh/s?k=phone&page=4&crid=IMVRWSKSO8X5&qid=1743577557&sprefix=%2Caps%2C290&xpid=LRsdSWdNkSPye&ref=sr_pg_4",
#       "rtt": "200",
#       "sec-ch-device-memory": "8",
#       "sec-ch-dpr": "1",
#       "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
#       "sec-ch-ua-mobile": "?0",
#       "sec-ch-ua-platform": "\"Windows\"",
#       "sec-ch-ua-platform-version": "\"10.0.0\"",
#       "sec-ch-viewport-width": "1912",
#       "sec-fetch-dest": "empty",
#       "sec-fetch-mode": "cors",
#       "sec-fetch-site": "same-origin",
#       "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
#       "viewport-width": "1912",
#       "x-amazon-rush-fingerprints": "AmazonRushAssetLoader:1202F8AA9B9E3A62A246BF3FA42812770110C222|AmazonRushFramework:2120192C7EB7263FB772CD294CC8AC09062D1B2D|AmazonRushRouter:2CCA57F4563CA787ECA85DBD7A3CA5CBC1744F4E",
#       "x-amazon-s-fallback-url": "https://www.amazon.com/-/zh/s?k=phone&page=5&crid=IMVRWSKSO8X5&qid=1743578110&sprefix=%2Caps%2C290&xpid=LRsdSWdNkSPye&ref=sr_pg_5",
#       "x-amazon-s-mismatch-behavior": "FALLBACK",
#       "x-amazon-s-swrs-version": "5429B58DEA87DF9D55A2B0F18B59072C,D41D8CD98F00B204E9800998ECF8427E",
#       "x-requested-with": "XMLHttpRequest"
#    }
#    cookies = {
#       "session-id": "143-7304992-7404309",
#       "session-id-time": "2082787201l",
#       "i18n-prefs": "USD",
#       "ubid-main": "135-7265586-7432610",
#       "lc-main": "zh_CN",
#       "sp-cdn": "\"L5Z9:CN\"",
#       "aws-target-data": "%7B%22support%22%3A%221%22%7D",
#       "regStatus": "pre-register",
#       "aws-target-visitor-id": "1739760556738-51869.42_0",
#       "AMCV_7742037254C95E840A4C98A6%40AdobeOrg": "1585540135%7CMCIDTS%7C20180%7CMCMID%7C68110874936468907323610892830072390376%7CMCAAMLH-1744126754%7C11%7CMCAAMB-1744126754%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1743529154s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-20187%7CvVersion%7C4.4.0",
#       "session-token": "NIZZTu8vmAE02mT7cpuKMx1Iw5t0ZvUWBR/LcGrmU50j20fhKTHcYmuxzquzy6Ck9Xc43M+4cQf36qFFYIJ+9C31jYZbuoduOqemMMGGzhPuJ8QM0EwzMc4OQzzrKsGYJxBj4shP3JG5cK3iXP57Tf+dsp+XXcfn+K80KWr22ua6p3RELb2kQRywW3mc33R11Zs2pQTWSOhOmSu5ezglUsY7pZnSiZf03ZpDoX4ahow5Hf8J79fR6YWF3QYCQY3qxWYu9puZSW7eNjTJiOT5Qb8e6HCxTP3dIvoWwtwEfDDYq0ZoWoXyivZONPYp477WnKTGb3tE6MCHsbJLoKW+fKZvfpaOA5Zz",
#       "csm-hit": "tb:PVZXA1G1Q2K8W372ZSCD+sa-PVZXA1G1Q2K8W372ZSCD-01MPC4756A5DJA0B4FRV|1743578168145&t:1743578168145&adb:adblk_no"
#    }
#    url = "https://www.amazon.com/s/query"
#    params = {
#       "crid": "IMVRWSKSO8X5",
#       "k": keyword,
#       "page": page,
#       "qid": "1743578110",
#       "ref": "sr_pg_4",
#       "sprefix": ",aps,290",
#       "xpid": "LRsdSWdNkSPye"
#    }
#    #prefetch_ajax_data 中含有转义符，不能用正常的方式提交参数
#    data = '{"rrid":"' + rrid + '","wIndexMainSlot":7,"prefetch-ajax-data":"' + prefetch_ajax_data + '","page-content-type":"btf","prefetch-type":"log","customer-action":"pagination"}'
#
#    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
#    good_name = re.findall(r'h2 aria-label=\\"(.*?)\\"', response.text) #商品名称
#    good_asin = re.findall(r'"asin" : "(.*?)"', response.text) #商品SKU
#    print(len(good_name))
#    print(len(good_asin))
#    for i in good_name:
#       good_list.append(i)
#       print(i)
#
#    return good_name
# print(good_name)
fi= open('amazon_goods1.csv',mode='w',encoding='utf-8',newline='')
# 字典写入
csv_writer=csv.DictWriter(fi,fieldnames=['name','价格','链接'])
# 写入表头
csv_writer.writeheader()
def good_info_1():

   url = "https://www.amazon.com/s/query"
   params = {
      "crid": "IMVRWSKSO8X5",
      "k": keyword,
      "page": page,
      "qid": "1743578110",
      "ref": "sr_pg_4",
      "sprefix": ",aps,290",
      "xpid": "LRsdSWdNkSPye"
   }
   data = {
      "page-content-type": "atf",
      "prefetch-type": "rq",
      "customer-action": "pagination"
   }
   data = json.dumps(data, separators=(',', ':'))
   res = requests.post(url, headers=headers,cookies=cookies, params=params, data=data)
   # , proxies = {'https': '127.0.0.1:33210', 'http': '127.0.0.1:33210'}
   # print(res.text)

   rrid=re.findall(r'"requestId" : "(.*?)"',res.text)[0]

   prefetch_ajax_data=re.findall(r'"payload" : "(.*?)"',res.text)[0]


   return res,rrid,prefetch_ajax_data

def good_info_2(rrid,prefetch_ajax_data):

   url = "https://www.amazon.com/s/query"
   params = {
      "crid": "IMVRWSKSO8X5",
      "k": keyword,
      "page": page,
      "qid": "1743578110",
      "ref": "sr_pg_4",
      "sprefix": ",aps,290",
      "xpid": "LRsdSWdNkSPye"
   }
   #prefetch_ajax_data 中含有转义符，不能用正常的方式提交参数
   data = '{"rrid":"' + rrid + '","wIndexMainSlot":7,"prefetch-ajax-data":"' + prefetch_ajax_data + '","page-content-type":"btf","prefetch-type":"log","customer-action":"pagination"}'

   response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
   # , proxies = {'https': '127.0.0.1:33210', 'http': '127.0.0.1:33210'}
   return response

def clean_data(res):
   res = res.replace('&&&', ',').strip()[:-1]
   return f'[{res}]'


def search_result_list(res):
   for i in res:
      if ("data-main-slot:search-result" in i[1]):
         # print(i[1],end='--->')
         result_text = i[2]['html']
         result_html = etree.HTML(result_text)
         try:
            good_name = result_html.xpath('//h2[@class="a-size-base-plus a-spacing-none a-color-base a-text-normal"]/span/text()')[0]
            good_price = result_html.xpath('//span[@class="a-offscreen"]/text()')[0]
            good_href = 'https://www.amazon.com' + result_html.xpath(
               '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style"]/@href')[
               0]
         except:
            good_name = ''
            good_price = 0
            good_href = ""
         goods_dict = {
            'name': good_name,
            '价格': good_price,
            '链接': good_href,

         }
         csv_writer.writerow(goods_dict)
         print(goods_dict)
target_list=['ball','socks','foods']

for i in range(5):
  page=i
  keyword='ball'
  first_response,rrid, prefetch_ajax_data = good_info_1()
  fist_res_json = json.loads(clean_data(first_response.text))

  # search_result_list(fist_res_json)

  sec_response=good_info_2(rrid, prefetch_ajax_data)
  sec_res_json = json.loads(clean_data(sec_response.text))

  search_result_list(sec_res_json)
  time.sleep(5)