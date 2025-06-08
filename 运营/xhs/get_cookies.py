from playwright.sync_api import sync_playwright
import json
import time
import os

def get_xiaohongshu_cookies():
    """
    使用Playwright获取小红书网站的cookies
    用户需要手动登录，登录成功后脚本会自动提取cookies
    """
    with sync_playwright() as p:
        # 启动浏览器（使用有界面模式，方便用户操作）
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # 访问小红书
        print("正在打开小红书网站，请在打开的浏览器中完成登录操作...")
        page.goto("https://www.xiaohongshu.com/")
        
        # 等待用户手动登录
        print("请在浏览器中登录小红书账号，登录成功后按回车键继续...")
        input()
        
        # 获取所有cookies
        cookies = context.cookies()
        
        # 转换cookies为字典格式
        cookies_dict = {}
        for cookie in cookies:
            cookies_dict[cookie["name"]] = cookie["value"]
        
        # 保存cookies到文件
        with open("xiaohongshu_cookies.json", "w", encoding="utf-8") as f:
            json.dump(cookies_dict, f, ensure_ascii=False, indent=4)
        
        print(f"Cookies已保存到文件: {os.path.abspath('xiaohongshu_cookies.json')}")
        
        # 获取headers中需要的信息
        headers_info = {
            "user-agent": page.evaluate("() => navigator.userAgent"),
            "referer": "https://www.xiaohongshu.com/",
            "origin": "https://www.xiaohongshu.com"
        }
        
        # 保存headers信息到文件
        with open("xiaohongshu_headers.json", "w", encoding="utf-8") as f:
            json.dump(headers_info, f, ensure_ascii=False, indent=4)
        
        print(f"Headers信息已保存到文件: {os.path.abspath('xiaohongshu_headers.json')}")
        
        # 关闭浏览器
        browser.close()
        
        return cookies_dict, headers_info

def load_cookies():
    """
    从文件加载cookies
    """
    try:
        with open("xiaohongshu_cookies.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("未找到cookies文件，请先运行get_xiaohongshu_cookies()获取cookies")
        return None

def load_headers():
    """
    从文件加载headers信息
    """
    try:
        with open("xiaohongshu_headers.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("未找到headers文件，请先运行get_xiaohongshu_cookies()获取headers信息")
        return None

if __name__ == "__main__":
    print("小红书cookies获取工具")
    print("1. 获取新的cookies")
    print("2. 查看已保存的cookies")
    choice = input("请选择操作 (1/2): ")
    
    if choice == "1":
        get_xiaohongshu_cookies()
    elif choice == "2":
        cookies = load_cookies()
        if cookies:
            print("已保存的cookies:")
            print(json.dumps(cookies, ensure_ascii=False, indent=4))
            
            headers = load_headers()
            if headers:
                print("\n已保存的headers信息:")
                print(json.dumps(headers, ensure_ascii=False, indent=4))
    else:
        print("无效的选择")