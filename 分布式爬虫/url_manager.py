'''
=========================================================    
       @File     : url_manager.py.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/4/16 02:35
       @Desc     : 
=========================================================   
'''
import redis  # 导入redis模块


class URLManager:
    """
    URL管理器类，负责管理待爬取、正在爬取和已完成的URL
    使用Redis作为后端存储
    """

    def __init__(self, redis_host='localhost', redis_port=6379):
        """
        初始化URL管理器
        :param redis_host: Redis服务器地址，默认为localhost
        :param redis_port: Redis服务器端口，默认为6379
        """
        # 创建Redis连接
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
        # 待爬取URL队列的键名
        self.waiting_queue = "urls:waiting"
        # 正在处理URL集合的键名
        self.processing_set = "urls:processing"
        # 已完成URL集合的键名
        self.completed_set = "urls:completed"

    def add_new_url(self, url):
        """
        添加新URL到待爬队列
        :param url: 要添加的URL字符串
        """
        # 检查URL是否已经在完成集合中
        if not self.redis.sismember(self.completed_set, url):
            # 如果不在，则添加到待爬队列头部
            self.redis.lpush(self.waiting_queue, url)

    def get_url(self):
        """
        从待爬队列获取一个URL，并将其移动到处理集合
        :return: URL字符串或None（如果没有待爬URL）
        """
        # 使用rpoplpush原子操作从待爬队列尾部取出URL并放入处理集合
        url = self.redis.rpoplpush(self.waiting_queue, self.processing_set)
        # 如果获取到URL，解码后返回；否则返回None
        return url.decode() if url else None

    def complete_url(self, url):
        """
        标记URL为已完成
        :param url: 已完成的URL字符串
        """
        # 将URL添加到已完成集合
        self.redis.sadd(self.completed_set, url)
        # 从处理集合中移除该URL
        self.redis.srem(self.processing_set, url)

    def is_duplicate(self, url):
        """
        检查URL是否已爬取（是否在已完成集合中）
        :param url: 要检查的URL字符串
        :return: 布尔值，True表示已存在
        """
        return self.redis.sismember(self.completed_set, url)