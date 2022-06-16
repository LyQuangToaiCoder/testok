import os

import telebot

bot = telebot.TeleBot("5534271637:AAG9IdOafmrrOKMGcH5baZRlBZZuw16wHL8")

@bot.message_handler(commands=["start"])
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')



def send_welcome(message):

    bot.reply_to(message, "Xin Chào",hello)

@bot.message_handler(commands=["help"])

def send_message(message):

    bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCL8PI42TZ_uaQWVVKUJx9Eg")




bot.polling()
