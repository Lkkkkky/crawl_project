'''
=========================================================    
       @File     : test.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/26 11:57
       @Desc     : 
=========================================================   
'''
'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/26 09:36
       @Desc     : 
=========================================================   
'''
import json
import hashlib
import requests
import time
import csv


f=open('company.csv','w',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['company_address','company_name','company_url','company_production','company_phone'])
csv_writer.writeheader()
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "origin": "https://s.1688.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://s.1688.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    'cna': 'VxbMHxwaJCYCAbfsE96tvqbx',
    'xlly_s': '1',
    'cookie2': '198d92feab839b20ab666f0539f80bb5',
    't': '3ee973d5b98de23e1476035588ef4c4c',
    '_tb_token_': '587e989fb7759',
    'ali_apache_tracktmp': 'c_w_signed=Y',
    'leftMenuLastMode': 'EXPEND',
    'leftMenuModeTip': 'shown',
    'keywordsHistory': '%E9%A6%99%E6%B0%B4',
    'mtop_partitioned_detect': '1',
    '_m_h5_tk': '2033cedeb45b503f941dc50e296a5592_1732601604408',
    '_m_h5_tk_enc': 'f4632178cc563e726b236cdde5931509',
    'cookie1': 'B0OpNm8iw1vCmzeEMg8jjagv4EcWfKpU6uh69POa6Pg%3D',
    'cookie17': 'UUpgRKQyFgw4s%2BrJng%3D%3D',
    'sgcookie': 'E100Lq8508A3hsYsfaplgZYgQdrytdt1VI5i4K6CSLNlzVxbUY0Zpb0G6pAQNA98%2Fb65HlWzn2fw0iCAoBgr6W%2BPlrTA8jA9PovzWaXEFFROMJU%3D',
    'sg': '85b',
    'csg': 'd80671ce',
    'lid': 'tb616835328',
    'unb': '2212982702355',
    'uc4': 'nk4=0%40FY4I7jF7l1i%2BKhyLxibEFGUPlKmWgQ%3D%3D&id4=0%40U2gqy1X09FRhJbH3XFvf%2BYnfDRW2lzu4',
    '_nk_': 'tb616835328',
    '__cn_logon__': 'true',
    '__cn_logon_id__': 'tb616835328',
    'ali_apache_track': 'c_mid=b2b-221298270235580f03|c_lid=tb616835328|c_ms=1',
    'last_mid': 'b2b-221298270235580f03',
    '_csrf_token': '1732591616405',
    'firstRefresh': '1732591624352',
    'lastRefresh': '1732591624352',
    'aliwwLastRefresh': '1732591624520',
    'is_identity': 'buyer',
    '_is_show_loginId_change_block_': 'b2b-221298270235580f03_false',
    '_show_force_unbind_div_': 'b2b-221298270235580f03_false',
    '_show_sys_unbind_div_': 'b2b-221298270235580f03_false',
    '_show_user_unbind_div_': 'b2b-221298270235580f03_false',
    '__rn_alert__': 'false',
    '_user_vitals_session_data_': '{"user_line_track":true,"ul_session_id":"f1hw2mlhk8e","last_page_id":"mind.1688.com%2Fapxmwsoolge"}',
    'isg': 'BJGRzEvBkuVfAf7xy4wQ_u5aoJ0r_gVwsC9f1nMmj9h3GrBsu0wwQNtrvu78Ep2o',
    'tfstk': 'fEgqcQjOlELqXDT15SzNzctsC3UYWrvBIVw_sfcgG-2DDmZi45NCIOcMHAuaExdYCPa0rgVYio26Hj0a7XHU1jtxCRDrLY2fhjxYIRDItZwD6AMNI8MThlgZ6NPisAdYCIKSMjUTSp9I7eGxMATIqMJ7SCcuwF2sAeTIMj4TSp9BRq_-wR2UIPq0m_Vue54gioDgEuV3Ot4iIPAzr5NCmtqcSUYu982gSPDiZAzjifbzOoALVLpldIza0Jc2vNbZzwZ4Kj2PSp0zgF2ni87GS-Gu_bGrGK7KNrhoLWMXrZkE94HzZvYwUPH-jAVZEeB_kDMxJulJxac7u8q3t4AG-RgqVX2z81Ymary4xqZD7CHnafmQ44OHJrz0ncax16JjaqkjM4l1sg44l0rEuyYdnRiSTVPZWdLrLX3-U7DH7KjyiOFlwnut0Ojgm7FzdQRPsQ6SU0vVkejOXu4LaJObGGITm7FzdQRPXGEuJ7yBGS1..',
}
my_token=cookies['_m_h5_tk'][0:32]
# 加密函数
def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

# 获取商品名称  id 的接口 ，用于后续获取手机号和地址信息
def get_userid(page):
    url = "https://search.1688.com/service/companyInfoSearchDataService"
    userid_list = []
    for i in range(page):
        params = {
            "keywords": "%CF%E3%CB%AE",
            "spm": "a260k.22462580.searchbox.0",
            "async": "true",
            "asyncCount": "14",
            "beginPage": str(i),
            "pageSize": "20",
            "requestId": "zhQbZKnPXi2YbbF4eYSHD6D4wm6fdkZh4wb1732584544169",
            "sessionId": "05a213c6d5c7453594b50c6822bca569",
            "startIndex": "6",
            "pageName": "findPCFactory"
        }
        # 不用带cookies
        response = requests.get(url, headers=headers, params=params)
        res_json=json.loads(response.text)

        try:
            data_list=res_json["data"]['data']['companyWithOfferLists']
            for data in data_list:
                userid=data['factoryInfo']['userId']
                userid_list.append(userid)
                print(userid)
        except Exception as e:
            print('post失败',e)
        time.sleep(3)
    return userid_list
# 获取联系方式id接口
def get_phone(userid):
    url = 'https://h5api.m.1688.com/h5/mtop.alibaba.alisite.cbu.server.pc.moduleasyncservice/1.0/'

    my_token = cookies['_m_h5_tk'][0:32]

    data_c = '{"componentKey":"wp_pc_contactsmall","params":"{\\"memberId\\":\\"'+userid+'\\"}"}'
    params = {
        'jsv': '2.7.0',
        'appKey': '12574478',
        't': '1732593182085',
        'sign': md5(my_token + "&" + '1732593182085' + "&" + '12574478' + "&" + data_c),
        'api': 'mtop.alibaba.alisite.cbu.server.pc.ModuleAsyncService',
        'v': '1.0',
        'type': 'jsonp',
        'valueType': 'string',
        'dataType': 'jsonp',
        'timeout': '10000',
        'callback': 'mtopjsonp1',
        'data': data_c,
    }

    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(response.text)
    res=response.text.replace('mtopjsonp1(','').replace(')','')
    res_json = json.loads(res)

    try:
        phone=res_json['data'].get('mobileNo')

        if (phone==None):
            phone = res_json['data']['phoneNum'].replace(' ','-')
    except Exception as e:
        phone = '暂无联系电话'
        print(e)
    return phone
#获取地址，公司名称，1688url，产品类目
def get_address(userid):
    url = "https://h5api.m.1688.com/h5/mtop.mbox.fc.common.gateway/2.0/"
    data_c = "{\"fcGroup\":\"cbu-seller-fc\",\"fcName\":\"factory-card-common-fn\",\"serviceName\":\"factoryCoreInfoService\",\"params\":\"{\\\"memberId\\\":\\\""+userid+"\\\",\\\"extendParam\\\":{\\\"query\\\":\\\"\\\",\\\"trafficSource\\\":\\\"factory_card@detail_pc\\\"}}\"}"
    params = {
        "jsv": "2.6.1",
        "appKey": "12574478",
        "t": "1732589228863",
        "sign": md5(my_token + "&" + '1732589228863' + "&" + '12574478' + "&" + data_c),
        "v": "2.0",
        "type": "jsonp",
        "isSec": "0",
        "timeout": "5000",
        "api": "mtop.mbox.fc.common.gateway",
        "jsonpIncPrefix": "mboxfc",
        "dataType": "jsonp",
        "callback": "mtopjsonpmboxfc1",
        "data": data_c
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    # print(response.text)
    res = response.text.replace('mtopjsonpmboxfc1(', '').replace(')', '')
    res_json = json.loads(res)
    company_address=res_json['data']['result']['factoryDetailedAddress']
    company_name=res_json['data']['result']['loginId']
    company_url=res_json['data']['result']['shopPcWpIndexUrl']
    company_production=res_json['data']['result']['productionService']
    company_phone=get_phone(userid)
    format_dict={
        "company_address":company_address,
        "company_name":company_name,
        "company_url":company_url,
        "company_production":company_production,
        "company_phone":company_phone
    }
    csv_writer.writerow(format_dict)

    return format_dict


# 主函数
def  final_task():
    userid_list = get_userid(20)
    for i in userid_list:
        get_address(i)
        print(f'userid为{i}的信息写入成功')
        time.sleep(2)

if __name__ == '__main__':
    final_task()