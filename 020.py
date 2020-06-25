#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 00:45:50 2020

@author: charles
"""


import pandas as pd

df = pd.read_csv('./data/bok_statistics_CD.csv', header = None)

print(df.head())
print('\n')
print(df.describe())
