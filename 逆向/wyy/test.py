import json
import threading
import time
import requests
import execjs
import csv
import pandas
# 创建文本对象
f= open('song.csv',mode='w',encoding='utf-8',newline='')
# 字典写入
csv_writer=csv.DictWriter(f,fieldnames=['歌曲名','时长','作者','专辑'])
# 写入表头
csv_writer.writeheader()
# 调用js文件加密参数
f=open('wyy.js','r').read()
js=execjs.compile(f)
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://music.163.com/my/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Cookie': 'NMTID=00OD4cbMMG4R0xXWEzDrJtX5-CzSxwAAAGM4lSHOg; WEVNSM=1.0.0; WNMCID=wibzgw.1704604240657.01.0; __snaker__id=FTkkOrQgZt0UJaYo; WM_TID=izbfXPl6N%2BNBFQEFVRKEsbwcJnGT2k1i; sDeviceId=YD-ntboOPfGnWhARhAFUBOBpbgJMzTG4G8K; ntes_utid=tid._.iWpxXyFj%252FY1EV0UFQAOA9axcMjHGjxky._.0; ntes_kaola_ad=1; __root_domain_v=.163.com; _qddaz=QD.386523510729330; __csrf=137714bbad7460e994f08267dcc0cd34; _ntes_nnid=545690a39082e3fb24ac8bdb668f8f03,1723669295739; _ntes_nuid=545690a39082e3fb24ac8bdb668f8f03; _iuqxldmzr_=32; gdxidpyhxdE=2i4x2yYQ89N6U%5CiO5XR92Mxik8liuH6YTmWn%2BGEgcNTy6MJXp8iPkGUOH%5CXP25OS3qcubnnwPOVB4r%5CCRZUPlC%5CgZQQQtAw5Ij5xiC1kig%2FGXNa%2BVgpQRk3o%2B%2FZaPeCnCBSbkxeMrY3KvzBQGxeu3hPTp6Z4jq7WPT3MCgVu%2FAYd0ztd%3A1724088436247; MUSIC_U=00C21CE6741D5DB8E670E77B8A5BB4504F7FE16B19916EBE9CDD134CFA536B1F87D1A2FA5F9DA8120C9E36517A82AA9CAAF9E998599657C9EB2941D7F20FF88B97681687B22584B3DC43B75A10FC94927600E25EDD87F66E887FC4050B54798359D807293BEAF380286BAA70424EF984A0AC156FED3D0DBB4FE81E63C6F6D2509774E4111862FBCC7AD0CB6634A665A173BFE3D212652D48B6E5D00BF468952D9D753F6D11B531F7AC751C287438207BDAE0BCAB82667070DF6B330829F530D5ACE35B59D7AE042C2BD243CBD9167788D9C686D2D60D6A23718245B4FDB1EC78019C7584DCB326FC2482CD858AB141E794F58BA08B24DB1975DEB112FF681C79F9A6534EC6E8A790BD6281654F987C89E80F0BFB129F4D5865B477369E8AB3EBA45A6DB64E4C4DB68A3C421F3313B0A76852F1261346D0381ECA56238A57384B90A4F44439A2EF0A28D7A4DBF6BFCA1287BBE27A3B931E6F04E2DAD132235B85A8; __remember_me=true; WM_NI=mNPtX4CSNlEdNRa0dGPm%2FLCWMub6jg%2FMjhafxctrc%2FgZxA2kBqFeWIPewYbEg4MT%2B14z6SRWHdVJIc0L9VyicaMoIt7qfADfVFgn1hsl0MDk5mWUgRzXcwRUuhXXVJFRaU8%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee87d480aabe0095d35ca9ef8bb2c14b929f9f86c75eaff1b9a9b350a3b682d5bc2af0fea7c3b92aaf92a095db40818d828dc8708e8eafd1e74d94b3e1adc25d8fabaed7e96ded93a689e46ebcbdbc93e225a586b8a2b16182af8a86d64394bbb9bae14fa5ec83b5aa3bf8a6fab4d15d8cbc9aabcc69f494f7b7fc63a1bf8390cc80f5afaaa2c76e969aa98fb464b1b400aec761f7b399b6e65aba88ad98d15fb7b898b9d542868eafb6bb37e2a3; JSESSIONID-WYYY=CzqjJPeVymdyQKb9M9ADCVy0eM77BKAGtNKNzxBnsxAJVqFitFn1iAHeeDFm7HFuY46xq35VITPIYnPYpE4beg6zaquiQ6cty%2FSFZfjMMA%5CCWVI%2F5Z0P%2FViYCi6dD0hbYH%2FbdPWRKgY4aVh1mrVv2uOxPCKqslgH4%5CfyvhHYW5eRz%5C7c%3A1724369705001',
    'content-type': 'application/x-www-form-urlencoded',
    'Host': 'music.163.com',
    'Connection': 'keep-alive'
}
# 获取歌单列表,取uid
def get_playlist():
    playlist_key=js.call('getlist_payload',1335347100)
    playlist_data = {
        "params": playlist_key['encText'],
        "encSecKey": playlist_key['encSecKey']
    }
    # 获取所有歌单信息
    playlist_res=requests.post(url_getlist,headers=headers,data=playlist_data)
    # 转json格式
    playlist_res_json=json.loads(playlist_res.text)
    # print(playlist_res_json)
    format_list_dict={}
    i=0
    for index in playlist_res_json['playlist']:
        # 判断是自己创建的歌单还是收藏的歌单  只有自己创建的才投入后续使用
        if index['subscribed']==False:

            format_list_dict.update({i:index['id']})
            i=i+1
                    # '歌曲时长':(index['dt']/1000)


    return format_list_dict
url_getlist = "https://music.163.com/weapi/user/playlist?csrf_token=137714bbad7460e994f08267dcc0cd34"

# 获取单个歌单内容
url_getsong = "https://music.163.com/weapi/v6/playlist/detail?csrf_token=137714bbad7460e994f08267dcc0cd34"


#填写歌单id
def get_song(listid):
    # id=12443218002  int
    getsong_key=js.call('getsong_payload',listid)
    print(getsong_key)
    data = {
        "params": getsong_key['encText'],
        "encSecKey": getsong_key['encSecKey']
    }
    res = requests.request("POST", url_getsong, headers=headers, data=data)
    res_dict=json.loads(res.text)
    song_dict=res_dict['playlist']['tracks']
    for index in song_dict:
        #计算歌曲时长
        duration=index['dt']/1000
        min=int(duration/60)
        sec=int(duration%60)
        format_duration=f'{min}:{sec}'
        format_dict={
            '歌曲名':index['name'],
            '作者':index['ar'][0]['name'],
            '时长':format_duration,
            '专辑':index['al']['name']

            # '歌曲时长':(index['dt']/1000)
        }
        #写入文件
        print(format_dict)
        csv_writer.writerow(format_dict)
# 根据用户id获取用户歌单id列表
songlist=get_playlist()
print(songlist)

#
# def task(songlist):
#     for index in songlist:
#         get_song(songlist[index])
#         time.sleep(5)
threadinglist=[]
threadnum=26
for i in range(threadnum):
    t=threading.Thread(target=get_song, args=(songlist[i],))
    threadinglist.append(t)
    t.start()
# for index in songlist:
#     get_song(songlist[index])
#     time.sleep(5)
    # r=pandas.read_csv('song.csv')
    # r.to_excel('song.xlsx')



