'''
=========================================================    
       @File     : master.py.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/4/16 02:36
       @Desc     : 
=========================================================   
'''
from url_manager import URLManager  # 导入URL管理器
import time  # 导入时间模块


def main():
    """
    主节点入口函数
    """
    url_manager = URLManager()  # 创建URL管理器实例

    # 添加种子URL
    seed_urls = ["http://example.com", "http://example.org"]  # 示例种子URL
    for url in seed_urls:  # 遍历种子URL
        url_manager.add_new_url(url)  # 添加到待爬队列

    # 监控队列状态
    while True:  # 持续监控
        # 获取待爬队列长度
        waiting_count = url_manager.redis.llen(url_manager.waiting_queue)
        # 获取正在处理集合的大小
        processing_count = url_manager.redis.scard(url_manager.processing_set)
        # 获取已完成集合的大小
        completed_count = url_manager.redis.scard(url_manager.completed_set)

        # 打印队列状态
        print(f"Queue Status - Waiting: {waiting_count}, Processing: {processing_count}, Completed: {completed_count}")
        time.sleep(10)  # 每隔10秒检查一次


if __name__ == "__main__":
    main()  # 启动主节点