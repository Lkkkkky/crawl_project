import  hashlib
import json
import time
from random import random, randint

from exceptiongroup import catch
from loguru import logger
import get_skuinfo


def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

import requests
import geth5st
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://item.jd.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://item.jd.com/",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "x-referer-page": "https://item.jd.com/1278496.html",
    "x-rp-client": "h5_1.0.0"
}
cookies = {
    "__jdu": "369041817",
    "shshshfpa": "0315a5f6-560b-3b6f-4a4f-e530675a58cd-1728735584",
    "shshshfpx": "0315a5f6-560b-3b6f-4a4f-e530675a58cd-1728735584",
    "areaId": "19",
    "PCSYCityID": "CN_440000_440100_0",
    "unpl": "JF8EAJhnNSttURlXUksFHxBDQlRRW1hfGEcCaTBVXQ1YSAYDElJOGkJ7XlVdWBRLFx9uYxRVXVNIVw4aAysSEXteU11bD00VB2xXVgQFDQ8WUUtBSUt-S1tXV1QOSh4AbGYDZG1bS2QFGjIZFRhKWFRXXQ57FjNoVzVkWFxCUAAYMhoiEXsfAAJVDEoQBmsqB1NVWU5UDBsEKxMgSA",
    "__jdv": "229668127|baidu-search|t_262767352_baidusearch|cpc|172887082207_0_8c2fa653b88444fba07fa8a12c78ad9c|1730740923879",
    "user-key": "3e92f6a9-cddc-463e-a67d-62539d0d757c",
    "_pst": "jd_sxwTrEZKeSVD",
    "unick": "jd_dr0vl2t52nre8n",
    "pin": "jd_sxwTrEZKeSVD",
    "_tp": "%2BKOvDtuzURMmdODDXI03ZQ%3D%3D",
    "ipLocation": "%u5317%u4eac",
    "cn": "0",
    "ipLoc-djd": "1-2800-55815-0.1986021178",
    "umc_count": "1",
    "mt_xid": "V2_52007VwEVWlxdUlMfTykOBWRQFFBaDE4NHBpNQABuABROVF4CDwNNHl8MY1YaUlkPBlIvShhfAHsDEk5cX0NbH0IcWA5mAiJQbVhiXh9JEV8GZgsVVm1dU1MZ",
    "jsavif": "1",
    "wlfstk_smdl": "26gf5noxw1xym6wrnycwmdw4kufkor7r",
    "3AB9D23F7A4B3C9B": "IP7ZOEW6HMAOR2YF23KYRWMTUEY6WE6YJCO4HO45KAOUDW75RJ6AXP3E73LX34Z3DYL6ZVYZKZQ2OLMLEB35CY63C4",
    "logintype": "wx",
    "npin": "jd_sxwTrEZKeSVD",
    "thor": "36B194B8495F9E3A641132CA8FEC5CACD9EC9AA9E4C125769E06FA89DF9503176744FFF9B113ECD19B04FF3CF850FED1E3FE7E5368CAA9447AA5CFFE8471B869AF10BC4C854B403734C5B9647FD8DE3255CCF596D292231AC694BBBA37E28A74FE0D9BFAB9248E6DDD1107D244187041DF10C0B416DD81EF1755F93F33DC95270013E4609FADC01776F9D59623DCDC6AE6C2A08AFB9E97FE53B53F07D50572F1",
    "pinId": "RLpX_zlVgJxiBN9IWvEMow",
    "flash": "3_9OaK6jlGxSuykE1lyNC0ceR0BAx1zVulUTL8EcnKVOtyQC76-bMSHV7zVuRfjVSeB-8zPN7Ben5ltfnu_6IJ8F8QnNhB6NzFy6_bqAItA-tSgNp3d8-pUwjEgc-8tAiNdxj2Rfb75aTPGN8I9_5BGWGEYdPXuU66IPgEer3etXQxQwAt",
    "token": "a4107fc2f202358a85a75024614a63ec,3,961571",
    "__jda": "181111935.369041817.1728735580.1730813462.1730828694.17",
    "__jdc": "181111935",
    "3AB9D23F7A4B3CSS": "jdd03IP7ZOEW6HMAOR2YF23KYRWMTUEY6WE6YJCO4HO45KAOUDW75RJ6AXP3E73LX34Z3DYL6ZVYZKZQ2OLMLEB35CY63C4AAAAMS7VYQS4IAAAAAC7V4XRK2DVKSIAX",
    "_gia_d": "1",
    "__jdb": "181111935.9.369041817|17.1730828694",
    "shshshfpb": "BApXSVSB6_vdA4wvmpEzV2_iGjEfcnOkXBmoyUqtu9xJ1MthSF4G2"
}
t=str(int(time.time()*1000))

