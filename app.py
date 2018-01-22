#!/usr/bin/env python

from urllib.request import Request, urlopen
import time


def load_page():
    req = Request('https://rajasthan-aanganwadi.herokuapp.com', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    return webpage


while True:
    print("Sleep ended")
    print(load_page())
    print("Web page called")
    print("Sleep started...")
    time.sleep(1200)
