import telebot
from telebot import types
import config
import requests
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot(config.token)
#Винница
vin = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B2%D1%96%D0%BD%D0%BD%D0%B8%D1%86%D1%8F')
html_vin = BS(vin.content, 'html.parser')

for el in html_vin.select('#content'):
    vin_min = el.select(".temperature .min")[0].text
    vin_max = el.select(".temperature .max")[0].text
    vin_text = el.select(".wDescription .description")[0].text

#kharkiv
kh = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%85%D0%B0%D1%80%D0%BA%D1%96%D0%B2')
html_kh = BS(kh.content, 'html.parser')

for el in html_kh.select('#content'):
    kh_min = el.select(".temperature .min")[0].text
    kh_max = el.select(".temperature .max")[0].text
    kh_text = el.select(".wDescription .description")[0].text
#kyiv
ky = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2')
html_ky = BS(ky.content, 'html.parser')

for el in html_ky.select('#content'):
    ky_min = el.select(".temperature .min")[0].text
    ky_max = el.select(".temperature .max")[0].text
    ky_text = el.select(".wDescription .description")[0].text
#uzhgorod
uz = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%83%D0%B6%D0%B3%D0%BE%D1%80%D0%BE%D0%B4')
html_uz = BS(uz.content, 'html.parser')

for el in html_uz.select('#content'):
    uz_min = el.select(".temperature .min")[0].text
    uz_max = el.select(".temperature .max")[0].text
    uz_text = el.select(".wDescription .description")[0].text

lv = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%8C%D0%B2%D1%96%D0%B2')
html_lv = BS(lv.content, 'html.parser')

for el in html_lv.select('#content'):
    lv_min = el.select(".temperature .min")[0].text
    lv_max = el.select(".temperature .max")[0].text
    lv_text = el.select(".wDescription .description")[0].text

IF = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%96%D0%B2%D0%B0%D0%BD%D0%BE-%D1%84%D1%80%D0%B0%D0%BD%D0%BA%D1%96%D0%B2%D1%81%D1%8C%D0%BA')
html_IF = BS(IF.content, 'html.parser')

for el in html_IF.select('#content'):
    IF_min = el.select(".temperature .min")[0].text
    IF_max = el.select(".temperature .max")[0].text
    IF_text = el.select(".wDescription .description")[0].text

ch = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%87%D0%B5%D1%80%D0%BD%D1%96%D0%B2%D1%86%D1%96')
html_ch = BS(ch.content, 'html.parser')

for el in html_ch.select('#content'):
    ch_min = el.select(".temperature .min")[0].text
    ch_max = el.select(".temperature .max")[0].text
    ch_text = el.select(".wDescription .description")[0].text

Ter = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%82%D0%B5%D1%80%D0%BD%D0%BE%D0%BF%D1%96%D0%BB%D1%8C')
html_Ter = BS(Ter.content, 'html.parser')

for el in html_Ter.select('#content'):
    Ter_min = el.select(".temperature .min")[0].text
    Ter_max = el.select(".temperature .max")[0].text
    Ter_text = el.select(".wDescription .description")[0].text

khmel = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%85%D0%BC%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D1%8C%D0%BA%D0%B8%D0%B9')
html_khmel = BS(khmel.content, 'html.parser')

for el in html_khmel.select('#content'):
    khmel_min = el.select(".temperature .min")[0].text
    khmel_max = el.select(".temperature .max")[0].text
    khmel_text = el.select(".wDescription .description")[0].text

riv = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%80%D1%96%D0%B2%D0%BD%D0%B5')
html_riv = BS(riv.content, 'html.parser')

for el in html_riv.select('#content'):
    riv_min = el.select(".temperature .min")[0].text
    riv_max = el.select(".temperature .max")[0].text
    riv_text = el.select(".wDescription .description")[0].text

lutsk = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%83%D1%86%D1%8C%D0%BA')
html_lutsk = BS(lutsk.content, 'html.parser')

for el in html_lutsk.select('#content'):
    lutsk_min = el.select(".temperature .min")[0].text
    lutsk_max = el.select(".temperature .max")[0].text
    lutsk_text = el.select(".wDescription .description")[0].text

#Житомир
zhit = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B6%D0%B8%D1%82%D0%BE%D0%BC%D0%B8%D1%80')
html_zhit = BS(zhit.content, 'html.parser')

for el in html_zhit.select('#content'):
    zhit_min = el.select(".temperature .min")[0].text
    zhit_max = el.select(".temperature .max")[0].text
    zhit_text = el.select(".wDescription .description")[0].text

#odesa
odes = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BE%D0%B4%D0%B5%D1%81%D0%B0')
html_odes = BS(odes.content, 'html.parser')

for el in html_odes.select('#content'):
    odes_min = el.select(".temperature .min")[0].text
    odes_max = el.select(".temperature .max")[0].text
    odes_text = el.select(".wDescription .description")[0].text
