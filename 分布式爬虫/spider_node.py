'''
=========================================================    
       @File     : spider_node.py.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/4/16 02:36
       @Desc     : 
=========================================================   
'''
import requests  # 用于HTTP请求
from urllib.parse import urlparse  # 用于URL解析
from url_manager import URLManager  # 导入URL管理器
from result_store import ResultStore  # 导入结果存储器


class SpiderNode:
    """
    爬虫节点类，负责实际爬取网页内容
    """

    def __init__(self, node_id):
        """
        初始化爬虫节点
        :param node_id: 节点唯一标识符
        """
        self.node_id = node_id  # 节点ID
        self.url_manager = URLManager()  # 创建URL管理器实例
        self.result_store = ResultStore()  # 创建结果存储器实例

    def crawl(self):
        """
        主爬取方法，持续从队列获取URL并爬取
        """
        while True:  # 持续运行
            url = self.url_manager.get_url()  # 获取一个待爬URL
            if not url:  # 如果没有获取到URL
                print(f"Node {self.node_id}: No more URLs to crawl")  # 打印提示信息
                break  # 退出循环

            try:
                print(f"Node {self.node_id}: Crawling {url}")  # 打印正在爬取的URL
                # 发送HTTP GET请求，设置10秒超时
                response = requests.get(url, timeout=10)
                if response.status_code == 200:  # 如果请求成功
                    # 存储爬取结果
                    self.result_store.store_result(url, response.text)

                    # 从响应内容中提取新的URL
                    new_urls = self.extract_urls(response.text, url)
                    for new_url in new_urls:  # 遍历新URL
                        self.url_manager.add_new_url(new_url)  # 添加到待爬队列

                # 无论成功与否，都标记URL为已完成
                self.url_manager.complete_url(url)

            except Exception as e:  # 捕获所有异常
                print(f"Node {self.node_id}: Error crawling {url} - {str(e)}")  # 打印错误信息
                # 将URL重新放回待爬队列
                self.url_manager.redis.lpush(self.url_manager.waiting_queue, url)
                # 从处理集合中移除该URL
                self.url_manager.redis.srem(self.url_manager.processing_set, url)

    def extract_urls(self, html, base_url):
        """
        从HTML内容中提取URL（需要实现具体逻辑）
        :param html: HTML文本内容
        :param base_url: 基础URL用于解析相对路径
        :return: 提取到的URL列表
        """
        # 这里应该实现实际的URL提取逻辑
        # 示例：使用正则表达式或BeautifulSoup解析HTML提取链接
        # 返回空列表作为示例
        return []