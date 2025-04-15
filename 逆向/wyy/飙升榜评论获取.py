'''
=========================================================    
       @File     : 飙升榜评论获取.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/11/21 11:51
       @Desc     : 
=========================================================   
'''
import json
import csv
import execjs
import requests

f=open('comment.csv','w',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['user_name','conmment'])
csv_writer.writeheader()

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://music.163.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://music.163.com/discover/toplist",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
cookies = {
    "WM_TID": "izbfXPl6N%2BNBFQEFVRKEsbwcJnGT2k1i",
    "ntes_utid": "tid._.iWpxXyFj%252FY1EV0UFQAOA9axcMjHGjxky._.0",
    "__snaker__id": "gUUfUdn3CE0uF1B0",
    "__root_domain_v": ".163.com",
    "_qddaz": "QD.777228586234557",
    "__csrf": "7b8049a83c76c7a219029617f71ec024",
    "MUSIC_U": "0034F3569E85D0FE7CD8D6713D9EFD159D1BE7AF3B3EDF1FBD8A45F252A85F2F1F307B33AA6DCD9AFA2781B0FED726A2AD34B59E1C5A251EF607505E983474587A36270E2EA9106C653A3E03016043BAA0C7F55FC6B3B7912D88716DD018AC221EB9C3C122373F23CDCACA8A2FB799DD384DAE32D8007F42A31022B8ED61822DF5D8C16EA63907BAE1102369DBD2954B44BB56FA69006462C464B754B46CEC8677524C0BCEFE48DEAE65804BDF4BC2775DE1F59BD783491568D78EB49D12274415629CED190C282DB8A8E1700784523E7EF6A929320E13286282736C94A307431E340B333FF7B42FCE8EF128C9EE6DBA7F536F24025F0859EBE4DF55CCB7168CD3A2B50FC76552746829800F5B21F58EC44AC69112C0ABC7089675CDAE96C51813D390CF47DD06C13D1FB45599310C68331CA6A49829418D0537B2736C4F819096",
    "NMTID": "00OXe-UM4hEZsiCqUNEntS1bcSpmKsAAAGTGi2u9w",
    "__remember_me": "true",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "9dd46e490148fbbd4740a03176d2bd44,1731311023774",
    "_ntes_nuid": "9dd46e490148fbbd4740a03176d2bd44",
    "ntes_kaola_ad": "1",
    "WEVNSM": "1.0.0",
    "WNMCID": "iavzdb.1731311024779.01.0",
    "sDeviceId": "YD-JKvQncebFy5FQwRBVFaU9KxJY3GW3kyB",
    "MUSICIAN_COMPANY_LAST_ENTRY": "1335347100_musician",
    "JSESSIONID-WYYY": "SIlOCmrryqjstm3MPSR8eUtGmXOO1Je1GczaUVrWJgbZqct8ufE2JsTwnJhdQlBjOGUK6bsrvl40iln%2F%2BRyJY5giRtwqB526HY14fcFXQ5K0%5CuyEN1qNZqAyM23Q%2Fw77CivT%2Fb8Q%2B0%5CsAB%5Cx2WCYpN26NRJ%2BKpcj73vU3gUqgEFuJuO0%3A1732161712988",
    "WM_NI": "iEugtL9kB2F1z%2BMOy2xxJrkacgusbicDhbzcud5%2FGyo87dlK0jne92bytMAG4cWpqOsDeSqUpme08wWUVRoVPmW%2F1saYa3YVFFTgMz17IhdUzKx0oyP3wC8Ubk4O%2FMjvdUU%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6eed2c64eaaef9a96c87aa2bc8ab6d45a868a9eb1d25dbb98ffd5d762b0f09c90b22af0fea7c3b92aab9bbb88f748fbb58ed3c53bbaf583b0fc3abca88693ea6ba1b9bb94e163a19ca883f969b7bcfbd0c673ade8f985ef41f4b6a286bc3aa2a7bcaec44df8bd9991f445b19cabb4f45fb4b3abd1bb7d958b9ab3ee5e94b399d0b479a387afd4dc5e869a9c88d072f3e98789e75fba95b8d1ee7394edb9a4bb5fa2b5fcb0ae47aaaaacb6d837e2a3"
}




def get_comment(page,cursor):
    url = "https://music.163.com/weapi/comment/resource/comments/get"
    params = {
        "csrf_token": "7b8049a83c76c7a219029617f71ec024"
    }
    enc_data = execjs.compile(open('wyy.js', 'r', encoding='utf-8').read()).call('get_comment', page,cursor)
    data = {
        "params": enc_data['encText'],
        "encSecKey": enc_data['encSecKey']
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    res_json = json.loads(response.text)
    comments = res_json["data"]["comments"]
    for index in comments:
        conmment = index["content"].replace("\n", "")
        user_name = index["user"]["nickname"]
        print(user_name, ':', conmment)
        format_dict={
            'user_name':user_name,
            'conmment':conmment
        }
        csv_writer.writerow(format_dict)
    new_cursor=res_json["data"]["cursor"]
    return new_cursor


for i in range(1000):
    if (i==0):
        new_c=get_comment(1,'-1')
    else:

        new_c = get_comment(1, new_c)
