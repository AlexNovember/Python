import math
from datetime import datetime as dt
from aiogram import Bot, types
from telebot import telebot, types
import os
import codecs
os.chdir(os.path.dirname(__file__))

BOT_TOKEN = '5820047270:AAEXfYZOginRytOpBRE6FnCvqS54Z6u-uN8' # Токен Телеграм-бота

bot = telebot.TeleBot(BOT_TOKEN)
 
value = ""
old_value = ""

keyboard = telebot.types.InlineKeyboardMarkup()

keyboard.row(   telebot.types.InlineKeyboardButton(" ", callback_data="no"),
                telebot.types.InlineKeyboardButton("C", callback_data="C"),
                telebot.types.InlineKeyboardButton("<=", callback_data="<="),
                telebot.types.InlineKeyboardButton("/", callback_data="/") )


keyboard.row(   telebot.types.InlineKeyboardButton("7", callback_data="7"),
                telebot.types.InlineKeyboardButton("8", callback_data="8"),
                telebot.types.InlineKeyboardButton("9", callback_data="9"),
                telebot.types.InlineKeyboardButton("*", callback_data="*") )

keyboard.row(   telebot.types.InlineKeyboardButton("4", callback_data="4"),
                telebot.types.InlineKeyboardButton("5", callback_data="5"),
                telebot.types.InlineKeyboardButton("6", callback_data="6"),
                telebot.types.InlineKeyboardButton("-", callback_data="-") )

keyboard.row(   telebot.types.InlineKeyboardButton("1", callback_data="1"),
                telebot.types.InlineKeyboardButton("2", callback_data="2"),
                telebot.types.InlineKeyboardButton("3", callback_data="3"),
                telebot.types.InlineKeyboardButton("+", callback_data="+") )

keyboard.row(   telebot.types.InlineKeyboardButton("Pi ", callback_data="Pi"),
                telebot.types.InlineKeyboardButton("0", callback_data="0"),
                telebot.types.InlineKeyboardButton(",", callback_data="."),
                telebot.types.InlineKeyboardButton("=", callback_data="=") )

@bot.message_handler(commands = ["start", "calc"])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text = "1 - простой калькулятор,\n 2 - комплексные числа")

@bot.message_handler()
def answer(msg: types.Message):
    text = msg.text
  
    if text == "1":
        bot.send_message(msg.from_user.id, text, reply_markup=keyboard)
    elif text == "2":
        bot.register_next_step_handler(msg, complex_)

    with codecs.open('logging.txt', 'a') as lg:
        operation_time = dt.now().strftime('%H:%M')
        lg.writelines({operation_time + ' ' + text + '\n'})

@bot.message_handler()
def complex_(msg: types.Message):

    lst = list(msg.text.split())
    sign = lst[1]
    
    first_num = complex(lst[0])
    second_num = complex(lst[2])

    if second_num == 0 and sign == '/':
        bot.send_message(chat_id=msg.from_user.id, text = "Деление на 0")

    if sign == "+":
        result = first_num + second_num
        bot.send_message(msg.from_user.id, text=f'Сложение {result}')
    elif sign == "-":
        result = first_num - second_num
        bot.send_message(msg.from_user.id, text=f'Вычитание {result}')
    elif sign == "*":
        result = first_num * second_num
        bot.send_message(msg.from_user.id, text=f'Умножение {result}')
    elif sign == "/":
         result = first_num / second_num
         bot.send_message(msg.from_user.id, text=f'Деление {result}')
    
    
    with codecs.open('logging.txt', 'a') as lg:
        operation_time = dt.now().strftime('%H:%M')
        lg.writelines(f'{operation_time, lst, result}\n')

   
@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data
    
    if data == "no" :
        pass
    elif data == "C" :
        value = ""
    elif data == "Pi" :
        value = math.pi
    elif data == "=" :
        try:
            value = str(eval(value))
        except:
            value = "Ошибка!"
    else:
        value += data

    if value != old_value:
        if value == "":
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="0", reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)

    old_value = value
    if value == "Ошибка!": value = ""

    with codecs.open('logging.txt', 'a') as lg:
        operation_time = dt.now().strftime('%H:%M')
        lg.writelines(operation_time + ' ' + value + '\n')


bot.polling(none_stop=False, interval=0)






