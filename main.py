import os
import telebot


bot = telebot.TeleBot("Api Key Here")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "welcome massege here")


@bot.message_handler(commands=["command here"])
def send_message(message):
  bot.send_message(message.chat.id, "command reply here")



bot.polling()
