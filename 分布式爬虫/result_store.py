'''
=========================================================    
       @File     : result_store.py.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/4/16 02:35
       @Desc     : 
=========================================================   
'''
import redis  # 导入redis模块


class ResultStore:
    """
    爬取结果存储类，使用Redis的Hash结构存储爬取结果
    """

    def __init__(self, redis_host='localhost', redis_port=6379):
        """
        初始化结果存储器
        :param redis_host: Redis服务器地址，默认为localhost
        :param redis_port: Redis服务器端口，默认为6379
        """
        # 创建Redis连接
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
        # 结果存储的Hash键名
        self.result_hash = "results:data"

    def store_result(self, url, result_data):
        """
        存储爬取结果
        :param url: 爬取的URL字符串
        :param result_data: 爬取结果内容（通常是HTML文本）
        """
        # 使用Hash结构存储，URL作为field，结果作为value
        self.redis.hset(self.result_hash, url, result_data)

    def get_result(self, url):
        """
        获取指定URL的爬取结果
        :param url: 要查询的URL字符串
        :return: 爬取结果内容或None（如果不存在）
        """
        # 从Hash中获取指定URL的结果
        return self.redis.hget(self.result_hash, url)