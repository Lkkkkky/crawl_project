import requests
import pandas as pd
from loguru import logger

headers = {
    "Origin": "https://m-portal-prod.chinagoldcoin.net",
    "Accept": "*/*",
    "X-Requested-With": "com.eg.android.AlipayGphone",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.122 MYWeb/1.3.126.260210151602 UWS/3.22.2.9999 UCBS/3.22.2.9999_220000000000 Mobile Safari/537.36 NebulaSDK/1.8.100112 Nebula AlipayDefined(nt:5G,ws:393|0|2.75) AliApp(AP/10.8.36.8000) AlipayClient/10.8.36.8000 Language/zh-Hans useStatusBar/true isConcaveScreen/true Region/CNAriver/10.8.36.8000 MiniProgram APXWebView",
    "Referer": "https://m-portal-prod.chinagoldcoin.net/",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip",
    "Sec-Fetch-Mode": "cors",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Android WebView\";v=\"126\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "x-mass-tappid": "2021005130647313",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "prod-oss.chinagoldcoin.net",
    "Connection": "Keep-Alive"
}
url = "https://prod-oss.chinagoldcoin.net/chngc_marketing/draw/info/luckList_thirdpart_216004_1.json"
response = requests.get(url, headers=headers)

print(response.text)
print(response)

if response.status_code == 200:
    data = response.json()
    # 提取 memberName 和 memberPhone
    # 注意：当前 JSON 中未发现显式的时间字段，将按照原始顺序（通常为时间顺序）处理
    df = pd.DataFrame(data)
    
    # 只保留需要的列
    if 'memberName' in df.columns and 'memberPhone' in df.columns:
        result_df = df[['memberName', 'memberPhone']]
        
        # 写入 Excel
        output_file = '深圳-龙银币中奖名单.xlsx'
        result_df.to_excel(output_file, index=False)
        logger.success(f"数据已成功保存至 {output_file}")
    else:
        logger.error("响应数据中未找到 memberName 或 memberPhone 字段")
else:
    logger.error(f"请求失败，状态码: {response.status_code}")