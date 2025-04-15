import requests
import json
import time
import re
import csv
import pandas as pd
from lxml import etree
import 企查查实现
import 商家信息
from loguru import logger


fi= open('song.csv',mode='a+',encoding='utf-8',newline='')
# 字典写入
csv_writer=csv.DictWriter(fi,fieldnames=['name','价格','链接','公司名称','公司地址','联系方式'])
# 写入表头
csv_writer.writeheader()
cookies = {
    "aws_lang": "cn",
    "skin": "noskin",
    "session-id-time": "2082787201l",
    "i18n-prefs": "USD",
    "lc-main": "zh_CN",
    "sp-cdn": "\"L5Z9:CN\"",
    "session-id": "142-5626825-0146612",
    "ubid-main": "135-4192287-8474760",
    "session-token": "6xvwAI09F+7t8qecAq9bIDjaa35XS7+KQbOO9oeCLhXaGU3G1rx0rc58VyxBnBGm3NNYeU9TgBKUCXvtuUb3Nqbgk4Zukt0Ibz4cOvAFQy8Vvwfn4FZlOfxl772ka3LH6AGKdlcbb9VPlZQPwDCoytS/9p5erJo/ZVbwhsxp5ZXTaHFRPat6gxlBqLXlSqrORru0wtFi1Cmb7U/wz2dA6TUYLduOstod2CTu5fIuiWC4/r7lm7bkuI4UMZ+XtfANTDOxECg4XgFW+hv1YJ+5QnNzY+Ki7lfkRqb314u4aacIucWqRBW3Y6Oxoy0oIG6BVY2IMfss2SBSrsZr+bpuZ2/R4GlzNrtv",
    "csm-hit": "tb:Y8GWZ9DFBWW0TDN0Q47Z+sa-8G9XBZRKF7NSX2W56EGC-4N5YPFPBN78P3J4TSHQ9|1732329956409&t:1732329956409&adb:adblk_no"
}
def post(page):
    t = str(int(time.time()))
    page=str(page)
    headers = {
        "accept": "text/html,image/webp,ajax/ajax,*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "device-memory": "8",
        "downlink": "1.35",
        "dpr": "1",
        "ect": "4g",
        "origin": "https://www.amazon.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": f"https://www.amazon.com/-/zh/s?k=%E7%94%B5%E8%84%91&page={page}&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=36LGZVZRFXCYL&qid={t}&sprefix=diannao%2Caps%2C321&ref=sr_pg_{int(page)-1}",
        "rtt": "250",
        "sec-ch-device-memory": "8",
        "sec-ch-dpr": "1",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua-platform-version": "\"10.0.0\"",
        "sec-ch-viewport-width": "1912",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "viewport-width": "1912",
        "x-amazon-rush-fingerprints": "AmazonRushAssetLoader:1202F8AA9B9E3A62A246BF3FA42812770110C222|AmazonRushFramework:EC446FBE6D4385B7660F56A844F4D427DE175225|AmazonRushRouter:15D9B6124DC03EC360DD1DF8362BD9C8156D4486",
        "x-amazon-s-fallback-url;": "",
        "x-amazon-s-mismatch-behavior": "ABANDON",
        "x-amazon-s-swrs-version": "C64040577D6105D1043686EC2CBD919A,D41D8CD98F00B204E9800998ECF8427E",
        "x-requested-with": "XMLHttpRequest"
    }

    url = "https://www.amazon.com/s/query"

    params = {
        "__mk_zh_CN": "亚马逊网站",
        "crid": "2W9URSHSWWR7E",
        "k": "香水",
        "page": page,
        "qid": t,
        "ref": "sr_pg_1",
        "sprefix": "xiangsh,aps,306"
    }
    data = {
        "page-content-type": "atf",
        "prefetch-type": "rq",
        "customer-action": "pagination"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)


    try:
        cookies['session-token'] = response.cookies.get_dict()['session-token']

    except KeyError:
        logger.info('无需更新token')
    try:
        rrid = response.headers['x-amz-rid']
        prefetch_ajax_data = re.findall("payload\" : \"(.*?)\"", response.text)[0]
        return response, rrid, prefetch_ajax_data, t, params
    except:
        logger.info('封控')
        time.sleep(60)


