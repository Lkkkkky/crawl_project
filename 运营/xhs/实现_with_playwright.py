import time
from curl_cffi import requests
import json

# 导入cookies管理模块
from cookies_manager import get_updated_cookies, get_updated_headers, check_cookies_status

def get_comments():
    """
    获取小红书笔记的评论
    """
    # 检查cookies状态
    status, message = check_cookies_status()
    if not status:
        print(message)
        print("请先运行get_cookies.py获取cookies")
        return
    
    # 获取更新后的cookies和headers
    cookies = get_updated_cookies()
    headers = get_updated_headers()
    
    if not cookies or not headers:
        print("无法获取cookies或headers，请先运行get_cookies.py")
        return
    
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
        "sec-fetch-site": "same-site"
    })
    
    url = "https://edith.xiaohongshu.com/api/sns/web/v2/comment/page"
    params = {
        "note_id": "681c9e37000000002001c41a",
        "cursor": "",
        "top_comment_id": "",
        "image_formats": "jpg,webp,avif",
        "xsec_token": "AB29wqWzcetRQSs_VRJ15XsedSy0NN9FkDtMYmfyFOEjs="
    }
    
    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
        comments = response['data']['comments']
        
        for comment in comments:
            format_dict = {
                'title': comment['content'],  # 内容
                'like_count': comment['like_count'],  # 点赞数
                'nickname': comment['user_info']['nickname']  # 昵称
            }
            print(format_dict)
            
            if comment.get('sub_comment_has_more', False):
                get_sub_comments(comment['note_id'], comment['id'], comment.get('sub_comment_cursor', ''))
    
    except Exception as e:
        print(f"获取评论失败: {e}")

def get_sub_comments(note_id, root_comment_id, cursor):
    """
    获取小红书笔记的二级评论
    """
    # 获取更新后的cookies和headers
    cookies = get_updated_cookies()
    headers = get_updated_headers()
    
    if not cookies or not headers:
        print("无法获取cookies或headers，请先运行get_cookies.py")
        return
    
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
        "sec-fetch-site": "same-site"
    })
    
    url = "https://edith.xiaohongshu.com/api/sns/web/v2/comment/sub/page"
    params = {
        "note_id": note_id,
        "root_comment_id": root_comment_id,
        "num": "10",
        "cursor": cursor,
        "image_formats": "jpg,webp,avif",
        "top_comment_id": "",
        "xsec_token": "AB29wqWzcetRQSs_VRJ15XsedSy0NN9FkDtMYmfyFOEjs="
    }
    
    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
        print(f"获取二级评论成功，共{len(response.get('data', {}).get('comments', []))}条")
        
        comments = response.get('data', {}).get('comments', [])
        for comment in comments:
            format_dict = {
                'title': comment['content'],  # 内容
                'like_count': comment['like_count'],  # 点赞数
                'nickname': comment['user_info']['nickname']  # 昵称
            }
            print(format_dict)
        
        # 如果还有更多评论，继续获取
        if response.get('has_more', False):
            new_sub_cursor = response.get('data', {}).get('cursor', '')
            if new_sub_cursor and new_sub_cursor != cursor:  # 避免无限循环
                get_sub_comments(note_id, root_comment_id, new_sub_cursor)
    
    except Exception as e:
        print(f"获取二级评论失败: {e}")

def main():
    print("小红书评论采集系统")
    print("1. 获取评论")
    print("2. 检查cookies状态")
    choice = input("请选择操作 (1/2): ")
    
    if choice == "1":
        get_comments()
    elif choice == "2":
        status, message = check_cookies_status()
        print(message)
        if not status:
            print("请先运行get_cookies.py获取cookies")
    else:
        print("无效的选择")

if __name__ == "__main__":
    main()