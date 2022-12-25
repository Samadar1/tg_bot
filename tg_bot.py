# -*- coding: UTF-8 -*-

from sys import flags
import telebot
from telebot import types
import random
import os


bot = telebot.TeleBot('5491906660:AAFP9IUsQ6hvPsG4G48CHq2AYk3GdQKnkQc')

rand = 0			#глобальные переменные
flag_ans = False


nomera_a = types.KeyboardButton('номера')					#кнопки осн
variant_a = types.KeyboardButton('составить вариант')		
teori_a = types.KeyboardButton('теория к заданиям')

nomer1 = types.KeyboardButton('номер 1')					#кнопки номеров 1- 15
nomer2 = types.KeyboardButton('номер 2')
nomer3 = types.KeyboardButton('номер 3')
nomer4 = types.KeyboardButton('номер 4')
nomer5 = types.KeyboardButton('номер 5')
nomer6 = types.KeyboardButton('номер 6')
nomer7 = types.KeyboardButton('номер 7')
nomer8 = types.KeyboardButton('номер 8')
nomer9 = types.KeyboardButton('номер 9')
nomer10 = types.KeyboardButton('номер 10')
nomer11 = types.KeyboardButton('номер 11')
nomer12 = types.KeyboardButton('номер 12')
nomer13 = types.KeyboardButton('номер 13')
nomer14 = types.KeyboardButton('номер 14')
nomer15 = types.KeyboardButton('номер 15')

sled1 = types.KeyboardButton('след1')						#кнопки передвижения
sled2 = types.KeyboardButton('след2')
back = types.KeyboardButton("Вернуться в главное меню")
pred1 = types.KeyboardButton('пред1')
pred2 = types.KeyboardButton('пред2')

markup_base = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=5)		#осн клавиатура
markup_base.add(nomera_a,teori_a)

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=5)			#клавиатура стр1
markup1.add(nomer1,nomer2,nomer3,nomer4,nomer5,back,sled1)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=5)			#клавиатура стр2
markup2.add(nomer6,nomer7,nomer8,nomer9,nomer10,pred1,back,sled2)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=5)			#клавиатура стр3
markup3.add(nomer11,nomer12,nomer13,nomer14,nomer15,pred2,back)



with open('quest.txt', 'r',encoding='UTF-8') as file:							#открытие фалов 1 вопросы  2 ответы
	nomera_list = []
	for x in file.readlines():
		x_str = str(x)
		nomera_list.append(x_str)

with open('answ.txt',encoding='UTF-8') as file:
	answ_list = []
	for x in file.readlines():
		x_str = str(x)
		x_str = x_str.strip('\n')
		answ_list.append(x_str)

n_4 = os.listdir("nom4")



@bot.message_handler(commands=["start"])									#старт
def start(message):
	mess = 'ку это бот по подготовке к огэ. Напиши команду /buttons'
	bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=["help"])
def com(message):
    markup = types.ReplyKeyboardMarkup()
    nomera = types.KeyboardButton('номера')
    variant = types.KeyboardButton('составить вариант')
    teori = types.KeyboardButton('теория к заданиям')
    markup.add(nomera,variant,teori)
    bot.send_message(message.chat.id,'ввыбор категории', reply_markup=markup)

@bot.message_handler(commands=["buttons"])
def com(message):																					#начало	
	bot.send_message(message.chat.id,'выбор категории', reply_markup=markup_base)


@bot.message_handler(content_types=["text"])											#при любом тексте
def func(message):
	global flag_ans
	global rand 


	if(message.text =='номера') or (message.text =='пред1'):										#номера 1-5 стр1
		bot.send_message(message.chat.id,'выбери номер', reply_markup=markup1)

	elif (message.text == "след1") or (message.text =='пред2'):											#номера 6-10 стр2
		bot.send_message(message.chat.id,'выбери номер', reply_markup=markup2)
		flag_ans = False

	elif (message.text == "след2") :																	#номера 10-15 стр3
		bot.send_message(message.chat.id,'выбери номер', reply_markup=markup3)
		flag_ans = False
	
	elif (message.text == "Вернуться в главное меню"):												#начало		
		bot.send_message(message.chat.id,'Вы вернулись в главное меню', reply_markup=markup_base)
		flag_ans = False

	
	
	elif message.text == 'номер 1':													#вывод номер1
		rand = random.randint(1,5)
		bot.send_message(message.chat.id,nomera_list[rand], parse_mode='html')
		bot.send_message(message.chat.id,'введите ответ слово как оно указано в тексте', parse_mode='html')
		flag_ans = True
		return

	elif message.text == 'номер 2':													#вывод номер2
		rand = random.randint(7,11)
		bot.send_message(message.chat.id,nomera_list[rand], parse_mode='html')
		bot.send_message(message.chat.id,'введите ответ ЗАГЛАВНЫМИ буквами без точек и пробелов', parse_mode='html')
		flag_ans = True
		return

	elif message.text == 'номер 3':													#вывод номер3
		rand = random.randint(13,17)
		bot.send_message(message.chat.id,nomera_list[rand])
		bot.send_message(message.chat.id,'введите ответ только число', parse_mode='html')
		flag_ans = True
		return

	elif message.text == 'номер 4':													#вывод номер4
		rand_2 = random.randint(0,4)
		rand = 19 + rand_2
		bot.send_message(message.chat.id,nomera_list[rand])
		bot.send_photo(message.chat.id, photo=open(f'nom4//{n_4[rand_2]}', 'rb'))
		bot.send_message(message.chat.id,'введите ответ только число', parse_mode='html')
		flag_ans = True
		return

	elif message.text == 'номер 5':													#вывод номер5
		rand = random.randint(25,29)
		bot.send_message(message.chat.id,nomera_list[rand])
		bot.send_message(message.chat.id,'введите ответ только число', parse_mode='html')
		flag_ans = True
		return

	elif message.text == 'номер 7':													#вывод номер7
		rand = random.randint(37,41)
		bot.send_message(message.chat.id,nomera_list[rand])
		bot.send_message(message.chat.id,'введите ответ  заглавными буквами без пробелов и запятых', parse_mode='html')
		flag_ans = True
		return
	
	elif flag_ans == False:																				#текст не распознан
		bot.send_message(message.chat.id,'бот не распознаёт ваше сообщение', parse_mode='html')

	if flag_ans == True:												#проверка номера если прав
		if (message.text == answ_list[rand]):
			bot.send_message(message.chat.id,'Молодец!')
			flag_ans = False
		else:														#вывод если неправильно номер 
			otvet = types.InlineKeyboardMarkup(row_width=1)			
			button1 = types.InlineKeyboardButton("Правильный ответ!", callback_data ='1')
			button2 = types.InlineKeyboardButton("Теория", callback_data ='2')
			otvet.add(button1, button2)
			bot.send_message(message.chat.id,'Ответ неправильный, если есть трудности посмотри теорию, а также можешь узнать правильный ответ.',reply_markup=otvet,parse_mode='html')
	

	

@bot.callback_query_handler(func=lambda call: True)					#кнопки правильных ответов 
def callback_inline(call):
	global flag_ans
	if call.message:
		if call.data == "1":
			bot.send_message(call.message.chat.id,answ_list[rand])
			flag_ans = False

		elif call.data == '2':
			bot.send_message(call.message.chat.id,'теория будет позже')
			flag_ans = False

bot.polling(none_stop=True)		

x = random.randint()
print(x)