def sec_post(page,rrid,prefetch_ajax_data,t,params):
    sec_headers = {
        "accept": "text/html,image/webp,ajax/ajax,*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "device-memory": "8",
        "downlink": "1.4",
        "dpr": "1",
        "ect": "4g",
        "origin": "https://www.amazon.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": f"https://www.amazon.com/-/zh/s?k=%E7%94%B5%E8%84%91&page={page}&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=36LGZVZRFXCYL&qid={t}&sprefix=diannao%2Caps%2C321&ref=sr_pg_{page}",
        "rtt": "150",
        "sec-ch-device-memory": "8",
        "sec-ch-dpr": "1",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua-platform-version": "\"10.0.0\"",
        "sec-ch-viewport-width": "1912",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "viewport-width": "1912",
        "x-amazon-rush-fingerprints": "AmazonRushAssetLoader:1202F8AA9B9E3A62A246BF3FA42812770110C222|AmazonRushFramework:EC446FBE6D4385B7660F56A844F4D427DE175225|AmazonRushRouter:15D9B6124DC03EC360DD1DF8362BD9C8156D4486",
        "x-amazon-s-fallback-url": "https://www.amazon.com/-/zh/s?k=%E7%94%B5%E8%84%91&page=11&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=36LGZVZRFXCYL&qid=1732213757&sprefix=diannao%2Caps%2C321&ref=sr_pg_11",
        "x-amazon-s-mismatch-behavior": "FALLBACK",
        "x-amazon-s-swrs-version": "C64040577D6105D1043686EC2CBD919A,D41D8CD98F00B204E9800998ECF8427E",
        "x-requested-with": "XMLHttpRequest"
    }

    sec_data = '{"rrid":"' + rrid + '","wIndexMainSlot":12,"prefetch-ajax-data":"' + prefetch_ajax_data + '","page-content-type":"btf","prefetch-type":"log","customer-action":"pagination"}'
    url = "https://www.amazon.com/s/query"
    response = requests.post(url, headers=sec_headers, cookies=cookies, params=params, data=sec_data)

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
                good_name = result_html.xpath('//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()')[0]
                good_price = result_html.xpath('//span[@class="a-offscreen"]/text()')[0]
                good_href = 'https://www.amazon.com' + result_html.xpath(
                    '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]/@href')[0]
                good_asin,good_seller=商家信息.get_asin_seller(good_href)
                good_company_detail=商家信息.get_company_name(good_seller,good_asin)
                good_company_phone=企查查实现.get_phone(good_company_detail[0])
            except:
                good_name = ''
                good_price = 0
                good_href = ""
            goods_dict = {
                'name': good_name,
                '价格': good_price,
                '链接': good_href,
                '公司名称':good_company_detail[0],
                '公司地址':good_company_detail[1],
                '联系方式':good_company_phone,
            }



            if (goods_dict['name']!=''):
                csv_writer.writerow(goods_dict)
                print(goods_dict)

# 每页22条数据  page为起始页数
def task(page):
    for i in range(page, page + 100):
        try:
            first_response, rrid, prefetch_ajax_data, t, params = post(i)
            fist_res_json = json.loads(clean_data(first_response.text))
            search_result_list(fist_res_json)
            # 第二个包
            sec_response = sec_post(i, rrid, prefetch_ajax_data, t, params)
            sec_res_json = json.loads(clean_data(sec_response.text))
            search_result_list(sec_res_json)
            time.sleep(2)
        except:
            time.sleep(30)
    df = pd.read_csv('song.csv')
    df_deduplicated = df.drop_duplicates( subset=['name'])
    # 保存去重后的 CSV 文件
    df_deduplicated.to_csv('out.csv', index=False,encoding='utf-8')
    print('去重成功')
# print(clean_data(response.text))
task(160)



# for i in range(25,50):
#     first_response,rrid,prefetch_ajax_data,t,params = post(i)
#     fist_res_json = json.loads(clean_data(first_response.text))
#     search_result_list(fist_res_json)
#     # 第二个包
#     sec_response = sec_post(i,rrid,prefetch_ajax_data,t,params)
#     sec_res_json = json.loads(clean_data(sec_response.text))
#     search_result_list(sec_res_json)