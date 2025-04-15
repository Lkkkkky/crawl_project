import requests
import hashlib




def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://sale.1688.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "4921a5565977fe903f3957f08fcb0107_1732592759270",
    "_m_h5_tk_enc": "7332d2de16aebcfb0133c585ed1f1c9e",
    "cna": "VxbMHxwaJCYCAbfsE96tvqbx",
    "xlly_s": "1",
    "cookie1": "U7kCem%2FLBWmXIqt07nPeXOgRpk%2F0MRabtVEeHmvwZtY%3D",
    "cookie2": "198d92feab839b20ab666f0539f80bb5",
    "cookie17": "UUpgQy0KpNd3GoIQ3g%3D%3D",
    "sgcookie": "E100Hm8SFALw%2FNzkwMNbedatEjI6qSwNjuEfTgrjt34WYTDi21aiA1Nl4%2B2U3EbbthseDXfcriK5wJ%2FbIhNjoW%2BSMQX8%2BIMAv450fFj7vr5HwHg%3D",
    "t": "3ee973d5b98de23e1476035588ef4c4c",
    "_tb_token_": "587e989fb7759",
    "sg": "68d",
    "csg": "3b30c807",
    "lid": "tb0794515046",
    "unb": "2215447194428",
    "uc4": "nk4=0%40FY4O7o5J9UxMoQfLR7DudvFY2wdtLnI%3D&id4=0%40U2gqzJtMDo8gL5hWPzkrZGufLn0LFwXv",
    "_nk_": "tb0794515046",
    "__cn_logon__": "true",
    "__cn_logon_id__": "tb0794515046",
    "ali_apache_track": "c_mid=b2b-2215447194428b1a46|c_lid=tb0794515046|c_ms=1",
    "ali_apache_tracktmp": "c_w_signed=Y",
    "last_mid": "b2b-2215447194428b1a46",
    "_csrf_token": "1732585677710",
    "leftMenuLastMode": "EXPEND",
    "leftMenuModeTip": "shown",
    "_user_vitals_session_data_": "{\"user_line_track\":true,\"ul_session_id\":\"nbvi933yp2\",\"last_page_id\":\"mind.1688.com%2F0lrfrktkol9p\"}",
    "keywordsHistory": "%E9%A6%99%E6%B0%B4",
    "isg": "BB0dKClxJvnlb8LVZ8gkUhrWLPkXOlGMRDNDMt_iWXSjlj3Ip4phXOsFwIqQVmlE",
    "tfstk": "fyImLW6LRZ8fFwukEz-b76UqDiUJlxt6O1n96hdazQRSD-1ThaxyKKlw7StAj_fhsin9DFENZ15MBGBNXdSGNn81kCdvshX1t8FLvkBfhht49WEK6-5O0nJq0F84QLJvILaCTBWfhhMSefzdztGGvQ3A_h5w4QJ6BhowgKyk4K9Hbm8Z04lyNQRwbIuqaYJ6KjuwgCylUQ9wbCka9cRhbgszMTTDciK2xgvDzzB2aqAdVKxMttSmbck6nEAF3QVI66f6zOTGfAiMgt7C1p5qgWLfQafknhq-uHWl76v50khDFZBPpQWnCc62mwjH0ZVSPnCc43SV-AoNEnAXSKYSi7AFcTSB4UEUKTS5MtslBArwe6dPhi-gYJtD0I-kFGFS0CbP7iLXfjPplO7lZKxF4V0r8qEZfLyO4Vg6uL9k95HSoWbm0qL7E80QlEJWHWeuEVg6uL9k982oRrT2FKFd."
}
url = "https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponentrequirelogin/2.0/"


my_token=cookies['_m_h5_tk'][0:32]
data_c="{\"cid\":\"FfGetFactoryTelService:FfGetFactoryTelService\",\"methodName\":\"execute\",\"params\":\"{\\\"facMemId\\\":\\\"b2b-22104521680951f9ca\\\",\\\"facUserId\\\":null,\\\"contactId\\\":\\\"0.20648272012294878_1732587124094\\\",\\\"clickId\\\":\\\"\\\",\\\"lastMid\\\":\\\"\\\",\\\"cna\\\":\\\"\\\"}\"}"
params = {
    "jsv": "2.6.1",
    "appKey": "12574478",
    "t": "1732587125288",
    "sign": md5(my_token+ "&" + '1732587125288' + "&" + '12574478' + "&" +data_c),
    "v": "2.0",
    "ecode": "1",
    "type": "jsonp",
    "isSec": "0",
    "timeout": "20000",
    "dataType": "jsonp",
    "api": "mtop.taobao.widgetService.getJsonComponentRequireLogin",
    "callback": "mtopjsonp14",
    "data": "{\"cid\":\"FfGetFactoryTelService:FfGetFactoryTelService\",\"methodName\":\"execute\",\"params\":\"{\\\"facMemId\\\":\\\"b2b-22104521680951f9ca\\\",\\\"facUserId\\\":null,\\\"contactId\\\":\\\"0.20648272012294878_1732587124094\\\",\\\"clickId\\\":\\\"\\\",\\\"lastMid\\\":\\\"\\\",\\\"cna\\\":\\\"\\\"}\"}"
}

response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)