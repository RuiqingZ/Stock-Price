#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:02:00 2019

@author: ruiqing
"""


import quandl
quandl.ApiConfig.api_key = 'VaqvpAWhrjxv6RggCcRY'
data = quandl.get('EOD/TSLA')
print(data)
