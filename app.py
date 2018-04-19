#!/usr/bin/env python

from urllib.request import Request, urlopen
import time


def load_page():
    req = Request('https://assetmanagement-stage.herokuapp.com', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    return webpage

count = 0
while True:
    count +=1
    print("Sleep ended")
    print(load_page())
    print("Web page called")
    print("Sleep started... {}".format(count))
    time.sleep(1200)
