#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:01:26 2020

@author: kimjanghyun
"""

import requests
import os
import json
import telegram

def telegram_send(chat_id,text):
    telegram_token='1222312662:AAHEP_Up0A6v9OmFtBRMV4pZvdghCXzZINo'
    bot=telegram.Bot(token=telegram_token)
    updates=bot.getUpdates()
    #1033674468
    return bot.sendMessage(chat_id=chat_id, text=text)

def get_data():
    #db에서 data 추출,playuser, 경기횟수, 세션타임, DAU