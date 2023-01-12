import os
# from file_manager import on_dysplay
os.chdir(os.path.dirname(__file__))
import codecs
from telebot import telebot, types

BOT_TOKEN = '5820047270:AAEXfYZOginRytOpBRE6FnCvqS54Z6u-uN8' # Токен Телеграм-бота

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ["start", "help"])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text = "1 - Новая запись\n 2 - Вывод на экран\n 3 - Импорт из файла\n 4 - Экспорт в файл\n")

@bot.message_handler()
def answer(msg: types.Message):
    text = msg.text
  
    if text == "1":
        bot.register_next_step_handler(msg, number_1)
        bot.send_message(chat_id=msg.from_user.id, text = "Введите Фамилию, Имя, Номер телефона, Описание через пробел")
    elif text == "2":
        bot.register_next_step_handler(msg, number_2)
    



def number_1(msg):
    last_name = list(msg.text.split())
    new_str(last_name)
    bot.send_message(chat_id=msg.from_user.id, text = "Добавлено")

def number_2(msg: types.Message):
    text = msg.text

    a = ''

def on_dysplay():
    str = codecs.open('book.txt','r', encoding= 'utf-8').read()
    str = list(str.split('\r\n'))
    for x, y in enumerate(str):
        str[x] = list(y.split(';'))
    j = (' '.join(str[x]))
    bot.send_message(chat_id=msg.from_user.id, text = j)



bot.polling()

# def answer(msg: types.Message):
#     filename = msg.document.file_name
#     with open(filename, 'wb') as file:
#         file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
#     bot.send_message(chat_id=msg.from_user.id, text='Loading')