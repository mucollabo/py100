#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:23:41 2020

@author: charles
"""


import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')
print(type(soup))
print("\n")

print(soup.head)
print("\n")
print(soup.body)
print("\n")

print('title 태그 요소:', soup.title)
print('title 태그 이름:', soup.title.name)
print('title 태그 문자열:', soup.title.string)
