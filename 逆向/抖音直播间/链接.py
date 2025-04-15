'''
=========================================================    
       @File     : 链接.py
       @IDE      : PyCharm
       @Author   : Jing3
       @Date     : 2025/4/5 02:48
       @Desc     : 
=========================================================   
'''
import gzip
import time

from websocket import WebSocketApp
import json
import requests
import re
import execjs
import hashlib
import ssl
import websocket

from dy2_pb2 import Webcast
def md5(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

def on_open(ws):
    print('on_open',ws)

def on_message(ws,message):
    # 根据proto结构体解析对象
    Frame=Webcast.Im.PushFrame()
    Frame.ParseFromString(message)
    # print("package::", Frame)
    RES=Webcast.Im.Response()
    RES.ParseFromString(gzip.decompress(Frame.payload))
    # print("res::",RES)
    # 返回直播间服务器链接存活确认消息，便于持续获取数据
    if RES.need_ack:
        ack = Webcast.Im.PushFrame(LogID=Frame.LogID,
                        payload_type='ack',
                        payload=RES.internal_ext.encode('utf-8')
                        ).SerializeToString()
        ws.send(ack, websocket.ABNF.OPCODE_BINARY)

    for msg in RES.messages:
            method = msg.method
            # print(method,msg.payload)
            try:
                {
                    'WebcastChatMessage': _parseChatMsg,  # 聊天消息
                    'WebcastGiftMessage': _parseGiftMsg,  # 礼物消息
                    'WebcastLikeMessage': _parseLikeMsg,  # 点赞消息
                    'WebcastMemberMessage': _parseMemberMsg,  # 进入直播间消息
                    'WebcastSocialMessage': _parseSocialMsg,  # 关注消息
                    'WebcastRoomUserSeqMessage': _parseRoomUserSeqMsg,  # 直播间统计
                    'WebcastFansclubMessage': _parseFansclubMsg,  # 粉丝团消息
                    'WebcastControlMessage': _parseControlMsg,  # 直播间状态消息
                    'WebcastEmojiChatMessage': _parseEmojiChatMsg,  # 聊天表情包消息
                    'WebcastRoomStatsMessage': _parseRoomStatsMsg,  # 直播间统计信息
                    'WebcastRoomMessage': _parseRoomMsg,  # 直播间信息
                    'WebcastRoomRankMessage': _parseRankMsg,  # 直播间排行榜信息
                    'WebcastRoomStreamAdaptationMessage': _parseRoomStreamAdaptationMsg,  # 直播间流配置
                }.get(method)(msg.payload)
            except Exception:
                pass

def _parseChatMsg(payload):
    """聊天消息"""
    _ChatMessage = Webcast.Im.ChatMessage()
    _ChatMessage.ParseFromString(payload)
    # print(_ChatMessage)
    user_name = _ChatMessage.user.nickname
    user_id = _ChatMessage.user.short_id
    content = _ChatMessage.content
    print(f"【聊天msg】[{user_id}]{user_name}: {content}")

def _parseGiftMsg( payload):
    """礼物消息"""
    _GiftMessage = Webcast.Im.GiftMessage()
    _GiftMessage.ParseFromString(payload)
    user_name = _GiftMessage.user.nickname
    user_id = _GiftMessage.user.short_id
    gift_name = _GiftMessage.gift.name
    gift_cnt = _GiftMessage.combo_count
    print(f"【礼物msg】[{user_id}]{user_name} 送出了 {gift_name}x{gift_cnt}")

def _parseLikeMsg( payload):
    '''点赞消息'''
    _LikeMessage = Webcast.Im.LikeMessage()
    _LikeMessage.ParseFromString(payload)
    user_name = _LikeMessage.user.nickname
    count = _LikeMessage.count
    print(f"【点赞msg】{user_name} 点了{count}个赞")

def _parseMemberMsg( payload):
    '''进入直播间消息'''
    message = Webcast.Im.MemberMessage().parse(payload)
    user_name = message.user.nick_name
    user_id = message.user.id
    gender = ["女", "男"][message.user.gender]
    print(f"【进场msg】[{user_id}][{gender}]{user_name} 进入了直播间")

def _parseSocialMsg( payload):
    '''关注消息'''
    message = Webcast.Im.SocialMessage().parse(payload)
    user_name = message.user.nick_name
    user_id = message.user.id
    print(f"【关注msg】[{user_id}]{user_name} 关注了主播")

def _parseRoomUserSeqMsg( payload):
    '''直播间统计'''
    message = Webcast.Im.RoomUserSeqMessage().parse(payload)
    current = message.total
    total = message.total_pv_for_anchor
    print(f"【统计msg】当前观看人数: {current}, 累计观看人数: {total}")

def _parseFansclubMsg( payload):
    '''粉丝团消息'''
    message = Webcast.Im.FansclubMessage().parse(payload)
    content = message.content
    print(f"【粉丝团msg】 {content}")

def _parseEmojiChatMsg( payload):
    '''聊天表情包消息'''
    message = Webcast.Im.EmojiChatMessage().parse(payload)
    emoji_id = message.emoji_id
    user = message.user
    common = message.common
    default_content = message.default_content
    print(f"【聊天表情包id】 {emoji_id},user：{user},common:{common},default_content:{default_content}")

def _parseRoomMsg( payload):
    message = Webcast.Im.RoomMessage().parse(payload)
    common = message.common
    room_id = common.room_id
    print(f"【直播间msg】直播间id:{room_id}")

def _parseRoomStatsMsg( payload):
    message = Webcast.Im.RoomStatsMessage().parse(payload)
    display_long = message.display_long
    print(f"【直播间统计msg】{display_long}")

def _parseRankMsg( payload):
    message = Webcast.Im.RoomRankMessage().parse(payload)
    ranks_list = message.ranks_list
    print(f"【直播间排行榜msg】{ranks_list}")

def _parseControlMsg( payload):
    '''直播间状态消息'''
    message = Webcast.Im.ControlMessage().parse(payload)

    if message.status == 3:
        print("直播间已结束")


def _parseRoomStreamAdaptationMsg( payload):
    message = Webcast.Im.RoomStreamAdaptationMessage().parse(payload)
    adaptationType = message.adaptation_type
    print(f'直播间adaptation: {adaptationType}')

def on_error(ws,message):
    print('on_error',ws,message)

def on_close(ws,*args,**kwargs):
    pass

def get_roomid_ttwid():

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://live.douyin.com/",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
    }
    cookies = {
        "UIFID_TEMP": "dca68353d0985e2a8bd3e6652fe656c462342d173f24572ea68edd0cbeddca385339a3b996f5e1611374f05a1c85270331758d4f36f282f016484fcaadc9b2d5f0794426782b86ad76bada76845d60cf",
        "hevc_supported": "true",
        "bd_ticket_guard_client_web_domain": "2",
        "UIFID": "dca68353d0985e2a8bd3e6652fe656c462342d173f24572ea68edd0cbeddca385339a3b996f5e1611374f05a1c8527036dbd0b1cf1d59fef35430cc9e1fe7deb3a1a16ad43dec3e3718211597721201441167a04b671c5cd5b2645244dced22d5d7834c4421a87c2253a901138eae5e45946291fbc0a4aa6a3023dfc8ed711cbaf47e5234545a4afeee399708ad7e5b7f1e0924baf0a04a9d28c9623148a331e",
        "SelfTabRedDotControl": "%5B%5D",
        "my_rd": "2",
        "live_use_vvc": "%22false%22",
        "xgplayer_user_id": "334264261600",
        "fpk1": "U2FsdGVkX1/SU0A6Yg9hTVP14xno88pVLvhkrEVILiOges6HSYyxDg1Qd5bDlYJlgpSI3iDVl1kPdCADkwrVfg==",
        "fpk2": "e2dd8fac9c214f2e57aa0dea655ff030",
        "store-region": "cn-gd",
        "store-region-src": "uid",
        "SEARCH_RESULT_LIST_TYPE": "%22single%22",
        "ttwid": "1%7Ck_nm2lGmS6zcqEz9absgb_FJ0nQ_7X-mPfCRwLZfFAo%7C1739761104%7Cf4eaf383f33edb16cc0cd2fefa8a284c6c1c906c5fbc97511b8f511775d4c4af",
        "strategyABtestKey": "%221743500772.604%22",
        "is_dash_user": "1",
        "passport_csrf_token": "221bd4a6bf4fdadafef7b9ad69d13e1a",
        "passport_csrf_token_default": "221bd4a6bf4fdadafef7b9ad69d13e1a",
        "is_staff_user": "false",
        "FORCE_LOGIN": "%7B%22videoConsumedRemainSeconds%22%3A180%7D",
        "__security_mc_1_s_sdk_crypt_sdk": "b6cba2ed-43bc-9758",
        "__security_mc_1_s_sdk_cert_key": "718988fd-4eb4-9479",
        "passport_mfa_token": "CjWpUVDgauUr6NoiBYBiCw6crrbnhwYryKVhRAuNqjzCqjA01Rb61T5mARsCZgVr%2BdvVj8I1oRpKCjwAAAAAAAAAAAAATtMV7YvMsd%2FxQ905Yi%2FYFpPAJbdM7jYRRRuhuFxpXObJOG42LW%2B0q8cm%2FIBQAYrLOp0Q3cntDRj2sdFsIAIiAQMIIHPm",
        "d_ticket": "0e4e2f2d4961d589e5a35321bae4c2ed1fbdf",
        "n_mh": "Cs1NG6_gtmJj06E01JQbe5DuL3OhSuAP90498oO932k",
        "_bd_ticket_crypt_cookie": "5a22390c6e3b123d7c33958411dd31fd",
        "__security_mc_1_s_sdk_sign_data_key_web_protect": "d90fe2ad-4fd7-897d",
        "__security_server_data_status": "1",
        "publish_badge_show_info": "%220%2C0%2C0%2C1743500815722%22",
        "FOLLOW_LIVE_POINT_INFO": "%22MS4wLjABAAAAwAlRMqIMw_EpFfNFpdYX-pqALXOlVB7KtmFH5CUlEUc%2F1743782400000%2F0%2F1743780403676%2F0%22",
        "login_time": "1743780413570",
        "sid_guard": "3723608aa0bb01deb79ef5a81486c8e0%7C1743780413%7C21600%7CFri%2C+04-Apr-2025+21%3A26%3A53+GMT",
        "uid_tt": "31cea67dedf5c2ba526576f275b2cc02",
        "uid_tt_ss": "31cea67dedf5c2ba526576f275b2cc02",
        "sid_tt": "3723608aa0bb01deb79ef5a81486c8e0",
        "sessionid": "3723608aa0bb01deb79ef5a81486c8e0",
        "sessionid_ss": "3723608aa0bb01deb79ef5a81486c8e0",
        "sid_ucp_v1": "1.0.0-KGQzMTMwMjdiMmVmYjdjZDBhNDA3MmU1ZDE5NTU2NjAzYWM1NTJlNjYKCBC99L-_BhgNGgJsZiIgMzcyMzYwOGFhMGJiMDFkZWI3OWVmNWE4MTQ4NmM4ZTA",
        "ssid_ucp_v1": "1.0.0-KGQzMTMwMjdiMmVmYjdjZDBhNDA3MmU1ZDE5NTU2NjAzYWM1NTJlNjYKCBC99L-_BhgNGgJsZiIgMzcyMzYwOGFhMGJiMDFkZWI3OWVmNWE4MTQ4NmM4ZTA",
        "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSXJxcEJ5UEpRcmErVzRyNlhxSlVQSVZ2b2szbkYxcGNKSnVkYnNmRTNPeHFmMldGMWZkTjVPdkx6bHlialpBRldSMUFxOEFFVGZMUlVaRkVPQ0R1VW89IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D",
        "odin_tt": "666ffd2b630c8a07fc2179c1fddfb03935dcc4da35ccbf81aa5e83596452a21f90a11b196942e7b7694f5a9fc06673c32099d2b157d72119ecbd3222ca63aed5815eb228a391f23226603bfeebcbc121",
        "xgplayer_device_id": "58879323321",
        "stream_recommend_feed_params": "%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A7.1%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22",
        "home_can_add_dy_2_desktop": "%221%22",
        "stream_player_status_params": "%22%7B%5C%22is_auto_play%5C%22%3A1%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22",
        "has_avx2": "null",
        "device_web_cpu_core": "8",
        "device_web_memory_size": "8",
        "csrf_session_id": "8c8d1107dcfa01b9d1da754f1b0993d3",
        "volume_info": "%7B%22isUserMute%22%3Atrue%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.253%7D",
        "webcast_leading_last_show_time": "1743781570921",
        "webcast_leading_total_show_times": "1",
        "download_guide": "%223%2F20250404%2F1%22",
        "WallpaperGuide": "%7B%22showTime%22%3A1743780448041%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A22%2C%22cursor2%22%3A6%7D",
        "webcast_local_quality": "ld",
        "xg_device_score": "7.658235294117647",
        "__live_version__": "%221.1.3.353%22",
        "__ac_nonce": "067f027c30043f4149ae4",
        "__ac_signature": "_02B4Z6wo00f01A6059gAAIDAOZAjhhXvufwOlONAAGRjSm7fY8fUc9atEKYRdBiCTEe8Oi5Letn72s3gBSOykDz0-zljkuXNo-8JsEVAm7MPhcTZRgWJlZlG-EcQzDHwm4zE.S-WZXmpPAZ695",
        "live_can_add_dy_2_desktop": "%221%22",
        "IsDouyinActive": "false"
    }
    url = "https://live.douyin.com/208823316033"
    response = requests.get(url, headers=headers, cookies=cookies)

    # print(response.text)
    roomid=re.findall(r'{\\"id_str\\":\\"(.*?)\\",',response.text)[0]
    print(roomid)
    ttwid=response.cookies.get_dict()['ttwid']
    print(ttwid)
    return ttwid,roomid

