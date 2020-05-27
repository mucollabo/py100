#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:33:15 2020

@author: charles
"""


import requests

url = "https://www.python.org/"
resp = requests.get(url)
print(resp)

url2 = "https://www.python.org/1"
resp2 = requests.get(url2)
print(resp2)
