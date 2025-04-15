'''
=========================================================
       @File     : 10.17实现.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2024/10/16 15:54
       @Desc     :
=========================================================
'''
from idlelib.iomenu import encoding

import requests
import subprocess
import re
import requests
import json

import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.douyin.com/discover?modal_id=7408174553953733907",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}
cookies = {
    "ttwid": "1%7Ck_nm2lGmS6zcqEz9absgb_FJ0nQ_7X-mPfCRwLZfFAo%7C1727085026%7C9335b482874a4103954039c638ea5751d4705a0476662ab852be67e015bdeb8a",
    "UIFID_TEMP": "dca68353d0985e2a8bd3e6652fe656c462342d173f24572ea68edd0cbeddca385339a3b996f5e1611374f05a1c85270331758d4f36f282f016484fcaadc9b2d5f0794426782b86ad76bada76845d60cf",
    "s_v_web_id": "verify_m1etu1ic_pRK9RqbQ_lyMK_4V8I_85pj_l7Psudhp8ltT",
    "hevc_supported": "true",
    "dy_swidth": "1920",
    "dy_sheight": "1080",
    "xgplayer_user_id": "808828832026",
    "passport_csrf_token": "7604d03af89bca7192b29e3e4c227958",
    "passport_csrf_token_default": "7604d03af89bca7192b29e3e4c227958",
    "bd_ticket_guard_client_web_domain": "2",
    "fpk1": "U2FsdGVkX1/DNR/Um6hb8SHmbSYf8J7EFsLZotMav31jGGNWWPjHvgfNT9aGrsLc6y8a8UHb8h46J1RDWnjVPw==",
    "fpk2": "e2dd8fac9c214f2e57aa0dea655ff030",
    "passport_assist_user": "CjyP8nPJiYcZ--ksslviueDRHRuUPOpP6aCwqVOo53uPcuR5DTPPsHcysfCx-LySWwWzcEE36mI2B6ivlSgaSgo8ee6qDcFjAGX0XEm5Py3QzKb32h3d29mqiHauGpOgzK17g7Q1q9xS14eqRr4fY-q5SfbXKxs6PpW0H01gEJjv3A0Yia_WVCABIgEDDixhdA%3D%3D",
    "n_mh": "Cs1NG6_gtmJj06E01JQbe5DuL3OhSuAP90498oO932k",
    "sso_uid_tt": "b019d385fcd8ac24fb65e0ba57b6269c",
    "sso_uid_tt_ss": "b019d385fcd8ac24fb65e0ba57b6269c",
    "toutiao_sso_user": "ac0d848a24af041a0aa2163caee8342f",
    "toutiao_sso_user_ss": "ac0d848a24af041a0aa2163caee8342f",
    "sid_ucp_sso_v1": "1.0.0-KDJiMGY2ZDYwMGY5Y2IyMDZlNWE5NjBmMzI3NGVkN2JiNWRjNzRjYjMKHwj0xLOzoQIQ-fPEtwYY7zEgDDCvo-_QBTgGQPQHSAYaAmhsIiBhYzBkODQ4YTI0YWYwNDFhMGFhMjE2M2NhZWU4MzQyZg",
    "ssid_ucp_sso_v1": "1.0.0-KDJiMGY2ZDYwMGY5Y2IyMDZlNWE5NjBmMzI3NGVkN2JiNWRjNzRjYjMKHwj0xLOzoQIQ-fPEtwYY7zEgDDCvo-_QBTgGQPQHSAYaAmhsIiBhYzBkODQ4YTI0YWYwNDFhMGFhMjE2M2NhZWU4MzQyZg",
    "passport_auth_status": "2b1690ab93fb7e1c0f716bac75f95882%2C",
    "passport_auth_status_ss": "2b1690ab93fb7e1c0f716bac75f95882%2C",
    "uid_tt": "07e9de4011dba89210da2eebf9dabe05",
    "uid_tt_ss": "07e9de4011dba89210da2eebf9dabe05",
    "sid_tt": "8f163a74ab8625004a5fafecceece89e",
    "sessionid": "8f163a74ab8625004a5fafecceece89e",
    "sessionid_ss": "8f163a74ab8625004a5fafecceece89e",
    "is_staff_user": "false",
    "UIFID": "dca68353d0985e2a8bd3e6652fe656c462342d173f24572ea68edd0cbeddca385339a3b996f5e1611374f05a1c8527036dbd0b1cf1d59fef35430cc9e1fe7deb3a1a16ad43dec3e3718211597721201441167a04b671c5cd5b2645244dced22d5d7834c4421a87c2253a901138eae5e45946291fbc0a4aa6a3023dfc8ed711cbaf47e5234545a4afeee399708ad7e5b7f1e0924baf0a04a9d28c9623148a331e",
    "SelfTabRedDotControl": "%5B%5D",
    "_bd_ticket_crypt_doamin": "2",
    "_bd_ticket_crypt_cookie": "18516782160fbeb30f55926d7b05e6e7",
    "__security_server_data_status": "1",
    "my_rd": "2",
    "live_use_vvc": "%22false%22",
    "store-region": "cn-gd",
    "store-region-src": "uid",
    "xgplayer_device_id": "73801574645",
    "SEARCH_RESULT_LIST_TYPE": "%22single%22",
    "__live_version__": "%221.1.2.4155%22",
    "publish_badge_show_info": "%221%2C0%2C0%2C1728799631562%22",
    "download_guide": "%223%2F20241008%2F1%22",
    "WallpaperGuide": "%7B%22showTime%22%3A1728895551200%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A10%2C%22cursor2%22%3A2%7D",
    "live_can_add_dy_2_desktop": "%221%22",
    "pwa2": "%220%7C0%7C3%7C0%22",
    "FOLLOW_NUMBER_YELLOW_POINT_INFO": "%22MS4wLjABAAAAwAlRMqIMw_EpFfNFpdYX-pqALXOlVB7KtmFH5CUlEUc%2F1729094400000%2F0%2F1729063879561%2F0%22",
    "__ac_signature": "_02B4Z6wo00f01wVz-eAAAIDC2igKrxLsdFsFU.1AAKZWtkYJP9a6fF3.UabznDRRtak.tnj.tAP8fW6ojMGQjAN5A-y2Sc9LOix7eEVNboz-G8INLhBrzx48pfS2.nj3nc03wA.OtWQhzp4qa5",
    "douyin.com": "",
    "xg_device_score": "7.658235294117647",
    "device_web_cpu_core": "8",
    "device_web_memory_size": "8",
    "architecture": "amd64",
    "stream_recommend_feed_params": "%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22",
    "strategyABtestKey": "%221729150608.58%22",
    "csrf_session_id": "0c70bac3f14e83ac4ee76828a5fe62b1",
    "FOLLOW_LIVE_POINT_INFO": "%22MS4wLjABAAAAwAlRMqIMw_EpFfNFpdYX-pqALXOlVB7KtmFH5CUlEUc%2F1729180800000%2F0%2F1729150608692%2F0%22",
    "biz_trace_id": "cc776afd",
    "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSXJxcEJ5UEpRcmErVzRyNlhxSlVQSVZ2b2szbkYxcGNKSnVkYnNmRTNPeHFmMldGMWZkTjVPdkx6bHlialpBRldSMUFxOEFFVGZMUlVaRkVPQ0R1VW89IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D",
    "home_can_add_dy_2_desktop": "%221%22",
    "sid_guard": "8f163a74ab8625004a5fafecceece89e%7C1729150610%7C5184000%7CMon%2C+16-Dec-2024+07%3A36%3A50+GMT",
    "sid_ucp_v1": "1.0.0-KDAxMTdkYzM3NzE1YmQ1ZTUyNDM2ZjdjYzk4NDA1YzczOWJhZDQwZjgKGQj0xLOzoQIQkv3CuAYY7zEgDDgGQPQHSAQaAmhsIiA4ZjE2M2E3NGFiODYyNTAwNGE1ZmFmZWNjZWVjZTg5ZQ",
    "ssid_ucp_v1": "1.0.0-KDAxMTdkYzM3NzE1YmQ1ZTUyNDM2ZjdjYzk4NDA1YzczOWJhZDQwZjgKGQj0xLOzoQIQkv3CuAYY7zEgDDgGQPQHSAQaAmhsIiA4ZjE2M2E3NGFiODYyNTAwNGE1ZmFmZWNjZWVjZTg5ZQ",
    "volume_info": "%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.379%7D",
    "odin_tt": "1ffd2b8096e6681da95b3c8b9143ff7f551a261cd6644bfb2e37e53f7b1b5f10f25861f836186dd5eedd5853619c56a1",
    "passport_fe_beating_status": "true",
    "IsDouyinActive": "true"
}
url = "https://www.douyin.com/aweme/v1/web/comment/list/reply/"
params = {
    "device_platform": "webapp",
    "aid": "6383",
    "channel": "channel_pc_web",
    "item_id": "7408174553953733907",
    "comment_id": "7408177626982990604",
    "whale_cut_token": "",
    "cut_version": "1",
    "cursor": "3",
    "count": "10",
    "item_type": "0",
    "update_version_code": "170400",
    "pc_client_type": "1",
    "pc_libra_divert": "Windows",
    "version_code": "170400",
    "version_name": "17.4.0",
    "cookie_enabled": "true",
    "screen_width": "1920",
    "screen_height": "1080",
    "browser_language": "zh-CN",
    "browser_platform": "Win32",
    "browser_name": "Edge",
    "browser_version": "129.0.0.0",
    "browser_online": "true",
    "engine_name": "Blink",
    "engine_version": "129.0.0.0",
    "os_name": "Windows",
    "os_version": "10",
    "cpu_core_num": "8",
    "device_memory": "8",
    "platform": "PC",
    "downlink": "10",
    "effective_type": "4g",
    "round_trip_time": "50",
    "webid": "7417773587292309026",
    "verifyFp": "verify_m1etu1ic_pRK9RqbQ_lyMK_4V8I_85pj_l7Psudhp8ltT",
    "fp": "verify_m1etu1ic_pRK9RqbQ_lyMK_4V8I_85pj_l7Psudhp8ltT",
    "msToken": "r2BPtDgM23jZ_pJTJSeH1DKVmQZN42e6-Od-lKuqOvfT3pKe5l-zNuQlMc2r3Dszc_Tbiu07I3ihhlIrNjMoLJklxvA1FJGvs7KaG7w8wWYUWXf-v4Mvxcm3XemhF5DEgED3aZ3yymidOKBT80y0nX-bR3VSHZGuT23FMO7EuA==",
    "a_bogus": "YfUVDeUJE2RbeVFtuKBZy1/lfLIMrTuyyPTxSbBPexPfYwFOJuP2xPeOGoKf/O-ybSBkkF5HwVP/TEdbBzUkZeepKmpfuFTRCtVVn6sLZqwRTUsmLqbpezvzKwBr0cGqe5V7iAy60UeqgjnAkqdg/B5e7/KKQ5uBBZOWk/TcP9B61F6AEZn1PpbpO7rG0tCj"
}

result = subprocess.run(['node', r'E:\Program Files\Desktop\Jing3\逆向\抖音\222.js'],
                        capture_output=True, text=True, encoding='utf-8')

# print(result.stdout)
h5st = re.findall(r'\$\$(.*?)\$\$', result.stdout)[0]
print(h5st)
params['a_bogus']=h5st
print(len(h5st))
response = requests.get(url, headers=headers, cookies=cookies, params=params)
print(response.text)
print(response)
# res_json=json.loads(response.text)
# txt=res_json['status_code']
# print(res_json)
