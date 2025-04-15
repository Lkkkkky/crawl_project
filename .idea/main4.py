def pythonit():
    n = input("请输入一段文本：")
    list_n = list(n)  # 将字符串转换为字符列表
    list_n.reverse()  # 反转列表中的字符
    reversed_n = "".join(list_n)  # 将反转后的字符列表转换回字符串
    print(reversed_n)

pythonit()
str='xxx'
str=str.lower()
print(str)