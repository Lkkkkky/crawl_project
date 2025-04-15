'''
=========================================================    
       @File     : 直播间弹幕.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/12/6 11:33
       @Desc     : 
=========================================================   
'''

import csv

from DrissionPage import Chromium
from loguru import logger



f=open('GetLive.csv','w',encoding='utf-8',newline='')
csv_writer=csv.DictWriter(f,fieldnames=['url','content'])
csv_writer.writeheader()
logger.add('./弹幕采集1.txt',rotation='100 MB',encoding='utf-8')
browse= Chromium(5678)
url = 'https://live.douyin.com/137021126717'
tab=browse.new_tab(url)

tab.console.start()

logger.warning(f'开始监听记录{tab.url}的弹幕')

tab.wait.eles_loaded('.webcast-chatroom___list')
tab.wait(2)

observer_code=r'''

//选择要监控的目标节点
const targetNode=document.querySelector('.webcast-chatroom___list');
//创建一个配置对象，指定要观察的变化类型
const config ={childList: true ,subtree: true};
//创建一个回调函数，当目标节点发生变化时执行
const callback =(mutationsList)=>{
    for(const mutation of mutationsList){
        if(mutation.type === 'childList'){
            mutation.addedNodes.forEach(node =>{
                //检查新增的节点是否是div元素
                if(node.nodeType === Node.ELEMENT_NODE && node.tagName === 'DIV'){
                    const currentTime = new Date().toLocaleTimeString();
                    console.log(`[${currentTime}] ${node.innerText}`);
                }
            });
        }
    }
};
//创建一个MutationObserver 实例
const observer =new MutationObserver(callback);

//开始观察目标节点
observer.observe(targetNode,config);
'''

tab.run_js(observer_code)

while True:
    text=tab.console.wait().text
    if ('%c' not in text and 'byteimg'  not in text):
        csv_writer.writerow({'url':tab.url,'content':text})
    logger.info(tab.console.wait().text)



