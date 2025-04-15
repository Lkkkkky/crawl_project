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
driver.listen.start({'aweme/v1/web/comment/list/','aweme/v1/web/comment/list/reply/'})
#打开目标网页
driver.get('https://www.douyin.com/discover?modal_id=7330208543905238287')
#点击评论按钮加载评论
driver.ele('@class=Jr187qmx').click()
#等待评论区加载完毕
driver.wait.ele_displayed('xpath://*[@id="merge-all-comment-container"]/div/div[3]')
asd=driver.ele('xpath://*[@id="merge-all-comment-container"]/div/div[3]')
driver.actions.move_to(ele_or_loc=asd)
print(asd)


#更多评论
morecomments_eles=driver.eles('@class=FIKiTPaU')

for page in range(3):
    driver.actions.move_to(ele_or_loc=asd).scroll(4000*page,0,asd)#不知道什么鸡毛逻辑  滑动到底部用不了 只能这样了
    driver.scroll.to_bottom()
    print(f'正在采集第{1+page}页的内容')
    #下滑页面到底部
    driver.scroll.to_bottom()
    #响应数据包加载
    resp=driver.listen.wait()
    # 获取数据包返回的响应数据
    json_data=resp.response.body
    #键值对取值
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
        #数据写入字典中
        csv_writer.writerow(dict)
        print(dict)
        #二级评论
    secend_eles=driver.eles('@class=GyvkCA6n comment-reply-expand-btn')
    more_eles=driver.eles('@class=FIKiTPaU')
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
            csv_writer.writerow(dict)
        #更多评论
            for more in more_eles:
                more.click()
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
                    csv_writer.writerow(dict)

        # driver.listen.set_targets('aweme/v1/web/comment/list/')
        driver.actions.move_to(ele_or_loc=asd).scroll(4000*page,0,asd)


        # driver.listen.start('aweme/v1/web/comment/list/')
        # driver.actions.move_to(ele_or_loc=asd).scroll(1000,0,asd)


        # if driver.wait.ele_displayed('xpath://*[@id="merge-all-comment-container"]/div/div[3]/div[247]')==True:
        #     cheak_is_over=driver.ele('xpath://*[@id="merge-all-comment-container"]/div/div[3]/div[247]')
        #     print(cheak_is_over.html)


        #(20000,0,asd)




