from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import ddddocr
import time
import json
# options = webdriver.ChromeOptions()
# options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
# options.add_experimental_option("detach",True)
# driver_location = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
# browser = webdriver.Chrome(service=Service(driver_location), options=options)
# browser.get('https://h5.gequ.art/#/pages/market/marketGoodsList?id=1015&isagreement=1')
# time.sleep(5)
# browser.find_element(By.XPATH,"//*[@id='container']/uni-view[2]/uni-view[2]/uni-view/uni-view/uni-view/uni-input/div/input").send_keys('17819461984')
# browser.find_element(By.XPATH,"//*[@id='container']/uni-view[2]/uni-view[3]/uni-view[1]/uni-view/uni-view/uni-input/div/input").send_keys('00000000ab')
#browser.find_element(By.XPATH,"//*[@id='container']/uni-view[2]/uni-view[5]/text()").click()

import requests


headers = {
    'Host': 'api.gequ.art',
    'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
    'Content-Type': 'form-data;',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36',
    'Token': '3d97e8db-eca9-4b9d-b4de-2683952ec3c8',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Accept': '*/*',
    'Origin': 'https://h5.gequ.art',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://h5.gequ.art/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Priority': 'u=1, i',
    'Connection': 'close',
}
params = {
    'validate': 'undefined',
}

data = 'K2PbszA5nOJLs3rCOeLKYbmMzekl2THKG7uuS9oSG+8jZ7nGU37XSuL2eO786EaYSYPYGdYzChYZCoBss/UM0k4FBhAL7qMFug0g+BgzMLuldHvsUzAuuY7s2StL/RVZOYwqGK+EI3UWZgSqZnK8vgYyCCtK1xht0Z12C/41lioXOsCTqq3/UBGnzdVHTVOYEU3L/U4v04vWgi3K1d8ZnPdq5/uXcTlQITiFEd8ek/O4riSusYGObq2DGW92zjZkNLPWTl0DD1wUixBLppiGoglS6MWuZRU8tb6bzbN6YqPhy7z/6TJrCggMPwmTwlI7chOQj9OdZ+zloYQfcLpN6A=='

i=1;
def send_wechat(msg): #微信推送
    token = '949dca5369d04791bb71261c17ed2853' #前边复制到那个token
    title = '监控'
    content = msg
    template = 'html'
    topic = '1'
    url = f"http://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}&topic={topic}"
    print(url)
    r = requests.get(url=url)
    print(r.text)

while True:
    response = requests.post('https://api.gequ.art/api/order/pay/fastOrder', params=params, headers=headers, data=data, verify=False)
    print("第"+i.__str__()+"次抢购 "+response.text)
    time.sleep(1)
    if "未找到合适商品"  not in response.text and "访问频繁"  not in response.text:
        send_wechat(拿下)


    i=i+1

# ocr = ddddocr.DdddOcr(show_ad = False)
# vertify = browser.find_element(By.ID, 'checkNumImage')
# vertify.screenshot('test.png')
# with open('test.png', 'rb') as f:
#     image = f.read()
# res = ocr.classification(image)
# print('识别出的验证码为：' + res)
# code=browser.find_element(By.ID,"code")
# code.send_keys(res)
# browser.find_element(By.ID,"radio").click()
# login=browser.find_element(By.CLASS_NAME,"login-btn")
# login.click()




