'''
=========================================================    
       @File     : execl提取爱企查查询.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/11 09:56
       @Desc     : 
=========================================================   
'''
import pandas as pd
import time
import csv
import requests
import re
import json
# 读取 Excel 文件
file_path = '全国跨境卖家数据-TK已筛选250108.xlsx'  # 替换为你的 Excel 文件路径
sheet_name = '跨境总表'  # 替换为你要读取的工作表名称
df = pd.read_excel(file_path, sheet_name=sheet_name)


# 提取前 1000 行数据
first_1000_rows = df.head(1000)  # 方法 1：使用 head() 方法
# 或者
# first_1000_rows = df.iloc[:1000]  # 方法 2：使用切片操作

# 如果需要将数据转换为数组（例如提取某一列）
first_column_array = first_1000_rows.iloc[:, 4].values  # 提取第一列并转换为数组

# 打印前 1000 行数据


# 打印第一列的数组

f=open('天眼查.csv','w',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['查询关键词','name','base','regLocation','phoneList','alias'])
csv_writer.writeheader()

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.tianyancha.com/login?from=%2Fsearch%3Fkey%3D%25E9%259E%258D%25E5%25B1%25B1%25E5%2585%25A8%25E4%25BA%258B%25E5%25A5%25BD",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Microsoft Edge\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "TYCID": "fb562c70733e11efaf3d9f3cb0cb3e6b",
    "CUID": "896180ecfaa6240e13f9370db34653eb",
    "ssuid": "3183649984",
    "_ga": "GA1.2.332962379.1726389985",
    "HWWAFSESTIME": "1739238896611",
    "HWWAFSESID": "39389fd44c1cf1f332",
    "csrfToken": "ay_NwvEaOAHZal6vbgAzivq5",
    "jsid": "SEO-BING-ALL-SY-000001",
    "Hm_lvt_e92c8d65d92d534b0fc290df538b4758": "1737705825,1739238904",
    "HMACCOUNT": "4D4F61CE5656C745",
    "bannerFlag": "true",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2215329814%22%2C%22first_id%22%3A%22191f4dc9b07a67-03908a380bcc96e-4c657b58-2073600-191f4dc9b08541%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxZjRkYzliMDdhNjctMDM5MDhhMzgwYmNjOTZlLTRjNjU3YjU4LTIwNzM2MDAtMTkxZjRkYzliMDg1NDEiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxNTMyOTgxNCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2215329814%22%7D%2C%22%24device_id%22%3A%22191f4dc9b07a67-03908a380bcc96e-4c657b58-2073600-191f4dc9b08541%22%7D",
    "_gid": "GA1.2.793565328.1739240711",
    "_gat_gtag_UA_123487620_1": "1",
    "searchSessionId": "1739240720.09025358",
    "Hm_lpvt_e92c8d65d92d534b0fc290df538b4758": "1739240722",
    "tyc-user-info": "{%22state%22:%223%22%2C%22vipManager%22:%220%22%2C%22mobile%22:%2215804611107%22%2C%22userId%22:%2215329814%22%2C%22isExpired%22:%220%22}",
    "tyc-user-info-save-time": "1739240744841",
    "auth_token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTgwNDYxMTEwNyIsImlhdCI6MTczOTI0MDc0MiwiZXhwIjoxNzQxODMyNzQyfQ.FbqaN9zJWUY8fpS6HbRwBAYX260gylDOrfR8u1m_jNGv9MVQJgp42Cqd12OGWS7zeHv3Qvzt-c66WtXDvIfc7A",
    "tyc-user-phone": "%255B%252215804611107%2522%252C%2522134%25203789%25201003%2522%255D"
}

url = "https://www.tianyancha.com/nsearch"
def get_info(keyword):
    params = {
        "key": keyword
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    res=re.findall("<script id=\"__NEXT_DATA__\" type=\"application/json\">(.*?)</script>",response.text)[0]
    res_json=json.loads(res)
    # print(response.text)
    companyList=res_json['props']['pageProps']['dehydratedState']['queries'][2]['state']['data']['data']['companyList']
    for i in companyList:
        try:
            name=i.get('name').replace('<em>', '').replace('</em>', '')
        except:
            name=i.get('name')
        base=i.get('base')
        loc=i.get('regLocation')
        phonelist=i.get('phoneList')
        try:
            alias=i['multiMatchField'][0]['content'].replace('<em>', '').replace('</em>', '')
        except:
            alias='暂无'
        format_dict={
            '查询关键词':keyword,
            'name':name,
            'base':base,
            'regLocation':loc,
            'phoneList':phonelist,
            'alias':alias,
        }
        print(format_dict)
        csv_writer.writerow(format_dict)
    # print(res_json.get('props.pageProps.dehydratedState.queries[2].state.data.data.companyList'))

for key in first_column_array:
    print(key)
    get_info(key)
    time.sleep(15)