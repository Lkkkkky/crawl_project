from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import ddddocr
import time
import requests
options = webdriver.ChromeOptions()
options.add_argument("--incognito")


options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
options.add_experimental_option("detach",True)
driver_location = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"

api_url = 'http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=b6840f11b6ca4cb1bf1e6e022eea51f9&orderNo=GL202407171002005Cw0dXVa&count=1&isTxt=1&proxyType=1&returnAccount=1'
#pro=requests.get(api_url)
#proxy=pro.text
# a = browser.find_element(By.XPATH,'/html/body/pre').text
#print(proxy)
#options.add_argument(f'--proxy-server={proxy}') # 添加代理
browser = webdriver.Chrome(service=Service(driver_location), options=options)
# browser.delete_all_cookies()
browser.get('https://ticket.wisdommuseum.cn/reservation/userOut/outSingle/toLoginSingle.do')
print(browser.current_url)
time.sleep(3)
# browser.implicitly_wait(10)
username=browser.find_element(By.ID,"telephone")
username.send_keys("19281057454")
password=browser.find_element(By.ID,"password")
password.send_keys("Kk123456")
ocr = ddddocr.DdddOcr(show_ad = False)
vertify = browser.find_element(By.ID, 'checkNumImage')
vertify.screenshot('test.png')
with open('test.png', 'rb') as f:
    image = f.read()
res = ocr.classification(image)
print('识别出的验证码为：' + res)
code=browser.find_element(By.ID,"code")
code.send_keys(res)
browser.find_element(By.ID,"radio").click()
login=browser.find_element(By.CLASS_NAME,"login-btn")
login.click()
browser.implicitly_wait(10)
# print(browser.current_url)
# windows = browser.window_handles
# print(windows)
# handles=browser.window_handles
# browser.switch_to.window(handles[-1])
# windows = browser.window_handles
# print(windows)
classedit1=browser.find_element(By.XPATH,"/html/body/div/div[3]/div[1]/div[1]/div/div[2]/ul/li/ul/li[1]/a/span")
classedit1.click()
time.sleep(1)
# handles=browser.window_handles
# browser.switch_to.window(handles[-1])
# print(windows)

# print(1)
key=True
browser.refresh()
re1=browser.find_element(By.XPATH,"/html/body/div/div/center/div/p[3]/a")
re1.click()
re2=browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/a[1]")
re2.click()
str1="/html/body/div[1]/div[2]/div/div/div/div/div[2]/table/tbody/tr[3]/td[5]"
while key==True:
    browser.refresh()
    browser.switch_to.frame(0)
    time.sleep(2)
    change=browser.find_element(By.XPATH,str1)  #定位日期
    if 'laydate-disabled' not in change.get_attribute('class'):
        change.click()
        key=False


# print(1)
js= 'arguments[0].class="1"'
# browser.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",change,'class',' ')  使日期可以点击
# change.click()
#//*[@id="Conframe"]      /html/body/div/div[3]/div[1]/div[2]/iframe
# browser.switch_to.frame('Conframe')
#//*[@id="tr26230219"]/td[1]/input 勾选框
# //*[@id="layui-laydate1"]/div/div[2]/table/tbody/tr[2]/td[2]   日期
browser.switch_to.default_content()
browser.switch_to.frame(0)

key1=0
elements = browser.find_elements(By.NAME,'ids')
for element in elements:
    element.click()
    time.sleep(0.1)
for element in elements:
    if element.is_selected()==False:
        key1+=1
if key1==0:
    sub=browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/form/div[5]/input")
    sub.click()

# classedit2=browser.find_element(By.XPATH,"//*[@id='tr26230219']/td[1]/input ")
# classedit2.click()
# classedit3=browser.find_element(By.XPATH,"//*[@id='tr26230222']/td[1]/input ")
# classedit3.click()
# classedit4=browser.find_element(By.XPATH,"//*[@id='tr26230225']/td[1]/input ")
# classedit4.click()
# classedit5=browser.find_element(By.XPATH,"//*[@id='tr26230227']/td[1]/input ")
# classedit5.click()
# classedit6=browser.find_element(By.XPATH,"//*[@id='tr26263695']/td[1]/input ")
# classedit6.click()


