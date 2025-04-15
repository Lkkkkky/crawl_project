'''
=========================================================    
       @File     : 公告监控.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/27 15:15
       @Desc     : 
=========================================================   
'''
import pymysql
import requests
import json
import time

# MySQL 数据库配置
DB_CONFIG = {
        "host": "47.236.198.227",
    "user": "data",
    "password": "data",
    "database": "data",
    "charset": "utf8mb4",
}


# 爬取公告数据的函数
def fetch_notice_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # 假设公告数据为 JSON 格式
        return data.get("noticeList", [])
    else:
        print("Failed to fetch data:", response.status_code)
        return []


# 插入新公告到数据库
def insert_new_notices(db_conn, new_notices):
    with db_conn.cursor() as cursor:
        for notice in new_notices:
            sql = """
            INSERT INTO notices (id, title, classid, url, publish_time)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                notice["id"],
                notice["title"],
                notice["classid"],
                notice["url"],
                notice.get("publish_time", None),
            ))
        db_conn.commit()


# 检查是否有新公告
def check_new_notices(db_conn, notice_list):
    new_notices = []
    with db_conn.cursor() as cursor:
        for notice_class in notice_list:
            for notice in notice_class.get("list", []):
                notice_id = notice.get("id")
                sql = "SELECT COUNT(*) FROM notices WHERE id = %s"
                cursor.execute(sql, (notice_id,))
                if cursor.fetchone()[0] == 0:
                    # 新公告
                    new_notices.append(notice)
    return new_notices


# 主逻辑
def main():
    url = "https://yst-info.zjcaee.com/api/noticeList"  # 替换为实际 API 地址

    # 连接 MySQL 数据库
    db_conn = pymysql.connect(**DB_CONFIG)

    try:
        while True:
            # 爬取公告数据
            notice_data = fetch_notice_data(url)

            # 检查是否有新公告
            new_notices = check_new_notices(db_conn, notice_data)

            if new_notices:
                print(f"发现新公告，共 {len(new_notices)} 条：")
                for notice in new_notices:
                    print(f"- {notice['title']} ({notice['url']})")

                # 插入新公告到数据库
                insert_new_notices(db_conn, new_notices)
            else:
                print("暂无新公告")

            # 设置爬取间隔，避免频繁爬取
            time.sleep(300)  # 每 5 分钟检测一次
    finally:
        db_conn.close()


if __name__ == "__main__":
    main()
