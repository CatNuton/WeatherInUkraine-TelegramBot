import telebot
from telebot import types
import config
import requests
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot(config.token)
r = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B2%D1%96%D0%BD%D0%BD%D0%B8%D1%86%D1%8F')
html = BS(r.content, 'html.parser')

for el in html.select('#content'):
    t_min = el.select(".temperature .min")[0].text
    t_max = el.select(".temperature .max")[0].text
    text = el.select(".wDescription .description")[0].text


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Ласкаво Просимо <b><u>{message.from_user.first_name}!</u></b>',
                     parse_mode="html")

@bot.message_handler(commands=['weather'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода В Вінниці:"+"\nТемпература: "+t_min+', '+t_max+"\nОпис:\n"+text)



bot.polling(none_stop=True)