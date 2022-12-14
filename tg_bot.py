# -*- coding: UTF-8 -*-

from sys import flags
import telebot
from telebot import types
import random


bot = telebot.TeleBot('5491906660:AAFP9IUsQ6hvPsG4G48CHq2AYk3GdQKnkQc')

rand = 0
flag = False




with open('quest.txt', 'r',encoding='UTF-8') as file:
	nomera_list = []
	for x in file.readlines():
		x_str = str(x)
		nomera_list.append(x_str)

with open('answ.txt', 'r',encoding='UTF-8') as file:
	answ_list = []
	for x in file.readlines():
		x_str = str(x)
		x_str = x_str.strip('\n')
		answ_list.append(x_str)
	

		
@bot.message_handler(commands=["start"])
def start(message):
	mess = 'ку это бот по подготовке к огэ. Напиши команду /buttons'
	bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=["buttons"])
def com(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	nomera = types.KeyboardButton('номера')
	variant = types.KeyboardButton('составить вариант')
	teori = types.KeyboardButton('теория к заданиям')
	markup.add(nomera,variant,teori)
	bot.send_message(message.chat.id,'выбор категории', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def func(message):
	global flag
	global rand 

	if(message.text =='номера'):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		nomer1 = types.KeyboardButton('номер 1')
		nomer2 = types.KeyboardButton('номер 2')
		nomer3 = types.KeyboardButton('номер 3')
		back = types.KeyboardButton("Вернуться в главное меню")
		markup.add(nomer1,nomer2,nomer3,back)
		bot.send_message(message.chat.id,'выбери номер', reply_markup=markup)
	
	elif (message.text == "Вернуться в главное меню"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		nomera_a = types.KeyboardButton('номера')
		variant_a = types.KeyboardButton('составить вариант')
		teori_a = types.KeyboardButton('теория к заданиям')
		markup.add(nomera_a,variant_a,teori_a)
		bot.send_message(message.chat.id,'Вы вернулись в главное меню', reply_markup=markup)

	elif flag == False:
		bot.send_message(message.chat.id,'бот не распознаёт ваше сообщение', parse_mode='html')

	if message.text == 'номер 1':
		rand = random.randint(0,3)
		bot.send_message(message.chat.id,nomera_list[rand], parse_mode='html')
		bot.send_message(message.chat.id,'введите ответ', parse_mode='html')
		flag = True
		return 
	if flag == True:	 
		if (message.text == answ_list[rand]):
			bot.send_message(message.chat.id,'Молодец!')
			flag = False
		else:
			otvet = types.InlineKeyboardMarkup(row_width=1)
			button1 = types.InlineKeyboardButton("Правильный ответ!", callback_data ='1')
			otvet.add(button1)
			bot.send_message(message.chat.id,'Ответ неправильный, если есть трудности посмотри теорию, а также можешь узнать правильный ответ.',reply_markup=otvet,parse_mode='html')
	
	
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	global flag
	if call.message:
		if call.data == "1":
			bot.send_message(call.message.chat.id,answ_list[rand])
			flag = False
		if call.data == "2":
			bot.send_message(call.message.chat.id,answ_list[rand])
			



	

bot.polling(none_stop=True)
