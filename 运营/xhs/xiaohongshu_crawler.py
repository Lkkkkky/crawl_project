from playwright.sync_api import sync_playwright
import json
import time
import os
from pathlib import Path
from curl_cffi import requests
from help import sign
from urllib.parse import urlencode,urlparse, parse_qs
import csv
import os
from datetime import datetime
from mimetypes import guess_extension
# 全局变量，用于存储浏览器和页面对象
f= open('comment.csv',mode='w',encoding='utf-8',newline='')
# 字典写入
csv_writer=csv.DictWriter(f,fieldnames=['title','like_count','nickname'])
# 写入表头
csv_writer.writeheader()
browser = None
context = None
page = None
note_list=[]
def init_browser(use_saved_state=True):
    """初始化浏览器，可选择是否使用保存的会话状态"""
    global browser, context, page
    playwright = sync_playwright().start()
    
    # 检查是否存在保存的会话状态文件
    state_file = Path("browser_state.json")
    if use_saved_state and state_file.exists():
        print("正在使用保存的浏览器会话状态...")
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state=str(state_file))
    else:
        print("创建新的浏览器会话...")
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
    
    page = context.new_page()
    return playwright

def get_xiaohongshu_cookies():
    """使用Playwright获取小红书网站的cookies
    用户需要手动登录，登录成功后脚本会自动提取cookies
    """
    global browser, context, page
    
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
    
    # 保存浏览器会话状态
    save_browser_state()
    
    return cookies_dict, headers_info

