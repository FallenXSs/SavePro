import telebot
import random
import threading
import datetime
from telebot import types
import telegram
import json
import requests
from telebot import TeleBot
from telebot import types
import base64
from io import BytesIO


TOKEN = '6670784434:AAHuZF37WWVA1odL7HuQg4tpq5Wvmg-9GSU'

bot = telebot.TeleBot("6670784434:AAHuZF37WWVA1odL7HuQg4tpq5Wvmg-9GSU")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Merhaba! SaveCoin 💎 resmi Botuyla iletişime geçtiniz. Grubumuza katılmak için butonları kullanabilirsiniz. /join komutuyla kanalımıza, ve grubumuza katılın. /help komutuyla tüm komutlara bakın. SaveCoin iyi günler diler efendim ❤️ 💌")



@bot.message_handler(commands=['help'])
def show_help(message):
    help_message = "Yardım komutları:\n"
    help_message += "/start - Botu başlat\n"
    help_message += "/help - Yardım mesajını görüntüle\n"
    help_message += "/info - Bot hakkında bilgi ver"

    bot.reply_to(message, help_message)

@bot.message_handler(commands=['info'])
def bot_info(message):
    info_message = "Bu bot örnek bir Crypto Coin botudur. Python telebot kütüphanesi kullanılarak oluşturulmuştur. Kurucu @Fivist 👨‍💻."
    bot.reply_to(message, info_message)



@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    if message.from_user.username == '@Fivist':  # Sadece belirli bir kullanıcının bu komutu kullanmasını sağlamak için kontrol edebilirsiniz
        # Gruplarda dolaşarak mesaj gönderme
        for chat in bot.get_chat(chat_id).chat_id:  # Tüm grupların ID'lerini alarak döngüyü kullanabilirsiniz
            bot.send_message(chat, message.text.replace('/broadcast', ''), parse_mode='Markdown')
        
        # Özel mesaj atan kullanıcılara mesaj gönderme
        users = bot.get_updates()[0].message.from_user.id  # Tüm kullanıcıların ID'lerini alarak döngüyü kullanabilirsiniz
        for user in users:
            bot.send_message(user, message.text.replace('/broadcast', ''), parse_mode='Markdown')



@bot.message_handler(commands=['join'])
def send_welcome(message):

    markup = telebot.types.InlineKeyboardMarkup()
    btn_chat = telebot.types.InlineKeyboardButton('Chat 👪', url='https://t.me/SaveCoinChat')
    btn_kanal = telebot.types.InlineKeyboardButton('Support 📢', url='https://t.me/SaveCoinSupport/2')    
    markup.add(btn_chat)
    markup.add(btn_kanal)
    
    bot.reply_to(message, "Grubumuza Katılmak İçin Buttonlara Basabilirsin!", reply_markup=markup)


bot.polling()
