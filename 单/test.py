
import datetime

import requests as req

req.packages.urllib3.disable_warnings()

# 执行下面步骤之前要先登录同区账号

# 需要查找的名字 名字 或 名字#编号
name = '玫瑰是我盗的#99058'

# 用管理员CMD执行 wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline
# 找到 –remoting-auth-token 和 –app-port
# 替换下面两个参数的值
token = 'XDC7PwMp4QTsse2H9VjZBg'
port = '35226'

base_url = 'https://riot:' + token + '@127.0.0.1:' + port


def get_summoner(name):
    url = base_url + '/lol-summoner/v1/summoners'
    resp = req.get(url, data={'name': name}, verify=False)
    return resp.json()


def get_match_history(name):
    uid = get_summoner(name)['puuid']
    url = base_url + '/lol-match-history/v1/products/lol/' + str(uid) + '/matches'
    resp = req.get(url, data={}, verify=False)
    return resp.json()


def get_champion_name(champion_id):
    url = base_url + '/lol-champ-select/v1/grid-champions/' + champion_id
    resp = req.get(url, data={}, verify=False)
    return resp.json()['name']


def parse_history(history):
    for i in history['games']['games']:
        start_time = datetime.datetime.strptime(i['gameCreationDate'][:19],
                                                '%Y-%m-%dT%H:%M:%S')
        start_time = start_time + datetime.timedelta(hours=8)
        start_time = start_time.strftime('%Y-%m-%d %H:%M:%S')
        print(start_time, ('\033[31m败\033[0m', '\033[34m胜\033[0m')[i['participants'][0]['stats']['win']],
              '[' + get_champion_name(str(i['participants'][0]['championId'])) + ']\t',
              str(i['participants'][0]['stats']['kills'])
              + '-' + str(i['participants'][0]['stats']['deaths'])
              + '-' + str(i['participants'][0]['stats']['assists']), i['gameMode'])


parse_history(get_match_history(name))
