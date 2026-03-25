import requests

session = requests.Session()

def print_new_cookies(old_cookies):
    current_cookies = session.cookies.get_dict()
    new_items = {k: v for k, v in current_cookies.items() if k not in old_cookies or old_cookies[k] != v}
    if new_items:
        print("\n--- [新增/更新的 Cookies] ---")
        for k, v in new_items.items():
            print(f"{k}: {v}")
        print("----------------------------\n")
    return current_cookies

def send_sms(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
        "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Microsoft Edge\";v=\"145\", \"Chromium\";v=\"145\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    cookies = {
    "AUTH_SESSION_ID": "43117648-d043-4f71-8417-64de950e258d.keycloaky-19-22730",
    "KC_STATE_CHECKER": "eyJhbGciOiJIUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2M2I4YzRkNS1jMTJjLTRhMGQtYjk5NC01ZTBjMDY0N2QwMDIifQ.eyJta3kiOiJzdWNjZXNzTG9nb3V0IiwibXR5IjoiU1VDQ0VTUyIsIm1wYXIiOltdLCJjbGlkIjoiMWViMmRkNTAtMTIzYi00MmZlLWFlZjMtY2VmZTgyOTJiYmY3Iiwic3QyIjoiNWFhMzIwNTktODI3Ni00NGYyLTllODAtMjc4MjkwMzY0NmYyIn0.T4egIH_oumJH5WK1S-yvMKZ1Hmo6AyhqfeNmxbOo6axt6P4iTI6qZ-6HMYPmaGO_4nwrd3LBk1MKZ09-svpCLA",
    "KC_RESTART": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..hESWMm4-yruaAZx_Spvpkg.7tBUBKVCI3Du2eA5zd3g7lkeSs6E_CsAHiegcNR9BJGmUuBKZlxy7rQNzOHRRAprg7Q4w9ao5xk4rcaBMH-gg55cZlCIbeUBgPJDHkZRm41BBP9ompDdSikad9a4B_AUDI6gyHrhU28bYO0lSE48oofRAUqCGeEM-En8mpks2yxJLOuX6PbePVvwtRjj5Nz7WHNFWROdojA7Z31VMK9Vfb1oxiaXrEVTPU9PWI382SEWcSFmECzWoXOJ36joCFyAPc7lXb2SRbixBXRff_xBD-fSydM6YAp-kG1prVGOIFOlDDnK0ZHK_8CMfCTLJFSAFFRlEkAK_A2Z7VI1dMLQR0o1RLBhJvmXEgXOHxzrIG27Jg5nAY7NYstfCQTGkApxX9dWoeHYH1mIz_6czpBxxAiajBsshrdIBUxf7LBvs1qdhpU8OqCD8-XWqg4X9NZ-Lrr60ZKG_8DLDZ1omDUe44nTvloXTmwj6vB7JyRDB8qg0-Wa_gw7TdhLAIE9lrk3Hw44rEIGuc64D7_9TRNnL5awWQL2ax8mWJhFzJZkrovfj2Biroz3XmEuIwRB186iAI1p64A_DwzXIym5XEXRj5ZrlV5bo8z2-eMODTmoFPzxgLDO97ijVJOjutkuzkTlolBhGtCapVdK9gzKpSfcOYJKSLh4XBw0Jph5FCIhs43B-dwdUOzSKx1jI1vGkecc3q6b3GV79fFsflINK1kBV6n0TKnFlfggN4ORkJWovJ7pgQsbhUqzZPyK3DEzBz8lpnDlx1d7tQvvCx1aWfdhOoKrHIPjm-NfTRLXfuievGLfg5icJBtrNMrGgEctfMa9HHQoOhgiT4vRrO1zr_eVdW1gNMwPR7OxADmtVKXfUpbIR5lS3EdfQBmjWgowM_NsIT3oFhR-r3kMhWVrXUTR_ufYBMNlqP7i7QeqdFpUJgPLfLNm2Mpe6f9sxq3_yZfOcWK30JLKWil30y8bFH4_fYBKNOcI2B-4gbkc9M6Q6Bw.aeYRHpd0CfDwHrC05GB23Q",
    "qcloud_visitId": "9586643282cb18ff444011c923bf95c2",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2219cd6fa493c25f5-05877ad67dff94-4c657b58-2073600-19cd6fa493d2700%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTljZDZmYTQ5M2MyNWY1LTA1ODc3YWQ2N2RmZjk0LTRjNjU3YjU4LTIwNzM2MDAtMTljZDZmYTQ5M2QyNzAwIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D",

    "i18next": "zh-CN",
    "qcloud_from": "qcloud.outside.seo-1773133253446",
    "_gcl_au": "1.1.54703199.1773133254",
    }
    url = "https://www.codebuddy.cn/auth/realms/copilot/sms/authentication-code"
    params = {
        "phoneNumber": phone
    }
    old_cookies = session.cookies.get_dict()
    response = session.get(url, headers=headers, cookies=cookies, params=params)
    print_new_cookies(old_cookies)

    print(response.text)
    print(response)