#mykolaev
myk = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BC%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D1%97%D0%B2')
html_myk = BS(myk.content, 'html.parser')

for el in html_myk.select('#content'):
    myk_min = el.select(".temperature .min")[0].text
    myk_max = el.select(".temperature .max")[0].text
    myk_text = el.select(".wDescription .description")[0].text
#kropivnytskyi
krop = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D1%80%D0%BE%D0%BF%D0%B8%D0%B2%D0%BD%D0%B8%D1%86%D1%8C%D0%BA%D0%B8%D0%B9')
html_krop = BS(krop.content, 'html.parser')

for el in html_krop.select('#content'):
    krop_min = el.select(".temperature .min")[0].text
    krop_max = el.select(".temperature .max")[0].text
    krop_text = el.select(".wDescription .description")[0].text
#cherkasy
cherk = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%87%D0%B5%D1%80%D0%BA%D0%B0%D1%81%D0%B8')
html_cherk = BS(cherk.content, 'html.parser')

for el in html_cherk.select('#content'):
    cherk_min = el.select(".temperature .min")[0].text
    cherk_max = el.select(".temperature .max")[0].text
    cherk_text = el.select(".wDescription .description")[0].text

qur = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%81%D0%B8%D0%BC%D1%84%D0%B5%D1%80%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C')
html_qur = BS(qur.content, 'html.parser')

for el in html_qur.select('#content'):
    qur_min = el.select(".temperature .min")[0].text
    qur_max = el.select(".temperature .max")[0].text
    qur_text = el.select(".wDescription .description")[0].text

khers = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%85%D0%B5%D1%80%D1%81%D0%BE%D0%BD')
html_khers = BS(khers.content, 'html.parser')

for el in html_khers.select('#content'):
    khers_min = el.select(".temperature .min")[0].text
    khers_max = el.select(".temperature .max")[0].text
    khers_text = el.select(".wDescription .description")[0].text

zap = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B7%D0%B0%D0%BF%D0%BE%D1%80%D1%96%D0%B6%D0%B6%D1%8F')
html_zap = BS(zap.content, 'html.parser')

for el in html_zap.select('#content'):
    zap_min = el.select(".temperature .min")[0].text
    zap_max = el.select(".temperature .max")[0].text
    zap_text = el.select(".wDescription .description")[0].text

dnipr = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B4%D0%BD%D1%96%D0%BF%D1%80%D0%BE')
html_dnipr = BS(dnipr.content, 'html.parser')

for el in html_dnipr.select('#content'):
    dnipr_min = el.select(".temperature .min")[0].text
    dnipr_max = el.select(".temperature .max")[0].text
    dnipr_text = el.select(".wDescription .description")[0].text

don = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B4%D0%BE%D0%BD%D0%B5%D1%86%D1%8C%D0%BA')
html_don = BS(don.content, 'html.parser')

for el in html_don.select('#content'):
    don_min = el.select(".temperature .min")[0].text
    don_max = el.select(".temperature .max")[0].text
    don_text = el.select(".wDescription .description")[0].text

lug = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%83%D0%B3%D0%B0%D0%BD%D1%81%D1%8C%D0%BA')
html_lug = BS(lug.content, 'html.parser')

for el in html_lug.select('#content'):
    lug_min = el.select(".temperature .min")[0].text
    lug_max = el.select(".temperature .max")[0].text
    lug_text = el.select(".wDescription .description")[0].text

polt = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BF%D0%BE%D0%BB%D1%82%D0%B0%D0%B2%D0%B0')
html_polt = BS(polt.content, 'html.parser')

for el in html_polt.select('#content'):
    polt_min = el.select(".temperature .min")[0].text
    polt_max = el.select(".temperature .max")[0].text
    polt_text = el.select(".wDescription .description")[0].text

su = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%81%D1%83%D0%BC%D0%B8')
html_su = BS(su.content, 'html.parser')

for el in html_su.select('#content'):
    su_min = el.select(".temperature .min")[0].text
    su_max = el.select(".temperature .max")[0].text
    su_text = el.select(".wDescription .description")[0].text

chern = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%87%D0%B5%D1%80%D0%BD%D1%96%D0%B3%D1%96%D0%B2')
html_chern = BS(chern.content, 'html.parser')

for el in html_chern.select('#content'):
    chern_min = el.select(".temperature .min")[0].text
    chern_max = el.select(".temperature .max")[0].text
    chern_text = el.select(".wDescription .description")[0].text


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Добрий День <b><u>{message.from_user.first_name}!</u></b> Для Того Щоб Бот Вивів Погоду, Зробіть Ці Дії: 1.Натисніть На Синю Кнопку "Меню"\n 2.Виберіть Місто, Погоду Якого Ви Б Хотіли Побачити',
                     parse_mode="html")