def douyin_websocket_client(url,ttwid):
    ws=WebSocketApp(
        url=url,
        header = {"User-Agent": "userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"},
        cookie=f"ttwid={ttwid}",
        on_open=on_open,
        on_message=on_message,
        on_close=on_close,
        on_error=on_error
    )
    # sslopt = {"cert_reqs": ssl.CERT_NONE}
    ws.run_forever()
for i in range(300):
    ttwid,roomid=get_roomid_ttwid()

    ori_data=f'live_id=1,aid=6383,version_code=180800,webcast_sdk_version=1.0.14-beta.0,room_id={roomid},sub_room_id=,sub_channel_id=,did_rule=3,user_unique_id=7417773587292309026,device_platform=web,device_type=,ac=,identity=audience'
    sign=execjs.compile(open('enc.js','r',encoding='utf-8').read()).call('enc',md5(ori_data))

    url=f"wss://webcast5-ws-web-hl.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.14-beta.0&update_version_code=1.0.14-beta.0&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/134.0.0.0%20Safari/537.36%20Edg/134.0.0.0&browser_online=true&tz_name=Asia/Shanghai&cursor=t-1743792338381_r-7489531062725491186_d-1_u-1_h-7489530815845092627&internal_ext=internal_src:dim|wss_push_room_id:{roomid}|wss_push_did:7417773587292309026|first_req_ms:1743792338309|fetch_time:1743792338381|seq:1|wss_info:0-1743792338381-0-0|wrds_v:7489531054135444300&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7417773587292309026&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&insert_task_id=&live_reason=&room_id={roomid}&heartbeatDuration=0&signature={sign}"
    # asyncio.run(douyin_websocket_client())

    douyin_websocket_client(url,ttwid)
    time.sleep(10)