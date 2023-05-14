import telebot
from telebot import types
from woorden import*
from family import*
from weather import*
from colours import*
from ttime import*
import random
import json

with open("users.json", 'r') as usrs:
    users_data = json.load(usrs)

TOKEN = '6144198214:AAEZy9E7rrcXWqYuJ_5Q_ZkHCoCBFYZWV7I'
bot = telebot.TeleBot(TOKEN)
def kortezh(text):
    if type(text) == tuple:
        return ', '.join(text)
    else:
        return text
try:
    @bot.message_handler(commands = ['start'])
    def start(message):
        global users_data
        if str(message.chat.id) in users_data:
            print('Already is')
            if users_data[str(message.chat.id)]['part'] == 'Adjective':
                users_data[str(message.chat.id)]['part'] = adjective
            elif users_data[str(message.chat.id)]['part'] == 'Weather':
                users_data[str(message.chat.id)]['part'] = weather
            elif users_data[str(message.chat.id)]['part'] == 'Time':
                users_data[str(message.chat.id)]['part'] = ttime
            elif users_data[str(message.chat.id)]['part'] == 'Family':
                users_data[str(message.chat.id)]['part'] == family
            elif users_data[str(message.chat.id)]['part'] == 'Colours':
                users_data[str(message.chat.id)]['part'] = colours
        else:
            print('not yet')
            users_data[str(message.chat.id)] = {}
            users_data[str(message.chat.id)]['word_index'], users_data[str(message.chat.id)]['part'] = [], None
            users_data[str(message.chat.id)]['task_numb'], users_data[str(message.chat.id)]['folder_name'] = 0, None
            users_data[str(message.chat.id)]['markup'], users_data[str(message.chat.id)]['text_m'] = None, None
        
        users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1, item2, item3 = types.KeyboardButton('Популярні прикметники'), types.KeyboardButton('Родина'), types.KeyboardButton('Погода')
        item4, item5 = types.KeyboardButton('Кольори'), types.KeyboardButton('Час')
        users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4, item5)
        bot.send_message(str(message.chat.id), 'Вітаю, {0.first_name}! Обери тему'.format(message.from_user), reply_markup = users_data[str(message.chat.id)]['markup'])
        

    @bot.message_handler(content_types = ['text'])
    def bot_message(message):
        global users_data
        def loop(party):
            global users_data
            while True:
                nonlocal word_num
                if len(users_data[str(message.chat.id)]['word_index']) >= len(party) - 1:
                    users_data[str(message.chat.id)]['word_index'], users_data[str(message.chat.id)]['task_numb'] = [], 0
                    bot.send_message(message.chat.id, f"<i><b>Повний круг пройдено</b></i>", parse_mode='HTML')
                word_num = random.randint(1, len(party)-1)
                if word_num in users_data[str(message.chat.id)]['word_index']:
                    continue
                if word_num not in users_data[str(message.chat.id)]['word_index']:
                    users_data[str(message.chat.id)]['word_index'].append(word_num)
                    break
        if message.chat.type == 'private':
            if message.text == 'Популярні прикметники':
                users_data[str(message.chat.id)]['text_m'] = 'Обери мову'
                if users_data[str(message.chat.id)]['part'] != adjective:
                    users_data[str(message.chat.id)]['part'], users_data[str(message.chat.id)]['word_index'], users_data[str(message.chat.id)]['task_numb'], users_data[str(message.chat.id)]['folder_name'] = adjective, [], 0, "adjective"
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1, item2, item3 = types.KeyboardButton('🇺🇦 Українська'), types.KeyboardButton('🇬🇧 English'), types.KeyboardButton('🇳🇱 Dutch')
                item4 = types.KeyboardButton('🔙 Назад')
                item5 = types.KeyboardButton('🗑️')
                users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4, item5) 
                bot.send_message(message.chat.id, users_data[str(message.chat.id)]['text_m'], reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == '🗑️':
                # try:
                bot.delete_message(message.chat.id, message.message_id)
                while True:
                    if message.message_id - 1:
                        bot.delete_message(message.chat.id, message.message_id - 1)
                        break
                    else:
                        message.message_id -= 1
                bot.send_message(message.chat.id, users_data[str(message.chat.id)]['text_m'], reply_markup = users_data[str(message.chat.id)]['markup'])
                # except Exception as ex:
                #     print(ex)
                #     bot.send_message(message.chat.id, text_m, reply_markup = markup)
            elif message.text == 'Родина':
                if users_data[str(message.chat.id)]['part'] != family:
                    users_data[str(message.chat.id)]['part'], users_data[str(message.chat.id)]['word_index'], users_data[str(message.chat.id)]['task_numb'], users_data[str(message.chat.id)]['folder_name'] = family, [], 0, 'family'
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1, item2, item3 = types.KeyboardButton('🇺🇦 Українська'), types.KeyboardButton('🇬🇧 English'), types.KeyboardButton('🇳🇱 Dutch')
                item4 = types.KeyboardButton('🔙 Назад')
                users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4) 
                bot.send_message(message.chat.id, 'Обери мову', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Погода':
                if users_data[str(message.chat.id)]['part'] != weather:
                    users_data[str(message.chat.id)]['part'], users_data[str(message.chat.id)]['word_index'], users_data[str(message.chat.id)]['task_numb'], users_data[str(message.chat.id)]['folder_name'] = weather, [], 0, 'weather'
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1, item2, item3 = types.KeyboardButton('🇺🇦 Українська'), types.KeyboardButton('🇬🇧 English'), types.KeyboardButton('🇳🇱 Dutch')
                item4 = types.KeyboardButton('🔙 Назад')
                users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4) 
                bot.send_message(message.chat.id, 'Обери мову', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Кольори':
                if users_data[str(message.chat.id)]['part'] != colours:
                    users_data[str(message.chat.id)]['part'], users_data[str(message.chat.id)]['word_index'], users_data[str(message.chat.id)]['task_numb'], users_data[str(message.chat.id)]['folder_name'] = colours, [], 0, 'colours'
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1, item2, item3 = types.KeyboardButton('🇺🇦 Українська'), types.KeyboardButton('🇬🇧 English'), types.KeyboardButton('🇳🇱 Dutch')
                item4 = types.KeyboardButton('🔙 Назад')
                users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4) 
                bot.send_message(message.chat.id, 'Обери мову', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Час':
                if users_data[str(message.chat.id)]['part'] != ttime:
                    users_data[str(message.chat.id)]['part'], users_data[str(message.chat.id)]['word_index'], users_data[str(message.chat.id)]['task_numb'], users_data[str(message.chat.id)]['folder_name'] = ttime, [], 0, 'ttime'
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1, item2, item3 = types.KeyboardButton('🇺🇦 Українська'), types.KeyboardButton('🇬🇧 English'), types.KeyboardButton('🇳🇱 Dutch')
                item4 = types.KeyboardButton('🔙 Назад')
                users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4) 
                bot.send_message(message.chat.id, 'Обери мову', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == '🇺🇦 Українська':
                try:
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1, item2, item3 = types.KeyboardButton('Правильна відповідь'), types.KeyboardButton('Наступне'), types.KeyboardButton('Змінити мову')
                    item4 = types.KeyboardButton('🔙 Назад')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4)
                    loop(users_data[str(message.chat.id)]['part'])
                    uk = users_data[str(message.chat.id)]['part'][word_num]['uk']
                    users_data[str(message.chat.id)]['task_numb'] +=1
                    bot.send_message(message.chat.id, f"<b>{users_data[str(message.chat.id)]['task_numb']} із {len(users_data[str(message.chat.id)]['part']) - 1}.</b> Переклади:\t\t<i><b>{kortezh(uk)}</b></i>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
                except TypeError:
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1, item2, item3 = types.KeyboardButton('Популярні прикметники'), types.KeyboardButton('Родина'), types.KeyboardButton('Погода')
                    item4, item5 = types.KeyboardButton('Кольори'), types.KeyboardButton('Час')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4, item5)
                    bot.send_message(message.chat.id, 'Обери тему', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text in ('🔙 Назад', '🔙 Back', '🔙 Terug', 'u', 'U'):
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1, item2, item3 = types.KeyboardButton('Популярні прикметники'), types.KeyboardButton('Родина'), types.KeyboardButton('Погода')
                item4, item5 = types.KeyboardButton('Кольори'), types.KeyboardButton('Час')
                users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4, item5)
                bot.send_message(message.chat.id, 'Обери тему', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Правильна відповідь':
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item2 = types.KeyboardButton('Наступне')
                item3 = types.KeyboardButton('Змінити мову')
                item4 = types.KeyboardButton('🇬🇧 🔊')
                item5 = types.KeyboardButton('🇳🇱 🔊')
                item6 = types.KeyboardButton('🔙 Назад')
                users_data[str(message.chat.id)]['markup'].add(item2, item3, item4, item5, item6) 
                try:
                    word_num = users_data[str(message.chat.id)]['word_index'][-1]
                    en = users_data[str(message.chat.id)]['part'][word_num]['en']
                    nd = users_data[str(message.chat.id)]['part'][word_num]['nd']
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(message.chat.id, f"EN\t🇬🇧\t-\t<i><b>{kortezh(en)}</b></i>\t\t|\t\t NL\t🇳🇱\t-\t<i><b>{kortezh(nd)}</b></i>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
                except Exception as ex:
                    print(ex)
                    bot.send_message(message.chat.id, f"Переклад недоступний\nНатисни:\t\t<b>Наступне</b>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == '🇬🇧 🔊' or message.text == '🇳🇱 🔊':
                try:
                    word_num = users_data[str(message.chat.id)]['word_index'][-1]
                    en = users_data[str(message.chat.id)]['part'][word_num]['en']
                    nd = users_data[str(message.chat.id)]['part'][word_num]['nd']
                    bot.delete_message(message.chat.id, message.message_id)
                    if message.text == '🇬🇧 🔊':
                        if type(en) == tuple:
                            for voice in en:
                                file = open(f"./sounds/{users_data[str(message.chat.id)]['folder_name']}/en/{voice.strip('?., ').replace(' ', '_')}.mp3", 'rb')
                                bot.send_audio(message.chat.id, file, reply_markup = users_data[str(message.chat.id)]['markup'])
                        else:
                            file = open(f"./sounds/{users_data[str(message.chat.id)]['folder_name']}/en/{en.strip('?., ').replace(' ', '_')}.mp3", 'rb')
                            bot.send_audio(message.chat.id, file, reply_markup = users_data[str(message.chat.id)]['markup'])
                    elif message.text == '🇳🇱 🔊':
                        if type(nd) == tuple:
                            for voice in nd:
                                file = open(f"./sounds/{users_data[str(message.chat.id)]['folder_name']}/nd/{voice.strip('?., ').replace(' ', '_')}.mp3", 'rb')
                                bot.send_audio(message.chat.id, file, reply_markup = users_data[str(message.chat.id)]['markup'])
                        else:
                            file = open(f"./sounds/{users_data[str(message.chat.id)]['folder_name']}/nd/{nd.strip('?., ').replace(' ', '_')}.mp3", 'rb')
                            bot.send_audio(message.chat.id, file, reply_markup = users_data[str(message.chat.id)]['markup'])
                except Exception as ex:
                    print(ex)
                    bot.send_message(message.chat.id, f"Аудіо недоступнe\nНатисни:\t\t<b>Наступне</b>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Наступне':
                try:
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1 = types.KeyboardButton('Правильна відповідь')
                    item2 = types.KeyboardButton('Наступне')
                    item3 = types.KeyboardButton('Змінити мову')
                    item4 = types.KeyboardButton('🔙 Назад')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4)  
                    loop(users_data[str(message.chat.id)]['part'])
                    uk = users_data[str(message.chat.id)]['part'][word_num]['uk']
                    users_data[str(message.chat.id)]['task_numb'] +=1
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(message.chat.id, f"<b>{users_data[str(message.chat.id)]['task_numb']} із {len(users_data[str(message.chat.id)]['part']) - 1}.</b> Переклади:\t\t<i><b>{kortezh(uk)}</b></i>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
                except TypeError:
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1, item2, item3 = types.KeyboardButton('Популярні прикметники'), types.KeyboardButton('Родина'), types.KeyboardButton('Погода')
                    item4, item5 = types.KeyboardButton('Кольори'), types.KeyboardButton('Час')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4, item5)
                    bot.send_message(message.chat.id, 'Обери тему', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Змінити мову':
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('🇺🇦 Українська')
                item2 = types.KeyboardButton('🇬🇧 English')
                item3 = types.KeyboardButton('🇳🇱 Dutch')
                item4 = types.KeyboardButton('🔙 Назад')
                users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4) 
                bot.send_message(message.chat.id, 'Обери мову', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == '🇬🇧 English':
                try:
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1 = types.KeyboardButton('Right answer')
                    item2 = types.KeyboardButton('Next')
                    item3 = types.KeyboardButton('Change the language')
                    item4 = types.KeyboardButton('🇬🇧 🔊')
                    item5 = types.KeyboardButton('🔙 Back')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4, item5) 
                    loop(users_data[str(message.chat.id)]['part'])
                    en = users_data[str(message.chat.id)]['part'][word_num]['en']
                    users_data[str(message.chat.id)]['task_numb'] +=1
                    bot.send_message(message.chat.id, f"<b>{users_data[str(message.chat.id)]['task_numb']} of {len(users_data[str(message.chat.id)]['part']) - 1}.</b> Translate:\t\t<i><b>{kortezh(en)}</b></i>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
                except TypeError:
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1, item2, item3 = types.KeyboardButton('Популярні прикметники'), types.KeyboardButton('Родина'), types.KeyboardButton('Погода')
                    item4, item5 = types.KeyboardButton('Кольори'), types.KeyboardButton('Час')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4, item5)
                    bot.send_message(message.chat.id, 'Обери тему', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Right answer':
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item2 = types.KeyboardButton('Next')
                item3 = types.KeyboardButton('Change the language')
                item5 = types.KeyboardButton('🇳🇱 🔊')
                item4 = types.KeyboardButton('🔙 Back')
                users_data[str(message.chat.id)]['markup'].add(item2, item3, item5, item4)
                try:
                    word_num = users_data[str(message.chat.id)]['word_index'][-1]
                    uk = users_data[str(message.chat.id)]['part'][word_num]['uk']
                    nd = users_data[str(message.chat.id)]['part'][word_num]['nd']
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(message.chat.id, f"UA\t🇺🇦\t-\t<i><b>{kortezh(uk)}</b></i>\t\t|\t\t NL\t🇳🇱\t-\t<i><b>{kortezh(nd)}</b></i>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
                except Exception as ex:
                    print(ex)
                    bot.send_message(message.chat.id, f"Translation is unavailable\nClick:\t\t<b>Next</b>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Next':
                try:
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1 = types.KeyboardButton('Right answer')
                    item2 = types.KeyboardButton('Next')
                    item3 = types.KeyboardButton('Change the language')
                    item5 = types.KeyboardButton('🇬🇧 🔊')
                    item4 = types.KeyboardButton('🔙 Back')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item5, item4)  
                    loop(users_data[str(message.chat.id)]['part'])
                    en = users_data[str(message.chat.id)]['part'][word_num]['en']
                    users_data[str(message.chat.id)]['task_numb'] +=1
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(message.chat.id, f"<b>{users_data[str(message.chat.id)]['task_numb']} of {len(users_data[str(message.chat.id)]['part']) - 1}.</b> Translate:\t\t<i><b>{kortezh(en)}</b></i>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
                except Exception as ex:
                    print(ex)
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1, item2, item3 = types.KeyboardButton('Популярні прикметники'), types.KeyboardButton('Родина'), types.KeyboardButton('Погода')
                    item4, item5 = types.KeyboardButton('Кольори'), types.KeyboardButton('Час')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4, item5)
                    bot.send_message(message.chat.id, 'Обери тему', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Change the language':
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('🇺🇦 Українська')
                item2 = types.KeyboardButton('🇬🇧 English')
                item3 = types.KeyboardButton('🇳🇱 Dutch')
                item4 = types.KeyboardButton('🔙 Back')
                users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4) 
                bot.send_message(message.chat.id, 'Choose a language', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == '🇳🇱 Dutch':
                try:
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1 = types.KeyboardButton('Juiste antwoord')
                    item2 = types.KeyboardButton('Volgende')
                    item3 = types.KeyboardButton('Verander de taal')
                    item5 = types.KeyboardButton('🇳🇱 🔊')
                    item4 = types.KeyboardButton('🔙 Terug')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item5,item4) 
                    loop(users_data[str(message.chat.id)]['part'])
                    nd = users_data[str(message.chat.id)]['part'][word_num]['nd']
                    users_data[str(message.chat.id)]['task_numb'] +=1
                    bot.send_message(message.chat.id, f"<b>{users_data[str(message.chat.id)]['task_numb']} van {len(users_data[str(message.chat.id)]['part']) - 1}.</b> Vertaal:\t\t<i><b>{kortezh(nd)}</b></i>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
                except TypeError:
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1, item2, item3 = types.KeyboardButton('Популярні прикметники'), types.KeyboardButton('Родина'), types.KeyboardButton('Погода')
                    item4, item5 = types.KeyboardButton('Кольори'), types.KeyboardButton('Час')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4, item5)
                    bot.send_message(message.chat.id, 'Обери тему', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Juiste antwoord':
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item2 = types.KeyboardButton('Volgende')
                item3 = types.KeyboardButton('Verander de taal')
                item5 = types.KeyboardButton('🇬🇧 🔊')
                item4 = types.KeyboardButton('🔙 Terug')
                users_data[str(message.chat.id)]['markup'].add(item2, item3, item5, item4)
                try:
                    word_num = users_data[str(message.chat.id)]['word_index'][-1]
                    uk = users_data[str(message.chat.id)]['part'][word_num]['uk']
                    en = users_data[str(message.chat.id)]['part'][word_num]['en']
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(message.chat.id, f"UA\t🇺🇦\t-\t<i><b>{kortezh(uk)}</b></i>\t\t|\t\t EN\t🇬🇧\t-\t<i><b>{kortezh(en)}</b></i>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
                except:
                    bot.send_message(message.chat.id, f"Vertaling is niet beschikbaar\nKlik:\t\t<b>Volgende</b>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Volgende':
                try:
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1 = types.KeyboardButton('Juiste antwoord')
                    item2 = types.KeyboardButton('Volgende')
                    item3 = types.KeyboardButton('Verander de taal')
                    item5 = types.KeyboardButton('🇳🇱 🔊')
                    item4 = types.KeyboardButton('🔙 Terug')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item5,item4) 
                    loop(users_data[str(message.chat.id)]['part'])
                    nd = users_data[str(message.chat.id)]['part'][word_num]['nd']
                    users_data[str(message.chat.id)]['task_numb'] +=1
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(message.chat.id, f"<b>{users_data[str(message.chat.id)]['task_numb']} van {len(users_data[str(message.chat.id)]['part']) - 1}.</b> Vertaal:\t\t<i><b>{kortezh(nd)}</b></i>", parse_mode='HTML', reply_markup = users_data[str(message.chat.id)]['markup'])
                except TypeError:
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                    item1, item2, item3 = types.KeyboardButton('Популярні прикметники'), types.KeyboardButton('Родина'), types.KeyboardButton('Погода')
                    item4, item5 = types.KeyboardButton('Кольори'), types.KeyboardButton('Час')
                    users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4, item5)
                    bot.send_message(message.chat.id, 'Обери тему', reply_markup = users_data[str(message.chat.id)]['markup'])
            elif message.text == 'Verander de taal':
                users_data[str(message.chat.id)]['markup'] = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('🇺🇦 Українська')
                item2 = types.KeyboardButton('🇬🇧 English')
                item3 = types.KeyboardButton('🇳🇱 Dutch')
                item4 = types.KeyboardButton('🔙 Terug')
                users_data[str(message.chat.id)]['markup'].add(item1, item2, item3, item4) 
                bot.send_message(message.chat.id, 'Kies een taal', reply_markup = users_data[str(message.chat.id)]['markup'])

    bot.polling(non_stop = True)
except Exception as ex:
        print(ex)
finally:
    print('finnally')
    for k in users_data.items():
        k[1]['markup'] = None
        k[1]['part'] = k[1]['part'][0]
        k[1]['text_m'] = None
    with open("users.json", 'w') as usrs:
        json.dump(users_data, usrs, indent= 3, ensure_ascii=False)