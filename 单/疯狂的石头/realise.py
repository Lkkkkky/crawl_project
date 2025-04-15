import ast
import json
import time
import subprocess
from functools import partial
import rapidjson

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import requests
from openpyxl import load_workbook

with open(r"./pp.js", encoding="utf-8") as f:
    ctx = execjs.compile(f.read())


def login(phone, password):
    payload = ctx.call('reAll', phone, password)

    time1 = str(int(round(time.time() * 1000)))
    time2 = str(int(round(time.time() * 1000)))
    key = ctx.call('keyAndIv')
    iv = ctx.call('keyAndIv')
    uuid = ctx.call('getuuid')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309091b) XWEB/8555',
        'timestamp': time1,
        'timestamp2': time2,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Iv': key,
        'Key': iv,
        'uuidhashcode': uuid
    }
    res = requests.post("https://gldzb-gateway.gldzb.com/gldzb-manage-api/api/web/loginByAuth", data=payload,
                        headers=headers)
    code = res.json()['statusCode']
    print(res.json()['businessMsg'])
    print(res.text)
    if code == "200":
        return res.json()['data']['accessToken'], res.json()['id']
    else:
        print(res.json()['businessMsg'])


def getD(token, id, laborId, sectionId, sectionName):
    key = "cCkLdm2c7U7WzZSf"
    iv = "SHiRPRNYdIUzvQDZ"
    ttt = ctx.call('getListAll', token)
    print(ttt)
    data = {
        "laborId": laborId,
        "__laborName__": "湖南2024年第四季度劳务分包价",
        "sectionId": sectionId,
        "__sectionName__": sectionName,
        "contract": ""
    }
    time2 = str(int(round(time.time() * 1000)))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309091b) XWEB/8555',
        'timestamp': str(ttt['timestamp']),
        'timestamp2': str(ttt['timestamp'] + 100),
        'Content-Type': 'application/json',
        'iv': ttt['iv'],
        'key': ttt['key'],
        'uuidHashCode': ttt['uuidHashCode'],
        'token': token,
        'encryptData': ttt['encryptData'],
        'casId': id
    }
    res = requests.post("https://gldzb-gateway.gldzb.com/gldzb-core-api/core/labor/getSectionDetails_v2", json=data,
                        headers=headers)
    print('ssss',res.text)
    aa = ctx.call('AES_Decrypt', res.json()['data'], key, iv)
    return aa


def getL(token, id):
    key = "cCkLdm2c7U7WzZSf"
    iv = "SHiRPRNYdIUzvQDZ"
    ttt = ctx.call('getListAll', token)
    print(ttt)
    data = {"laborId": "4840959987899432992", "contract": ""}
    time2 = str(int(round(time.time() * 1000)))


    # print(encryptData2)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309091b) XWEB/8555',
        'timestamp': str(ttt['timestamp']),
        'timestamp2': str(ttt['timestamp'] + 100),
        'Content-Type': 'application/json',
        'iv': ttt['iv'],
        'key': ttt['key'],
        'uuidHashCode': ttt['uuidHashCode'],
        # "deviceId": "13edeae8324167becb486b88e22982d758dc62cd59ef7330e0ddac24a0480e43",
        'token': token,
        "encryptData2":ttt['encryptData'],
        'encryptData': ttt['encryptData'],
        'casId': id
    }
    res = requests.post("https://gldzb-gateway.gldzb.com/gldzb-core-api/core/labor/getLaborSections_v2", json=data,
                        headers=headers)
    print('sssaa',res.text)
    aa = ctx.call('AES_Decrypt', res.json()['data'], key, iv)
    return aa


def append_row(file_path, sheet_name, data):
    workbook = load_workbook(file_path)
    sheet = workbook[sheet_name]

    # 整行追加写入 Excel
    sheet.append(data)

    workbook.save(file_path)


def task():
    ll = []
    info = login("13787058992@bj4923", "aaaa5599")
    token = info[0]
    id = info[1]
    lists = rapidjson.loads(getL(token, id).strip('\x00'))
    for l in lists['sectionList']:
        ll.append({
            'laborId': l['laborId'],
            'id': l['id'],
            'name': l['name']
        })
    for k in ll:
        print(k)
        d = getD(token, id, k['laborId'], k['id'], k['name'])
        d = d.rstrip("\x00")
        Datas = json.loads(d)
        for oo in Datas['sectionDataList']:
            datee = []
            # 设置文件名和工作表名，大小写敏感
            file_path = 'ceshi.xlsx'
            sheet_name = 'Sheet1'
            if 'unit' in oo:
                datee.append(oo['name'])
                datee.append(oo['unit'])
                datee.append(oo['referenceRange'])
                datee.append(oo['excludedTaxPrice'])
                datee.append(oo['taxRate'])
                datee.append(oo['rule'])
                datee.append(oo['content'])
                datee.append(oo['description'])
            else:
                datee.append(oo['name'])
                datee.append(' ')
                datee.append(' ')
                datee.append(' ')
                datee.append(' ')
                datee.append(' ')
                datee.append(' ')
                datee.append(' ')
            append_row(file_path, sheet_name, datee)
            datee.clear()
        d = ""
        print("等待下个任务。。。。")
        # time.sleep(2)
    print("所有任务完成！")

if __name__ == '__main__':

    task()

