#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:47:24 2020

@author: charles
"""


import requests

url = "https://www.python.org/"
resp = requests.get(url)

html = resp.text
print(html)
