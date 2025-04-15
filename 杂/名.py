'''
=========================================================    
       @File     : 名.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/2/13 11:51
       @Desc     : 
=========================================================   
'''
from faker import Faker

# 创建 Faker 实例，并设置为中文
fake = Faker('zh_CN')

# 生成随机中文名字
for _ in range(1000):  # 生成 10 个名字
    name = fake.name()
    print(name)