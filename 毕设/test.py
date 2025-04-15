'''
=========================================================    
       @File     : test.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/30 12:08
       @Desc     : 
=========================================================   
'''
import requests
import json
def get_goods_info(keyword):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "baggage": "sentry-environment=production,sentry-release=016,sentry-public_key=a320a900b5e049ac8719b0a3247da612,sentry-trace_id=504a9211d7dc4a08a7ae21847149054a,sentry-sample_rate=0.1,sentry-transaction=searchList-products,sentry-sampled=false",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "lang": "enus",
        "origin": "https://www.globalsources.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.globalsources.com/searchList/products?keyWord=make%20up&pageNum=1",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sensorsid": "$device_id=1306818073229",
        "sentry-trace": "504a9211d7dc4a08a7ae21847149054a-bce35006b1435bd2-0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }
    cookies = {
        "lang": "enus",
        "SiteVer": "1",
        "visid_incap_2720266": "dpAQRHv1TkyhMYu4WBhN2jWsa2cAAAAAQUIPAAAAAAA3SEXOxmUvNHIT1FQXs/Bg",
        "nlbi_2720266": "6LnUeEQ5uHME1pm2WlZLAwAAAADAPPbvnzVJAdWGuJuNBg2W",
        "bucket": "c",
        "sajssdk_2015_cross_new_user": "1",
        "sensorsdata2015jssdkchannel": "%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D",
        "_gcl_au": "1.1.122497227.1735109689",
        "visid_incap_2815037": "Pmihi1lkTQ6ltNvaaGBtjjisa2cAAAAAQUIPAAAAAAA+OEcSim/e7zIr4dx1nqQb",
        "_ga": "GA1.1.991508900.1735109690",
        "_fbp": "fb.1.1735109690701.429401778895011427",
        "_clck": "1aqou64%7C2%7Cfs0%7C0%7C1820",
        "visid_incap_2920482": "MaASV3u8Q6SQT+KsjM075Tqsa2cAAAAAQUIPAAAAAAAbxVVZ4nYbZfseypjY3uaY",
        "nlbi_2920482": "ovhtX/Ig5j7qJyIsANt64gAAAAANJoRa5KCDpu0rTon3/Q54",
        "search_spell_check-193fc98bd4e10e3-03925db0eadc1c6-4c657b58-2073600-193fc98bd4f1505": "%7B%22layerCode%22%3A%22search_spell_check%22%2C%22experimentCode%22%3A%22spell_check%22%2C%22groupName%22%3A%22spell_check_control1%22%2C%22groupCode%22%3A%22ctrl1%22%7D",
        "search_recall-193fc98bd4e10e3-03925db0eadc1c6-4c657b58-2073600-193fc98bd4f1505": "%7B%22layerCode%22%3A%22search_recall%22%2C%22experimentCode%22%3A%22exact_match%22%2C%22groupName%22%3A%22exact_match_test%22%2C%22groupCode%22%3A%22exp%22%7D",
        "ul_cookie": "w40vZqnIcCfl5LRLx0dZsw%3D%3D",
        "ul2_cookie": "eyJ2ZXIiOiIxLjAiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MzU3MTQ5MjEsInVsMl9jb29raWUiOiJTR0I4bytuMnBCeEN3WDltMXYxK3NJUnQ1eG9sN1R6OTA3dHdtK1NjM0c4PSJ9.ZshNb9f3_BDm0cuYrAH8OFDV5l3rF39jCXs4XRBT5bs",
        "nlbi_2815037": "OW5jMDMr5AfG2laVQ07hiwAAAADqFjGUFJzZ847eM5wBjmJo",
        "search_spell_check-1306818073229": "%7B%22layerCode%22%3A%22search_spell_check%22%2C%22experimentCode%22%3A%22spell_check%22%2C%22groupName%22%3A%22spell_check_test%22%2C%22groupCode%22%3A%22exp%22%7D",
        "search_recall-1306818073229": "%7B%22layerCode%22%3A%22search_recall%22%2C%22experimentCode%22%3A%22exact_match%22%2C%22groupName%22%3A%22exact_match_control1%22%2C%22groupCode%22%3A%22ctrl1%22%7D",
        "incap_ses_577_2720266": "3n+fMFW00w9EaoIEkuoBCJjUa2cAAAAAVSCYi6lhsaZ6i27hQoFd3A==",
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221306818073229%22%2C%22first_id%22%3A%22193fc98bd4e10e3-03925db0eadc1c6-4c657b58-2073600-193fc98bd4f1505%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fmcndc4emxnd1.feishu.cn%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzZmM5OGJkNGUxMGUzLTAzOTI1ZGIwZWFkYzFjNi00YzY1N2I1OC0yMDczNjAwLTE5M2ZjOThiZDRmMTUwNSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjEzMDY4MTgwNzMyMjkifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221306818073229%22%7D%2C%22%24device_id%22%3A%22193fc98bd4e10e3-03925db0eadc1c6-4c657b58-2073600-193fc98bd4f1505%22%7D",
        "incap_ses_1221_2815037": "hv/GcEh47kNRWkbmON3xEJvUa2cAAAAAdV56zb0TeilUvxh5zpT49w==",
        "incap_ses_577_2920482": "De0nHo7Ln26ka4IEkuoBCJrUa2cAAAAANPbWE+Csk+Uo/x4VDXScWg==",
        "nlbi_2720266_2147483392": "S/maf8Dg9X7pmDITWlZLAwAAAACfoLh6O8ABPciZXlOreUdu",
        "reese84": "3:FIdu+8zXJ3dLWtmbl7IBbQ==:CkxecWXsNPnN/4rLC9pp48+1sg3ngGKLh7VocHREznJK7YufdW5Ld9/zyKBLFFXld+AkjCujqJCwPgwzX3wk+0UfINR4hgVEIpme5e425jXvEJzjVFFO162UaH2aGGuKnHFAg8D4ufNlrzFc53uQhDKcdbN7/pKXrg81VldprY4ubJPskbjbiDIdB9IT8spDPU3jyTVoQZ6kXy9VlcsAtaSHzevqU6wc3O0Lj/V5kxw/WNOSxYgU5oLWFM7pUufVylAPup0zaX0WI44o8A0veAD4hSXsAwBRtmen1/9Qy07kxbjwyhe6BogKPoXtLXXvjiT8LqlBXEJks619R8hOazWoNHhtJUKH+ARFdB7V6iTkp5iLO2jgASKx72Aybtj7SkFxvbt3RzEXWTPWDSfhjBL2AO7HQuTLbnCFzCkNfR+Hl6/oq+k9CjriDAd9uvMfmctzmK80zY5n1g2CC856wQ==:5jK/o8rdniZbLf2OZbjvy1D0BoLUO4jXCNK2phZsm+4=",
        "_ga_M0GFGLPMZ2": "GS1.1.1735120027.2.1.1735120115.33.0.1071509610",
        "_uetsid": "23230f30c28d11efb502f92526a6c1a7",
        "_uetvid": "23232a80c28d11efac7c3bbaf8c48d05",
        "GsCookieFlag": "%7B%22isIndexTop%22%3A%22on%22%2C%22globalTimeOut%22%3A1735120388563%2C%22pageCont%22%3A2%7D"
    }
    url = "https://www.globalsources.com/api/agg-search/DESKTOP/v3/product/search"
    data = {
        "pageNum": 1,
        "pageSize": 1000,
        "query": keyword,
        "popupFlag": False,
        "spellCheck": 0
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data).json()
    company_name_list=[]
    dict={}
    for index, i in enumerate(response['data']['list']):
        if i['companyName'] not in company_name_list:
            company_name_list.append(i['companyName'])
            categoryinfo = i['categoryInfo']['l1CategoryVo']['categoryName'] + '->' + i['categoryInfo']['l2CategoryVo']['categoryName'] + '->' + i['categoryInfo']['l3CategoryVo']['categoryName'] + '->' +i['categoryInfo']['l4CategoryVo']['categoryName']
            print(i['companyName'], end='   ')
            print(categoryinfo,index)
            # insert_product(i['productName'],i['listVoShowPriceStr'],'https://www.globalsources.com' + i['desktopProductDetailUrl'],'GlobalSource')
            # format_dict= {index:
            #     {
            #         'good_name': i['productName'],
            #         'good_price': i['listVoShowPriceStr'],
            #         'url': 'https://www.globalsources.com' + i['desktopProductDetailUrl'],
            #         'source': 'GlobalSource'
            #     }
            # }
            # dict.update(format_dict)
get_goods_info('big')
