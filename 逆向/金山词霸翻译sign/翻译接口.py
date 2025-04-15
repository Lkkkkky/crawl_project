import requests
import execjs
import json
from loguru import logger
headers = {
    "referer": "https://www.iciba.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
url = "https://ifanyi.iciba.com/index.php"
params = {
    "c": "trans",
    "m": "fy",
    "client": "6",
    "auth_user": "key_web_new_fanyi",

}
def tran(word):
# word=input('请输入要翻译的单词:')
    data = {
        "from": "en",
        "to": "zh",
        "q": word
    }
    js=execjs.compile(open('get_sign.js','r',encoding='utf-8').read())
    # print(json_res['content'])
    sign=js.call('getsign',data)
    params['sign']=sign
    response = requests.post(url, headers=headers, params=params, data=data)
    json_res=json.loads(response.text)
    res=js.call('dec',json_res['content'])

    json_obj=json.loads(res)
    logger.info('翻译结果如下：'+json_obj['out'])
    return json_obj['out']
