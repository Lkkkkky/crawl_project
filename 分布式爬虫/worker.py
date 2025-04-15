'''
=========================================================    
       @File     : worker.py.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/4/16 02:36
       @Desc     : 
=========================================================   
'''
from spider_node import SpiderNode  # 导入爬虫节点类
import sys  # 导入系统模块

if __name__ == "__main__":
    """
    工作节点入口
    """
    if len(sys.argv) < 2:  # 检查是否提供了节点ID参数
        print("Usage: python worker.py <node_id>")  # 打印使用说明
        sys.exit(1)  # 退出程序

    node_id = sys.argv[1]  # 获取节点ID参数
    spider = SpiderNode(node_id)  # 创建爬虫节点实例
    spider.crawl()  # 启动爬取