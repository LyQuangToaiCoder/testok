import os
import telebot


bot = telebot.TeleBot("5327605752:AAGPpMAP43dbRVXYJgdAyjk7kilpN49FaYA")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Adu, Toại Dzzzz {full_name}")


@bot.message_handler(commands=["help"])
def send_message(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCL8PI42TZ_uaQWVVKUJx9Eg")



bot.polling()
