import telebot
from telebot import types
from woorden import*
from family import*
from weather import*
from colours import*
from ttime import*
import random

TOKEN = '6144198214:AAEZy9E7rrcXWqYuJ_5Q_ZkHCoCBFYZWV7I'
bot = telebot.TeleBot(TOKEN)
def kortezh(text):
    if type(text) == tuple:
        return ', '.join(text)
    else:
        return text
word_index = list()
part = None
task_numb = 0
@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Популярні прикметники')
    item2 = types.KeyboardButton('Родина')
    item3 = types.KeyboardButton('Погода')
    item4 = types.KeyboardButton('Кольори')
    item5 = types.KeyboardButton('Час')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Вітаю, {0.first_name}! Обери тему'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    global part, word_index, task_numb
    def loop(party):
        global word_index, task_numb
        while True:
            nonlocal word_num
            if len(word_index) >= len(party):
                word_index = []
                task_numb = 0
                bot.send_message(message.chat.id, f"<i><b>Повний круг пройдено</b></i>", parse_mode='HTML')
            word_num = random.randint(0, len(party)-1)
            if word_num in word_index:
                continue
            if word_num not in word_index:
                word_index.append(word_num)
                break
    if message.chat.type == 'private':
        if message.text == 'Популярні прикметники':
            part = adjective
            word_index = []
            task_numb = 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇦 Українська')
            item2 = types.KeyboardButton('🇬🇧 English')
            item3 = types.KeyboardButton('🇳🇱 Dutch')
            item4 = types.KeyboardButton('🔙 Назад')
            markup.add(item1, item2, item3, item4) 
            bot.send_message(message.chat.id, 'Обери мову', reply_markup = markup)
        elif message.text == 'Родина':
            part = family
            word_index = []
            task_numb = 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇦 Українська')
            item2 = types.KeyboardButton('🇬🇧 English')
            item3 = types.KeyboardButton('🇳🇱 Dutch')
            item4 = types.KeyboardButton('🔙 Назад')
            markup.add(item1, item2, item3, item4) 
            bot.send_message(message.chat.id, 'Обери мову', reply_markup = markup)
        elif message.text == 'Погода':
            part = weather
            word_index = []
            task_numb = 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇦 Українська')
            item2 = types.KeyboardButton('🇬🇧 English')
            item3 = types.KeyboardButton('🇳🇱 Dutch')
            item4 = types.KeyboardButton('🔙 Назад')
            markup.add(item1, item2, item3, item4) 
            bot.send_message(message.chat.id, 'Обери мову', reply_markup = markup)
        elif message.text == 'Кольори':
            part = colours
            word_index = []
            task_numb = 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇦 Українська')
            item2 = types.KeyboardButton('🇬🇧 English')
            item3 = types.KeyboardButton('🇳🇱 Dutch')
            item4 = types.KeyboardButton('🔙 Назад')
            markup.add(item1, item2, item3, item4) 
            bot.send_message(message.chat.id, 'Обери мову', reply_markup = markup)
        elif message.text == 'Час':
            part =  ttime
            word_index = []
            task_numb = 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇦 Українська')
            item2 = types.KeyboardButton('🇬🇧 English')
            item3 = types.KeyboardButton('🇳🇱 Dutch')
            item4 = types.KeyboardButton('🔙 Назад')
            markup.add(item1, item2, item3, item4) 
            bot.send_message(message.chat.id, 'Обери мову', reply_markup = markup)
        elif message.text == '🇺🇦 Українська':
            try:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Правильна відповідь')
                item2 = types.KeyboardButton('Наступне')
                item3 = types.KeyboardButton('Змінити мову')
                item4 = types.KeyboardButton('🔙 Назад')
                markup.add(item1, item2, item3, item4)
                loop(part)
                uk = part[word_num]['uk']
                task_numb +=1
                bot.send_message(message.chat.id, f"<b>{task_numb} із {len(part)}.</b> Переклади:\t\t<i><b>{kortezh(uk)}</b></i>", parse_mode='HTML', reply_markup = markup)
            except TypeError:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Популярні прикметники')
                item2 = types.KeyboardButton('Родина')
                item3 = types.KeyboardButton('Погода')
                item4 = types.KeyboardButton('Кольори')
                item5 = types.KeyboardButton('Час')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id, 'Обери тему', reply_markup = markup)
        elif message.text in ('🔙 Назад', '🔙 Back', '🔙 Terug'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Популярні прикметники')
            item2 = types.KeyboardButton('Родина')
            item3 = types.KeyboardButton('Погода')
            item4 = types.KeyboardButton('Кольори')
            item5 = types.KeyboardButton('Час')
            markup.add(item1, item2, item3, item4, item5)
            bot.send_message(message.chat.id, 'Обери тему', reply_markup = markup)
        elif message.text == 'Правильна відповідь':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item2 = types.KeyboardButton('Наступне')
            item3 = types.KeyboardButton('Змінити мову')
            item4 = types.KeyboardButton('🔙 Назад')
            markup.add(item2, item3, item4) 
            try:
                word_num = word_index[-1]
                en = part[word_num]['en']
                nd = part[word_num]['nd']
                bot.send_message(message.chat.id, f"EN\t🇬🇧\t-\t<i><b>{kortezh(en)}</b></i>\t\t|\t\t NL\t🇳🇱\t-\t<i><b>{kortezh(nd)}</b></i>", parse_mode='HTML', reply_markup = markup)
            except:
                bot.send_message(message.chat.id, f"Переклад недоступний\nНатисни:\t\t<b>Наступне</b>", parse_mode='HTML', reply_markup = markup)
        elif message.text == 'Наступне':
            try:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Правильна відповідь')
                item2 = types.KeyboardButton('Наступне')
                item3 = types.KeyboardButton('Змінити мову')
                item4 = types.KeyboardButton('🔙 Назад')
                markup.add(item1, item2, item3, item4)  
                loop(part)
                uk = part[word_num]['uk']
                task_numb +=1
                bot.send_message(message.chat.id, f"<b>{task_numb} із {len(part)}.</b> Переклади:\t\t<i><b>{kortezh(uk)}</b></i>", parse_mode='HTML', reply_markup = markup)
            except TypeError:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Популярні прикметники')
                item2 = types.KeyboardButton('Родина')
                item3 = types.KeyboardButton('Погода')
                item4 = types.KeyboardButton('Кольори')
                item5 = types.KeyboardButton('Час')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id, '*UN* Обери тему', reply_markup = markup)
        elif message.text == 'Змінити мову':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇦 Українська')
            item2 = types.KeyboardButton('🇬🇧 English')
            item3 = types.KeyboardButton('🇳🇱 Dutch')
            item4 = types.KeyboardButton('🔙 Назад')
            markup.add(item1, item2, item3, item4) 
            bot.send_message(message.chat.id, 'Обери мову', reply_markup = markup)
        elif message.text == '🇬🇧 English':
            try:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Right answer')
                item2 = types.KeyboardButton('Next')
                item3 = types.KeyboardButton('Change the language')
                item4 = types.KeyboardButton('🔙 Back')
                markup.add(item1, item2, item3, item4) 
                loop(part)
                en = part[word_num]['en']
                task_numb +=1
                bot.send_message(message.chat.id, f"<b>{task_numb} of {len(part)}.</b> Translate:\t\t<i><b>{kortezh(en)}</b></i>", parse_mode='HTML', reply_markup = markup)
            except:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Популярні прикметники')
                item2 = types.KeyboardButton('Родина')
                item3 = types.KeyboardButton('Погода')
                item4 = types.KeyboardButton('Кольори')
                item5 = types.KeyboardButton('Час')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id, 'Обери тему', reply_markup = markup)
        elif message.text == 'Right answer':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item2 = types.KeyboardButton('Next')
            item3 = types.KeyboardButton('Change the language')
            item4 = types.KeyboardButton('🔙 Back')
            markup.add(item2, item3, item4)
            try:
                word_num = word_index[-1]
                uk = part[word_num]['uk']
                nd = part[word_num]['nd']
                bot.send_message(message.chat.id, f"UA\t🇺🇦\t-\t<i><b>{kortezh(uk)}</b></i>\t\t|\t\t NL\t🇳🇱\t-\t<i><b>{kortezh(nd)}</b></i>", parse_mode='HTML', reply_markup = markup)
            except:
                bot.send_message(message.chat.id, f"Translation is unavailable\nClick:\t\t<b>Next</b>", parse_mode='HTML', reply_markup = markup)
        elif message.text == 'Next':
            try:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Right answer')
                item2 = types.KeyboardButton('Next')
                item3 = types.KeyboardButton('Change the language')
                item4 = types.KeyboardButton('🔙 Back')
                markup.add(item1, item2, item3, item4)  
                loop(part)
                en = part[word_num]['en']
                task_numb +=1
                bot.send_message(message.chat.id, f"<b>{task_numb} of {len(part)}.</b> Translate:\t\t<i><b>{kortezh(en)}</b></i>", parse_mode='HTML', reply_markup = markup)
            except TypeError:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Популярні прикметники')
                item2 = types.KeyboardButton('Родина')
                item3 = types.KeyboardButton('Погода')
                item4 = types.KeyboardButton('Кольори')
                item5 = types.KeyboardButton('Час')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id, 'Обери тему', reply_markup = markup)
        elif message.text == 'Change the language':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇦 Українська')
            item2 = types.KeyboardButton('🇬🇧 English')
            item3 = types.KeyboardButton('🇳🇱 Dutch')
            item4 = types.KeyboardButton('🔙 Back')
            markup.add(item1, item2, item3, item4) 
            bot.send_message(message.chat.id, 'Choose a language', reply_markup = markup)
        elif message.text == '🇳🇱 Dutch':
            try:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Juiste antwoord')
                item2 = types.KeyboardButton('Volgende')
                item3 = types.KeyboardButton('Verander de taal')
                item4 = types.KeyboardButton('🔙 Terug')
                markup.add(item1, item2, item3, item4) 
                loop(part)
                nd = part[word_num]['nd']
                task_numb +=1
                bot.send_message(message.chat.id, f"<b>{task_numb} van {len(part)}.</b> Vertaal:\t\t<i><b>{kortezh(nd)}</b></i>", parse_mode='HTML', reply_markup = markup)
            except TypeError:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Популярні прикметники')
                item2 = types.KeyboardButton('Родина')
                item3 = types.KeyboardButton('Погода')
                item4 = types.KeyboardButton('Кольори')
                item5 = types.KeyboardButton('Час')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id, 'Обери тему', reply_markup = markup)
        elif message.text == 'Juiste antwoord':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item2 = types.KeyboardButton('Volgende')
            item3 = types.KeyboardButton('Verander de taal')
            item4 = types.KeyboardButton('🔙 Terug')
            markup.add(item2, item3, item4)
            try:
                word_num = word_index[-1]
                uk = part[word_num]['uk']
                en = part[word_num]['en']
                bot.send_message(message.chat.id, f"UA\t🇺🇦\t-\t<i><b>{kortezh(uk)}</b></i>\t\t|\t\t EN\t🇬🇧\t-\t<i><b>{kortezh(en)}</b></i>", parse_mode='HTML', reply_markup = markup)
            except:
                bot.send_message(message.chat.id, f"Vertaling is niet beschikbaar\nKlik:\t\t<b>Volgende</b>", parse_mode='HTML', reply_markup = markup)
        elif message.text == 'Volgende':
            try:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Juiste antwoord')
                item2 = types.KeyboardButton('Volgende')
                item3 = types.KeyboardButton('Verander de taal')
                item4 = types.KeyboardButton('🔙 Terug')
                markup.add(item1, item2, item3, item4) 
                loop(part)
                nd = part[word_num]['nd']
                task_numb +=1
                bot.send_message(message.chat.id, f"<b>{task_numb} van {len(part)}.</b> Vertaal:\t\t<i><b>{kortezh(nd)}</b></i>", parse_mode='HTML', reply_markup = markup)
            except TypeError:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Популярні прикметники')
                item2 = types.KeyboardButton('Родина')
                item3 = types.KeyboardButton('Погода')
                item4 = types.KeyboardButton('Кольори')
                item5 = types.KeyboardButton('Час')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id, 'Обери тему', reply_markup = markup)
        elif message.text == 'Verander de taal':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇦 Українська')
            item2 = types.KeyboardButton('🇬🇧 English')
            item3 = types.KeyboardButton('🇳🇱 Dutch')
            item4 = types.KeyboardButton('🔙 Terug')
            markup.add(item1, item2, item3, item4) 
            bot.send_message(message.chat.id, 'Kies een taal', reply_markup = markup)

bot.polling(non_stop = True)