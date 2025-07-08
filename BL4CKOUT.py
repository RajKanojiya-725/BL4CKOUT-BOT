import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# === Bot Setup ===
BOT_TOKEN = '7645679923:AAGvhoQn41cbDwT66lg09od3N3XpAh2LwXo'
your_channel = 'BL4CKOUT_EMPIRE'


bot = telebot.TeleBot(BOT_TOKEN)
user_states = {}

# === Helper Function ===
def send_coming_soon(chat_id, text, html=True):
    max_len = 4096  # Telegram's message length limit
    parts = [text[i:i+max_len] for i in range(0, len(text), max_len)]
    
    for part in parts:
        if html:
            bot.send_message(chat_id, part, parse_mode="HTML")
        else:
            bot.send_message(chat_id, part, parse_mode="Markdown")
# === Menus ===
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("📌 About Admin"))
    markup.add(KeyboardButton("🔥 Banning Sikhni Hai?"))
    return markup

def banning_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("✅ YES"), 
               KeyboardButton("❎ NO"))
    markup.row("🔙 Back Menu", "🏠 Main Menu")
    return markup

def banning_steps_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("🔜 NEXT"))
    markup.add(KeyboardButton("BANNING BASICS ~"), 
               KeyboardButton("ADVANCED METH ~"))
    markup.add(KeyboardButton("CB METH ~"), 
               KeyboardButton("IMPER ACC ~"))
    markup.add(KeyboardButton("ALL BANNING FORMS ~"), 
               KeyboardButton("ALL UNBAN FORMS ~"))
    markup.add(KeyboardButton("HARD OG METH ~"))
    markup.row("🔙 Back Menu", "🏠 Main Menu")
    return markup

def cb_meth_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("CB PATCH METH ~"), 
               KeyboardButton("CB ENABLE ~"))
    markup.add(KeyboardButton("CB METHS ~"), 
               KeyboardButton("BEST I'D FOR CB ~"))
    markup.row("🔙 Back Menu", "🏠 Main Menu")
    return markup

def next_page_1():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("NEXT ➡"))
    markup.add(KeyboardButton("NEW BANNER ~"), 
               KeyboardButton("88 NEW METH ~"))
    markup.add(KeyboardButton("OTHER METH ~"), 
               KeyboardButton("POWERFUL METH ~"))
    markup.add(KeyboardButton("1 MIN LOCK METH ~"), 
               KeyboardButton("PERMA BAN METH ~"))
    markup.add(KeyboardButton("FREE WEB HOSTING ~"))
    markup.row("🔙 Back Menu", "🏠 Main Menu")
    return markup

def next_page_2():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("NEXT 🔜"))
    markup.add(KeyboardButton("FF METH ~"), 
               KeyboardButton("ANIME METH ~"))
    markup.add(KeyboardButton("BOT METH ~"), 
               KeyboardButton("PAID GIRL METH ~"))
    markup.add(KeyboardButton("JACKING ~"),
               KeyboardButton("FYTER BANEGA? ~"))
    markup.add(KeyboardButton("LONG BIO METH ~"))
    markup.row("🔙 Back Menu", "🏠 Main Menu")
    return markup


def next_page_3():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("NEXT :-"))
    markup.add(KeyboardButton("FAN PAGE METH ~"),
               KeyboardButton("INCREASE OG METH ~"))
    markup.add(KeyboardButton("STORY REMOVE METH ~"),
               KeyboardButton("YT BAN METH ~"))
    markup.add(KeyboardButton("WP BAN METH ~"),
               KeyboardButton("SNAP BAN METH ~"))
    markup.add(KeyboardButton("REPORT RESTORATION ~"),
               KeyboardButton("PATCH ID ~"))
    markup.add(KeyboardButton("REMOVE VIO ~"))
    markup.row("🔙 Back Menu", "🏠 Main Menu")
    return markup
    

def jacking_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("JACKING FILE ~"),
               KeyboardButton("PIP + PYDROID 3 APK + VPN ~"))
    markup.add(KeyboardButton("UNLIMITED GMAILS ~"),
               KeyboardButton("5L FILE ~"))
    markup.row("🔙 Back Menu", "🏠 Main Menu")
    return markup


def fyter_banega_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("KEYBOARD LEGA ~"),
               KeyboardButton("GALI SPAM LEGA ~"))
    markup.add(KeyboardButton("CP HANGER LEGA ~"),
               KeyboardButton("RDP LEGA LALA ~"))
    markup.row("🔙 Back Menu", "🏠 Main Menu")
    return markup


def gali_spam_lega_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("GALI 1 ~"),
               KeyboardButton("GALI 2 ~"))
    markup.add(KeyboardButton("GALI 3 ~"),
               KeyboardButton("GALI 4 ~"))
    markup.add(KeyboardButton("GALI 5 ~"),
               KeyboardButton("GALI 6 ~"))
    markup.add(KeyboardButton("GALI 7 ~"),
               KeyboardButton("GALI 8 ~"))
    markup.add(KeyboardButton("GALI 9 ~"),
               KeyboardButton("GALI 10 ~"))
    markup.row("🔙 Back Menu", "🏠 Main Menu")
    return markup
    

def cb_meth_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("CB PATCH METH ~"), 
               KeyboardButton("CB ENABLE ~"))
    markup.add(KeyboardButton("CB METHS ~"), 
               KeyboardButton("BEST I'D FOR CB ~"))
    markup.row("🔙 Back Menu", "🏠 Main Menu")
    return markup

# === /start Command ===
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    try:
        status = bot.get_chat_member(f"@{your_channel}", user_id).status
        if status in ['member', 'administrator', 'creator']:
            user_states[user_id] = 'main_menu'
            bot.send_message(message.chat.id, "👋 Welcome to BL4CKOUT BOT!", parse_mode="Markdown")
            bot.send_message(message.chat.id, "👇 Here's your main menu:", reply_markup=main_menu())
        else:
            raise Exception("Not Joined")
    except:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📣 Join our Channel", url=f"https://t.me/{your_channel}"))
        markup.add(InlineKeyboardButton("✅ I've Joined", callback_data="check_joined"))
        bot.send_message(message.chat.id, "⚠ Please join our official Telegram channel to continue.", parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "check_joined")
def check_joined(call):
    user_id = call.from_user.id
    try:
        status = bot.get_chat_member(f"@{your_channel}", user_id).status
        if status in ['member', 'administrator', 'creator']:
            user_states[user_id] = 'main_menu'
            bot.answer_callback_query(call.id, "✅ Verified! You're in.")
            bot.send_message(call.message.chat.id, "👇 Here's your main menu:", reply_markup=main_menu())
        else:
            bot.answer_callback_query(call.id, "⛔ You haven't joined yet!")
    except:
        bot.answer_callback_query(call.id, "❌ Couldn't verify. Try again later.")

