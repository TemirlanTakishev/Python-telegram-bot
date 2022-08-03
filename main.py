import telebot
import random
from telebot import types

token = '5547091954:AAGCoosjIPOoqan6wz7lq-gjzM4vzzmKMyA'
bot = telebot.TeleBot(token)
 
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    movie_botton = types.KeyboardButton('сайт с фильмами 📺')
    book_botton = types.KeyboardButton('сайт с книгами 📚')
    walk_button = types.KeyboardButton('прогулка 🗺')
    markup.add(movie_botton,book_botton,walk_button)
    bot.send_message(message.chat.id,'Выбери',reply_markup=markup)
    
@bot.message_handler(content_types=["text"])
def blabla(message):
    if message.text == 'сайт с фильмами 📺':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        movie_botton = types.KeyboardButton('Морбиус 🧛')
        book_botton = types.KeyboardButton('Игры сознания 🧠')
        walk_button = types.KeyboardButton('Миротворцы 🗺')
        walk_button = types.KeyboardButton('Рандомный фильм 🤔')
        back_button = types.KeyboardButton('Назад 🔙')
        markup.add(movie_botton,book_botton,walk_button,back_button)
        bot.send_message(message.chat.id,'Выбери',reply_markup=markup)

    if message.text == 'Рандомный фильм 🤔':
        movies = ['http://baskino.me/films/boeviki/32486-morbius.html','http://baskino.me/films/dramy/32464-igry-soznaniya.html','http://baskino.me/films/komedii/32458-mirotvorcy.html']
        random.shuffle(movies)
        murkup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('фильмы', url = movies[0])
        murkup.add(btn)
        bot.send_message(message.chat.id,'Будет интересно!',reply_markup=murkup)

    if message.text == 'Морбиус 🧛':
        murkup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('фильмы', url = 'http://baskino.me/films/boeviki/32486-morbius.html')
        murkup.add(btn)
        bot.send_message(message.chat.id,'не будь вампиром',reply_markup=murkup)

    if message.text == 'Игры сознания 🧠':
        murkup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('фильмы', url = 'http://baskino.me/films/dramy/32464-igry-soznaniya.html')
        murkup.add(btn)
        bot.send_message(message.chat.id,'Смотри',reply_markup=murkup)    

    if message.text == 'Миротворцы 🗺':
        murkup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('фильмы', url = 'http://baskino.me/films/komedii/32458-mirotvorcy.html')
        murkup.add(btn)
        bot.send_message(message.chat.id,'мир',reply_markup=murkup)

    if message.text == 'Назад 🔙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        movie_botton = types.KeyboardButton('сайт с фильмами 📺')
        book_botton = types.KeyboardButton('сайт с книгами 📚')
        walk_button = types.KeyboardButton('прогулка 🗺')
        markup.add(movie_botton,book_botton,walk_button)
        bot.send_message(message.chat.id,'Выбери',reply_markup=markup)
bot.polling(non_stop=True)
