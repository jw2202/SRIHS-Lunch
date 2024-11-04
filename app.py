#!/usr/bin/env python3
import ssl
import requests
import re
import urllib3.poolmanager
import sys
from bs4 import BeautifulSoup

days = int(sys.argv[1])
if 0 > days or days > 3:
    raise ValueError("days must be lower then 4 and more then 0")

class TLSAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_context=ctx)

session = requests.session()
session.mount('https://sunrint.sen.hs.kr/', TLSAdapter())

res = session.get('https://sunrint.sen.hs.kr/', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
})

school_menu_info = BeautifulSoup(res.text, 'html.parser').find('div', class_='school_menu_info')
dates = [date.text for date in school_menu_info.find_all('p', class_='date')]
menus = [re.sub(r'\s+', ' ', menu.text).strip() for menu in school_menu_info.find_all('p', class_='menu')]
menu_dict = dict(zip(dates[:days], menus[:days]))

for date, menu in menu_dict.items():
    print(f'{date}: {menu}')
