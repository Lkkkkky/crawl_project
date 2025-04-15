import requests
from collections import Counter

class firstHeaders:
    def items(self):
        headers = {
            "Content-Length": "0",
            "Sec-Ch-Ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Sec-Ch-Ua-Platform": "Windows",
            "Accept": "*/*",
            "Origin": "https://match.yuanrenxue.cn",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://match.yuanrenxue.cn/match/3",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1716902967; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1717295263,1717314335; tk=-8838488315772654498; sessionid=t2ivk05m79d9oxqxutbcynikyeb93u88; m=7d8915425233260fbbc811c253bdc577|1717314348000; Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1717311666,1717314893; Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3=1717314893; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1717314899; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1717334940"

        }
        return ((k,v) for k,v in headers.items())

def firstRequests():
    """获取：JSSM的sessionid"""
    url = "https://match.yuanrenxue.cn/jssm"
    response = requests.post(url, headers=firstHeaders(), verify=False)
    cookies = {
        "sessionid": response.cookies.get("sessionid")
    }
    return cookies

class secondHeaders:
    def items(self):
        headers = {
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": "Windows",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://match.yuanrenxue.cn/match/3",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        return ((k,v) for k,v in headers.items())

def secondRequests(cookies, page):
    url = "https://match.yuanrenxue.cn/api/match/3?page={}".format(page)
    response = requests.get(url, headers=secondHeaders(), cookies=cookies)
    return response.json()['data']


if __name__ == '__main__':
    calculate_num = []
    for page in range(1, 6):
        cookies = firstRequests()
        data_row = secondRequests(cookies, page)
        print(data_row)
        for row in data_row:
            val = row['value']
            calculate_num.append(val)
    top = Counter(calculate_num).most_common(1)[0]
    print(top)