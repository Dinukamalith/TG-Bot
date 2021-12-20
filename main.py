import os
import telebot


bot = telebot.TeleBot("5048168243:AAGO8V5VpkxxhYD4ZZvJFBp_gABCkKRaVUU")

#welcome 

@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hi I'm SZ Team Information Bot Service. My Owner is @dinukamalith.")



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
  
  vpn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🧭 Back 🧭", callback_data="https://t.me/VPN_HUB_LK_CHAT")
                ]
            ]
        )

@app.on_message(filters.command(["normal"]))
async def start(client, message):
    await message.reply_text(
        text=NORMAL_TEXT,
        disable_web_page_preview=False,
        reply_markup=vpn) 
  
#roseupdate

@bot.message_handler(commands=["roseup"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/szroseupdates")


bot.polling()