def load_cookies():
    """从文件加载cookies"""
    try:
        with open("xiaohongshu_cookies.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("未找到cookies文件，请先获取cookies")
        return None

def load_headers():
    """从文件加载headers信息"""
    try:
        with open("xiaohongshu_headers.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("未找到headers文件，请先获取headers信息")
        return None

def get_updated_cookies():
    """获取更新后的cookies，包括动态更新的时间戳"""
    cookies = load_cookies()
    if not cookies:
        return None
    
    # 更新时间戳相关的cookie
    cookies["loadts"] = str(int(time.time()*1000))
    
    return cookies

def get_updated_headers():
    """获取更新后的headers，包括动态更新的时间戳和traceid"""
    headers = load_headers()
    if not headers:
        return None
    
    # 从保存的基本headers开始构建完整headers
    # 添加时间戳
    
    return headers

def save_browser_state():
    """保存浏览器会话状态到文件，以便下次使用"""
    global context
    if context:
        try:
            # 使用Playwright的storage_state方法保存会话状态
            state_file = "browser_state.json"
            context.storage_state(path=state_file)
            print(f"浏览器会话状态已保存到文件: {os.path.abspath(state_file)}")
            return True
        except Exception as e:
            print(f"保存浏览器会话状态失败: {e}")
    return False

def check_cookies_status():
    """检查cookies文件和浏览器会话状态是否存在及其状态"""
    cookies_file = Path("xiaohongshu_cookies.json")
    headers_file = Path("xiaohongshu_headers.json")
    state_file = Path("browser_state.json")
    
    if not cookies_file.exists() or not headers_file.exists():
        return False, "cookies或headers文件不存在，请先获取cookies"
    
    # 检查文件修改时间，判断cookies是否可能过期
    cookies_modified_time = cookies_file.stat().st_mtime
    current_time = time.time()
    days_since_modified = (current_time - cookies_modified_time) / (24 * 3600)
    
    status_message = ""
    if days_since_modified > 7:  # 假设cookies一周后可能过期
        status_message += f"警告：cookies文件已有{days_since_modified:.1f}天未更新，可能已过期\n"
    else:
        status_message += "cookies状态正常\n"
    
    # 检查浏览器会话状态文件
    if state_file.exists():
        state_modified_time = state_file.stat().st_mtime
        days_since_state_modified = (current_time - state_modified_time) / (24 * 3600)
        if days_since_state_modified > 7:  # 假设会话状态一周后可能过期
            status_message += f"警告：浏览器会话状态文件已有{days_since_state_modified:.1f}天未更新，可能已过期"
        else:
            status_message += "浏览器会话状态正常，可以使用保存的登录状态"
    else:
        status_message += "未找到浏览器会话状态文件，将无法使用保存的登录状态"
    
    return True, status_message

def extract_url_params(url):
    parsed = urlparse(url)

    # 提取 note_id
    path_segments = parsed.path.strip("/").split("/")
    note_id = path_segments[1] if len(path_segments) >= 2 and path_segments[0] == "explore" else None

    # 提取查询参数
    query_params = parse_qs(parsed.query)
    params = {
        "note_id": note_id,
        "xsec_token": query_params.get("xsec_token", [""])[0],
        "xsec_source": query_params.get("xsec_source", [""])[0]
    }
    return params

def generate_encryption_params(url,data=None):
    """使用浏览器执行JavaScript生成加密参数"""
    global page
    
    if not page:
        print("浏览器未初始化，无法生成加密参数")
        return None
    
    try:
        # 访问小红书页面确保环境正确
        if not page.url.startswith("https://www.xiaohongshu.com"):
            page.goto("https://www.xiaohongshu.com/")
            time.sleep(2)
        
        # 执行JavaScript代码生成加密参数
        # 注意：这里的JavaScript代码需要根据小红书的实际加密方式进行调整
        encryption_result = page.evaluate("([url, data]) => window._webmsxyw(url,data)", [url, data])
        
        print("成功生成加密参数")
        return encryption_result
    except Exception as e:
        print(f"生成加密参数失败: {e}")
        return None

def get_comments(ori_url,cursor=''):
    """获取小红书笔记的评论"""
    global page
    
    # 检查cookies状态
    status, message = check_cookies_status()
    if not status:
        print(message)
        print("请先获取cookies")
        return
    
    # 获取更新后的cookies和headers
    cookies = get_updated_cookies()
    headers = get_updated_headers()
    
    if not cookies or not headers:
        print("无法获取cookies或headers，请先获取cookies")
        return
    
    # 生成加密参数
    note_params=extract_url_params(ori_url)
    url = "https://edith.xiaohongshu.com/api/sns/web/v2/comment/page"
    params = {
        "note_id": note_params['note_id'],
        "cursor": cursor,
        "top_comment_id": "",
        "image_formats": "jpg,webp,avif",
        "xsec_token": note_params['xsec_token'],
    }
    encryption_params = generate_encryption_params('/api/sns/web/v2/comment/page',params)
    local_storage=page.evaluate("() => window.localStorage")
    signs = sign(
            a1=cookies.get("a1", ""),
            b1=local_storage.get("b1", ""),
            x_s=encryption_params.get("X-s", ""),
            x_t=str(encryption_params.get("X-t", "")),
        )
    headers_ex = {
            "X-S": signs["x-s"],
            "X-T": signs["x-t"],
            "x-S-Common": signs["x-s-common"],
            "X-B3-Traceid": signs["x-b3-traceid"],
        }
    # 补充headers中的必要字段
    headers.update({
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-xray-traceid":'cb599a6471c91cf4468ef13eedb35fa2'
    })
    headers.update(headers_ex)
    # print(headers)
    # 更新cookies中的加密相关字段
    
    # 获取笔记ID
    
    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
        comments = response.get('data', {}).get('comments', [])
        
        print(f"成功获取{len(comments)}条评论")
        
        for comment in comments:
            format_dict = {
                'title': comment.get('content', ''),  # 内容
                'like_count': comment.get('like_count', 0),  # 点赞数
                'nickname': comment.get('user_info', {}).get('nickname', '')  # 昵称
            }
            print(format_dict)
            csv_writer.writerow(format_dict)
            if comment.get('pictures'):
                for image_list in comment.get('pictures'):
                    image_url=image_list.get('url_default', '')#获取图片链接
                    download_image_with_date(image_url, date_format="%Y%m%d_%H%M%S")
            for sub_comment in comment['sub_comments']: #一级评论会自带一个子评论
                    format_dict = {
                        'title': sub_comment.get('content', ''),  # 内容
                        'like_count': sub_comment.get('like_count', 0),  # 点赞数
                        'nickname': sub_comment.get('user_info', {}).get('nickname', '')  # 昵称
                    }
                    print(format_dict)
                    csv_writer.writerow(format_dict)
            if comment.get('sub_comment_has_more')==True: #自带的子评论是否还可展开
                time.sleep(2)
                get_sub_comments(comment.get('note_id', note_params['note_id']), comment.get('id', ''), comment.get('sub_comment_cursor', ''),note_params['xsec_token'])
        if response.get('data').get('has_more')==True: #是否有下一页
            new_cursor = response.get('data', {}).get('cursor', '')
            get_comments(ori_url,new_cursor)
    except Exception as e:
        print(f"获取评论失败: {e}")

def get_sub_comments(note_id, root_comment_id, cursor,xsec_token):
    """获取小红书笔记的二级评论"""
    global page
    
    # 获取更新后的cookies和headers
    cookies = get_updated_cookies()
    headers = get_updated_headers()
    
    if not cookies or not headers:
        print("无法获取cookies或headers，请先获取cookies")
        return
    
    # 生成加密参数
    url = "https://edith.xiaohongshu.com/api/sns/web/v2/comment/sub/page"
    
    uri="/api/sns/web/v2/comment/sub/page"
    params = {
        "note_id": note_id,
        "root_comment_id": root_comment_id,
        "num": "10",
        "cursor": cursor,
        "image_formats": "jpg,webp,avif",
        "top_comment_id": "",
        "xsec_token": xsec_token
    }
    final_uri = f"{uri}?" f"{urlencode(params)}"
    encryption_params = generate_encryption_params(final_uri)
    local_storage=page.evaluate("() => window.localStorage")
    signs = sign(
            a1=cookies.get("a1", ""),
            b1=local_storage.get("b1", ""),
            x_s=encryption_params.get("X-s", ""),
            x_t=str(encryption_params.get("X-t", "")),
        )
    headers_ex = {
            "X-S": signs["x-s"],
            "X-T": signs["x-t"],
            "x-S-Common": signs["x-s-common"],
            "X-B3-Traceid": signs["x-b3-traceid"],
        }
    # 补充headers中的必要字段
    headers.update({
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-xray-traceid": 'cb599a6471c91cf4468ef13eedb35fa2'
    })
    headers.update(headers_ex)
    # print(headers)

    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
        # print(response)
        print(f"获取二级评论成功，共{len(response.get('data', {}).get('comments', []))}条")
        
        comments = response.get('data', {}).get('comments', [])
        for comment in comments:
            format_dict = {
                'title': comment.get('content', ''),  # 内容
                'like_count': comment.get('like_count', 0),  # 点赞数
                'nickname': comment.get('user_info', {}).get('nickname', '')  # 昵称
            }
            csv_writer.writerow(format_dict)
            print(format_dict)
            if comment.get('pictures'):
                for image_list in comment.get('pictures'):
                    image_url = image_list.get('url_default', '')  # 获取图片链接
                    download_image_with_date(image_url, date_format="%Y%m%d_%H%M%S")
        time.sleep(2)
        # 如果还有更多评论，继续获取
        if response.get('data').get('has_more')==True:
            new_sub_cursor = response.get('data', {}).get('cursor', '')
            get_sub_comments(note_id, root_comment_id, new_sub_cursor,xsec_token)
    
    except Exception as e:
        print(f"获取二级评论失败: {e}")

def download_image_with_date(
        url,
        save_dir="images",
        date_format="%Y%m%d_%H%M%S",  # 默认格式：20231025_153045
        include_original_name=False,  # 是否包含原文件名
        avoid_overwrite=True,  # 同名文件追加序号
):
    try:
        os.makedirs(save_dir, exist_ok=True)
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        # 生成基础日期部分
        timestamp = datetime.now().strftime(date_format)

        # 处理原始文件名（可选）
        original_name = ""
        if include_original_name:
            original_name = os.path.splitext(os.path.basename(url))[0]  # 去扩展名
            original_name = f"_{original_name}" if original_name else ""

        # 确定扩展名
        content_type = response.headers.get("Content-Type", "")
        ext = guess_extension(content_type.split(";")[0].strip()) or ".jpg"

        # 组合基础文件名
        base_filename = f"{timestamp}{original_name}{ext}"
        save_path = os.path.join(save_dir, base_filename)

        # 防止文件覆盖（可选）
        if avoid_overwrite:
            counter = 1
            while os.path.exists(save_path):
                name, extension = os.path.splitext(base_filename)
                save_path = os.path.join(save_dir, f"{name}_{counter}{extension}")
                counter += 1

        # 保存文件
        with open(save_path, "wb") as f:
            for chunk in response.iter_content():
                if chunk:
                    f.write(chunk)

        print(f"保存成功: {save_path}")
        return True

    except Exception as e:
        print(f"错误: {str(e)}")
        return False
def search_by_keyword(keyword,num):
    global page

    # 获取更新后的cookies和headers
    cookies = get_updated_cookies()
    headers = get_updated_headers()

    if not cookies or not headers:
        print("无法获取cookies或headers，请先获取cookies")
        return

    # 生成加密参数

    for p in range(1000):
        uri = "/api/sns/web/v1/search/notes"
        params = {
            "keyword": keyword,
            "page": 1,
            "page_size": 20,
            "search_id": "2es86io5294vznurpn6nn",
            "sort": "general",
            "note_type": 0,
            "ext_flags": [],
            "filters": [
                {
                    "tags": [
                        "general"
                    ],
                    "type": "sort_type"
                },
                {
                    "tags": [
                        "不限"
                    ],
                    "type": "filter_note_type"
                },
                {
                    "tags": [
                        "不限"
                    ],
                    "type": "filter_note_time"
                },
                {
                    "tags": [
                        "不限"
                    ],
                    "type": "filter_note_range"
                },
                {
                    "tags": [
                        "不限"
                    ],
                    "type": "filter_pos_distance"
                }
            ],
            "geo": "",
            "image_formats": [
                "jpg",
                "webp",
                "avif"
            ]
        }
        final_uri = f"{uri}?" f"{urlencode(params)}"
        encryption_params = generate_encryption_params(final_uri) #生成headers参数
        local_storage = page.evaluate("() => window.localStorage")
        signs = sign(
            a1=cookies.get("a1", ""),
            b1=local_storage.get("b1", ""),
            x_s=encryption_params.get("X-s", ""),
            x_t=str(encryption_params.get("X-t", "")),
        )
        headers_ex = {
            "X-S": signs["x-s"],
            "X-T": signs["x-t"],
            "x-S-Common": signs["x-s-common"],
            "X-B3-Traceid": signs["x-b3-traceid"],
        }
        # 补充headers中的必要字段
        headers.update({
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "x-xray-traceid": 'cb599a6471c91cf4468ef13eedb35fa2'
        })
        headers.update(headers_ex)
        url = "https://edith.xiaohongshu.com/api/sns/web/v1/search/notes"

        data = json.dumps(params, separators=(',', ':'))
        # try:
        response = requests.post(url, headers=headers, cookies=cookies, data=data).json()
        for item in response.get('data').get('items'):
            note_id = item.get('id')
            xsec_token = item.get('xsec_token')
            if item.get('note_card'):
                format_dict={
                'title':item.get('note_card').get('display_title'),
                'note_id':note_id,
                'xsec_token':xsec_token,
                'url':f'https://www.xiaohongshu.com/explore/{note_id}?xsec_token={xsec_token}&xsec_source=pc_feed'
                }
                print(format_dict)
                note_list.append(format_dict['url'])
                if len(note_list)>=num:
                    return
    # except Exception as e:
    #     print(f"获取笔记列表失败: {e}")
def get_comments_by_search():
    for url in note_list:
        get_comments(url)
def main():
    global browser, context, page
    
    playwright = None
    # try:
    print("小红书评论采集系统")
    print("1. 获取cookies并保持浏览器会话")
    print("2. 根据笔记链接获取评论")
    print("3. 根据关键词获取评论")
    print("4. 检查浏览器会话状态")
    print("5. 退出")

    choice = input("请选择操作 (1/2/3/4/5): ")

    if choice == "1":
        # 初始化浏览器
        playwright = init_browser(use_saved_state=False)
        # 获取cookies
        get_xiaohongshu_cookies()
        print("浏览器会话已保持活跃，可以继续获取评论")

        # 继续操作
        while True:
            print("\n1. 获取评论")
            print("2. 检查cookies状态")
            print("3. 保存浏览器会话状态")
            print("4. 退出")
            sub_choice = input("请选择操作 (1/2/3/4): ")

            if sub_choice == "1":
                ori_url = input("请输入小红书笔记链接,包含xsec_token : ")
                if not ori_url:
                    ori_url = "https://www.xiaohongshu.com/explore/68176b7200000000220249f8?xsec_token=AB6UdqLKmsHM2T4gqBIl2bseRM9uNvOdusuhG8v8LDIFw=&xsec_source=pc_feed"  # 默认ID
                    print(f"使用默认笔记链接: {ori_url}")

                get_comments(ori_url,'')
            elif sub_choice == "2":
                status, message = check_cookies_status()
                print(message)
            elif sub_choice == "3":
                if save_browser_state():
                    print("浏览器会话状态已成功保存，下次启动时将自动使用")
            elif sub_choice == "4":
                print("正在退出...")
                break
            else:
                print("无效的选择")

    elif choice == "2":
        # 检查浏览器是否已初始化
        if not page:
            print("浏览器未初始化，将先初始化浏览器...")
            # 尝试使用保存的会话状态初始化浏览器
            playwright = init_browser(use_saved_state=True)
        # 获取评论
            ori_url = input("请输入小红书笔记链接,包含xsec_token : ")
            if not ori_url:
                ori_url = "https://www.xiaohongshu.com/explore/68176b7200000000220249f8?xsec_token=AB6UdqLKmsHM2T4gqBIl2bseRM9uNvOdusuhG8v8LDIFw=&xsec_source=pc_feed"  # 默认ID
                print(f"使用默认笔记链接: {ori_url}")

            get_comments(ori_url,'')
            print("评论获取完成")
    elif choice == "3":
        if not page:
            print("浏览器未初始化，将先初始化浏览器...")
            # 尝试使用保存的会话状态初始化浏览器
            playwright = init_browser(use_saved_state=True)
            # 获取评论
            key_word = input("请输入关键词: ")
            search_by_keyword(key_word,20)
            print("笔记获取完成")
            get_comments_by_search()
    elif choice == "4":
        # 检查浏览器会话状态文件是否存在
        state_file = Path("browser_state.json")
        if state_file.exists():
            print(f"浏览器会话状态文件存在: {os.path.abspath(state_file)}")
            print(f"文件大小: {state_file.stat().st_size} 字节")
            print(f"最后修改时间: {time.ctime(state_file.stat().st_mtime)}")
            print("下次启动时将自动使用该会话状态")
        else:
            print("未找到浏览器会话状态文件，请先登录并保存会话状态")

    elif choice == "6":
        print("正在退出...")
    elif choice == "7":
        # 检查浏览器是否已初始化
        if not page:
            print("浏览器未初始化，将先初始化浏览器...")
            # 尝试使用保存的会话状态初始化浏览器
            playwright = init_browser(use_saved_state=True)
        # 获取评论
            test('663f67cb000000001e0360c7','66d96d41000000000d01c5de','66eb9e99000000000b022ea9','ABTHAUtzQNry4PfGXRLLz261zLHIMkWWyXvgnl7BDdzbI=')


            print("评论获取完成")
    else:
        print("无效的选择")
    
    # except Exception as e:
    #     print(f"发生错误: {e}")
    
    # finally:
    #     # 清理资源
    #     if browser:
    #         browser.close()
    #     if playwright:
    #         playwright.stop()


def test(note_id, root_comment_id, cursor, xsec_token):
    """获取小红书笔记的二级评论"""
    global page

    # 获取更新后的cookies和headers
    cookies = get_updated_cookies()
    headers = get_updated_headers()

    if not cookies or not headers:
        print("无法获取cookies或headers，请先获取cookies")
        return

    # 生成加密参数
    url = "https://edith.xiaohongshu.com/api/sns/web/v2/comment/sub/page"

    uri = "/api/sns/web/v2/comment/sub/page"
    params = {
        "note_id": note_id,
        "root_comment_id": root_comment_id,
        "num": "10",
        "cursor": cursor,
        "image_formats": "jpg,webp,avif",
        "top_comment_id": "",
        "xsec_token": xsec_token
    }
    final_uri = f"{uri}?" f"{urlencode(params)}"
    encryption_params = generate_encryption_params(final_uri)
    local_storage = page.evaluate("() => window.localStorage")
    signs = sign(
        a1=cookies.get("a1", ""),
        b1=local_storage.get("b1", ""),
        x_s=encryption_params.get("X-s", ""),
        x_t=str(encryption_params.get("X-t", "")),
    )
    headers_ex = {
        "X-S": signs["x-s"],
        "X-T": signs["x-t"],
        "x-S-Common": signs["x-s-common"],
        "X-B3-Traceid": signs["x-b3-traceid"],
    }
    # 补充headers中的必要字段
    headers.update({
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-xray-traceid": 'cb599a6471c91cf4468ef13eedb35fa2'
    })
    headers.update(headers_ex)
    # print(headers)

    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
        print(response)
        print(f"获取二级评论成功，共{len(response.get('data', {}).get('comments', []))}条")

        comments = response.get('data', {}).get('comments', [])
        for comment in comments:
            format_dict = {
                'title': comment.get('content', ''),  # 内容
                'like_count': comment.get('like_count', 0),  # 点赞数
                'nickname': comment.get('user_info', {}).get('nickname', '')  # 昵称
            }
            csv_writer.writerow(format_dict)
            print(format_dict)
            if comment.get('pictures'):
                for image_list in comment.get('pictures'):
                    image_url = image_list.get('url_default', '')  # 获取图片链接
                    download_image_with_date(image_url, date_format="%Y%m%d_%H%M%S")
        time.sleep(2)
        # 如果还有更多评论，继续获取
        if response.get('data').get('has_more') == True:
            new_sub_cursor = response.get('data', {}).get('cursor', '')
            get_sub_comments(note_id, root_comment_id, new_sub_cursor, xsec_token)

    except Exception as e:
        print(f"获取二级评论失败: {e}")

if __name__ == "__main__":
    main()