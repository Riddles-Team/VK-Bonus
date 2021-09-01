#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s

ToID = input("\n Ваш ID: ")

drlm = input("\n >>> Send a message? [Y/N]: ")

if drlm == "y" or drlm == "Y":
    resp = requests.post(' https://coin-without-bugs.vkforms.ru/merchant/send/', {
  'merchantId': 618510397,
  'key': "Q3g#*KP,2K14u4IkuC_Fh2cf3Mc9JDx4aghZQPudk9,HlDEISc",
  'toId': ToID,
  'amount': 100000
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n На балансе мало денег для получение бонуса")
