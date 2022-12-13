# -*- coding: cp1251 -*-
import telebot
from telebot import types
import random



bot = telebot.TeleBot('5491906660:AAFP9IUsQ6hvPsG4G48CHq2AYk3GdQKnkQc')

f = open('C:\\Users\\urapo\\OneDrive\\tg_bot\\acs.txt', 'r',encoding='UTF-8')
sss = str(f.read())
f.close()

@bot.message_handler(commands=["start"])
def start(message):
    mess = 'ку это бот по подготовке к огэ'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=["help"])
def com(message):
    markup = types.ReplyKeyboardMarkup()
    nomera = types.KeyboardButton('номера')
    variant = types.KeyboardButton('составить вариант')
    teori = types.KeyboardButton('теория к заданиям')
    markup.add(nomera,variant,teori)
    bot.send_message(message.chat.id,'ввыбор категории', reply_markup=markup)



@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'номера':
        print('asad')
    if message.text.strip() == 'составить вариант':
        print('ac')   
    if message.text.strip() == 'теория к заданиям':
        print('abc')
bot.polling(none_stop=True)
