import hashlib

# 待加密信息

flag='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str = 'this is a md5 Test.'
hl = hashlib.md5()
for i in flag:
    for j in flag:


            str=i+j
            print(str,end=' ')
            hl = hashlib.md5()
            hl.update(str.encode(encoding='utf-8'))
            hl.update(hl.hexdigest().encode(encoding='utf-8'))

            print(hl.hexdigest())



# 创建md5对象


# Tips
# 此处必须声明encode
# 若写法为hl.update(str) 报错为： Unicode-objects must be encoded before hashing


