'''
=========================================================    
       @File     : main.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/10 17:49
       @Desc     : 
=========================================================   
'''
from DrissionPage import Chromium,ChromiumOptions
from loguru import logger
import time
import requests
from pathlib import Path
import os
import change_excel

session = requests.Session()
session.trust_env=False
attr_list=[]
img_url_list=[]
# co=ChromiumOptions()
# co.headless()
# co.incognito()
browse=Chromium(5683)
goods_url_list=['https://www.temu.com/-fur-earmuffs-for-men-boho-style-knit-fabric-foldable--ear-covers-g-601099830854595.html']

observer_code=r'''
    //setInterval=function(){};
    setTimeout=function (){};
    (function () {
    // 禁止 window.location 修改

    // 禁用 window.open
    window.open = function () {
        console.log('window.open 被阻止');
        return null;
    };

    // 禁用 form 提交
    document.addEventListener('submit', function (event) {
        event.preventDefault();
        console.log('表单提交被阻止: ', event.target);
    });

    // 移除 Meta Refresh
    document.addEventListener('DOMContentLoaded', () => {
        const metaTags = document.querySelectorAll('meta[http-equiv="refresh"]');
        metaTags.forEach(tag => {
            console.log('Meta Refresh 被移除: ', tag);
            tag.parentNode.removeChild(tag);
        });
    });

    // 禁止 history.pushState 和 history.replaceState
    const originalPushState = history.pushState;
    const originalReplaceState = history.replaceState;

    history.pushState = function (...args) {
        console.log('history.pushState 被阻止: ', args);
    };

    history.replaceState = function (...args) {
        console.log('history.replaceState 被阻止: ', args);
    };
})();
'''
for url in goods_url_list:
    main_tab=browse.new_tab(url)
    main_tab.run_js(observer_code)
    img_eles=main_tab.eles('@class:_3ACovDZO')
    # main_tab.actions.move_to(ele_or_loc=img_eles[0])
    title=main_tab.ele('@class=HZ_BBbqn').attr('aria-label')
    # title=title
    print(title)
    main_tab.actions.move_to(ele_or_loc=img_eles[0]).scroll(4000,0,img_eles[0])#滑动页面触发懒加载
    main_tab.scroll(200)
    to_save_title=title.replace(',','').replace(' ','').replace('&','').replace('.','').replace('*','').replace('"','')
    file_path = Path(f"{to_save_title}")
    txt_path=Path(f"{to_save_title}/商品链接.txt")
    # 自动创建父目录
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    with open(txt_path,'w+',encoding='utf-8') as f:
        f.write(url)
    # 获取图片url
    for index,i in enumerate(img_eles):
        url=i.ele('xpath:/img/@src').replace('180','800')
        # print(url)
        img_url_list.append(url)
        img_path=f'./{to_save_title}/{index}.png'
        with open(img_path,'wb') as f:
            f.write(session.get(url).content)
            f.close()
        print(url+'下载完成')

    try:
        main_tab.ele('xpath://div[@class="_3xcJKtRB"]').click()#点击加载更多，渲染所有属性
        print('已完全加载属性列表')
        # time.sleep(2)
    except:
        print('已完全加载属性列表')
    attr_eles=main_tab.eles('xpath://div[@class="_1YBVObhm"]')#获取属性的元素列表
    key_list=[]
    for i in attr_eles:
        print(i.attr('aria-label').split(':')[0])
        attr_list.append(i.attr('aria-label').split(':')[0])#将属性加入数组中
        key_list.append(i.attr('aria-label').split(':')[1])
    # main_tab.close()
    change_excel.change_excel(attr_list,file_path,key_list)
    time.sleep(3)

