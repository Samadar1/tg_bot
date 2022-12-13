# -*- coding: UTF-8 -*-
import telebot
from telebot import types
import random

bot = telebot.TeleBot('5491906660:AAFP9IUsQ6hvPsG4G48CHq2AYk3GdQKnkQc')

with open('C:\\Users\\urapo\\Documents\\GitHub\\tg_bot\\quest.txt', 'r',encoding='UTF-8') as file:
	nomera_list = []
	for x in file.readlines():
		x_str = str(x)
		nomera_list.append(x_str)

with open('C:\\Users\\urapo\\Documents\\GitHub\\tg_bot\\answ.txt', 'r',encoding='UTF-8') as file:
	nomera_list = [x for x in file.readlines()]
	
		
@bot.message_handler(commands=["start"])
def start(message):
	mess = 'ку это бот по подготовке к огэ'
	bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=["help"])
def com(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	nomera = types.KeyboardButton('номера')
	variant = types.KeyboardButton('составить вариант')
	teori = types.KeyboardButton('теория к заданиям')
	markup.add(nomera,variant,teori)
	bot.send_message(message.chat.id,'выбор категории', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def func(message):
	if(message.text =='номера'):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		nomer1 = types.KeyboardButton('номер 1')
		nomer2 = types.KeyboardButton('номер 2')
		nomer3 = types.KeyboardButton('номер 3')
		back = types.KeyboardButton("Вернуться в главное меню")
		markup.add(nomer1,nomer2,nomer3,back)
		bot.send_message(message.chat.id,'выбери номер', reply_markup=markup)
	elif (message.text =='номер 1'):
		rand = random.randint(0,3)
		bot.send_message(message.chat.id,nomera_list[rand], parse_mode='html')
		bot.send_message(message.chat.id,'введите ответ', parse_mode='html')



	elif (message.text == "Вернуться в главное меню"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		nomera_a = types.KeyboardButton('номера')
		variant_a = types.KeyboardButton('составить вариант')
		teori_a = types.KeyboardButton('теория к заданиям')
		markup.add(nomera_a,variant_a,teori_a)
		bot.send_message(message.chat.id,'Вы вернулись в главное меню', reply_markup=markup)


bot.polling(none_stop=True)