def auth(phone,code):

    url = "https://www.codebuddy.cn/auth/realms/copilot/login-actions/authenticate?session_code=TNJaV9LcpYfXIU5DJqJQJC4V--3ug_fi1tN_e98aqc8&execution=b12d313c-ef6d-4be8-b1e3-944d8b65f5fe&client_id=console&tab_id=BHqZzjM8dcg&client_data=eyJydSI6Imh0dHBzOi8vd3d3LmNvZGVidWRkeS5jbi9sb2dpbi8_cGxhdGZvcm09dXNlcmNlbnRlciZzdGF0ZT0wJnJlZGlyZWN0X3VyaT1odHRwcyUzQSUyRiUyRnd3dy5jb2RlYnVkZHkuY24lMkZwcm9maWxlJTJGdXNhZ2UiLCJydCI6ImNvZGUifQ"
    cookies = {
    "AUTH_SESSION_ID": "43117648-d043-4f71-8417-64de950e258d.keycloaky-19-22730",
    "KC_STATE_CHECKER": "eyJhbGciOiJIUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2M2I4YzRkNS1jMTJjLTRhMGQtYjk5NC01ZTBjMDY0N2QwMDIifQ.eyJta3kiOiJzdWNjZXNzTG9nb3V0IiwibXR5IjoiU1VDQ0VTUyIsIm1wYXIiOltdLCJjbGlkIjoiMWViMmRkNTAtMTIzYi00MmZlLWFlZjMtY2VmZTgyOTJiYmY3Iiwic3QyIjoiNWFhMzIwNTktODI3Ni00NGYyLTllODAtMjc4MjkwMzY0NmYyIn0.T4egIH_oumJH5WK1S-yvMKZ1Hmo6AyhqfeNmxbOo6axt6P4iTI6qZ-6HMYPmaGO_4nwrd3LBk1MKZ09-svpCLA",
    "KC_RESTART": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..hESWMm4-yruaAZx_Spvpkg.7tBUBKVCI3Du2eA5zd3g7lkeSs6E_CsAHiegcNR9BJGmUuBKZlxy7rQNzOHRRAprg7Q4w9ao5xk4rcaBMH-gg55cZlCIbeUBgPJDHkZRm41BBP9ompDdSikad9a4B_AUDI6gyHrhU28bYO0lSE48oofRAUqCGeEM-En8mpks2yxJLOuX6PbePVvwtRjj5Nz7WHNFWROdojA7Z31VMK9Vfb1oxiaXrEVTPU9PWI382SEWcSFmECzWoXOJ36joCFyAPc7lXb2SRbixBXRff_xBD-fSydM6YAp-kG1prVGOIFOlDDnK0ZHK_8CMfCTLJFSAFFRlEkAK_A2Z7VI1dMLQR0o1RLBhJvmXEgXOHxzrIG27Jg5nAY7NYstfCQTGkApxX9dWoeHYH1mIz_6czpBxxAiajBsshrdIBUxf7LBvs1qdhpU8OqCD8-XWqg4X9NZ-Lrr60ZKG_8DLDZ1omDUe44nTvloXTmwj6vB7JyRDB8qg0-Wa_gw7TdhLAIE9lrk3Hw44rEIGuc64D7_9TRNnL5awWQL2ax8mWJhFzJZkrovfj2Biroz3XmEuIwRB186iAI1p64A_DwzXIym5XEXRj5ZrlV5bo8z2-eMODTmoFPzxgLDO97ijVJOjutkuzkTlolBhGtCapVdK9gzKpSfcOYJKSLh4XBw0Jph5FCIhs43B-dwdUOzSKx1jI1vGkecc3q6b3GV79fFsflINK1kBV6n0TKnFlfggN4ORkJWovJ7pgQsbhUqzZPyK3DEzBz8lpnDlx1d7tQvvCx1aWfdhOoKrHIPjm-NfTRLXfuievGLfg5icJBtrNMrGgEctfMa9HHQoOhgiT4vRrO1zr_eVdW1gNMwPR7OxADmtVKXfUpbIR5lS3EdfQBmjWgowM_NsIT3oFhR-r3kMhWVrXUTR_ufYBMNlqP7i7QeqdFpUJgPLfLNm2Mpe6f9sxq3_yZfOcWK30JLKWil30y8bFH4_fYBKNOcI2B-4gbkc9M6Q6Bw.aeYRHpd0CfDwHrC05GB23Q",
    "qcloud_visitId": "9586643282cb18ff444011c923bf95c2",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2219cd6fa493c25f5-05877ad67dff94-4c657b58-2073600-19cd6fa493d2700%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTljZDZmYTQ5M2MyNWY1LTA1ODc3YWQ2N2RmZjk0LTRjNjU3YjU4LTIwNzM2MDAtMTljZDZmYTQ5M2QyNzAwIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D",
    "sajssdk_2015_cross_new_user": "1",
    "i18next": "zh-CN",
    "qcloud_from": "qcloud.outside.seo-1773133253446",
    "_gcl_au": "1.1.54703199.1773133254",
    }

    headers = {
    "Host": "www.codebuddy.cn",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Microsoft Edge\";v=\"145\", \"Chromium\";v=\"145\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Origin": "null",
    "Content-Type": "application/x-www-form-urlencoded",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "iframe",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    data = f"""phoneActivated=true&phoneNumber={phone}&code={code}&credentialId=&login=%E7%99%BB%E5%BD%95"""
    old_cookies = session.cookies.get_dict()
    res = session.post(url, headers=headers, cookies=cookies, data=data, allow_redirects=False)
    print_new_cookies(old_cookies)

    if res.status_code == 302:
        print(f"Redirecting to: {res.headers.get('Location')}")
    # print(res.text)


def redirect():
    url = "https://www.codebuddy.cn/console/accounts/.apisix/redirect?state=4c74ebe750a58023f3a4c942a51ac7a5&session_state=43117648-d043-4f71-8417-64de950e258d&iss=https%3A%2F%2Fwww.codebuddy.cn%2Fauth%2Frealms%2Fcopilot&code=082da0e7-6ce1-49e1-a93d-fee604b019c2.43117648-d043-4f71-8417-64de950e258d.3feb966c-1151-42a6-9619-5ac899a8ba88"
    cookies = {
    "qcloud_visitId": "9586643282cb18ff444011c923bf95c2",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2219cd6fa493c25f5-05877ad67dff94-4c657b58-2073600-19cd6fa493d2700%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTljZDZmYTQ5M2MyNWY1LTA1ODc3YWQ2N2RmZjk0LTRjNjU3YjU4LTIwNzM2MDAtMTljZDZmYTQ5M2QyNzAwIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D",
    "sajssdk_2015_cross_new_user": "1",
    "i18next": "zh-CN",
    "qcloud_from": "qcloud.outside.seo-1773133253446",
    "_gcl_au": "1.1.54703199.1773133254",
    "session": "dLQQ8hgDqzmBaI71Y5pCkQ|1773137216|aRlGo97rIFjHwAEwQw1QKmEfgzJQMXZxIc6oNcPNfm-JDZuXKfkaBuG38yQpKBMxNMzX8qiYc8dInUyjMZCtVbNSY2PEqFSCQeAhjFDHPjUlqVDl7rWNkuh9C6Qf-Pg-TicyE65EJDc9zU3Dsfbrqwi8TX1mlFZOAeZJOaFNKsIM0EPHahiTFa4eplYrIosqPfpQ6QViggnl5YS-hBBm9A|cSgUlp6jcgQR0-aoCO2FF2eqIVc",
    }

    headers = {
    "Host": "www.codebuddy.cn",
    "Connection": "keep-alive",
    "traceparent": "00-6c0e573aa4b0a35d876352e768c04830-88cf4d9187da9e09-01",
    "sec-ch-ua-platform": "\"Windows\"",
    "X-Domain": "www.codebuddy.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Microsoft Edge\";v=\"145\", \"Chromium\";v=\"145\"",
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    old_cookies = session.cookies.get_dict()
    res = session.get(url, headers=headers, cookies=cookies)
    print_new_cookies(old_cookies)
    # print(res.text)

def claim():
    url = "https://www.codebuddy.cn/billing/meter/claim-gift"
    cookies = {
    "qcloud_from": "qcloud.outside.seo-1773133253446",
    "_gcl_au": "1.1.54703199.1773133254",
    "qcloud_visitId": "9586643282cb18ff444011c923bf95c2",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2219cd6fa493c25f5-05877ad67dff94-4c657b58-2073600-19cd6fa493d2700%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTljZDZmYTQ5M2MyNWY1LTA1ODc3YWQ2N2RmZjk0LTRjNjU3YjU4LTIwNzM2MDAtMTljZDZmYTQ5M2QyNzAwIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D",
    "i18next": "zh-CN",
    "session": "02Gly6tvRaYaYXBceAU7iQ|1773253955|zRVvfbWGL1xDjcBdeEUJKaVnl9e--iRxlnPVfSbm0152Qvrq-UetmBj7TZwuzzzMnZjDuupCdNzatbxhzmdKOCXh33LG70FcFU0qtRulmAGy1nlKFIa7xxV7QZV0P-yh5dRVZVYh7slh0x4PG9ZzeAkMUYz9QqLcMd8mscw3ROQmCrz3B8XtazjSzQU2oheQ0WjSJ1Csosgj6G0tUOhDGV9g-K9wnaMjvx7_jr8rmdK0hEzw8gSMKcUnVqD0_bZv-5gi9jtZqP3UYvvpzyrixATYRomsuXO-HGm2oZ_rAW7w2xuwlkNa9lpS4WX6pIry0frHVP8_OPe00rUEmu8osmWQXKUIsFY382dntMXniRCZnPgQGv1zYSJdnlx4MfvqrTSu9G3FWdRXWSM5TBT0fVv9uu8OudIh6GX34y7G-NorN1FEeUm7gokcdYrAeWr4kdFNYNEyCx9ojW4ql-XQWPWZ1zwLhuO7kt1sdZUD91FfSBB92YZvjxDkf0BOPr3sZ6MvlVBDiYX_8IngO05WQsRjcAJebljD-oR5aUM1JzmoSolrokb_nMbai8ygTdwomgAFeCyOjcTbmUEAk3i4PlZiHtIPpZ0w2GhQUfmTNlGWgazQomzzgrjocihAjJFOZDe5i9iscI27tcBwuKlcN-Wit2mFesudkR8OEPI-FGG4Qd84bS4AAP90GG0qyxol0d3xQHcl3BUJKnsEOkELtHUdZKvABqxXVFOA41wi-kqYNfzMJG-x8tF5SQoI-BuB4GRUOco6zup9XoBvRSE3GtDneFfOkot8gC9TgE6tY1BhXfvP4JJW0FHX4f2PFoOtixULv5ZT1SbpdhwtAyBdjsL0SIiR3HsrCJFW6C4y1T63KLiUfBpiNy-Rl5e916lQFPDoBBuPRs5UWSIhLCcEnlVKdGgRKXWwwZi_aMtm4iq7GYM1iiXsKRsIUdhudCP6qrTxyUGYvhnMtpstEaPyYSE0_XfiCzhNY7XPiPbFrBmae62nXTKT60YX2hOEch6uU275EqiQA12LCku1MLaMwfuPvTMB448Rc0R2hrWf3r1MM9FbQROTgIxuzP4Q4UNcy-7M2RkB25lt4UBTrfXfPbR231sBvksYwIigpv9BGvcEuVe1HpYXx8KItpFh42-j0bN5_vFHIyQLuOmj_pot2eOFsV1SwnIOiBuMlyPW0OYx3xAClMN3cL4ohPNXHpzjWwqR_iaDAdgcp0OhcTn7SLb1itpL8HLfB-NhQUSIQ-TiOGyeVfG1kjwloQLjKVcWkGzjLXsqX2dFFL69Tmc9tGLjgXXrABOWe0ey4w1Deu3d0xdjWzj8XyS1I7Xb6sc_kDRI9JsNc3JKptU8c0wxV7lnxv2GJFD6kn-LhAMWMQIQ8OJ1Y4tkU-9Uoju_C1yQGYa83pIaTyiU_-o4VX_TX7BbvMFJUUtumCTMZP_jYRxrH5AJLaSqGkm4FcbFbvPjLoNdvzbRFRAebyqxSNyAT0-5cYnA1dvrbcsvT6Ro4me3H7Vr3ZeuukAaYUcSgWksRH3qyNEngCvuUieeoXRzQk6I8tBz7HUfTKS6k4G4biug9Tq50v5KS5Ttqj9X1wbQDM7vDhBCbPCKUBgCCEZxNDl6M51G22r8LZx5cWoRS1UB3v9Xv6HKc4m1CS-1oM6o6ZJf-dSF_Yzk6f4fT39xruYbrq8QAYETIR-K8FcA6E3Vdj5j5sy7VWL1iGNlVzT4-KV6yk2rs9jYiunVbriidpoTGZsv0S8gHMWcUWLa45R8y_fl9XTzNq-bAU_EEvFWplvLz6HI0bZFM01gpZG1Ri0wDKH7zehjXfcSwZGgll6Co0X4i9qqDHnw1znKCEHnywyNiemISm9Xot06UD8WP6jbqmtIOUT38pQ2Ar4FF9K0IXKL5ctprwF6hmn5nUDLT-XJ2lM-sk49eLL6PnsSqdYgHB2WDBSvRltCTGYobk9dYX4-QjJ9Sc3AUZiOBYoZ5Ba4ne_1MjjEX3iZwbr0cLdfy-SiR2SzutmKw9Q0e0NfaK6JUUJAI7QK8uCtGkf6g4oMq_aHzai4FSehfUC688PWBo-RvpayPkc5jQjPKrBOnJoypK_SndJSBADJa2Eb-yz0Mx8JS2oFEpNGosLDAPCfK-xDae5ghCqcr1NIGULJcq6kE-y_Mo_2djYhYZYR_B9noZLupvurEJ1CZcSIb1WHvf2TQzb47H8-AUFRR-UIUW7Zd0fGW4niFskHgMqJXt7xt8RgCY1NY-LxwmMqzMzKbISe28Nmz3c0aSTDq164ysqwkJ0tfB808AF_YARJKTFby8jYQUzmD8qBZUnAVgDirhZU6SXh_n7FAJro20JRKTK57U2blk1Uj1vdZoCD6ww2sGSI6jhPFisPbv1iD_0nUBb4jOfqyFvsWHGSW5OHTbaVhbYupwHfz3Hy5UBNwGSGCz1hH-kMi1OLGlDv33rAkFMpm0YH4ghAm5_w_LqEJrbIh7yq5yyq2CXhkOj9mtOuen_9F3m-h2SZXp8gSZv16tMx3wg3Beo8jmLvum8ROT5LKv1mnkfrDENdtHxy1GNLID54FxpP_XMAbH-cHvwNHmjqbSWonHmdm_6gSPcegNwBltwx9WhCWq7WXGh6gXYUGJXkvroqc793ZRvtfZS9CH-2PIrxLgmklVNtGnuIq9HDfFexo6az3A3kJ8AHIpOXSJ24ZHyX922GxXvmE_qLVAkbASxrn3n3sBVHG5kVHFLOWvjn6ZfK9II8Im7dUC7-21RZ1D-NDtr0x12uuJy470F3QZR8TooRYZkeGhjkFcUnGiFr1v-Aej_RFbB6WUcRzfwgp0Ub3TyeMGVXyE_lXy54_mTKbyxcMbjgBg50T3Q38GTKLkDoWrt3ydLY2URV_v6w7ohJCYe9Dz-FV7nG2ociFWjW-SpJl8mCAVlgdh0CX2UvLw3b6ZSCKv3nwsmVi9dRAvESEBk71qu4Cqf_hNdCYPJ07uiBnHvpzZrRpHj1IOss-YSbT71TgqljghUtYj6bmslQ0aTGFicyupX1yYXjkENywPcbwPr4RhQuf9nMLcX8pzvbOZJcbhlKKk0lfk8nMhyOC1BItIUg3pTMQFIyMkzbJXRv4CUb45-5xXQ-wdoEkZREInlRVmJ1uxeLiQPBVhO_qlId77wZi8mZLAsnd_w54KvOTRfb3JTGOmKnE6t-rLmrjxYcNbyIUCJeeqv5wy-5yvk2na9UssHq8xfenr7P-VLmSNnGnmZR-Ig-TG03Y6jRe7rmGT-Njw3RK0tkbA-N5FivgCrVUhVSgDCMNEw4gpUY76Cn7URYgE9IpU9vRDxnrkGn6AeuJ0qb7msO6nlhz0dzP2dhxgwB2aw5lfbz_S05y9itYqPLI1m65QipzF2ftASS2FrZv5zLY0HbyqPcMilOUepA0kCgadgkcJeWw-UBiBZlipRXlDtahBAnGQfvkyJuIDfb-dLjJDt4rUm-kTEMVNpOTnZgEStpG3di-FkVDuxDSBqYf9WMYL05cBUk-xZxCFwMexbMNETiXLomaD1ojuX2Ma6NCmoXbI3-QTLfyY6vSSYtQFd43FIBWDGjSX8wOIdhDTyMILDA7CwFEZul_eIHZBAgUjJpqvvZaUB9tiL3v8JLJ21WUBMA-stmPwzuIXiXx6lzTu2MSZJ2hM1mkkDdbTBgT7HxED9E2mcCI6X_chifQs5IfihfpPIvLjNtHVDHe_CoKAHgivxIQY8mM_XPVnJUG-MigtUSVQ9vrAhY1PBRvHPpNZ4MeaYihaHdFhkzc62FkStxp03zjyFeoEJ3nKxzkaUz9vL6wxkNtfYix0K3hK3wYgbELPT4-M55z6OwvNNoL4wnWtcI7bmLv674ShyZCiNu5mL250UhZL302pqgfNsk-gCbPLUZHQXMWuxPUm-r6yBiQiB13B3dM8UCFbzWk4fbqY8CNKJ0JLXCmRWQlxZCcOOcK8K0MMZ4Xy0",
    "session_2": "pOG4ZXwzt3RFsqcMuDBsYa3x5KOqFB6wCrpkhkKR-edW-f24HMMVuJmfb2qFTtc9NRibvsTd3XZcKOoafu6YeyurWn8qUoWe0bbVu_lmPbnfVBbwH_TqCK5eOw7v76PVgG9Kj7P6lR-iD9NnAxZsXK4wh4PJm38psZRUByHNbPKjO4NqYRkvca7-NEMmkaOrjKUfmAtw_i5XHMn5iJcJuz5ign-PTgbVFCwe7hox_mSOTAQSBrng05v2_zmQUumEJ6nrHQrkUvLAI9w6afK5xo7xLG1JdTRV-uZQLdcuH85qmneXr6jp4pKx3pSpRwUsfrY45dh5LpXEYQaDC4htPRfeLw19zusil0BenrHelamI4rg95Y_UBSI8xTDh_RF7hF12UDWuwuREj4Yxna54E4AkGquoVk6YIJKzAXhbXSsExeMzdLRRJE22uAYdiyt3jwkUH3qvz08ZjURZB8ah6iHRnFMhYv33LOBHAPvrbcVoIiTf0LTrEUEjhU0UEYDcWsO95j10qlPVHsBWnya1mUXQ8tqWWT49rLFKrEW9PwI4BrPGHGU4FfqyzEfsegrjrJn-S-nbcjAxBK7fd-BkVdMH2cUZYgKXPkjSk3Y_MRhevrvVXPVDsGQpZwWM6mkFZkpskwLh0AgOCsZbrBBakHs9drjdp2M_haP4r8KQ0ErZZ_HgrBqDj3DkWWlEKhACk9BR7wAu0s9l49lfpYdORXfq09BB_Ha75cQ9i3wYaKtD5UrwLp3nAcXvmew1cu7uv8WojU2_XNrsTVzqcrcGqNtE3r1kDG4bkKi-nSEeXrGhKffPtlwLPd9nLKLwWkFBdGNl5dHPvzmaszXjjgVPUrLxqnRJG5uT8eqMlxD-EKYbYr3NFOMmDa3OdJlRyfTFAq|socfT-FEEm9mTNMONHJ9_DD-BRc"
    }
    headers = {
    "Host": "www.codebuddy.cn",
    "Connection": "keep-alive",
    "sec-ch-ua-platform": "\"Windows\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Microsoft Edge\";v=\"145\", \"Chromium\";v=\"145\"",
    "sec-ch-ua-mobile": "?0",
    "Origin": "https://www.codebuddy.cn",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.codebuddy.cn/profile/usage",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    old_cookies = session.cookies.get_dict()
    res = session.post(url, headers=headers, cookies=cookies)
    print_new_cookies(old_cookies)
    print(res.text)

# send_sms('17737112279')

auth('17737112279','651870')
redirect()
claim()