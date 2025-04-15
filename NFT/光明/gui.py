import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import time
import requests
import ddddocr
import json
import 豪猪模块
from loguru import logger
import sys
import os

class RegistrationGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('光明注册程序')
        self.window.geometry('400x500')

        # 创建样式
        style = ttk.Style()
        style.configure('TLabel', padding=5)
        style.configure('TEntry', padding=5)
        style.configure('TButton', padding=5)

        # 创建并布局控件
        ttk.Label(self.window, text='豪猪账号:').pack()
        self.account_entry = ttk.Entry(self.window, width=40)
        self.account_entry.pack()
        self.account_entry.insert(0, 'db9d44ce09b33035e60f817d368429e124b49f64671f21ed')

        ttk.Label(self.window, text='豪猪密钥:').pack()
        self.key_entry = ttk.Entry(self.window, width=40)
        self.key_entry.pack()
        self.key_entry.insert(0, '876bacf58d02fd8080c8fb9a1cb6acb6d473ed0abc06dee8')

        ttk.Label(self.window, text='运行次数:').pack()
        self.count_entry = ttk.Entry(self.window, width=40)
        self.count_entry.pack()
        self.count_entry.insert(0, '500')

        ttk.Label(self.window, text='密码:').pack()
        self.pwd_entry = ttk.Entry(self.window, width=40)
        self.pwd_entry.pack()
        self.pwd_entry.insert(0, '20030531lky')

        # 创建开始按钮
        ttk.Label(self.window, text='姓名:').pack()
        self.name_entry = ttk.Entry(self.window, width=40)
        self.name_entry.pack()
        self.name_entry.insert(0, '李铠阳')

        ttk.Label(self.window, text='身份证号:').pack()
        self.sfz_entry = ttk.Entry(self.window, width=40)
        self.sfz_entry.pack()
        self.sfz_entry.insert(0, '445122200305304715')

        ttk.Label(self.window, text='手机号:').pack()
        self.mobile_entry = ttk.Entry(self.window, width=40)
        self.mobile_entry.pack()
        self.mobile_entry.insert(0, '17819461984')

        # 创建开始按钮和实名按钮
        button_frame = ttk.Frame(self.window)
        button_frame.pack(pady=20)
        
        self.start_button = ttk.Button(button_frame, text='开始运行', command=self.start_registration)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.auth_button = ttk.Button(button_frame, text='实名', command=self.start_auth)
        self.auth_button.pack(side=tk.LEFT, padx=5)

        # 创建日志文本框和滚动条
        log_frame = ttk.Frame(self.window)
        log_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.log_text = tk.Text(log_frame, height=15, width=40)
        scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 配置日志输出到文本框
        logger.remove()
        logger.add(lambda msg: self.update_log(msg), format="{message}")

    def update_log(self, message):
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.see(tk.END)

    def start_registration(self):
        # 获取输入值
        user_account = self.account_entry.get()
        user_key = self.key_entry.get()
        try:
            cnt = int(self.count_entry.get())
        except ValueError:
            messagebox.showerror('错误', '请输入有效的运行次数')
            return

        # 禁用开始按钮
        self.start_button.configure(state='disabled')

        # 在新线程中运行注册程序
        thread = threading.Thread(target=self.run_registration, args=(user_account, user_key, cnt))
        thread.daemon = True
        thread.start()

    def run_registration(self, user_account, user_key, cnt):
        try:
            # 导入注册模块中的所有函数
            from 注册 import get_captcha, sms_send, login, get_captcha_setpwd, sms_send_setpwd, setpwd

            # 获取用户输入的密码
            pwd = self.pwd_entry.get()
            haozhu_token = 豪猪模块.login(user_account, user_key)
            
            # 读取已存在的手机号
            try:
                with open('成功手机号_实名.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()
            except FileNotFoundError:
                lines = []

            for i in range(cnt):
                try:
                    # 注册
                    phone = 豪猪模块.get_phone(haozhu_token, '56080')
                    if phone in lines:
                        logger.info('手机号已存在,重新获取')
                        continue

                    captcha_token, image = get_captcha()
                    sms_send(captcha_token, image, phone)
                    yzm = 豪猪模块.get_yzm(haozhu_token, '56080', phone)
                    login(phone, yzm)

                    # 改密
                    time.sleep(30)
                    豪猪模块.get_phone_zhiding(haozhu_token, '56080', phone)
                    setpwd_captcha_token, setpwd_image = get_captcha_setpwd()
                    sms_send_setpwd(setpwd_captcha_token, setpwd_image, phone)
                    setpwd_yzm = 豪猪模块.get_yzm_no(haozhu_token, '56080', phone)
                    setpwd(setpwd_yzm, phone)
                except Exception as e:
                    logger.error(f'发生错误: {str(e)}')
                    time.sleep(5)

        except Exception as e:
            logger.error(f'程序发生错误: {str(e)}')
        finally:
            # 重新启用开始按钮
            self.window.after(0, lambda: self.start_button.configure(state='normal'))

    def start_auth(self):
        # 获取输入值
        name = self.name_entry.get()
        sfz = self.sfz_entry.get()
        mobile = self.mobile_entry.get()

        # 禁用实名按钮
        self.auth_button.configure(state='disabled')

        # 在新线程中运行实名程序
        thread = threading.Thread(target=self.run_auth)
        thread.daemon = True
        thread.start()

    def run_auth(self):
        try:
            from 实名 import sm
            sm()
            logger.info('实名认证完成')
        except Exception as e:
            logger.error(f'实名认证发生错误: {str(e)}')
        finally:
            # 重新启用实名按钮
            self.window.after(0, lambda: self.auth_button.configure(state='normal'))

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    app = RegistrationGUI()
    app.run()