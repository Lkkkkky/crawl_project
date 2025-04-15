import json
import re
import requests
import subprocess

url = "https://www.douyin.com/aweme/v1/web/comment/list/"
params = "device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7400670230101396746&cursor=0&count=10&item_type=0&insert_ids=&whale_cut_token=&cut_version=1&rcFT=&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=128.0.0.0&browser_online=true&engine_name=Blink&engine_version=128.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7341451502348879375&verifyFp=verify_m04tkch2_vu0KsKuh_Wy2Z_4Usb_9iIv_ozTFEaRH6mWJ&fp=verify_m04tkch2_vu0KsKuh_Wy2Z_4Usb_9iIv_ozTFEaRH6mWJ&msToken=F8ZJyHW6PlN83q5Aw8I2mUWeMJmUFkVwYP0zHIqoKzFsWe6mhkusx1C3XhL8Hm8bZnmcFONxpldnvCTJzer6LR-k07xFT3XXjxmyje2u-8F7jc_OXUg-aflBQG-GGw%3D%3D&a_bogus=OX8M%2FQwvdk2BgV6h53VLfY3q6IB3Yh5n0trEMD2fMx3uAL39HMTc9exYsGTvuFujN4%2FkIeEjy4hbO3KkrQC9M1wf7Wsx%2F2CZQg00t-P2so0j53intL6mE0hN4kb3SFlm5XNAEOJ0y75nFbi0Wo9amhK4bfebY7Y6i6tr4E%3D%3D"
payload = {}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/user/self?from_tab_name=main&modal_id=7400670230101396746&showTab=post',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'Cookie': 'LOGIN_STATUS=1; store-region=cn-gd; store-region-src=uid; live_use_vvc=%22false%22; bd_ticket_guard_client_web_domain=2; xgplayer_user_id=420453306873; d_ticket=a6d750979f29e8099706af9f861faec1ccde5; n_mh=Cs1NG6_gtmJj06E01JQbe5DuL3OhSuAP90498oO932k; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; my_rd=2; UIFID_TEMP=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e385280d70e5b989dd9d077bf892330ced1e1cb59fef738362b1370878d97b31e858deab1b6f7b29d0a9c52a9f1e79d1d4394db; fpk1=U2FsdGVkX19Iyl6GrlQi1svoby046/FJkp0DylZsXu7QkkzcZKVqVwCwYls4ge1kvcvAE3mK9lfZbRQng5ZKWA; fpk2=5f4591689f71924dbd1e95e47aec4ed7; UIFID=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e385280837990e4f1602971417bc3e1f08138c6fefe8bc5e45ad3c0c3098040346745ee3e2142f5eafb1c26712d4975023d4b3d022833edfb295221ba1da2bdcedadc77689e897b1ce568e2009b2efc4afc8ff4ad19edfca2b12d8b48eca4b9e9fd4efe1923562a0181cb0830122dd7f1d6a09054388a56521075f8f9e97e179acf252a; passport_assist_user=Cjxb5Uy9jYYV8LseGJWxs1ZTqPHDziUBQst9yn51ZxEV3NyArtngUa6_fBhS1Ugg3L4fXrkfjpd0U42GYvcaSgo86s0N8ef2ybj8Suz-0FirciIeGTArdJJA0_Nwl2cHHjT3ppkL9497VJw67dWBymXkAlsiR_wX0FramXlqEIPO1w0Yia_WVCABIgEDZJVOOA%3D%3D; sso_uid_tt=fe559f4efd58586e4eb06a0a25860ccb; sso_uid_tt_ss=fe559f4efd58586e4eb06a0a25860ccb; toutiao_sso_user=d1bb873384802c10aa2dca7fae98964e; toutiao_sso_user_ss=d1bb873384802c10aa2dca7fae98964e; sid_ucp_sso_v1=1.0.0-KDY5YmQ1MmIyNTNhNDI4NzQzNThiNmVjM2JlMDUwM2U5N2UzMzYxNjAKHwj0xLOzoQIQq8qJtQYY7zEgDDCvo-_QBTgGQPQHSAYaAmxxIiBkMWJiODczMzg0ODAyYzEwYWEyZGNhN2ZhZTk4OTY0ZQ; ssid_ucp_sso_v1=1.0.0-KDY5YmQ1MmIyNTNhNDI4NzQzNThiNmVjM2JlMDUwM2U5N2UzMzYxNjAKHwj0xLOzoQIQq8qJtQYY7zEgDDCvo-_QBTgGQPQHSAYaAmxxIiBkMWJiODczMzg0ODAyYzEwYWEyZGNhN2ZhZTk4OTY0ZQ; uid_tt=f9a8752e6063af7b39404cef6399632c; uid_tt_ss=f9a8752e6063af7b39404cef6399632c; sid_tt=25aabc3f2976502b6720ed96077f65ea; sessionid=25aabc3f2976502b6720ed96077f65ea; sessionid_ss=25aabc3f2976502b6720ed96077f65ea; _bd_ticket_crypt_cookie=1571542dbd98a59c11ce6319159ccd0d; s_v_web_id=verify_m04tkch2_vu0KsKuh_Wy2Z_4Usb_9iIv_ozTFEaRH6mWJ; dy_swidth=1920; dy_sheight=1080; passport_csrf_token=5b48be2b84bbefd4e40b23b269fc8713; passport_csrf_token_default=5b48be2b84bbefd4e40b23b269fc8713; sid_guard=25aabc3f2976502b6720ed96077f65ea%7C1724303156%7C5184000%7CMon%2C+21-Oct-2024+05%3A05%3A56+GMT; is_staff_user=false; sid_ucp_v1=1.0.0-KGU1NmE1MDFmM2JjYmY5ZTY3YTQ3MGE3MGVmYjM2NWJiY2NlOGM5MDgKGQj0xLOzoQIQtI6btgYY7zEgDDgGQPQHSAQaAmhsIiAyNWFhYmMzZjI5NzY1MDJiNjcyMGVkOTYwNzdmNjVlYQ; ssid_ucp_v1=1.0.0-KGU1NmE1MDFmM2JjYmY5ZTY3YTQ3MGE3MGVmYjM2NWJiY2NlOGM5MDgKGQj0xLOzoQIQtI6btgYY7zEgDDgGQPQHSAQaAmhsIiAyNWFhYmMzZjI5NzY1MDJiNjcyMGVkOTYwNzdmNjVlYQ; hevc_supported=true; SelfTabRedDotControl=%5B%5D; download_guide=%223%2F20240827%2F0%22; __live_version__=%221.1.2.3141%22; h265ErrorNum=-1; volume_info=%7B%22isMute%22%3Atrue%2C%22isUserMute%22%3Atrue%2C%22volume%22%3A0.253%7D; pwa2=%220%7C0%7C3%7C1%22; live_can_add_dy_2_desktop=%221%22; publish_badge_show_info=%221%2C0%2C0%2C1725008131554%22; ttwid=1%7C2RgI8tTD1_o4KcDqMVUqUYkXn648apmXsPUtMtZ2vks%7C1725084202%7C6d4928aae9b7a8a78b24c600be8195451e816991b2e80a9fa1957e8d8bbb961b; WallpaperGuide=%7B%22showTime%22%3A1725008139879%2C%22closeTime%22%3A0%2C%22showCount%22%3A3%2C%22cursor1%22%3A63%2C%22cursor2%22%3A0%2C%22hoverTime%22%3A1725084204132%7D; strategyABtestKey=%221725205772.721%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAwAlRMqIMw_EpFfNFpdYX-pqALXOlVB7KtmFH5CUlEUc%2F1725292800000%2F0%2F1725211211802%2F0%22; csrf_session_id=0e6d965134e8f68d0ef9a683f7865aae; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAwAlRMqIMw_EpFfNFpdYX-pqALXOlVB7KtmFH5CUlEUc%2F1725292800000%2F0%2F1725244404170%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSXJxcEJ5UEpRcmErVzRyNlhxSlVQSVZ2b2szbkYxcGNKSnVkYnNmRTNPeHFmMldGMWZkTjVPdkx6bHlialpBRldSMUFxOEFFVGZMUlVaRkVPQ0R1VW89IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; passport_fe_beating_status=true; EnhanceDownloadGuide=%220_0_0_0_1_1725247289%22; __ac_nonce=066d52f450017c4be4027; __ac_signature=_02B4Z6wo00f01rwwE0wAAIDDY2vgAzS8Q2a8EBfAAMnlsrFnec7nnLVR7AGz.nxMqwd7Zk4fBZjv-vHuI-IVRIcvu5qscCiKkxpq33zOgSKlQ0NZAP5uytO9ODnT60CQdGyo5j9PV-aKl6nhca; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A6.8%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; odin_tt=fc2854b51ae6eeb8a869d9993e16ee5c98d621ac308d4798ef756fd9fe6350b0e8d5698c09ba2722ae1a3413b1829e2f; IsDouyinActive=true',
    'Host': 'www.douyin.com',
    'Connection': 'keep-alive'
}
args = [
    0,  
    1,
    12,
    params,
    "",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
]
# result=subprocess.run(['node',r'E:\Program Files\Desktop\qianggou\nixiang\抖音\a_bogus.js',json.dump(args)],capture_output=True,text=True,encoding='utf-8')
# a_bogus=re.findall(r'\&\&(.*?)\&\&',result.stdout)[0]
# print(a_bogus)
# '&'.join([f"{i}={params[i]}" for i in params.key()])  构造参数
# params='?'+params+'&a_bogus='+a_bogus
response = requests.request("GET", url, headers=headers, data=payload, params=params)

print(response.text)
