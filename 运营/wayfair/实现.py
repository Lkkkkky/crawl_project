'''
=========================================================    
       @File     : 实现.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/4/1 18:19
       @Desc     : 
=========================================================   
'''
import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.wayfair.com/",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}
cookies = {
    "WFDC": "DSM",
    "CSNUtId": "67b63762-a4ed-4c1e-9da6-8c4a5d0b9af7",
    "pxcts": "0408fdf7-0ee2-11f0-a296-8817869d427e",
    "_pxvid": "0408ed55-0ee2-11f0-a295-165d47c0605c",
    "postalCode": "63122",
    "i18nPrefs": "lang%3Den-US",
    "ExCSNUtId": "67b63762-a4ed-4c1e-9da6-8c4a5d0b9af7",
    "vid": "23e17d3a-67eb-bc62-19b2-2261fd150602",
    "SFSID": "3ed54b8a25217198f46a2f5e480f5c36",
    "canary": "0",
    "serverUAInfo": "%7B%22browser%22%3A%22Google%20Chrome%22%2C%22browserVersion%22%3A134%2C%22OS%22%3A%22Windows%22%2C%22OSVersion%22%3A%22%22%2C%22isMobile%22%3Afalse%2C%22isTablet%22%3Afalse%2C%22isTouch%22%3Afalse%7D",
    "CSN_CSRF": "fe13e6f25e09a70d6bd5aee8c9540e603168f169919cb329198bc4ec59795d5f",
    "_px3": "dc17e8fc4d934660e9c55b71d5dd5641e1329324d029d7cbd05ce4b0e58ccddd:emtwzInjknGoCWzjGMok41cehSe9Xr24NdwXKTR5DMk1kSVPz1GQ0kOqIEZLKzSyyPlaDz9Kv0fS0bk6nQYRbw==:1000:m5QusXpEl9XUMYL01HUtg0xCxVX0Z9XSwVsCfOqGi+1ng5Pqu/I8ntd001P8TVXwZDzNFg6A7LC0vqUENRYo1840fppXcLuG+xX5fk1HGZlbesudK4IWCt05dd0qL8M2YUXza84SePOS6qO0dVgmX5xCRbC8k1oi1DBhGLNLIkc2Ru6f7u3obLF4J/2zvydhWpVpAv4HQF1ZsqeBxB1a9jDmfnZIJ8cOlkLpT9y6zVU=",
    "__pxvid": "063b912d-0ee2-11f0-9fb5-ba8fdb6bf831",
    "coreGatewayOptOut": "modal",
    "forterToken": "44eafcdaaa1c4f68ae7587c933be64f6_1743502450014___24ck",
    "FVSID": "49-673ff984-d1ef-42c7-8254-9c7050ba514b",
    "CSNPersist": "page_of_visit%3D3",
    "originPageViewID": "ODE1OGRlMWEtYWMwYy00Nw==",
    "cjConsent": "MHxOfDB8Tnww",
    "cjUser": "6f670499-c3de-4cc5-8444-8ddbad9a0ef0",
    "navigationPairID": "450c145e-5635-47e6-bb0d-b4f15bbf02a2"
}
url = "https://www.wayfair.com/keyword.php"
params = {
    "keyword": "girl"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params,proxies={'http': '127.0.0.1:33210', 'https': '127.0.0.1:33210'})

print(response.text)
print(response)