# === Main Handler ===
@bot.message_handler(func=lambda msg: True)
def handle_message(msg):
    user_id = msg.from_user.id
    text = msg.text

    if user_id not in user_states:
        user_states[user_id] = 'main_menu'

    current_state = user_states[user_id]

    if text == "📌 About Admin":
        bot.send_message(msg.chat.id,
            "👑 Admin Info:\n\n📱 Telegram: [@Lustrix_me](https://t.me/Lustrix_me)\n📸 Instagram: [@Lustrix.me](https://instagram.com/Lustrix.me)",
            parse_mode="Markdown",
            reply_markup=banning_steps_menu()
        )

    elif text == "🔥 Banning Sikhni Hai?":
        user_states[user_id] = 'banning_menu'
        bot.send_message(msg.chat.id, "🔥 Choose an option:", reply_markup=banning_menu())

    elif text == "✅ YES":
        user_states[user_id] = 'banning_steps'
        bot.send_message(msg.chat.id, "💀 Let's begin with the basics:", reply_markup=banning_steps_menu())

    elif text == "❎ NO":
        bot.send_message(msg.chat.id, "🤣 Toh yaha timepass karne aaya hai kya?", reply_markup=banning_menu())

    elif text == "🔜 NEXT":
        user_states[user_id] = 'next_page_1'
        bot.send_message(msg.chat.id, "🔜 NEXT", reply_markup=next_page_1())

    elif text == "NEXT ➡":
        user_states[user_id] = 'next_page_2'
        bot.send_message(msg.chat.id, "NEXT ➡", reply_markup=next_page_2())

    elif text == "NEXT 🔜":
        user_states[user_id] = 'next_page_3'
        bot.send_message(msg.chat.id, "NEXT 🔜", reply_markup=next_page_3())
   
    elif text == "CB METH ~":
        user_states[user_id] = 'cb_meth_menu'
        bot.send_message(msg.chat.id, "🧠 CB Methods here:", reply_markup=cb_meth_menu())

    elif text == "JACKING ~":
        user_states[user_id] = 'jacking_menu'
        bot.send_message(msg.chat.id, "JACKING ~", reply_markup=jacking_menu())

    elif text == "GALI SPAM LEGA ~":
        user_states[user_id] = 'gali_spam_lega_menu'
        bot.send_message(msg.chat.id, "GALI SPAM LEGA LAULE 🤣 ~", reply_markup=gali_spam_lega_menu())


    elif text == "FYTER BANEGA? ~":
        user_states[user_id] = 'fyter_banega_menu'
        bot.send_message(msg.chat.id, "JACKING ~", reply_markup=fyter_banega_menu())
    

    elif text == "JACKING FILE ~":
        bot.send_message(msg.chat.id, "📁 Sending Jacking Files...")

        with open("Jacking-File.py", "rb") as file1:
            bot.send_document(msg.chat.id, file1)

        with open("NEW ( 2K12 -- 2K13 HUNTER) BY RAZA.py", "rb") as file2:
            bot.send_document(msg.chat.id, file2)

        with open("Jacking_Gmail_by_@Bl4ck_Ch4tan.py", "rb") as file3:
            bot.send_document(msg.chat.id, file3)


    elif text == "PIP + PYDROID 3 APK + VPN ~":
        with open("all pip for jacking.py", "rb") as file4:
            bot.send_document(msg.chat.id, file4)

            bot.send_message(msg.chat.id, """ PYDROID DIRECT LINK
https://en.mrproblogger.com/pydroid """)

            bot.send_message(msg.chat.id, """ VPN DIRECT LINK
https://en.mrproblogger.com/eAJni""")

    
    elif text == "5L FILE ~":
        with open("5L USERNAMES BY Gojo !!.py", "rb") as file:
            bot.send_document(msg.chat.id, file)


    elif text == "RDP LEGA LALA ~":
        bot.send_message(msg.chat.id, """ YOUTUBE VIDEO LINK
                         https://en.mrproblogger.com/ip0iIM """)

        bot.send_message(msg.chat.id, """ GITHUB LINK
                         https://en.mrproblogger.com/BL4CKOUT """)

        bot.send_message(msg.chat.id, """NGROK LINK
                         https://en.mrproblogger.com/Onfw0E""")

        bot.send_message(msg.chat.id, """
Username- runneradmin
Password- P@ssw0rd!

NGROK_AUTH_TOKEN """)
    
    
    # === Banning Step Buttons ===
    elif text == "BANNING BASICS ~":
        send_coming_soon(msg.chat.id, """🚨 REPORTING MASTERLIST 🔥 | CLEAN THE TOXIC ZONE 💯

📍If you see ANY of these in BIO / USERNAME / POSTS / STORIES — REPORT FOR THE RIGHT REASON 👇


---

💠 HATE / TOXICITY

Words like:
devil, 666, savage, hate, followers, seller, dick, ban, banned, abuse, method etc.

🧨 These words indicate hate, dark themes, and potentially abusive behavior. Report under: Hate Speech / Harmful content


---

🥹 SELF-HARM / SUICIDAL SIGNS

Words like:
suicide, blood, death, kill myself, depressed, I want to die, etc.

🆘 Report under: Self-injury or suicide prevention – this can trigger others.


---

🌚 BULLYING / HARASSMENT

If you or your friend’s username is getting targeted in:

Posts

Stories

Bio

Mentions or shady tagging


⚠ Even memes targeting someone = Bullying


---

🥵 VIOLENT / EXTREMIST STUFF

Words or images like:
Hitler, Osama Bin Laden, weapons, soldiers, guns, masks, ISIS, flags, riots, bombs, etc.

Report as: Violence or Dangerous Organizations


---

🧪 DRUGS / ILLEGAL STUFF

Images or mentions of:
drugs, cocaine, weed, syringes, pills, marijuana leaves, “plug” bio, medicine emojis, etc.

Report under: Sale or use of illegal or regulated goods


---

🤡 FAKE IDENTITY / CELEB IMPERSONATION

When someone:

Uses celeb pic or name in username

Blue tick celeb name in bio

Pretending to be a verified person


Report as: Pretending to be someone else → Celebrity or Public Figure


---

☠ NUDITY / SEXUAL CONTENT

Words like:
sex, nudes, send nudes, 18+, OnlyFans, hot pic, etc.
Or nude/sexual posts/stories/profile pic.

Report as: Sexual Activity / Nudity / Adult Content


---

🏆 SPAM / SCAM

Red flags:

Phone numbers in bio or captions

Repeated posts

“DM me for followers / giveaway / crypto / methods”


Report as: Spam or Scam


---

✅ PRO STRATEGY:

👉 Want better results?

First report stories individually (as Hate/Bully/etc.)

Then report the profile for the same categories — but multiply it (e.g., 10x Hate, 5x Bully)



---

🧠 PRO TIP:

Use Old Accounts like 2K12 / 2K13 IG IDs — their reports are taken way more seriously and reviewed faster.


---

🚨 REMINDER:

Accounts without any violations CANNOT be removed easily!
So always look for stories, bios, or old posts for violations — and target those first 🕵


---

🔍 TO CHECK IF ACCOUNT GOT REVIEWED:

Go to → instagram.com/settings/help/
OR
Use Insta Lite / Insta X to check report review status.


---

🔥 FINAL LINE (Add this to your bio if you want):

> 🧨 Reporting isn’t hate, it’s digital justice. Clean the trash. Protect the vibe. 🔥""")
        
    elif text == "ADVANCED METH ~":
        send_coming_soon(msg.chat.id, """🚨💣 Instagram Reporting Master Plan – Ultimate Guide 💣🚨

(For Target Removal | Real & Working Country + Special Methods)

🧠 Purpose: Takedown of Toxic / Fake / Abusing / Violating Accounts
📌 Works best on targets under 20K Followers
📍 Use 2K12 / 2K13 Old IG IDs for max power
🌍 Always use VPN of the country of the method
📲 Check ban status: instagram.com/settings/help/


---

✅ 88 METHOD (🇩🇪 Germany – Nazi Reference)

If username has "88" (common in hate/Nazi IDs):

🔹 Using 2K12/2K13 Account

5x Hate

10x Self-Injury

15x Dangerous Organizations

2x Spam


🔹 Using Normal Account

2x Self

2x Hate

1x Pornographic Content

1x Child Nudity



---

🇫🇷 France Method

4x Self-Injury

1x Nudity (Option 3)

2x Drug Use

5x Hate



---

🇳🇱 Netherlands Method

2x Spam

3x Hate

1x False Info

2x Nudity (Option 1)

3x Dangerous Content

4x Self

2x Bullying (Mentioning Me)

1x Scam

1x False Report



---

🇹🇷 Turkey Method 2022

4x Self-Injury

3x Nudity (Option 4)

10x Hate

1x Violence



---

🇪🇸 Spanish Method

3x Dangerous Organizations

6x Self

2x Hate

3x Bullying

1x Hate (again)

1x False

2x Sale (Option 2)



---

🇦🇪 Arab Method

4x Self

3x Hate

2x Nudity (Option 2)

3x Child Nudity

1x Self



---

🇦🇱 Albanian Method

Last Post → 4x Violence

Another Post → 6x Hate

Highlight → Self-Injury

Another Highlight → Self

Profile Report → 1x Self, 1x Drug



---

🇮🇳 India Method

2x Self

1x Bullying (Option 1)

2x False Info

2x Violence (Option 3)



---

🧨🔥 MASTER STRATEGY TIPS:

🚫 Story Removal Trick (WORKS EVEN IF ACCOUNT IS CLEAN)

If target profile has no violations in bio/posts:

1. First report their story multiple times (for Hate / Bully / Self)


2. Then report the account as if you saw those things in the profile

e.g. If you removed 5 stories for hate, do 10x Hate on profile report.




💣 Force Instagram to think account is repeat violator.


---

🧠 Smart Reporting Tactics:

📲 Don’t use same report combo in the same time window. Space it 1-2 mins apart.

🔁 Use multiple accounts (2-3 max, not more to avoid shadowban)

🧾 Keep screenshots of your report summary

⚙ Clear Instagram cache before and after session

🎯 Report specific content (highlight/post/story) first, THEN account



---

🛑 Do Not Do This (Important):

❌ Don’t report randomly without checking for signs — it weakens the method

❌ Don’t share the same account too many times in same IG DM — triggers auto-protection

❌ Don’t use fake VPN or unknown apps — Instagram detects IP mismatch



---

⚠ If Method Not Working:

Try imped method (removal after few hours delay)

Use Lite / X app version to boost review

Switch to different country method next day

Use different 2K12/13 ID for another shot



---

✅ FINAL WORDS:

> “This isn’t hate, it’s digital karma. Remove toxicity, keep the space clean.” 🔥
“We don’t mass report — we precision strike 💣.”""")
        
    elif text == "IMPER ACC ~":
        send_coming_soon(msg.chat.id, """🎭 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐈𝐌𝐏𝐄𝐑𝐒𝐎𝐍𝐀𝐓𝐈𝐎𝐍 (IMPER) 𝐌𝐄𝐓𝐇𝐎𝐃 🔥

Updated for 2025 | Profile-based & Color Impersonation Working ✅


---

🧠 WHAT IS IT?

Instagram triggers auto-review when an account looks like it’s pretending to be someone else (IMPERSONATION) — this method uses profile types, usernames, bios, and themes to exploit that system.

---SS

🔍 Profile-Based Impersonation Targets

@c – 3x IMP  
One-letter usernames get flagged quickly.

@suitshop – 3x IMP  
Users with pantsuit/formal outfit pfp → impersonating business figure.

@ppzmovie – 3x IMP  
Users with zombie/horror movie content → impersonate horror film pages.

@dogfoodz – 3x IMP  
Users selling dogs/pet food → impersonating product brands.

@vforvoid – 3x IMP  
Accounts with hacker mask, Guy Fawkes mask → impersonating hacktivists.

@sportsdirectme – 3x IMP  
If bio has “support”, “team”, “official” → impersonating brand help.

@trippieredd – 3x IMP  
No profile picture + YouTube link → impersonating artists/public.

@story – 3x IMP  
Last viewer in someone’s story list → use as “team watcher”.

@changedotorg – 3x IMP  
Fake org lookalikes with .org name → impersonating activism sites.

@supportandfeed – 3x IMP  
Anyone with “support” in username/bio → team impersonation.

@playboicarti – 3x IMP  
No pfp/post/bio → report with aged ID (2012–13) for better hit.

@ar7nly – 3x SELF + 1x IMP @kendricklamar  
Plain black pfp → Color impersonation method


---

🎨 Color-Based IMPER Method (PFP Based)

Use if target's profile picture is majorly a specific color 🎯

🔴 Red PFP

@ryder_ripps  
@diddy

🟠 Orange PFP

@pppiccioli  
@sterlingruby  
@heronpreston  
@headspace

⚪ White PFP

@erl__  
@therealmikedean  
@490tx  
@erl__kids  
@luvadepedreiro  
@lilshop  
@kevinabstract  
@torylanez

🟣 Purple PFP

@purple

⚫ Black PFP

@kendricklamar  
@dababy  
@shots


---

🧠 BONUS TRICKS:

Use PicsArt or Instagram Pro to make your pfp match theirs

If target has @meta or @support in bio → use "Impersonating Meta/Support"

Always mix 3x IMP with 1x Meta Imp + 1x Zuck if needed

Use different VPN locations per report (USA, Germany, France 🔥)



---

✅ HOW TO REPORT:

🧾 Go to Profile → Report →
🔘 Impersonating Someone
→ Choose: “Public Figure / Celebrity” OR “Me” (if cloning)
→ For Meta staff targets: “Someone at Meta”
→ Add real page name like @kendricklamar in note if allowed


---

🔚 FINAL HIT:

Use this combo for best result:

3x IMP (Public Figure)

2x Vio or Self

1x Meta Imp

Use 2012–2016 IDs for strong signal

VPN ON = Better impact 🔥""", html=True)
        
    elif text == "ALL BANNING FORMS ~":
        send_coming_soon(msg.chat.id, """⚠ 1. Violation Form

📎 Link: https://help.instagram.com/contact/383679321740945

🧾 Message to Paste:

Dear Instagram Team,

I would like to report the account @target due to repeated violations of your community standards. This profile appears to be engaging in spam-like behavior, possibly linked with automated tools or unauthorized third-party services. Its content includes potentially harmful material that seems to exploit loopholes in Instagram’s filters.

For the safety of the community and platform integrity, I kindly urge you to conduct a thorough review and take appropriate enforcement action.

Thank you for your support.

✅ Use When: Target is posting spam, automation content, 3rd party tool suspect.


---

⚠ 2. Bullying / Harassment Form

📎 Link: https://help.instagram.com/contact/188391886430254

🧾 Message to Paste:

To Instagram Moderation Team,

I am reaching out because the user @target has forced me to deactivate my own Instagram account due to constant harassment and threatening messages directed at me and my family.

I’m deeply concerned for our safety and sincerely request immediate intervention and removal of this account.

Sincerely,  
A concerned user

✅ Use When: You're claiming the target caused bullying, threats, or emotional damage.


---

⚠ 3. Human PFP / Impersonation Form

📎 Link: https://help.instagram.com/contact/636276399721841

🧾 Message to Paste:

Dear Instagram,

This account (@target) is impersonating me. The user has copied my profile picture, name, and other details in an attempt to appear as me.

I request an immediate investigation and takedown of this impersonating profile. Thank you for your support.

Kind regards.

✅ Use When: Target has a human face pfp or mimicking your identity.


---

⚠ 4. Sex Offender Report Form

📎 Link: https://help.instagram.com/contact/334013860059654

🧾 Message to Paste:

Hi Instagram,

The user @target appears to be sharing inappropriate or sexually explicit material, which is not only against your terms but also potentially harmful to underage audiences.

Please take action and review this account for violation of your sexual content policy.

Thank you.

✅ Use When: Target posts nudity, sexual jokes, or adult behavior in public view.


---

⚠ 5. Copyright Violation Form

📎 Link: https://help.instagram.com/contact/552695131608132

🧾 Message to Paste:

Hello Instagram,

I have identified that the account @target is using copyrighted content that they do not own or have permission for. This includes images, videos, and branding materials.

Please investigate and take appropriate action under your copyright enforcement policy.

Best regards.

✅ Use When: Target is using logos, watermarked edits, stolen reels, anime scenes with watermark.


---

⚠ 6. Underage Account Report Form

📎 Link: https://help.instagram.com/contact/723586364339719

🧾 Message to Paste:

Hello,

This account @target belongs to someone under the age of 13, which violates Instagram’s age policy.

Please take the necessary steps to verify and disable this account if proven true.

Thank you.

✅ Use When: Suspect account of kids pretending to be older (e.g., “13 y/o gang” in bio, childish behavior).


---

⚠ 7. India Grievance Officer Form

📎 Link: https://help.instagram.com/contact/779201836048501

🧾 Message to Paste:

Dear Instagram India Grievance Officer,

I would like to file a complaint regarding the account @target, which is continuously violating community guidelines and spreading offensive, misleading, or harmful content.

As per Indian IT Rules 2021, I request your assistance in taking down this account after a thorough investigation.

Regards,
Indian User

✅ Use When: You’re from India, and account is disturbing or politically sensitive.


---

⚠ 8. Memorialize Account (Death Certificate Method)

📎 Link: https://help.instagram.com/contact/1474899482730688

📝 Steps:

1. Go to:
https://www.pdffiller.com/40879334-fillable-jamaican-death-certificate-pdf-form


2. Also use:
https://www.signnow.com/fill-and-sign-pdf-form/9495-certificate-of-live-birth-template-form
                         





3. Fill the Memorial Form using above documents


4. Message to paste:



Hello sir, this person has passed away due to COVID-19 and someone else is using their account. I humbly request you to memorialize it. Thank you.

✅ Use When: You want to permanently lock an account by faking death certificate.


---

✅ BONUS: HOW TO DO IT RIGHT (Steps)

1. 🔍 Gather Target Info: Username, Bio, PFP, Posts, Stories


2. 📸 Take Screenshots (in case needed later)


3. 🌐 Use VPN (Target’s country or India if local)


4. 🧠 Pick Right Form from above based on content


5. 📝 Paste Relevant Message and submit


6. 📬 Wait for Reply / Action within 24–72 hrs


7. ❌ If IG says ‘Not Removed’ → retry with stronger method or alt form """)

    elif text == "ALL UNBAN FORMS ~":
        send_coming_soon(msg.chat.id, """✅ UNBAN APPEAL FORMS – COPY-PASTE WITH LINK ✅

📎 UNBAN Form (Facebook Mobile View):
https://m.facebook.com/help/contact/241600464824952

📎 UNBAN Form (Instagram Mobile View):
https://m.instagram.com/help/contact/241600464824952


---

🔓 Professional Message for Legit Unban Appeal:

"Hello Instagram Team,

My account was recently disabled, and I believe this action may have been taken by mistake. I have always made sure to follow Instagram’s Community Guidelines and Terms of Use.

I kindly request a detailed review of the account and a chance to restore access. If any specific issue led to the ban, I would appreciate being informed and I’m more than willing to correct or remove any content if needed.

Please help me recover access to my account. Thank you for your time and understanding.

Regards,  
[Your Full Name]  
[Registered Email]  
[Username]"


---

⚠ UNBAN Message (If the account was reported falsely or mass reported):

"Dear Instagram,

My account was recently taken down due to false reports or mass reporting. I assure you that I have not violated any guidelines or terms. It seems like someone intentionally targeted my profile using fake reports.

Please review my account and the decision. I kindly request a reactivation as I’ve always respected the rules of the community.

Thank you for reviewing my request.

Sincerely,  
[Your Name]  
[Username]  
[Email Linked to Account]"


---

📢 TIPS FOR BETTER UNBAN CHANCE:

Use original email & username as registered

Keep your language calm and respectful

Don't spam the form. Submit once, wait 24–48 hrs

Use real reason, don’t fake too much or they'll flag again

Use same device where you last logged in (IP match helps)



---

🔥 Bonus: Use this if account was hacked before ban:

"Hello Instagram Support,

My account may have been compromised before it was disabled. I noticed suspicious activity, and shortly after, I lost access.

I request a manual review and recovery of the account. I'm happy to verify my identity or provide any needed documents to prove ownership.

Thank you for your help.

[Full Name]  
[Username]  
[Linked Email]"

""")

    elif text == "HARD OG METH ~":
        send_coming_soon(msg.chat.id, """💣 𝗛𝗔𝗥𝗗 𝗢𝗚 𝗠𝗘𝗧𝗛𝗢𝗗 – 2025 FINAL VERSION 💣


🔥 STEP 1: Ban Attack via Bots

🔹 Use 30+ clean bots (with 0 posts, 0 followers, fresh login)
🔹 All bots should report the same target using this pattern:

🔞 10x Nudity (Option 3rd)

☠ 5x Self-Injury / Suicide / Death

🗯 5x Hate Speech / Violence


📌 Do this within 15-20 minutes for high-impact.


---

⚠ STEP 2: Disable Your Own Account

Go to your profile → Settings → Deactivate/Disable Account

Reason: "Just need a break"

Wait for exactly 1 hour ⏳
(Don’t open Instagram in that time)



---

✅ STEP 3: Re-Enable Your Account

Log in again after 1 hour

IG system now flags your account for internal review

Proceed immediately to mail step



---

📩 STEP 4: Send Mail To Meta Support

Send To:
📧 support@instagram.com or via contact form
📎 Link (Unban form): https://m.instagram.com/help/contact/241600464824952


---

✉ Email Text (Fully Rewritten & Professional)

"Subject: Request for Priority Review of My Instagram Account

Dear Instagram (Meta) Team,

My name is (Your Full Name), and my account username is @yourusername.  

For the past few days, I’ve seen several suspicious profiles on the platform involved in spam, impersonation, and offensive activities. As a responsible user, I’m requesting a quick and thorough review of my account to ensure it remains secure and compliant with your guidelines.

I’ve always used Instagram fairly and would really appreciate your support in making sure everything is safe on my profile.

Thanks a lot for your time and help.

Best regards,  
(Your Name)  
Username: @yourusername "

🧠 Use your real registered name & email that’s linked to your IG account.


---

🧠 PRO TIPS:

Use a VPN when banning the target (USA, Germany, France = strong filters)

Do reporting between 2 AM – 5 AM (Instagram’s low moderation window)

Don’t change your username/bio after reactivation

If Meta replies “We didn’t remove” → wait 48h and retry method



---

📌 EXTRA UNBAN TOOLS (For Backup):

📋 Form Name	
    🔗 Link

🔓 Unban Form (Meta)	
    https://m.instagram.com/help/contact/241600464824952
                         
⚖ Violation Review	
    https://help.instagram.com/contact/383679321740945
                         
🙎 Human PFP / Impersonate
    https://help.instagram.com/contact/636276399721841
                         
🧒 Underage Report	
    https://help.instagram.com/contact/723586364339719
                         
⚠ Bullying / Threat Form	
    https://help.instagram.com/contact/188391886430254
                         
⚰ Memorial Form (Fake Death)	
    https://help.instagram.com/contact/1474899482730688


""")

    # === NEXT Page 1 Buttons ===
    elif text == "NEW BANNER ~":
        send_coming_soon(msg.chat.id, """💥 𝐍𝐄𝗪 𝐁𝐀𝐍𝐍𝐄𝐑𝐒 — 𝗪𝐎𝐑𝐊𝐈𝐍𝐆 𝐑𝐄𝐏𝐎𝐑𝐓 𝐓𝐑𝐈𝐆𝐆𝐄𝐑𝐒 💥

📌 If you find these words or content in Bio / Username / Story / Posts — REPORT as per below:


---

🔷 HATE

🧨 Words like:
devil, 666, savage, love, hate, followers, selling, sold, seller, dick, ban, banned, free, method, paid
➡ Report Category: Hate Speech / Harassment


---

😢 SELF HARM

🩸 Words like:
suicide, blood, death, dead, kill myself, cut, depressed, etc.
➡ Report Category: Self-Harm / Threats to Life


---

🧨 BULLYING

📍 If you or someone else (@mention) is targeted in:

Their story

Their post captions

Or in bio
➡ Report Category: Bullying or Harassment → "Someone I know"



---

🪖 VIOLENCE / TERRORISM

🔫 Words/images related to:
Hitler, Osama bin Laden, guns, bombs, AK-47, soldiers with weapons, masked men, flags of terror orgs
➡ Report Category: Violence / Dangerous Organization / Threats


---

🌿 ILLEGAL / DRUG CONTENT

💊 Images or text like:
drugs, cocaine, weed, marijuana, plants, syringe, medicines, pill emojis, drug leaf icons
➡ Report Category: Sale or Promotion of Illegal Drugs


---

🎭 IMPERSONATION / FAKE IDENTITY

🧑‍🎤 If PFP or Username looks like:

A celebrity

A verified blue tick account

Famous influencer
OR

Bio contains name of a real celebrity with a blue tick
➡ Report Category: Impersonation → Public Figure / Celebrity



---

🚫 NUDITY / SEXUAL CONTENT

🍑 Words like:
nude, send nudes, sex, horny, OnlyFans, or any porn references
OR
📸 PFP / Posts showing nudity, sexual behavior, or adult content
➡ Report Category: Nudity / Pornographic Content


---

🧠 PRO TIP:
After reporting — check review status at:
🔗 https://instagram.com/settings/help
Or use Insta X / Insta Lite for faster review update.


---

💣 BONUS TIP:
Accounts with none of these violations are harder to ban directly —
➡ In such case:
Remove 4–5 stories (as hate/bully)
Then report profile as 10x hate or 10x bully for stronger chance """)
        
    elif text == "88 NEW METH ~":
        send_coming_soon(msg.chat.id, """🇩🇪 𝟖𝟖 METH (NEW) — GERMAN ACCOUNT TARGET METHOD 🔥

> Working | High Ban Rate | Step-by-Step Format




---

🎯 TARGET:

Accounts with 88 in their username, usually belonging to German users or suspected extremist/bot accounts.

➤ Example Usernames:
@hitler88, @xx88xx, @germanpower88, etc.
✅ These are flagged easily under Hate / Org reports.


---

🛠 STEP-BY-STEP REPORTING:


---

👑 From a 2012/2013 Aged Account:

🔹 5x Hate Speech or Symbols
🔹 10x Self-Harm (User might harm themselves)
🔹 15x Dangerous Organization (Terrorist or hate group)
🔹 2x Spam or Scam

✅ Use Insta Lite / Insta X
✅ Use VPN set to Germany (🇩🇪)
✅ Wait 3–5 seconds between reports
✅ Use only one aged ID per 1 target for best result


---

👤 From Normal Account:

🔸 2x Self-Harm
🔸 2x Hate Speech
🔸 1x Nudity or Pornography
🔸 1x Nudity involving a Child (Option 3 under Nudity)

✅ This adds pressure on the backend filters
✅ Combine with aged account method for high success


---

⚙ ADDITIONAL TIPS:

✔ Don’t overreport in 1 minute. Spread it out
✔ Always remove a few stories/posts before profile report
✔ You can check review at:
👉 https://instagram.com/settings/help

✔ Works better on:

Low engagement accounts

No mutuals

Suspicious bios/usernames



---

🎯 EXPECTED RESULT:

⏱ Within 1–3 hours, account goes into Review or Lock
🔐 High chance of full disable if all steps are done properly """)

    elif text == "OTHER METH ~":
        send_coming_soon(msg.chat.id, """🧿 𝗙𝗔𝗡 𝗣𝗔𝗚𝗘 𝗠𝗘𝗧𝗛 ~ 🥶

> Target: Fake fanpages impersonating verified accounts




---

🔍 Steps:

🔹 6x Impersonation
➤ Choose “Impersonating someone I know”, then select @realpage (verified username) like @arianagrande or @viratkohli

🔹 4x Hate Speech or Symbols
➤ Report for hateful/abusive content in bio/post/story


---

💡 Tips:

✅ Works best when the fanpage uses celeb name/pfp
✅ Use aged account (2013, 2012) for higher strike
✅ Use VPN: USA or Global


---

🚨 Result:

🔒 Account goes under review → High disable chance within hours


---


---

💋 𝗣𝗔𝗜𝗗 𝗚𝗜𝗥𝗟 𝗠𝗘𝗧𝗛 ❤

> Target: NSFW or semi-paid model pages




---

🔍 Steps:

🔹 3x Nudity → Option 3 (involving a child)
🔹 2x Violence → Option 4 (physical abuse)


---

💡 Tips:

✔ Report NSFW words in bio like “OnlyFans”, “DM me”, “Selling”
✔ Use Insta Lite / X for fast response
✔ Use VPN: France, India or Germany


---

🚨 Result:

🔐 High chance of temporary lock → repeated hits = PERMA ban


---


---

❄ 𝗦ɴᴏᴡʏ 𝗠𝗘𝗧𝗛𝗢𝗗

> Target: Adult / dirty meme / anonymous accounts




---

🔍 Steps:

🔹 5x Nudity → Option 3
🔹 3x Drugs → Cocaine, leaf emojis, etc.
🔹 1x Spam → Same content repeating
🔹 5x Hate → Abusive words in caption/story


---

💡 Tips:

✔ Works well on black/dark themed meme pages
✔ Aged account hit boosts the result
✔ Ideal VPNs: Netherlands 🇳🇱 or France 🇫🇷


---

🚨 Result:

🔒 1–2 hour lock, then full review within 12 hours
🔥 90% pages don’t recover from this combo   
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
💣 SPANISH METHOD 🇪🇸 – Shadow Execution Mode 😎

> This method works silently but hits HARD. Use it only if you’re ready for serious results.



🛡 Phase 1: First Wave of Reports

⚠ 3x Dangerous Organisation – Triggers terrorism/extremist flags

😰 6x Self-Harm Reports – Plays on IG’s safety protocols

💢 2x Hate Speech – Pushes algorithm red flags

🥺 2x Bullying Me – Shows personal attack angle


🎭 Now Pause… Let IG AI process it. Then strike again.


---

🗡 Phase 2: Second Wave – Final Blow

🖤 1x Hate Speech Again – Reinforces violent behavior flag

🧊 1x False Information – Targets misinformation policy

🚫 2x Sale of Illegal Goods (2nd Option) – Adds criminal activity signal


✅ Success Rate: Almost 100% if done step-by-step.
🧠 Note: Timing + VPN = 🔥. Always use a Spanish VPN if you're not located there.


---

💋 NETHERLANDS METHOD 🇳🇱 – Cold Ban Style

> Pure precision. No overkill, just exact targeting — works extremely well when done with focus.



🧊 Phase 1: Base Level Triggering

⚠ 2x Spam – Starts the bot-check trigger

💯 3x Hate Speech – Pins toxic behavior

🫠 1x False Info – Misinformation alert



---

💥 Phase 2: Deep Flagging with Multiple Angles

🔞 2x Nudity (1st Option) – Exploits adult content violation

💋 3x Dangerous Organisation – Sends terrorism/extremist signal

🫠 4x Self Harm – Adds mental health alert

🥶 2x Bully Me – Personal harassment tag

😇 1x Misleading + Scam – Final bait for fraud detection



---

❗ Δ FINAL STRIKE:

🚩 1x False Information – One last clean hit for permanent risk



---

📌 IMPORTANT NOTE:
🔗 Use VPN of the target country. If you're not in Spain or Netherlands, your reports won’t hold that impact without proper geo-spoofing.

🎯 Final Reminder:
If executed correctly step-by-step, this method has a 75%+ success rate in banning or locking the target account. Use it wisely. 💋❤ """)

    elif text == "POWERFUL METH ~":
        send_coming_soon(msg.chat.id, """👑 POWERFUL IRAN METHOD – Ultimate Insta Ban Formula 🔥
If you're serious about taking someone down on Instagram, this method is your secret weapon — but only for the real ones who know how to move smart.
Let’s break it down step by step:


---

🔒 Step 1: Activate Iran VPN
To begin with, connect to an Iran-based VPN. Instagram’s report system reacts differently based on region — and Iran servers hit differently. Most users don’t know this hack, but region manipulation is the first key to trigger high-impact bans.


---

🎯 Step 2: Attack Plan (Reporting Combo)
You’re not just pressing report randomly. Follow this exact combo:

🚫 10x Self-Harm Reports – Signals personal danger to IG’s moderation AI.

💢 5x Hate Speech Reports – Targets community guidelines on violence or abuse.

⚠ 2x Spam Reports – Adds algorithm pressure from the spamming angle.


This mixed-method attack fools the system into thinking the account is dangerous, abusive, and violating multiple policies at once.


---

⏰ Step 3: Timing is Everything
🕓 Best Working Time: 4:00 AM to 5:39 AM (IST)
At this hour, Instagram’s moderation system is less active manually and more dependent on AI auto-flags, which makes this method even more effective. You’ll notice accounts getting actioned faster and harder during this window.


---

⚠ Note:
This method is not for random use or personal grudges. Use it wisely and responsibly. Once triggered, recovery becomes extremely hard for the target account. """)

    elif text == "1 MIN LOCK METH ~":
        send_coming_soon(msg.chat.id, """🔐 𝗢𝗡𝗘 𝗠𝗜𝗡𝗨𝗧𝗘 𝗟𝗢𝗖𝗞 𝗠𝗘𝗧𝗛 ~ 💋❤

🔥 Status: WORKING | Instant Lock Method
🔐 Result: Temporary lock in seconds (can extend to full review)


---

⚔ STEP-BY-STEP REPORTING:

1️⃣ Report the victim’s post or reel for:
1x Nudity (Option 3) ➡ Sexual Content involving Minors or Illegal Activity

2️⃣ Report their profile/post/story for:
1x Self Harm ➡ User might harm themselves


---

⏱ 𝗥𝗘𝗦𝗨𝗟𝗧:

This combo locks the account within 60 seconds – works best on:

🔸 Low-engagement accounts

🔸 Accounts with story/highlights active

🔸 Non-verified & unprotected pages

🔸 Use 2012/2013 aged acc for higher hit 💥



---

🧠 𝗧𝗜𝗣𝗦:

✅ Use Insta Lite / Insta X for faster reporting
✅ Change IP/VPN after each report
✅ Don’t overreport from one ID — 2× is enough
✅ Wait 3–5 mins between reports """)
        
    elif text == "PERMA BAN METH ~":
        send_coming_soon(msg.chat.id, """🔥 PERMA B4N METHOD – Ultimate Termination Move 🔥

This method isn't for temporary bans. It's for permanent account deletion — used by elites who want the job done once and for all.


---

🧨 Step-by-Step: Initial Pressure Phase

1. 💢 Report a message from the target for Hate Speech – 10 times


2. 😤 Report another message for Bullying – 10 times


3. ⚠ Then report the Account itself for Bullying – 5 times



🛡 Note: Use a VPN (preferably US/UK) for faster and more effective triggering by IG systems.


---

🔒 Step-by-Step: Permanent Lock Method

> Now for the main strike...



1. Go to the target's Profile


2. Check if their bio contains @instagram, @creators, or anything that impersonates Instagram or Meta


3. Go to Report > Pretending to Be Someone > A Business or Organization


4. Select or enter Instagram


5. ✅ Submit the report



🕒 Waiting Time: 0 – 48 hours
🎯 Success Rate: High — Target will get permanently disabled if bio impersonation is detected.


---

💥 BAN METHOD (IG) – Quick Action Sequence 💥

> ⚠ For this method, you need access to an OG Support Request account (aged & trusted).




---

🔧 Tools Needed:

OG support access

Browser

VPN (optional but preferred)



---

⚙ Execution Steps:

🔹 Step 1 – Story-Based Strike

Open the target’s story (any one of the last 3)

Report 1x for Self-Harm (from a browser)

Then report 3–5x for Nudity
This pushes serious auto-detection triggers on content.



---

🔹 Step 2 – Bot Attack

Use a report bot to flood the account with Self-Harm reports
(This step weakens the account health silently in the background.)



---

🔹 Step 3 – DM Violation Abuse

If the victim has DMs with bad words, do this:

Report for Hate Speech – 5 times

If you spot words like “ban”, even written like “b@n”, report for:

Bullying – 3 times

Hate – 5 times





---

⏱ Expected Time to Vanish:

Within 24 hours – account either disabled, under review, or shadow-locked.


---

🧠 Final Tips:

Always use aged or warmed-up accounts to report.

Using a VPN matching the target's country improves results.

Try combining this method with Iran or Spanish VPN methods for even faster reaction. """)

    elif text == "FREE WEB HOSTING ~":
        send_coming_soon(msg.chat.id, """🌐 FREE WEB HOSTING SITES 💻✨

🚀 Use these platforms to host your sites, scripts, tools, or files completely free — no credit card, no BS.

1. 🔗 cwahi            
http://cwahi.com

2. 🔗 110mb            
http://110mb.com

3. 🔗 Ripway          
http://ripway.com

4.  🔗 SuperFreeHost   
http://superfreehost.info

5. 🔗 Freehostia      
http://freehostia.com

6. 🔗 Freeweb7        
http://freeweb7.com

7. 🔗 t35             
http://t35.com

8. 🔗 Free Web Hosting Pr 
http://freewebhostingpro.com

9. 🔗 Awardspace      
http://awardspace.com

10.🔗 PHPNet          
http://phpnet.us

11.🔗 ProHosts        
http://prohosts.org

12.🔗 000webhost      
http://000webhost.com

13.🔗 AtSpace         
http://atspace.com

14.🔗 FreeZoka        
http://www.freezoka.com

🛠 Most support PHP/MySQL
📦 Good for file hosting, small sites, tools, CPanel tricks """)

    # === NEXT Page 2 Buttons ===
    elif text == "FF METH ~":
        send_coming_soon(msg.chat.id, """🔥 FF BAN METH ~

📛 5x Impersonation Reports
→ Use: @freefirelatam OR @freefirebdofficial
Go to:
Report > Pretending to be > Business or Organization > Enter Handle

💢 4x Hate Speech Reports
😢 2x Self-Harm Reports

📍 Use VPN (Brazil/BD/India) for fast effect
📆 Ban Time: 24–72 hrs """)
        
    elif text == "ANIME METH ~":
        send_coming_soon(msg.chat.id, """🌀 ANIME PFP METHOD ~

📌 Target: Anime profile users using stolen or AI art


---

🔷 Step 1 – App Reports:

📩 3x Spam

💢 3x Hate Speech

🎭 5x Impersonation → Select "Someone on Pinterest"



---

🔷 Step 2 – Browser Reports (More Powerful):

😢 3x Self-Harm

🎭 5x Impersonation (Pinterest again)
(Browser reports hit harder — don’t skip this)



---

✅ Tips:

Use US or Japan VPN

Report from multiple accounts for higher effect

Works best on anime/fan pages using Pinterest art without credit


⏱ Result Time: 24–48 hrs """)

    elif text == "BOT METH ~":
        send_coming_soon(msg.chat.id, """🤖 BOT METH ~

💥 Option 1 (Quick Strike):

3x Nudity (Use 3rd option under Sexual Content)


OR

💢 Option 2 (Soft Touch):

1x Self-Harm

1x Hate Speech



---

✅ Use any report bot or do manually
🌍 VPN (India/US) optional for better hit rate
🕒 Result Time: 12–48 hrs """)

    elif text == "PAID GIRL METH ~":
        send_coming_soon(msg.chat.id, """💔 PAID GIRL BAN METHOD

If you wanna wipe out any so-called “paid girl” account:

😢 3x Self-Harm Reports

🔞 4x Nudity Reports (Use 3rd Option under Sexual Content)


💣 That’s it. She’s gone in 24–48 hrs. No mercy.
                         
✅ Bonus if done with a VPN (India/US) """)

    elif text == "LONG BIO METH ~":
        send_coming_soon(msg.chat.id, """💗 𝗟𝗼𝗻𝗴 𝗕𝗶𝗼 𝗛𝗮𝗰𝗸 (Invisible + Safe)

Use this trick to hide your bio, avoid long bio reports, and keep your profile looking clean & pro. No third-party apps needed!


---

✅ Step-by-Step Guide:

🧩 Step 1:
Copy this invisible text below completely:

‌                   
‌
‌
‌
‌
‌
‌
‌
‌
‌‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌
‌

🌐 Step 2:
Go to Edit Profile on Instagram.

💼 Step 3:
Switch your account to Professional (Business/Creator).

📝 Step 4:
Now again tap Edit Profile, and scroll to find:
👉 Contact Options

📍 Step 5:
Tap Business Address

Paste the invisible text into the Street Address

In City/Town, type: Good night 🌙


✔ Step 6:
Enable Display Contact Info, then click ✓ and save.


---

🎉 Done!
Your bio will now appear completely blank, looking aesthetic and protected from bio-length ban reports.""")

    # === CB METH Inner Buttons ===

    elif text == "CB PATCH METH ~":
        send_coming_soon(msg.chat.id, """⚒ 𝐂𝐇𝐀𝐓 𝐁𝐀𝐍 𝐏𝐀𝐓𝐂𝐇 𝐌𝐄𝐓𝐇𝐎𝐃 (CB PATCH METHOD)

📡 Status: WORKING ✅ | Updated: 2025


---

📌 Purpose:

This method patches your main account’s Chat Ban detection, allowing you to bypass CB locks or unlock CB methods that weren’t working before.


---

🧾 STEPS TO FOLLOW:


---

1. TEXT FROM YOUR MAIN ACCOUNT

Send a simple, clean message like:

> “Hello Instagram”
“I love Instagram”
“Great platform!”



To 2 different accounts (can be random friends or bots).


---

2. REPORT VIA FIRST ACCOUNT (YOU TEXTED)

Now login to the first account (receiver #1):

📥 Go to chat with your main account →
📌 Report 7x for Hate Speech on that chat.


---

3. REPORT VIA SECOND ACCOUNT (YOU TEXTED)

Now login to the second account (receiver #2):

📥 Go to chat →
📌 Report 7x for Violence

📲 Then go to your main account profile
📌 Report 7x for Impersonation → select:

> “Impersonating Instagram or Meta”




---

🎉 𝐂𝐎𝐍𝐆𝐑𝐀𝐓𝐒:

Your Chat Ban is now patched!
✅ You can now use any working CB method
✅ Account becomes CB method-compatible (101% success rate)


---

🧠 PRO TIPS:

Do this with a stable VPN (🇺🇸 USA recommended)

Don’t overuse — one patch = good for weeks

Use fresh or trusted alt accounts to avoid detection

Don’t change username/pfp during patch process



---

🧪 WHY THIS WORKS:

Instagram’s AI watches for interactions with reports.
This method forces your own account into a system trust loop, by mixing positive and negative signals — helping bypass flag locks.
""")

    elif text == "CB ENABLE ~":
        send_coming_soon(msg.chat.id, """🔥 CHAT BAN (CB) METHOD – METH 1 + METH 2 🔥

💯 Enable Chat Ban & Trigger Silent Shadow System


---

🚨 What is Chat Ban (CB)?

Chat Ban = The target user is silently blocked from replying or sending DMs, even though everything looks normal from their side. Pure ghost ban.




---

🧨 METH 1: Silent Trigger Method (Ghost Style)

⚙ Steps:

1. Don’t report the target for 3 days.
❗ Let the system reset their activity score.


2. After 3 days → Use a strong VPN
🌐 Recommended: 🇫🇷 France / 🇺🇸 USA / 🇳🇱 Netherlands


3. Deactivate your own IG account

> Go to Settings → Deactivate → Choose any reason




4. Wait for 48 hours. Don’t login.
📵 Don’t access your account from anywhere


5. After 48 hours, login again
Then wait another 24 hours for system balance.


6. Now, start reporting the victim’s account:

2x Self-Injury

2x Hate

1x Nudity

1x False Info



7. ✅ ChatBan will silently trigger within 1–3 days
(Victim can't DM, ghost ban active)




---

🚀 METH 2: CB Activation Booster (50 Chat Report Method)

📌 What You Need:

Use a fresh new account or an old-aged account (2012/2013 if possible, but not compulsory)

Keep VPN ON (use a static IP or USA location for better results)


📤 Reporting Strategy (Do this daily for 7 days):

Go to chats (any random chats — can be abusive or normal)

Report 50 chats daily:

✅ 1x Violation

✅ 1x Hate Speech



📌 No matter if the reviews come negative or positive.
The system reads it as “reporting behavior score”.

⏳ After 7 Days:

Your account gets CB ability activated

You can now use any working CB method on targets

Hit rate becomes 101% effective ⚔



---

📍 BONUS TIPS:

Do not change username, pfp, or email during the CB process

Never report from the same IP on multiple accounts

Use light activity (like scrolling reels) to make your reporting account look human



---

🧠 FINAL RESULT:

After 7 days of Method 2 + 1 execution of Method 1 =
🔥 Full CB Power Activated + Shadow Bans on Targeted Accounts

“They’ll never know what hit them.” 🥷💥 """)

    elif text == "CB METHS ~":
        send_coming_soon(msg.chat.id, """💥 𝐆𝐂 + 𝐃𝐌 𝐌𝐄𝐓𝐇 – ADVANCED REPORT SYSTEM 💥

(GC = Group Chat / DM = Direct Message Targeting)
🔥 Works Best When You’re Tagged or Abused in a Story/Chat 🔥


---

💬 𝐆𝐂 𝐌𝐄𝐓𝐇 (When You’re Tagged or Abused in a Group/Story)

📌 Scenario 1: Tagged in Story / Group Mention

Report this way (from multiple accounts):

2x Violence

3x Bullying someone else

1x Hate speech



---

📌 Scenario 2: Abusive Words Used in Caption/Story

Use these report types:

2x Violence

1x Hate speech

1x Meta Impersonation

1x Targeting Meta Staff / Zuck (Zuckerberg impersonation)


(This triggers their internal trust & safety system fast)


---

📩 𝐃𝐌 𝐌𝐄𝐓𝐇 – If You Receive Toxic or Scam DMs

Report using this format:

3x Bullying

2x Scam or Fraud

1x Hate Speech


OR (Alternate Boost Combo):

5x Hate Speech

2x Scam / Phishing

2x Violence

1x Report for @meta or impersonating public figure



---

🧠 PRO TIPS:

Report within 10 minutes of abuse/tag for highest success

Use old-aged accounts or active-looking accounts

Always use a VPN (Germany / US / Netherlands)

Take screenshots if needed for backup (in case you email Meta later)



---

📩 Want to Email for Review?

Use this:
Link: https://help.instagram.com/contact/383679321740945
Message Template:

"Hello Instagram Team,

I was recently mentioned/tagged in an abusive story or message by @target. This content included bullying, threats, and possibly impersonation of Meta staff.

It’s seriously disturbing and violates Instagram’s community guidelines. Kindly look into this and take action.

Thanks,  
[Your Name / @username] "


---

✅ Final Summary:

🎯 Type	🔁 Reports

GC Tag	2x Vio, 3x Bully Someone Else, 1x Hate
Abuse	2x Vio, 1x Hate, 1x Meta Imp, 1x Zuck
DM	3x Bully, 2x Scam, 1x Hate or 5x Hate, 2x Scam, 2x Vio, 1x Meta """)

    elif text == "BEST I'D FOR CB ~":
        send_coming_soon(msg.chat.id, """💎 ʙᴇsᴛ ɪᴅ ғᴏʀ ᴄʙ ʙᴀɴɴɪɴɢ: 𝟐𝐊𝟏𝟔 ✅


---

💡 Why 2K16 IDs Work So Well:

🔹 Aged Enough – Not too new to get flagged, not too old to be blacklisted by system.

🔹 Still Inside Active Filtering System – 2K16 IDs are actively watched by Instagram AI, so their reports hit harder.

🔹 Clean Track Record – If unused or low activity, they carry trusted report signals.

🔹 Less Cooldown Delay – Their reports trigger actions faster than newer or 2K12–2K13 IDs (which often hit cooldown flags).


---

✅ Other Good Years:

🔢 Year	⚙ Use Case

2K12–2K13	    Best for Impersonation & Deep Ban methods
2K14–2K15	    Multi-method safe (ban, CB, unban)
2K16 ✅	       ⚠ Best balance: CB ban + Meta report + patching
2K17–2K18	    Use for backup / patching / review bypass
2K20+	        Only good for chat report farming, not main CB



---

💥 PRO TIP:

If you’re using a 2K16 ID:

Pair it with a USA/France VPN

Avoid logging in from multiple devices

Do reporting in bursts (10–10–10 every 2 hrs) """)
        

    elif text == "UNLIMITED GMAILS ~":
        send_coming_soon(msg.chat.id, """🔰 Unlimited Gmail Accounts Creator (Dot Trick Method)

> 🧠 One Gmail = Thousands of Variants
📥 All inboxes redirect to your main Gmail — no need to create new accounts!




---

⚙ Steps to Use:

1️⃣ Have 1 Gmail Account
👉 Example: example@gmail.com

2️⃣ Go to:
🔗 https://thebot.net/api/gmail/

3️⃣ Enter Your Gmail Username (without @gmail.com)
👉 Example: just enter example

4️⃣ Click "Generate"
📩 You’ll get thousands of Gmail variants like:

ex.ample@gmail.com

e.x.a.m.p.l.e@gmail.com

exam.ple+1@gmail.com


5️⃣ All Variants = Same Inbox
📥 Any email sent to any generated address will land in your main Gmail inbox


---

💡 Use Cases:

Create multiple logins/accounts on websites

Avoid spam filters

Bypass “one account per email” restrictions

Test apps or scripts



---

✅ No verification needed
✅ No extra Gmail setup
✅ Fully legit – works via Google’s own aliasing system""")

    elif text == "KEYBOARD LEGA ~":
        send_coming_soon(msg.chat.id, 
"""https://play.google.com/store/apps/details?id=com.cutestudio.font.keyboard

https://www.androidapksbox.com/hi-keyboard/

https://keyboard-designer-keyboard.en.softonic.com/android/download

👻""")

    elif text == "CP HANGER LEGA ~":
        send_coming_soon(msg.chat.id, 
"""https://yktricksindia.blogspot.com

https://yktricksindia.blogspot.com

https://yktricksindia.blogspot.com/?m=1""")



    elif text == "GALI 1 ~":
        send_coming_soon(msg.chat.id, 
"""LUSTRIX 
   ⣴⣾⣿⣿⣶⡄           
  ⢸⣿⣿⣿⣿⣿⣿           
  ⠈⢿⣿⣿⣿⣿⠏          
    ⠈⣉⣩⣀⡀           
    ⣼⣿⣿⣿⣷⡀          
  ⢀⣼⣿⣿⣿⣿⣿⡇         
 ⢀⣾⣿⣿⣿⣿⣿⣿⣷  enemy ki maa
⢠⣾⣿⣿⠉⣿⣿⣿⣿⣿⡄ ⢀⣠⣤⣤⣀   
 ⠙⣿⣿⣧⣿⣿⣿⣿⣿⡇⢠⣿⣿⣿⣿⣿⣧  
  ⠈⠻⣿⣿⣿⣿⣿⣿⣷⠸⣿⣿⣿⣿⣿⡿  
    ⠘⠿⢿⣿⣿⣿⣿⡄⠙⠻⠿⠿⠛⠁  
       ⡟⣩⣝⢿  ⣠⣶⣶⣦⡀  
       ⣷⡝⣿⣦⣠⣾⣿⣿⣿⣿⣷⡀ 
       ⣿⣿⣮⢻⣿⠟⣿⣿⣿⣿⣿⣷ 
       ⣿⣿⣿⡇  ⠻⠿⠻⣿⣿⣿ 
      ⢰⣿⣿⣿⠇    ⠘⣿⣿⣿
      ⢸⣿⣿⣿      ⣠⣾⣿ 
      ⢸⣿⣿⡿   ⢀⣴⣿⣿⣿⣿ 
      ⠹⣿⣿⠇   ⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇ """)

    
    elif text == "GALI 2 ~":
        send_coming_soon(msg.chat.id, 
    """⣠⣶⣶⣦⡀            
      ⢰⣿⣿⣿⣿⣿            
       ⠻⣿⣿⡿⠋            
      ⣴⣶⣶⣄              
     ⣸⣿⣿⣿⣿⡄             
    ⢀⣿⣿⣿⣿⣿⣧             
    ⣼⣿⣿⣿⡿⣿⣿⣆      ⣠⣴⣶⣤⡀ 
   ⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦    ⣸⣿⣿⣿⣿⣷ 
   ⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀ ⢀⣿⣿⣿⣿⡿⠋ 
    ⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷    
    ⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇    
⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇   ⠉⠛⣽⣿⣇⣀⣀⣀ 
⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇     ⠻⠿⠿⠛⠛⠛⠃""")
        

    elif text == "GALI 3 ~":
        send_coming_soon(msg.chat.id, """
╔════•ೋೋ•════╗ 
    𝗟𝗨𝗦𝗧𝗥𝗜𝗫 𝗘𝗡𝗧𝗘𝗥 😆
╚════•ೋೋ•════╝







𝗚𝗔𝗥𝗜𝗕 𝗞𝗘 𝗝𝗛𝗔𝗔𝗧 𝗞𝗘 𝗣𝗔𝗦𝗜𝗡𝗘 🤣🤣🤣𝗦𝗔𝗡𝗞𝗜 𝗦𝗘 𝗟𝗔𝗗𝗘𝗚𝗔 𝗔𝗨𝗞𝗔𝗔𝗧 𝗛𝗔𝗜 𝗧𝗘𝗥𝗜








𝗧𝗘𝗥𝗜 𝗦𝗔𝗦𝗧𝗜 𝗥𝗔𝗡𝗗𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗡𝗔𝗡𝗚𝗔 𝗡𝗔𝗖𝗛𝗔𝗨𝗡𝗚𝗔 🤣🤣








𝗟𝗨𝗦𝗧𝗥𝗜𝗫
  😏
    | 👐💵
    |//    💵
    |          💸 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔
   /\            👯👯
👟👟

  𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗘 𝗕𝗛𝗢𝗦𝗗𝗘 𝗞𝗢 𝗟𝗨𝗦𝗧𝗥𝗜𝗫 𝗞𝗜 𝗦𝗔𝗟𝗔𝗠𝗜 𝗛𝗔𝗜 ☠☠☠☠☠☠☠









𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗞𝗢 𝗘𝗞 𝗕𝗔𝗥 𝗙𝗨𝗖𝗞 𝗬𝗢𝗨 🤣🤣🤣🤣🤣🤣🤣🤣🤣

…………………../´¯/)
……………….../¯../
………………../…./
…………./´¯/’…’/´¯¯`·¸
………./’/…/…./……./¨¯\
……..(‘(…´…´…. ¯~/’…’)
………\……………..’…../
…….…\………..... _.·´
…………\…………..(
…………..\………….\…



𝗖𝗛𝗔𝗟 𝗕𝗛𝗔𝗚 𝗚𝗔𝗥𝗜𝗕 𝗔𝗨𝗞𝗔𝗔𝗧 𝗕𝗔𝗡𝗔 𝗞𝗘 𝗔𝗔 🤣🤣𝗔𝗕 𝗥𝗨𝗞𝗘𝗚𝗔 𝗧𝗢 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗟𝗔𝗦𝗛 𝗖𝗛𝗨𝗗 𝗝𝗔𝗬𝗘𝗚𝗜 𝗡𝗘𝗞𝗔𝗟 😎😎😎😎😎""")


    elif text == "GALI 4 ~":
        send_coming_soon(msg.chat.id, """"
MADH3RXHOD KI AULAD BH3NXHODI XAL3 RANDI BHANGI
MADHERXHOD T3RI MA KI KALI GAAND M3 LUND MARU B3H3N K3
L0WD3 SUWR K3 BACH3 T3RI MA KA BH0SDA B3H3NCH0UD K3
BACH3 RANDII K3 DIN3 B3TICH0UD KI AUALD SADI GAAND VAL3
KUT3 K3 BACH3 B3H3NCH0UD K3 DIN3 T3RI MA KI SADI CH00T
M3 LUND MAR K3 USKA BH0SDA FADU CH00T MARI K3
GAANDV3 K3 BADCH3 B3H3NCH0UD K3 BACH3 B3TICH0UD KI
AUALD T3RI MA KI KALI CH00T T3RI MA K3 BH0SD3 M3 THPAD
DUNGA SAL3 GHANDV3 K3 BADCH3 B3H3NCH0UD K3 DIN3 T3RI MA
KI SADI CH00T MAI GATR M3 DUB0 DUB0 K3 MARUNGA KANJR K3
DIN3 B3H3NCH0UD MA K3 LUND B3TICH0UD K3 BACH3 T3RI MA K3
BH0SD3 K0 CH33R K3 RKH DU SAL3 GAANDv3 T3RI MA KI
GAAND M3 SAND KA LULLA FASA DU BH0SDI K3 DAL33T K3 BACH3
T3RI MA K3 BH0SD3 M3 CURRNT LAGA K3 USK3 BHS0D3 M3 S3
BACH3 PAIDA KAR DUNGA MA K3 LUND T3RI B3H3N KI CH0TI
CH00T M3 APN3 L0WD3 K0 DAL K3 USKI CH00T KH0LU MATHRCHD
K3 BACH3 CHUD3 HU3 TATT3 YHA APNI MA K0 CHUDAN3 AYA THA
MA K3 LUND T3RI MA K3 BH0SD3 M3 APN3 LUND S3 USK3 BH0SD3
K0 KHULA KAR DUNGA SAL3 CHAMR CHINAL K3 PIL3 K0TH3 VALI
RANDI K3 IKL0T3 KUTIYA K3 BACH3 B3H3NCH0UD K3 DIN3 T3RI MA
K3 KAL3 BH00SD3 M3 B0MB F0D K3 BLAST KRVA DUNGA
MATHRCHD K3 BACH3 CH00T MARI K3 DIN3 T3RI B3H3N KA RAP3
KARUNGA BHARI M3TR0 M3 L3 JA K3 MA K3 LUND SAL3 CHTIY3 K3
BACH3 CHUDAKAD KH0R KI AUALD HRAM K3 PIL3 M3RA L0WDA
CHOOS3GA T3RI MA KI GAAND M3 ITN3 L0WD3 MARUNGA USKI
GAAND L0D0 KI KHAN LAG3N3 LG3GI B3H3NCH0UD MATHRCHD K3
BACH3 SUWR K3 BACH3 T3RI MA KI GAAND M3 MUKK3 MAR K USKI
GAAND SUJA DU B3H3NCH0UD K3 DIN3 CH00TIY3 K3 BACH3
GAANDV3 K3 DIN3 APNI MA K0 CHUDAN3 VAL3 PIL3 SAL3 T3RI MAA
KI CH00T MAI MIRCHI AUR T3L GARAM KARK3 TADKA LAGA DUNGA
T3RI MAA N3 TUJH3 PAIDA KARN3 S3 P3HL3 T3R3 BAAP KA
1 INCH KA L0WDA L3N3 S3 USK0 CH00T KA CANC3R H0 GYA AB MAI
D0CT0R BAN K3 T3RI MAA KI CH00T KA ILAAJ KARUNGA
T3RI MAA KI CH00T MAI AATANKWADI0 S3 NISHAAN3 LAGWAUNGA
B3 BH0SDIK3 T3RI MAA KI CH00T MAI GARRAM L0HA DAAL
K3 JAMA DUNGA H3H33H3H3H3H3H3H3HH T3RI MAA KI CH00T
BL0CK H0 JAYGI T3RI B3H3N KI CH00T K0 CHAAQU S3 KAAT
KAR FIR TAANK3 LAGA KAR WAPIS P3HL3 JAISA KAR DUNGA T3RI
MAA K3 BH0SD3 MAI TUJH3 WAAPIS GHUSS3D DUNGA BAAP S3
FADDA KAR3 GA TU H3IN T3RI MAA KI CH00T MAI GHUSS KAR
KHUJLI KARUNGA MAI USS S3 T3RI MAA K0 ACHA LAG3GA AB3
BH0SDIK3 T3RI MAA KI CH00T MAI M3THAN3 KI PIP3 DAL K3 AAG
LAGA DUNGA T3RI MAA R0CK3T KI TARA UD3GI HAHAAHAHAH
SUNA HAI T3RA BAAP CIGRATT3 APNI GAAND S3 P33TA HAY ?
Y3 SACH HAI KYA ? AB3 T3RI MAA KI CH00T D3KH JAA K3 ZUNG
LAG GYA HAI SAAF T0H KAR LIYA KAR B3H3N K3 L0WD3
SUNA HAI T3RI MAA N3 KISSI AUR S3 CHUDWA K3 TUJH3 P3DA
KIYA HAY KYUNK3 T3RA BAAP KHUSRA HAI ? Y3 SACH HAI KYA ?
AB3 T3RI MAA KI NAAK MAI 2 M3T3R LAMBI K33L GAAD DUNGA FIR
T3RI MAA K0 MUHH S3 SAANS L3NA PAD3GA H33H3H3H3H3
ACHA CHAL R00 MAT ACHA Y3 BATA T3RA BAAP BR3AK DANC3
K3R L3TA HAI KYA SUNA HAI T3RA BAAP GALI0N MAI L0WDA
CH00TA HAI ? Y3 SACH HAI KYA ? SUNA HAI T3RA BAAP KACHRAA
UTHAAN3 GALI GALI FIRTA HAI Y3 SACH HAI KYA ? SUNA HAI T3RI
BAAJI BH33K MANG MANG K3 APNI CH00T CHUDWATI HAI ? SUNA
HAI T3RI BAAJI CH00T MAI D00DH DAAL0 T0U """)

    elif text == "GALI 5 ~":
        send_coming_soon(msg.chat.id, """BHAN KA LODA TARI MAA KO CHOD CHOD KA PAGAL KAR DU BHAN KA DINA TU GALI DAGA MUJAE RANDI KA BAALK HARMI KA CHUDA HUA SATVA NAMUNA TARI BHAN CHOD DUNGA ASA CHODUNGA KI TARI BHAN KI SAAT PUSTA MARA LUND KA VAAR SA PARALISS NIKALNGI SALA TARI BHAN KO ROAD PA LAJA KA KA NANGA KAR KA BAAXHO SA CHUD VAU ।। 🤬🤬🤮🥵

TARI MAA KO CHOD KA 9MONTH BAAD EK OUR RAAVAN NIKALGA BHAN KA LODO SAMBAL KA RAHNA BAAP SA MAA CHOD DAGA JIS NA BHI FAADA KIYA MUJSA..# 🤧😡🤬""")

    elif text == "GALI 6 ~":
        send_coming_soon(msg.chat.id, """ABA CHOOT KA 🚀 TAPAKTA PANI NANKU MOCHI KI 🆖🤴 LAWARIS AULAD TERI MAA KA 🚀 BHOSDA PHAD KA 🔫 JHAAD PA 👨 TANG 🍋 DUGA MADARBHOSDI AAJ TO CHODUGA TERI AMMA TOD KA 🔫 KHATIYA UKHAD LENA 🎽⚽ BETA 💰 MERI JHAATIYA o_OSAlA SUAR KI 🆖🤴🅱 AKHRI NASAL 👃. TERIBHN KO 🤶 LAMBI LAMbI ROAD 🗾🛣 PE 🍇💉 LAMBA LAMBA DAUDA KA 🔫 LAMBA LAMBA LUND DUGA ABA aPNI MAA KI 🆖🤴 PHATI CHOOT KA 🔫 DIWANA ITNI ZOR SA 🅱 GAND PALAAT MARUGA JIS ⁉❕❔ CHOOT KA 🔫 TU 🤔 DIWANA HAI 🐯 USSI CHUT MAIGHUS JAYAGA...:-[:-);-):-""")

    elif text == "GALI 7 ~":
        send_coming_soon(msg.chat.id, """teri ammy ke jh@nto ko pakad ke building se latka dunga.
Chhipkali jaise deewal pe chadh ke tere baap ke muh me moot dunga.
Fortune laga ke pelunga teri ammy ke ch00t ko chus jaunga.
Vimal khane wale r@ndi ke bachhe m@dharch0d.
Mask pehna ke apne l0de ko teri behn ke ch00xt me daal dunga.
Paodaan ki shakal ke g@ndu sale.
G@nd me sarso ke tail ke sath tezab dal dunga tere jb tu marwane ayega mujhse.
Kaali ch00t wali r@nd ke bachhe behnch0d""")

    elif text == "GALI 8 ~":
        send_coming_soon(msg.chat.id, """
ＬＵＳＴＲＩＸ                      
⣿⣿⣿⠋⠁⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿       
⣿⣿⣷⡀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⠶⠖⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⠃⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠁⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡟⠁⠀⠀⣶⠀⠀⠀⠀⠀⢻⣿⡿⠟⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣦⠀⠀⠘⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣧⣀⡀⠀⠀⠀⠀⢻⣦⣄⣀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⢠⠖⠢⡀⣿⣿⠟⠉⠉⠙⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠈⢢⠀⠙⠟⠁⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠑⡄⠀⣠⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣄⣀⣄⠀⠀⠀⠀⠙⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣸⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⣸⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⢀⣿⣿⣿⡿⠋⠀⠀⠀⠀⠠⠴⠾⠿⠿⣿
⣿⣿⣿⣿⣿⣿⣆⠀⠀⣸⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸
               𝐇𝐀𝐓𝐄𝐑𝐒 𝐊𝐈 𝐌𝐀𝐀 😈""")
        

    elif text == "GALI 9 ~":
        send_coming_soon(msg.chat.id,
"""                        RUDRA⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⣰⣶⣶⣄⠀
⠀⠀   LUSTRIX⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢿⣿⣿⡟⠀
⠀⠀⠀⠀⠀⢀⣶⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣭⡉⠀⠀   
⠀⠀⠀⠀⠀⠸⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣄⠀
⠀⠀⠀⠀⠀⣠⣬⣍⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⣿⣆
⠀⠀⠀⠀⢸⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣷⡿⠋
⠀⠀⠀⢀⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⢠⣤⣤⣄⢸⣿⣿⣿⠟⠁⠀
⠀⠀⠀⣼⣿⣿⡿⠘⢿⣧⣀⣴⣶⡆⣿⣿⣿⣿⢾⣿⣿⠀⠀⠀⠀
⠀⠀⠀⢿⣿⣿⢃⣴⣾⡻⣿⡍⠉⢁⣈⡛⠛⠋⠸⣿⣿⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⡄⠀⠀⠀
⢀⣀⣀⣈⣿⣿⡆⢿⣿⡇⠉⠉⢿⣿⣿⡏⠀⠀⠀⢿⣿⡇⠀⠀⠀
⠺⣿⣿⣿⣿⣿⢷⣿⣿⡇⠀⠀⠀⠀⣿⣷⣶⣶⡦⠸⣿⠇⠀⠀⠀
         hater ki maa """)

    elif text == "GALI 10 ~":
        send_coming_soon(msg.chat.id, """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿LUSTRIX⣿⣿⡏⠀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⡿⠟⠛⠛⢇⠀⠀⠀⠀⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⡜⠋⠀⠀⠀⠀⠈⣷⣦⣴⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠐⡀⠀⠀⢀⡀⠀⠸⣿⣿⣿⣿⠿⠿⢿HATER KI MAA 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢰⠀⠀⠀⠡⠴⠾⠿⠀⠀⠀⠙⢿⣿⠁⠀⠀⠀⢹
⣿⠿⠿⠿⠿⠿⠿⠋⠁⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠀⠀⠀⠀⢰
⣯⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣄⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⣀⣀⣤⣿
⣿⣿⣿⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")
  

    elif text == "NEXT :-":
        send_coming_soon(msg.chat.id, """COMING SOON LALA........""")

    elif text == "FAN PAGE METH ~":
        send_coming_soon(msg.chat.id, """📛 FANPAGE METH ~ 100% Noti Trigger

🎯 Target: Fake fanpages pretending to be real/official handles


---

⚙ Steps:

1️⃣ 3x Impersonation Reports
→ Use original handle as reference (e.g. @arianagrande, @freefirelatam, etc.)

2️⃣ 📲 Use Instagram Lite App for all reports
✖ Don’t use main app — Lite hits harder for fanpage cases

3️⃣ ⏸ Log out for 2 hours after reporting
→ Helps IG system prioritize & flag silently


---

✅ 100% Noti Guarantee
⏱ With good OG accounts, ban/review may start in under 1 hour

💡 Tip: Combine with VPN (US/India) for better impact""""")

    elif text == "INCREASE OG METH ~":
        send_coming_soon(msg.chat.id, """🤡 OG IMPROVE METH ~ NEW TACTIC

> Boost your OG’s power by farming bans. Here's how:




---

🔥 Step-by-Step:

1️⃣ Follow 7 P*rnstars in under 1 minute

@viking.barbie

@sophiedee

@amandacerny

@akadanidaniels

@miakhalifa

@miamalkova

@lanarhoades

@bhadbhabie (optional boost)



---

2️⃣ Wait for 3 mins
📥 8–10 bots will auto-follow or DM you


---

3️⃣ Report those bots:

🔞 3x Nudity (Option 3)



---

4️⃣ They get insta-banned
🧠 IG auto-systems reward accounts that "clean spam"
You just played the system 😈


---

💯 Result:

✅ OG score improves
🚀 Higher review priority
🔓 Ban methods hit faster in future""")

    elif text == "STORY REMOVE METH ~":
        send_coming_soon(msg.chat.id, """📛 STORY REMOVE METHOD

🌐 VPN: Use USA VPN for maximum effect


---

⚙ Main Report Sequence:

1️⃣ Hate – 7x
2️⃣ Self-Harm – 7x
3️⃣ Spam – 3x


---

🤝 Teammates Role:

🗯 Abuse Reports → Hate

😢 Other Reports → Self-Harm


📲 Use Instagram Lite or Web for stronger story reporting impact


---

⏳ Result:
Story gets auto-removed in 30 mins – 1 hour """)

    elif text == "YT BAN METH ~":
        send_coming_soon(msg.chat.id, """🔥 YOUTUBE CHANNEL BAN METHOD

(BGMI Hack/Scam Channel Takedown)


---

🌍 Step 1: Connect VPN

– Use USA or India VPN for faster action by YouTube system.


---

📹 Step 2: Target Video Reports

🚫 2x Spam/Scams

💢 1x Hate Speech

⚠ 1x Violent/Repulsive Content



---

📡 Step 3: Channel-Level Reports

🚫 2x Spam

💢 1x Hate


✍ In report description, paste this:

He is using BGMI hacks and scamming money. Ban this channel as soon as possible. Thanks in advance.


---

⏱ Step 4: Wait & Monitor

– Visit: https://www.youtube.com/reporthistory
– Track your reports & actions taken


---

🚨 FINAL STRIKE (If 3 Videos Get Removed):

📣 Report Channel Again – 5x Hate Speech ✍ Write:


This is an illegal channel. Please ban this urgently. He scammed my money.


---

✅ Result:
With 3+ video takedowns, channel is flagged as high-risk = ban chances spike 🔥""")

    elif text == "WP BAN METH ~":
        send_coming_soon(msg.chat.id, """📵 WHATSAPP BAN METHOD

💡 No VPN Needed — Pure Method


---

🧩 Step-by-Step Guide:

0️⃣ No VPN Needed
Works best without VPN to avoid suspicion


---

1️⃣ Go to:
🔗 https://www.whatsapp.com/contact/?subject=messenger


---

2️⃣ Fill the Form:

🌍 Country Code + Target Number
(Example: +91XXXXXXXXXX)

📧 Your Email

📧 Repeat Email

📱 Device: Select iPhone



---

3️⃣ In Message Box, Paste This:

I want to delete this number because I lost access to it. I didn’t receive the verification code. Please delete it from WhatsApp and contact me. (Gimilton)

OR

Lost/Stolen: Please deactivate my account.


---

4️⃣ Submit & Wait
📩 Confirmation email arrives instantly
⏳ WhatsApp will review & respond within 3 working days


---

✅ Result:
If successful, the target number gets deactivated temporarily or permanently """)

    elif text == "SNAP BAN METH ~":
        send_coming_soon(msg.chat.id, """✅ SNAPCHAT BAN METHOD ⚡

> Use this method to ban or deactivate any Snapchat account 🔥




---

⚙ Steps:

1️⃣ Go to:
🔗 https://support.snapchat.com

2️⃣ In the search bar, type:
Lost / Stolen

3️⃣ Click the result:
📌 "I lost my device" or "Report a lost/stolen account"

4️⃣ Fill out the form:

📞 Enter the target’s username

📧 Your email (any working one)

📱 Select device: iPhone / Android



---

📝 In the message box, write:

Hi Snapchat, please remove my Snapchat account because I lost my iPhone and my Snapchat account is in it.


---

✅ Result:
Snapchat may deactivate or lock the account within 24–72 hours """)

    elif text == "REPORT RESTORATION ~":
        send_coming_soon(msg.chat.id, """🎈 INSTAGRAM PAGE RESTORE METHOD (AFTER BAN)

🔗 Form Link:
https://help.instagram.com/contact/1610459702591585


---

🛠 Steps to Restore a Reported/Disabled Page:

1️⃣ Go to the Link Above
👉 This is Instagram’s official appeal form for business pages.

2️⃣ First Box:
Enter the username/ID of the banned page (without @)

3️⃣ Second Box (Message):
Paste this message:

Hello, do not be bored. My page (insert page ID) linked to (insert phone number or email) is now out of my reach. I did not know the law related to this, and after reading it, I realize I was wrong and will not repeat it. Thank you for returning my page, which was related to my work. I truly appreciate your support.

4️⃣ Device:
Select a device (any one — preferably iPhone)

5️⃣ Email:
Use a valid email where IG can contact you.


---

📌 Important Tips:

🔁 Resend the form every 2 days

📧 Use different email addresses each time

📣 This shows Instagram that the page is important to you

📆 Increases the chance of getting your page restored faster



---

✅ Used by many for page recovery
💯 Works best for business/fan/work-related accounts """)

    elif text == "PATCH ID ~":
        send_coming_soon(msg.chat.id, """🛡 ID PATCH METHOD (UNBAN & HARDEN TRICK)

💡 Use this to "patch" your Instagram ID and make it more resistant to future bans.


---

⚙ STEP-BY-STEP:

1️⃣ Change Your PFP
→ Set your profile picture to @instagramforbusiness's official display pic


---

2️⃣ From Another Account (or with teammates):
Report your own ID with the following:

🔁 5x Impersonation → @instagramforbusiness

🚫 5x Spam

😢 5x Self-Harm

💊 5x Drugs

🔞 5x Nudity

💢 5x Hate Speech

⚠ 5x Violence

🗯 5x Bullying

🧠 5x Scam or Fraud

❌ 5x False Info



---

3️⃣ Wait
Your account will likely get temporarily banned or disabled


---

4️⃣ Appeal Immediately:
Go to the Instagram Help Center or use the email they send to appeal the ban


---

✅ Result:
If done right, once restored, your ID becomes "patched" —
Harder to report, lower future ban risk, and flagged as reviewed in Meta systems.


---

🧠 Pro Tip: Use this method only on OGs, business handles, or mains you want to protect """)

    elif text == "REMOVE VIO ~":
        send_coming_soon(msg.chat.id, """⚠ Violation Removal Method (Appeal for Repost)

✅ Step-by-Step:

1️⃣ Go to your Instagram Violation Notice
→ Tap the specific violation you want removed.

2️⃣ Tap “Appeal for Repost” Option
→ This opens the appeal form directly.

3️⃣ Copy & Paste This Message:

Hi Instagram, please remove the violation from my ID. I did not post anything that intentionally violated Instagram’s guidelines. Due to this, my reach is going down and it’s affecting my career growth. I request you to kindly review this again. I’ll make sure such mistakes don’t happen again in the future.


---

✅ Tips for Best Results:

Use professional tone

Avoid slang or aggressive words

Appeal within 24 hours of the violation notice


📩 Most replies come within 24–72 hours """)


    # === Back Navigation ===
    elif text == "🔙 Back Menu":
        if current_state == 'cb_meth_menu':
            user_states[user_id] = 'banning_steps'
            bot.send_message(msg.chat.id, "🔙 Back...", reply_markup=banning_steps_menu())

        elif current_state == 'next_page_1':
            user_states[user_id] = 'banning_steps'
            bot.send_message(msg.chat.id, "🔙 Back...", reply_markup=banning_steps_menu())

        elif current_state == 'next_page_2':
            user_states[user_id] = 'next_page_1'
            bot.send_message(msg.chat.id, "🔙 Back...", reply_markup=next_page_1())

        elif current_state == 'next_page_3':
            user_states[user_id] = 'next_page_2'
            bot.send_message(msg.chat.id, "🔙 Back...", reply_markup=next_page_2())

        elif current_state == 'jacking_menu':
            user_states[user_id] = 'next_page_2'
            bot.send_message(msg.chat.id, "🔙 Back...", reply_markup=next_page_2())
            
        elif current_state == 'fyter_banega_menu':
            user_states[user_id] = 'next_page_2'
            bot.send_message(msg.chat.id, "🔙 Back...", reply_markup=next_page_2())
             
        elif current_state == 'banning_steps':
            user_states[user_id] = 'banning_menu'
            bot.send_message(msg.chat.id, "🔙 Back...", reply_markup=banning_menu())

        elif current_state == 'gali_spam_lega_menu':
            user_states[user_id] = 'fyter_banega_menu'
            bot.send_message(msg.chat.id, "🔙 Back...", reply_markup=fyter_banega_menu())

        elif current_state == 'banning_menu':
            user_states[user_id] = 'main_menu'
            bot.send_message(msg.chat.id, "🔙 Back...", reply_markup=main_menu())

        else:
            user_states[user_id] = 'main_menu'
            bot.send_message(msg.chat.id, "🔙 Back to main menu:", reply_markup=main_menu())

    elif text == "🏠 Main Menu":
        user_states[user_id] = 'main_menu'
        bot.send_message(msg.chat.id, "🏠 You're back at main menu:", reply_markup=main_menu())

    else:
        bot.send_message(msg.chat.id, "❓ Invalid input. Please use the menu buttons.", reply_markup=main_menu())

# === Run the Bot ===
bot.polling()