def get_price(skuid,cat,shopId,venderId):
    url = "https://api.m.jd.com/"
    params = {
        "appid": "pc-item-soa",
        "functionId": "pc_detailpage_wareBusiness",
        "client": "pc",
        "clientVersion": "1.0.0",
        "t": t,
        "body": "{\"skuId\":"+skuid+",\"cat\":\""+cat+"\",\"area\":\"1_2800_55815_0\",\"shopId\":\""+shopId+"\",\"venderId\":"+venderId+",\"paramJson\":\"{\\\"platform2\\\":\\\"1000000101\\\",\\\"specialAttrStr\\\":\\\"p0ppppppppppp1ppp1ppppppppppp\\\",\\\"skuMarkStr\\\":\\\"00\\\"}\",\"num\":1,\"bbTraffic\":\"\",\"canvasType\":1,\"giftServiceIsSelected\":\"\",\"customInfoId\":\"0\"}",
        "h5st": "20241106015007051;yhhyevevirzk9149;fb5df;tk03wbfad1cab18nDE1hOqzilOj3dIATuo_uuAb8zGmEzKt87YAYSjgMe9FrvL03iGYlipvZEAJLG2AspQta61qXVysJ;0e9433b9a0525018995e576c271cc599;4.9;1730829007051;of7ruCLjzzZf9rIjLDIj6XETJrpjh7JjybYfy-FN5GFOGSUSyKlRyipjxjpPFipjLDrgzrJdJz1TIipjLDrgJrIf6XVd1b4e2PYezLoS4flf2bVf3nlf3TFTzfVd5T4eJrJdJrEa-OFTGOEjLrJp-jpe7PYSHKYeIWlf1roeJaleJq4e2XYd3fVS5X1ezHIS4jpjxj5PKSEQKeFjLrJp-jJf9HIg3T0UG6VRFuWeDipjxjJOJrpjh7JjnW4PnCWg_TEa3i1PJrJdJ31QHyVT5ipjLDrgJj4f9G1WJrJdJTlPJrpjh7ZMLrJp7rJdJLYOJipjLrpjh7JjJrJdJPYOJipjLrpjh7pf3rJdJTYOJipjLrpjh7pfLDIj2XETJrpjLrJp-rojxjpe2iFjLrpjLDrg0Lojxj5f2iFjLrpjLDrg53pjxjJf2iFjLrpjLDrgJHIg6zpfJrJdJnYOJipjLrpjh7pfLDIjAOEjLrpjLDrg2rJdJfkQJrpjLrJp-rojxjpQJrpjLrJp-rojxjpS0ipjLrpjh-kjxjpS9WlOzWFjLrJp-3kjLDLjnS2XG_HVmikW0K0PMaFRJrJdJjoPJrpjLrJpwqJdJrkPJrpjh7Jj3ToNL-oe1zVRUq5d7zpf6rpWdq5P0ulS9G1WJrJdJnVO4ipjLD7N;273d4a3bea5f8c223b827f28bd45492b",
        # "x-api-eid-token": "jdd03IP7ZOEW6HMAOR2YF23KYRWMTUEY6WE6YJCO4HO45KAOUDW75RJ6AXP3E73LX34Z3DYL6ZVYZKZQ2OLMLEB35CY63C4AAAAMS7VYQS4IAAAAAC7V4XRK2DVKSIAX",
        "loginType": "3",
        "scval": "1278496",
        "uuid": "181111935.369041817.1728735580.1730813462.1730828694.17"
    }
    sha = sha256(params['body'])
    h5st = geth5st.get_h5st(
        '{"appid":"pc-item-soa","body":' + '\"' + sha + '\","clientVersion":"1.0.0","client":"pc","functionId":"pc_detailpage_wareBusiness","t":' + t + '}')
    params['h5st'] = h5st
    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        res_json = json.loads(response.text)

        logger.success(response.status_code)
        price = res_json.get('price')
        regularPrice = price.get('regularPrice')
        nowPrice = price.get('p')
        # print(price)
        return regularPrice,nowPrice
    except Exception as e:
        logger.info('封控啦')



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

# print(cat,sku_venderId,sku_shopId)

for index in arr:
    try:
        cat, sku_venderId, sku_shopId = get_skuinfo.get_cat_of_sku(str(index))
        cat = cat[0].replace("'", '').split(',')
        cat = (','.join(cat))
        regularPrice, nowPrice = get_price(str(index), cat, sku_venderId, sku_shopId)
        print('skuid:',index, '日常价格:', regularPrice, '现价:', nowPrice)
        time.sleep(randint(10,15))
    except Exception as e:
       time.sleep(randint(10,15))
