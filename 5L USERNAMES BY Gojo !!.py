#تخمط_بس_ادكر_المصدر_تدكر_انو_في_شي_اسمه_يوم_القيامة
import webbrowser
webbrowser.open('https://t.me/Jacking_god')
import requests 
import random,datetime,sys 
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
W="\033[1;37m" # White
insta="1234567890qwertyuiopasdfghjklzxcvbnm"
all="qwertyuiopasdfghjkzxcvbnm"

#-------------------------start code ---------------------------#
def instaa(user):
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
'content-length':'85',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?0',
'x-instagram-ajax':'81f3a3c9dfe2',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'x-asbd-id':'198387',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'sec-ch-ua-platform':'"Linux"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
    if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
        print(W+f" [+] {Z} ErRoR UsEr : {X}{user} ")
    elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
        print(W+f" [+] {Z} Bad user ➯ {X}{user} ")
    else:
        email=0
        print(W+f" [+] {F} Good User ➯ {C}{user} ")
        email+=1
        god=f""" ❤️‍🔥 𝙃𝙚𝙮 𝙢𝙖𝙣 𝙔𝙤𝙪 𝙜𝙤𝙩 𝙖 𝙣𝙚𝙬 5𝙡 𝙪𝙣𝙪𝙨𝙚𝙙 𝙄𝙣𝙨𝙩𝙖 𝙪𝙨𝙚𝙧𝙣𝙖𝙢𝙚 ❤️‍🔥 @Wasgojo✅
←•━━━━━━━━━━━━•→
💥 𝙪𝙣𝙪𝙨𝙚𝙙 𝙪𝙨𝙚𝙧𝙣𝙖𝙢𝙚 ➠ {user}
←•━━━━━━━━━━━━•→
💁🏼‍♂️ 𝐁𝐘 » @Wasgojo  - @Jacking_god"""
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={god}')
def users():
    ran1="1234567890..__qwertyuiopasdfghjklzxvcbnm__.."
    while True:
	       v1 = str(''.join((random.choice(insta) for i in range(1))))
	       v2 = str(''.join((random.choice(insta) for i in range(1))))
	       v3 = str(''.join((random.choice(insta) for i in range(1))))
	       v4 = str(''.join((random.choice(insta) for i in range(1))))
	       v5 = str(''.join((random.choice(all) for i in range(1))))
	       user1 = (v5+v1+v2+v3+v4)
	       user2 = (v1+v5+v2+v3+v4)
	       user3 = (v1+v2+v5+v3+v4)
	       user4 = (v1+v2+v3+v5+v4)
	       hamo010 = (user1, user2, user3, user4)
	       user = random.choice(hamo010)
	       instaa(user)
id=input(f"{X} ➠TEL ID {C}")
token=input(f"{X} ➠BOT TOKEN {C}")
print()	
users()

#تخمط_بس_ادكر_المصدر_تدكر_انو_في_شي_اسمه_يوم_القيامة
Wasgojo
