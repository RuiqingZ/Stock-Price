#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:31:46 2019

@author: ruiqing
"""
import quandl
quandl.read_key()
quandl.ApiConfig.api_key = quandl.ApiConfig.api_key
data = quandl.get('EOD/MSFT')

# days represents how many days have been starting from the first day the program starts
day = 1
# A represents 250 days moving average while B represents 50 days moving average
A_moving = 250
B_moving = 50

A_today_avg = data.Adj_Close.tail(A_moving).mean()
#print(A_today_avg)
A_yesterday_avg = (data.Adj_Close.tail(A_moving+day).sum()-data.Adj_Close.tail(day).mean())/A_moving
#print(A_yesterday_avg)

B_today_avg = data.Adj_Close.tail(B_moving).mean()
#print(B_today_avg)
B_yesterday_avg = (data.Adj_Close.tail(B_moving+day).sum()-data.Adj_Close.tail(day).mean())/B_moving
#print(B_yesterday_avg)

Result = ''

if A_yesterday_avg > B_yesterday_avg and A_today_avg > B_today_avg:
    Result = 'Doing nothing'
elif A_yesterday_avg < B_yesterday_avg and A_today_avg < B_today_avg:
    Result = 'Doing nothing'
elif A_yesterday_avg < B_yesterday_avg and A_today_avg > B_today_avg:
    Result = 'Selling signal'
else:
    Result = 'Buying signal'


# add a line to print data
print(data.Adj_Close.tail(day))    
print(Result)


from twilio.rest import Client

import config


client = Client(config.account_sid, config.auth_token)

message = client.messages \
                .create(
                     body=str(data.Adj_Close.tail(day))+Result,
                     from_='+12267985353',
                     to='+16478718675'
                 )

