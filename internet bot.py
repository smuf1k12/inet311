import telebot
from telebot import types
import os
bot =  telebot.TeleBot('5752560348:AAGQqOLko-EFa4fqlr2LWSiD9Mvw4Ptrzu8') 
@bot.message_handler(commands=['start'])
def start(messege):
  markup = types.ReplyKeyboardMarkup()
  svet = types.KeyboardButton("Проверить")
  markup.add(svet)
  bot.send_message(messege.chat.id, 'Бот для проверки интернета',parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_uset_text(messege):
  if messege.text == 'Проверить':
    bot.send_message(messege.chat.id, 'Проверяю...', parse_mode='html')
    hostname = "80.64.92.46"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
      bot.send_message(messege.chat.id, 'Интернет есть')
    else:
      bot.send_message(messege.chat.id, 'Интернета нет')

  


bot.polling(non_stop=True)
