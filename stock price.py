#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:31:46 2019

@author: ruiqing
"""

import quandl
quandl.ApiConfig.api_key = quandl.ApiConfig.api_key


def trading_signal(stiker):
    data = quandl.get(stiker)
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
    print(Result)
    return Result
