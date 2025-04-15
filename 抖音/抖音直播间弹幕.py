import time  # 事件库，用于硬性等待
import threading
from bs4 import BeautifulSoup
from selenium import webdriver  # 导入selenium的webdriver模块
from selenium.webdriver.chrome.service import Service

live_dy_url = 'https://live.douyin.com/xxxxxxxxx'  # 直播间链接
crawling_browser_dy = None  # 浏览器
comment_list = []  # 评论列表

# 打开直播间浏览器
def init_crawling_browser_dy(url):
    global crawling_browser_dy
    service = Service('./chromedriver.exe')
    options = webdriver.ChromeOptions()
    # 无头模式
    # options.add_argument('--headless')
    options.add_experimental_option('detach', True)
    # 忽略证书错误
    options.add_argument('--ignore-certificate-errors')
    # 忽略 Bluetooth: bluetooth_adapter_winrt.cc:1075 Getting Default Adapter failed. 错误
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 忽略 DevTools listening on ws://127.0.0.1... 提示
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    crawling_browser_dy = webdriver.Chrome(options=options,service=service)
    crawling_browser_dy.get('https://live.douyin.com/')  # 抖音直播主页
    crawling_browser_dy.maximize_window()  # 浏览器全屏
    time.sleep(3)  # 等待3s
    crawling_browser_dy.get(url)  # 跳转到直播间链接
    threading.Timer(10, get_comment_list, args=()).start()  # 执行：10s

# 获取html标签中的评论文本
def get_comment_list():
    global comment_list ,crawling_browser_dy
    try:
        content_dy = crawling_browser_dy.page_source
        soup_dy = BeautifulSoup(content_dy, 'html.parser')
        # 找到评论的class名称
        items_dy = soup_dy.find_all(class_='webcast-chatroom___xxx webcast-chatroom___xxx')  # 元素xpath已被篡改，代码仅供学习参考使用
        for item in items_dy[-5:]:  # 获取最新的5条评论
            text = item.text.split('：')[1] if item.text.count('：') > 0 else item.text
            comment_list .append(text)
        print(comment_list)  # 打印评论列表
        comment_list.clear()
        threading.Timer(10, get_comment_list, args=()).start()  # 重复执行：10s
    except:
        print('抖音自动化测试浏览器：未找到弹幕标签,请查看直播链接是否已结束或异常关闭')

init_crawling_browser_dy(live_dy_url)
