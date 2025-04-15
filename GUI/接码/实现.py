'''
=========================================================    
       @File     : 抢购.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/9 17:26
       @Desc     : 
=========================================================   
'''


import sys
import time
import tkinter as tk
from tkinter import scrolledtext  # 导入滚动文本框的模块
import requests


main=tk.Tk()
main.title('接码')
main.geometry('800x600')

Label_frame=tk.Frame(main)
Label_frame.pack(anchor=tk.W,padx=50,pady=30)
tk.Label(Label_frame,text='账号:',font=('黑体',20)).grid(row=0,column=0)
admin_entry=tk.Entry(Label_frame,font=('黑体',20))
admin_entry.insert(0,'db9d44ce09b33035e60f817d368429e124b49f64671f21ed')
admin_entry.grid(row=0,column=1)
tk.Label(Label_frame,text='密码:',font=('黑体',20)).grid(row=1,column=0)
password_entry=tk.Entry(Label_frame,font=('黑体',20))
password_entry.insert(0,'876bacf58d02fd8080c8fb9a1cb6acb6d473ed0abc06dee8')
password_entry.grid(row=1,column=1)
def get_entry_text():
    admin=admin_entry.get()
    password=password_entry.get()
    response=requests.get(f'https://api.haozhuma.cn/sms/?api=login&user={admin}&pass={password}')
    try :
        token=response.json()['token']
        get_account_info(token)
        
    except Exception as e:
        ternimal_print('登录失败')


# 定义日志输出到tkiner类
class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget
    def write(self, str):
        self.text_widget.insert(tk.END, str)  # 在text末尾追加文字
        self.text_widget.see(tk.END)  # 光标一直追加到文件末尾
        self.text_widget.update()  # 一直更新输出

    def flush(self):
        pass


# 控制台输出函数，输出到t1
def ternimal_print(msg):
    DATE_TIME = time.strftime('[%Y-%m-%d %H:%M:%S]')
    t1.insert('end', f'{DATE_TIME}  {msg}\n')  # 向text文本框末尾追加文字
    t1.see(tk.END)  # 光标一直追加到文件末尾
    t1.update()  # 一直更新输出
button_frame=tk.Frame(main)
tk.Button(button_frame, text='登录',width=10, command=get_entry_text).grid(row=2, column=1)
button_frame.pack(anchor=tk.W,padx=220,pady=10)



def get_account_info(token):
    res=requests.get(f'https://api.haozhuma.cn/sms/?api=getSummary&token={token}')
    # print(res.text)
    money=res.json()['money']
    ternimal_print('登录成功,余额为:'+money)



# 定义Laber组件
# 定义Laber组件
log_frame = tk.Frame(main)
log_frame.pack(anchor='w')
l1 = tk.Label(log_frame, text='程序运行日志：', font=('宋体', 12))
l1.pack(side='left', padx=1, pady=1, ipadx=1, ipady=1)

# 定义滚动文本组件
frm3 = tk.Frame(main)
frm3.pack(anchor='w')
t1 = scrolledtext.ScrolledText(frm3, width=200, height=200, bg='#cfdccf', font=('宋体', 13))
t1.pack(fill='both', side='left', expand=True)

# 启动默认打开帮助页面
sys.stdout = StdoutRedirector(t1)  # 重定向标准输出到t1（日志区域）
# print('欢迎使用，这是测试文字')


main.mainloop()