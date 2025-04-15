'''
=========================================================    
       @File     : API.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/1/6 16:09
       @Desc     :
=========================================================
'''
'''
=========================================================    
       @File     : API.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/27 17:56
       @Desc     : 
=========================================================   
'''
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

import json
import pymysql
from pymysql import cursors
import re
from flask import Flask, jsonify, request
# connection=pymysql.connect( user='goods', password="20030531lky",host='47.236.198.227',database='goods',)
db_config = {
    'host': '47.236.198.227',
    'user': 'goods',
    'password': '20030531lky',
    'database': 'goods',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor  # 使用字典游标以便于转换为JSON
}

# 连接数据库并执行查询

app = Flask(__name__)
CORS(app)

# 创建一个简单的API接口
@app.route('/run-python', methods=['GET'])

def get_products():
    # 获取请求参数
    search_query = request.args.get('keyword', '')
    connection = pymysql.connect(**db_config)
    # 假设你在这里做一些处理，然后返回字典格式的数据
    with connection.cursor() as cursor:
        # 构建SQL查询语句
        query = """
        SELECT * 
        FROM goods_list 
        WHERE good_name LIKE %s 

        """
        # 执行查询
        cursor.execute(query, (f'%{search_query}%'))
        print(search_query)
        results = cursor.fetchall()  # 获取所有匹配的行

        # 将结果转换为JSON格式
        json_results = json.dumps(results, ensure_ascii=False, indent=4)

        # 打印或返回JSON结果
        print(json_results)

        return json_results


if __name__ == '__main__':
    app.run(debug=True)
