# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:02:26 2021

@author: nagas
"""

import requests
from bs4 import BeautifulSoup

r = requests.get("https://news.yahoo.co.jp/")

soup = BeautifulSoup(r.content, "html.parser")


# print(soup.select("h1"))

print(soup.find("ul", "newsFeed_list"))