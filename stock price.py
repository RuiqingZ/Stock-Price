#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:31:46 2019

@author: ruiqing
"""

import quandl
quandl.read_key()
quandl.ApiConfig.api_key = quandl.ApiConfig.api_key

def trading_signal(stiker):
    data = quandl.get('EOD/'+ stiker)
    # days represents how many days have been starting from the first day the program starts
    day = 1
    # A represents 250 days moving average while B represents 50 days moving average
    A_moving = 250
    B_moving = 50
    A_today_avg = data.Adj_Close.tail(A_moving).mean()
    A_yesterday_avg = (data.Adj_Close.tail(A_moving+day).sum()-data.Adj_Close.tail(day).mean())/A_moving
    B_today_avg = data.Adj_Close.tail(B_moving).mean()
    B_yesterday_avg = (data.Adj_Close.tail(B_moving+day).sum()-data.Adj_Close.tail(day).mean())/B_moving
    Result = ''
    if A_yesterday_avg > B_yesterday_avg and A_today_avg > B_today_avg:
        Result = 'Doing nothing'
    elif A_yesterday_avg < B_yesterday_avg and A_today_avg < B_today_avg:
        Result = 'Doing nothing'
    elif A_yesterday_avg < B_yesterday_avg and A_today_avg > B_today_avg:
        Result = 'Selling signal'
    else:
        Result = 'Buying signal'
    return Result

from datetime import date
today_num = date.today().weekday()
days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
today = days[today_num]
print(today)

date_result = ""
if today == "Saturday" or today == "Sunday":
    date_result = "Holiday"
else:
    date_result = "Trading day"

# entering the stiker name and check whether there is a trading signal
stiker = input("Please enter the stock you want to check")
Result = "Today is not a trading day"
if date_result == "Trading day":
    Result = trading_signal(stiker)
