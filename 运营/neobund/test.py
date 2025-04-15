'''
=========================================================    
       @File     : test.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/1/2 09:58
       @Desc     : 
=========================================================   
'''
import requests
import re

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "_ga": "GA1.1.298371489.1733880376",
    "vuex": "{%22user%22:{%22userId%22:null%2C%22nickName%22:null%2C%22userAvatar%22:null%2C%22token%22:null%2C%22levelType%22:null%2C%22balance%22:0%2C%22unReadNotices%22:0%2C%22pageLoading%22:false%2C%22pageSize%22:10%2C%22payList%22:[]%2C%22tz%22:%22US%22%2C%22authTips%22:false%2C%22isOpenNbs%22:1%2C%22userEmail%22:null}}",
    "_ga_CP3T51ZM9M": "GS1.1.1735780783.17.1.1735781531.0.0.0"
}
url = "https://mall.neobund.com/detail/3794"
response = requests.get(url, headers=headers, cookies=cookies)
if response.status_code == 200:
    # 提取 HTML 内容
    html_content = response.text

    # 使用正则表达式匹配指定内容
    # 匹配以 "(null," 开头，以 ");" 结尾的内容
    pattern = r"jpg\",.*?\"en\"\)"
    matches = re.findall(pattern, html_content)

    # 输出匹配的内容
    if matches:
        for match in matches:
            match=match.strip('()')
            result=[item.strip() for item in match.split(',"')]
            for index,i in enumerate(result):
                if "+1 " in i and len(i)<17:
                    print(i)
                    print(result[index+1])
            print(result)
    else:
        print("未找到匹配内容")
else:
    print(f"请求失败，状态码: {response.status_code}")
print(len('+1 909 319 3819"'))