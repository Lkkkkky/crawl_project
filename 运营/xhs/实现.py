import time

from curl_cffi import requests
import json

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "origin": "https://www.xiaohongshu.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.xiaohongshu.com/",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "x-b3-traceid": "f6876913770d87d3",
    "x-mns": "unload",
    "x-s": "XYW_eyJzaWduU3ZuIjoiNTYiLCJzaWduVHlwZSI6IngyIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6ImMxMGMzOTljYTU1ZTMwN2I2Zjc0YjM2MmU3OWJiZjhiZDg2ZGU3YTM1ZjM5ZmNjNzFlZDIxNjQzZmIwZmNmZWMyMjFjYTU3Yzg3OWE4NWM1OWVlMzllYjlkMzhmYjc2ODc5ODA5MzY3YjIxZWNlOTJiZGVmNDg4NDIyNmRiM2E1MzViYjcwNTQxYzA3ZjAxOTQ0ZGQ5YzQ1YThiODc0NTU1ODI0MzU5NWJkNjc0OTA2ZmQxMDAwYjRjNGQ4YTI4ZTdhMWJiYzBjMDM5ZTJjYmM3MzFjMzA4Y2Q0ZTY1NDJjMTdkYzczMzY3OGZiNGVkZTQ3YjgxMDEyNTMzMjFmYjNjM2FiMWVkMWYzNDVjNzAxZmU4ODRmYTUxMWZhNjM4NjZkMjJjN2M0ZjQ3NTVjNGY2OTQ0ZTIzOTU4NDg0MWQ4NTAxNWMwNmY3MzNjY2M2MWNiZDQzOGQ5NzA1MGIzYTZjZTMwMmRjMjM5ZTRmODU4ZmFmNTI3MzQwNmNkODZiMmE3NDI3OTQ2NTM3ZDE5YjQ5YjM0MzI4N2FkNTlhMjMyIn0=",
    "x-s-common": "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",
    "x-t": "1746724774434",
    "x-xray-traceid": "cb58746efffbf0be3700f528308d8934"
}
cookies = {
    "abRequestId": "dd0419ac-d5ac-516d-bfae-e371522dad21",
    "a1": "1951c0033d4gzy900uedtkrj977h5fcsnqmtgeica50000857898",
    "webId": "92bc1c6492cff53edeb04d845b78d6cf",
    "gid": "yj2yS884qWIyyj2yS88qqAd3f4kuvj887df96S0TFVjWW928x2iSMk888Y2WYjY8j0YyyqKJ",
    "x-user-id-creator.xiaohongshu.com": "65c1c8480000000016002321",
    "customerClientId": "014013214631522",
    "web_session": "040069b0a591cc12badb8f68293a4be78eca19",
    "webBuild": "4.62.3",
    "acw_tc": "0a4a953c17467247202912945e64206cc00afd6d8d5b32f72ee7c956ebca6f",
    "websectiga": "984412fef754c018e472127b8effd174be8a5d51061c991aadd200c69a2801d6",
    "sec_poison_id": "0c397778-731e-4031-85e3-71b7bba6aeb1",
    "unread": "{%22ub%22:%22681b51a9000000002101aec1%22%2C%22ue%22:%22680df5d0000000000900dddd%22%2C%22uc%22:25}",
    "xsecappid": "xhs-pc-web",
    "loadts": "1746724767107"
}
def get_comments():
    url = "https://edith.xiaohongshu.com/api/sns/web/v2/comment/page"
    params = {
        "note_id": "681c9e37000000002001c41a",
        "cursor": "",
        "top_comment_id": "",
        "image_formats": "jpg,webp,avif",
        "xsec_token": "AB29wqWzcetRQSs_VRJ15XsedSy0NN9FkDtMYmfyFOEjs="
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
    comments = response['data']['comments']
    for comment in comments:
        format_dict={
            'title':comment['content'],#内容
            'like_count':comment['like_count'],#点赞数
            'nickname':comment['user_info']['nickname']#昵称
        }
        print(format_dict)
        if comment['sub_comment_has_more']==True:
            get_sub_comments(comment['note_id'],comment['id'],comment['sub_comment_cursor'])



def get_sub_comments(note_id,root_comment_id,cursor):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "origin": "https://www.xiaohongshu.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.xiaohongshu.com/",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
        "x-b3-traceid": "b9ab68502a848aa2",
        "x-mns": "awf0X6zOxn4wdoRekwjn6mgeoYuwBoO5PM5ggXmnny4byMXtNyizB/2+SheIjjloweSZgQNLvpmKHZQ4F+WRwNJo9waRcNLB+Z87wW4u6dx2u+o6wDa3tvOQwxekdpkn7pbH5DLBKwH9B4jPGLOJptgEbMBXhFFj93nQ03hl6IDSmaQXh062xXzjfMSafIp1nXc/aCe5/Tj9SLou6xS9weYKD+pPRWTfXkmhaTbWQLtFJltjYIdBekyDpuwENMnfRxNGiaFyYod83okeZdRCHS0n9w5zJYoxDP0O5jvdNti3Pzy/i73Qybm7xLnPKfWIB5jDgdmZ22lYdbJZzuxhST465/lZI50zugP85pcw8EOig6X+b0Il3BKMy8Xn8XlFOCc/ZtQyM3NgXylyi60PyDigao3o3XCuKMTg5GM5E5fxdQS6eul2nm5jW2Dkw232fZ355C2Pl/7OT4Xf70QYKflX3zBTfPZcC9o4wDfkI6+0+JEen2LuO6c/j4t0",
        "x-s": "XYW_eyJzaWduU3ZuIjoiNTYiLCJzaWduVHlwZSI6IngyIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6IjAwN2Q2NzZjNjkxYzM3NGM5MWUxODJjMWExZjVlZTM5YTM2MmY3ZjJhMTdmNWVkYjYzMTVhMDRlNTAzYzRhZGM4YjE0MGIwZTA1NzNjZDM0MTdhYjk0Mzc5NjEyYmZmZDFjYTVlNGJlYTE0Y2E2MjYyZDE0MWQyZTNlMGFjMTg1MTM4OWJiZDkzZjEwODQzNDJiZWQ4NGU3ZDc4ZTAwY2JiNTlmMjBhYTRjZTBjOWE3NTM2YjM1YjliMDVhOThiYWRjZjM5M2M5ZjFmNGE4MDMzZWMzZjM3YjJiYWIzYzIzNDM2MzMzNDExNDk1MzA3MGU0ZWI2ZjhjY2E1NThkODk2MTJlODEwZmU3MmZlN2FmZDZhNDY4N2MxNDY0NDE2MTNiYjJmZmIzOWU0NGM4NzQ3NzZkN2MxMjU3YzY4MTljNTc0YjFlYzQ5NWQ2OGRiZTBiNGMyMjEwZjJkN2JkMjI3YWU1YzQ3ZTg2M2IyOTJlZGJiZTcyOTA3ZWIyYmMyNmEyNWU3YjVhNWM0ZTczMThhOGQ4YmExNzA5OWQzY2EzIn0=",
        "x-s-common": "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",
        "x-t": "1746725343086",
        "x-xray-traceid": "cb5878c7b27bf0c7c7021953ebc084c8"
    }
    cookies = {
        "abRequestId": "dd0419ac-d5ac-516d-bfae-e371522dad21",
        "a1": "1951c0033d4gzy900uedtkrj977h5fcsnqmtgeica50000857898",
        "webId": "92bc1c6492cff53edeb04d845b78d6cf",
        "gid": "yj2yS884qWIyyj2yS88qqAd3f4kuvj887df96S0TFVjWW928x2iSMk888Y2WYjY8j0YyyqKJ",
        "x-user-id-creator.xiaohongshu.com": "65c1c8480000000016002321",
        "customerClientId": "014013214631522",
        "web_session": "040069b0a591cc12badb8f68293a4be78eca19",
        "webBuild": "4.62.3",
        "acw_tc": "0a4a953c17467247202912945e64206cc00afd6d8d5b32f72ee7c956ebca6f",
        "unread": "{%22ub%22:%22681b51a9000000002101aec1%22%2C%22ue%22:%22680df5d0000000000900dddd%22%2C%22uc%22:25}",
        "xsecappid": "xhs-pc-web",
        "loadts": str(int(time.time()*1000)),
        "websectiga": "a9bdcaed0af874f3a1431e94fbea410e8f738542fbb02df1e8e30c29ef3d91ac",
        "sec_poison_id": "42d88e3d-f43c-4433-be5f-7cceff028ee0"
    }
    url = "https://edith.xiaohongshu.com/api/sns/web/v2/comment/sub/page"
    params = {
        "note_id": note_id,
        "root_comment_id": root_comment_id,
        "num": "10",
        "cursor": cursor,
        "image_formats": "jpg,webp,avif",
        "top_comment_id": "",
        "xsec_token": "AB29wqWzcetRQSs_VRJ15XsedSy0NN9FkDtMYmfyFOEjs="
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
    print(response)
    comments = response['data']['comments']
    for comment in comments:
        format_dict = {
            'title': comment['content'],  # 内容
            'like_count': comment['like_count'],  # 点赞数
            'nickname': comment['user_info']['nickname']  # 昵称
        }
    if response['has_more']==True:
        new_sub_cursor=response['data']['cursor']
        get_sub_comments(note_id,root_comment_id,new_sub_cursor)


    print(response)

get_comments()