@bot.message_handler(commands=['vinnytsia'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода В Вінниці:"+"\nТемпература: "+vin_min+', '+vin_max+"\nОпис:\n"+vin_text)


@bot.message_handler(commands=['kharkiv'])
def aswerMenu(message):
    bot.send_message(message.chat.id,
                     "Погода В Харкові:" + "\nТемпература: " + kh_min + ', ' + kh_max + "\nОпис:\n" + kh_text)


@bot.message_handler(commands=['kyiv'])
def answeMenu(message):
    bot.send_message(message.chat.id, "Погода В Києві:" + "\nТемпература: " + ky_min + ', ' + ky_max + "\nОпис:\n" + ky_text)


@bot.message_handler(commands=['uzhgorod'])
def answeMenu(message):
    bot.send_message(message.chat.id, "Погода В Ужгороді:" + "\nТемпература: " + uz_min + ', ' + uz_max + "\nОпис:\n" + uz_text)


@bot.message_handler(commands=['lviv'])
def answeMenu(message):
    bot.send_message(message.chat.id, "Погода У Львові:" + "\nТемпература: " + lv_min + ', ' + lv_max + "\nОпис:\n" + lv_text)


@bot.message_handler(commands=['ivanofrankivsk'])
def answeMenu(message):
    bot.send_message(message.chat.id, "Погода У Івано-Франківську:" + "\nТемпература: " + IF_min + ', ' + IF_max + "\nОпис:\n" + IF_text)


@bot.message_handler(commands=['chernivtsi'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Чернівцях:" + "\nТемпература: " + ch_min + ', ' + ch_max + "\nОпис:\n" + ch_text)


@bot.message_handler(commands=['ternopil'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Тернополі:" + "\nТемпература: " + Ter_min + ', ' + Ter_max + "\nОпис:\n" + Ter_text)


@bot.message_handler(commands=['khmelnytskyi'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Хмельницькому:" + "\nТемпература: " + khmel_min + ', ' + khmel_max + "\nОпис:\n" + khmel_text)


@bot.message_handler(commands=['rivne'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Рівному:" + "\nТемпература: " + riv_min + ', ' + riv_max + "\nОпис:\n" + riv_text)


@bot.message_handler(commands=['lutsk'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Луцьку:" + "\nТемпература: " + lutsk_min + ', ' + lutsk_max + "\nОпис:\n" + lutsk_text)


@bot.message_handler(commands=['zhytomyr'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Житомирі:" + "\nТемпература: " + zhit_min + ', ' + zhit_max + "\nОпис:\n" + zhit_text)


@bot.message_handler(commands=['odesa'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода В Одесі:" + "\nТемпература: " + odes_min + ', ' + odes_max + "\nОпис:\n" + odes_text)


@bot.message_handler(commands=['mykolayiv'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Миколаєві:" + "\nТемпература: " + myk_min + ', ' + myk_max + "\nОпис:\n" + myk_text)


@bot.message_handler(commands=['kropyvnytskyi'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Кропивницькому:" + "\nТемпература: " + krop_min + ', ' + krop_max + "\nОпис:\n" + krop_text)


@bot.message_handler(commands=['cherkasy'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Черкасах:" + "\nТемпература: " + cherk_min + ', ' + cherk_max + "\nОпис:\n" + cherk_text)


@bot.message_handler(commands=['symferopol'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Сімферополі:" + "\nТемпература: " + qur_min + ', ' + qur_max + "\nОпис:\n" + qur_text)


@bot.message_handler(commands=['kherson'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Херсоні:" + "\nТемпература: " + khers_min + ', ' + khers_max + "\nОпис:\n" + khers_text)


@bot.message_handler(commands=['zaporizhzhia'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Запоріжжі:" + "\nТемпература: " + zap_min + ', ' + zap_max + "\nОпис:\n" + zap_text)


@bot.message_handler(commands=['dnypro'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Дніпрі:" + "\nТемпература: " + dnipr_min + ', ' + dnipr_max + "\nОпис:\n" + dnipr_text)


@bot.message_handler(commands=['donetsk'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Донецьку:" + "\nТемпература: " + don_min + ', ' + don_max + "\nОпис:\n" + don_text)


@bot.message_handler(commands=['lugansk'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Луганську:" + "\nТемпература: " + lug_min + ', ' + lug_max + "\nОпис:\n" + lug_text)


@bot.message_handler(commands=['poltava'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Полтаві:" + "\nТемпература: " + polt_min + ', ' + polt_max + "\nОпис:\n" + polt_text)


@bot.message_handler(commands=['sumi'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У Сумах:" + "\nТемпература: " + su_min + ', ' + su_max + "\nОпис:\n" + su_text)


@bot.message_handler(commands=['chernihiv'])
def answerMenu(message):
    bot.send_message(message.chat.id, "Погода У чернігові:" + "\nТемпература: " + chern_min + ', ' + chern_max + "\nОпис:\n" + chern_text)



bot.polling(none_stop=True)