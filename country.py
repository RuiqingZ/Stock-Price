# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



ticker = input("Please enter a ticker?")
import quandl
quandl.ApiConfig.api_key = 'VaqvpAWhrjxv6RggCcRY'
data = quandl.get('EOD/'+ ticker)
print(data)

