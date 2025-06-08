# 小红书评论采集系统

这是一个使用Playwright自动获取小红书cookies并采集评论的系统。系统可以采集一级评论和二级评论，解决了二级评论采集时cookies加密参数的问题。

## 功能特点

- 使用Playwright自动获取小红书cookies
- 自动更新cookies中的时间戳等动态参数
- 支持一级评论和二级评论的采集
- 检测cookies状态，提醒用户及时更新

## 安装依赖

在使用本系统前，请先安装必要的依赖：

```bash
pip install playwright curl-cffi
python -m playwright install chromium
```

## 使用方法

### 1. 获取cookies

首先需要运行`get_cookies.py`脚本获取小红书的cookies：

```bash
python get_cookies.py
```

运行后会打开浏览器，请在浏览器中手动登录小红书账号。登录成功后，按回车键继续，系统会自动提取cookies并保存到文件中。

### 2. 采集评论

获取cookies后，可以运行`实现_with_playwright.py`脚本采集评论：

```bash
python 实现_with_playwright.py
```

选择"1. 获取评论"选项开始采集评论。

### 3. 检查cookies状态

如果采集过程中出现问题，可以检查cookies状态：

```bash
python cookies_manager.py
```

或者在`实现_with_playwright.py`中选择"2. 检查cookies状态"选项。

## 文件说明

- `get_cookies.py`: 使用Playwright获取小红书cookies的脚本
- `cookies_manager.py`: cookies管理模块，提供cookies的加载、更新和状态检查功能
- `实现_with_playwright.py`: 使用Playwright获取的cookies采集评论的主程序
- `实现.py`: 原始的评论采集程序（不使用Playwright）

## 注意事项

1. cookies有效期有限，如果采集失败，请重新运行`get_cookies.py`获取最新的cookies
2. 系统会自动检测cookies的状态，如果cookies可能已过期，会给出提示
3. 采集过程中请遵守小红书的使用条款，不要频繁请求以避免被封禁
4. 本系统仅供学习和研究使用，请勿用于商业目的