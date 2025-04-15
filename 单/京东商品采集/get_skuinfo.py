'''
=========================================================    
       @File     : get_skuinfo.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/10/20 02:45
       @Desc     : 
=========================================================   
'''
import requests
import re

from Tools.demo.sortvisu import Array
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "origin": "https://item.jd.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://item.jd.com/",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "x-referer-page": "https://item.jd.com/100120099996.html",
    "x-rp-client": "h5_1.0.0"
}
cookies = {
    "__jdu": "1468058068",
    "shshshfpa": "c273795a-d734-cfaa-ce50-9d031a6538ec-1700461744",
    "shshshfpx": "c273795a-d734-cfaa-ce50-9d031a6538ec-1700461744",
    "areaId": "19",
    "PCSYCityID": "CN_440000_440100_0",
    "user-key": "e2c2f1c9-05f5-4953-b352-b9dad9179828",
    "ipLoc-djd": "19-1601-50258-62836",
    "_pst": "jd_MhNyBaXRXFnl",
    "unick": "lkyyyyyyyyyyy",
    "pin": "jd_MhNyBaXRXFnl",
    "_tp": "LckDemJZ9vjD7CXeUJhnPA%3D%3D",
    "jsavif": "1",
    "mba_muid": "1468058068",
    "unpl": "JF8EAJhnNSttC0kBBhkHTxoQTA0BWwkIHERXPWVXBFVZTFNSH1UbERB7XlVdWBRLFh9sZhRUWVNPUQ4eCisSEXteU11bD00VB2xXVgQFDQ8WUUtBSUt-S1tXV1QOSh4AbGQBZG1bS2QFGjIbFxdCXFBXXA9CJwJfYDVkbVFOUQQZMhoiEXsfAAJZCE0UBCJnAFNUWU9dBBwLKxMgSA",
    "wlfstk_smdl": "0dtj4aw0ivghoahla3qp903amt8aaiia",
    "logintype": "wx",
    "npin": "jd_MhNyBaXRXFnl",
    "thor": "1F63723E3B0B854D9454AB8BE6A4EAB5D6AE0AE74007F05D682072A2346EEFEAEAF1CFAC69D6CAC2B6C9CC46D121347D200BD9B42E299A8CE0D9F1D1A58988557D389C71C8B5DCAF5F8EF14CD71D917A91B8EA3201EB86B930ED0D5940EEB4462517D4762FB1F9F916177E67ECF399634AD4A564AD9721F819B91168A5D02CC624F291418C6DF24150D5FCF86C5CD58EAA729A0FCA8B58C7725EE7F941234DD3",
    "pinId": "8iMjBrpr1TnSWYxYoJoW6g",
    "token": "37bb1a620178e430b7d4a05f57fe88a0,3,960784",
    "__jdv": "229668127|baidu-search|t_262767352_baidusearch|cpc|172887082225_0_b3d234e916ad4e1fbec3ca9066f5f121|1729411331442",
    "3AB9D23F7A4B3C9B": "SHHR7HCVAO4D4OCSDSIWSXEE4MOIEPIUNLGHXXVVANTJVFYEPODQK76V7LLAH4AWCTIWGK2SSONE362YELGJVYGV24",
    "__jda": "181111935.1468058068.1728325094.1729408215.1729410895.13",
    "__jdc": "181111935",
    "mt_xid": "V2_52007VwMXVVRZVlMeThBsBzNWFQVaWgZGG04aWBliUxRWQQhbWk1VEQ8FYQsVAFQKAgodeRpdBmIfElNBW1NLH04SXQxsAxdiX2hSah1JGlUDZwsSUFhfYlkYQA%3D%3D",
    "shshshfpb": "BApXSwUnyq_dAhddKJXMhHnyZ9HSho4k2BkIHEGtg9xJ1MvT02IO2",
    "flash": "3_wMGvdKMJsK0wmIIvy1YXPZERxU71sX1syA0FKBk87FgTHS0P-714rmkreMufbXOQkt1WaSO_HgwDh_rw_o9NQEDAwFiW2qJRGVrHRA0hVD-_OkKqxqShxvJOW6v8mpJzmXgJmY6rz3R9aJLo5MJGEU8HFe8MqH_cXGDoSd2X-3AEHk**",
    "3AB9D23F7A4B3CSS": "jdd03SHHR7HCVAO4D4OCSDSIWSXEE4MOIEPIUNLGHXXVVANTJVFYEPODQK76V7LLAH4AWCTIWGK2SSONE362YELGJVYGV24AAAAMSVD7BAIAAAAAADO64KECQQLCXMAX",
    "_gia_d": "1",
    "__jdb": "181111935.14.1468058068|13.1729410895"
}

arr = [10101480827426,
       100102400164,
       10108443978328,
       100028801866,
       10112130288623,
       100028714785,
       10104365731700,
       100064047572,
       100008892359,
       100079610074,
       10058974326125,
       100058134238,
       10108443829259,
       100097792444,
       10044194995776,
       100068663271,
       10088943088357,
       100063659488,
       1714167,
       100066770117,
       4533173,
       7224900,
       100071851785,
       100052341569,
       5885758,
       10101480827426,
       10119807579329,
       10112130288623,
       1107845,
       10104365731700,
       10093019902950,
       100008892359,
       100085696540,
       10058974326125,
       10092699833581,
       10044194995776,
       10095560622784,
       10088943088357,
       10085669996478,
       1714167,
       10095374084894,
       100015756636,
       10091426143300,
       100075787555,
       100042780499,
       100025393062,
       100078857688,
       100021166736,
       10084686434308,
       10084480043516]
def get_cat_of_sku(skuid):
    url=f'https://item.jd.com/{skuid}.html'
    response = requests.get(url, headers=headers, cookies=cookies)
    sku_cat = re.findall('cat: \[(.*?)\]', response.text)
    sku_venderId=re.findall('venderId:(.*?),', response.text)[0]
    sku_shopId=re.findall('shopId:\'(.*?)\',', response.text)[0]
    # print(response.text)
    # print(response)
    # print(sku_cat)
    return sku_cat,sku_venderId,sku_shopId

cat,sku_venderId,sku_shopId=get_cat_of_sku('1278496')
cat=cat[0].replace("'",'').split(',')

cat=(','.join(cat))
# print(cat,sku_venderId,sku_shopId)


