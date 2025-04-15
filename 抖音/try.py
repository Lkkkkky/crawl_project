import  datetime
from DrissionPage import ChromiumPage
import csv
#创建文件对象
f= open('data.csv',mode='w',encoding='utf-8',newline='')
#字典写入
csv_writer=csv.DictWriter(f,fieldnames=['昵称','评论时间','地区','评论内容'])
#写入表头
csv_writer.writeheader()
#创建浏览器对象
driver=ChromiumPage()
#监听数据包
driver.listen.start('aweme/v1/web/comment/list/')
#打开目标网页
driver.get('https://www.douyin.com/discover?modal_id=7330208543905238287')
#点击评论按钮加载评论
driver.ele('@class=Jr187qmx').click()
resp=driver.listen.wait()

json_data=resp.response.body
print(json_data['comments'])
#等待评论区加载完毕
driver.wait.ele_displayed('xpath://*[@id="merge-all-comment-container"]/div/div[3]')
asd=driver.ele('xpath://*[@id="merge-all-comment-container"]/div/div[3]')
driver.actions.move_to(ele_or_loc=asd)
driver.listen.start('aweme/v1/web/comment/list/reply/')
secend_eles=driver.eles('@class=GyvkCA6n comment-reply-expand-btn')
for each in secend_eles:
    each.click()
    resp=driver.listen.wait()
    json_data=resp.response.body
    comments=json_data['comments']
    for index in comments:
        text=index['text']#评论内容
        nickname=index['user']['nickname']#昵称
        comtime=index['create_time']#评论时间
        area=index['ip_label']#地区
        date = str(datetime.datetime.fromtimestamp(comtime))
        dict={
            '昵称':nickname,
            '评论时间':date,
            '地区':area,
            '评论内容':text
        }
        print(dict)


