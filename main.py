import os
import telebot


bot = telebot.TeleBot("5048168243:AAGO8V5VpkxxhYD4ZZvJFBp_gABCkKRaVUU")

#welcome 

@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hi I'm SZ Team Information Bot Service. My Owner is @dinukamalith.")

#help menu

@bot.message_handler(commands=["help"])
def send_message(message):
  bot.send_message(message.chat.id, 
"Hi 😎 This is Sz Total Bot Service Help Menu.

       🚀 Bot Commands are ✅

✔️ /tech95lk - Go to my admine group.

✔️ /slbot - Go to sz bots chats group.

✔️ /szbots - Go to sz bots updates chenel.

✔️ /technews - Give tech news update.

✔️ /vpn - Free internet tricks.")



#my telegram group

@bot.message_handler(commands=["tech95lk"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/tech95lkofficial")



#slbotzone

@bot.message_handler(commands=["slbot"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/slbotzone")

#szteambots

@bot.message_handler(commands=["szbots"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/szteambots")

#uptodatelk

@bot.message_handler(commands=["technews"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/uptodatelk")
 

#vpnhublk

@bot.message_handler(commands=["vpn"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/VPN_HUB_LK_CHAT")
  
#roseupdate

@bot.message_handler(commands=["roseup"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/szroseupdates")


bot.polling()
