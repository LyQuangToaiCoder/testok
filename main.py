import os
import telebot


bot = telebot.TeleBot("1969051592:AAFtyw2lD0u8K9EA5Pm3qp4_pOXiJ9MAoJg")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm VndGroup Chat Bot 📌Made by VndGroup")


@bot.message_handler(commands=["help"])
def send_message(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCL8PI42TZ_uaQWVVKUJx9Eg")

PM_START_TEXT = """
𝙃𝙚𝙡𝙡𝙤 𝙩𝙝𝙚𝙧𝙚, 𝙄'𝙢 VndGroup Bot ✨
𝙄'𝙢 𝙖 𝙋𝙤𝙬𝙚𝙧𝙛𝙪𝙡 gr�𝙤𝙪𝙥 𝙢𝙖𝙣𝙖𝙜𝙚𝙧 𝙗𝙤𝙩 𝙒𝙞𝙩𝙝 𝘾𝙤𝙤𝙡 𝙈𝙤𝙙𝙪𝙡𝙚𝙨. 𝙈𝙖𝙙𝙚 𝙗𝙮 TEᗩᗰ Vnd Group
𝙃𝙞𝙩 /help 𝙩𝙤 𝙛𝙞𝙣𝙙 𝙢𝙮 𝙡𝙞𝙨𝙩 𝙤𝙛 𝙖𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨 🕹
 
"""
buttons = [
    [
        InlineKeyboardButton(text="📌Owner", url="https://t.me/venuja_sadew"),
        InlineKeyboardButton(text="🖲 Simple", url="https://t.me/venuja_sadew"),
    ],
    [
        InlineKeyboardButton(text="📜 By", url="https://t.me/venuja_sadew"),
        InlineKeyboardButton(text="❔ ʜᴇʟᴘ", url="https://t.me/venuja_sadew"),
    ],
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ ᴀɴᴋɪ ᴠᴇᴄᴛᴏʀ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url="https://t.me/venuja_sadew"
        ),
    ],
]


ANKIVECTOR_IMG = "https://telegra.ph/file/75579c20520fc79f5b68d.jpg"


bot.polling()
