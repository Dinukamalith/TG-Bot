import os
import telebot


bot = telebot.TeleBot("Api Key Here")

#welcome 

@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hi I'm SZ Team Information Bot Service. My Owner is @dinukamalith.")

#my telegram group

@bot.message_handler(commands=["tech95lk"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/tech95lkofficial")

InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Tech95lk🚀", callback_data="https://t.me/tech95lkofficial")
                ])

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


bot.polling()
