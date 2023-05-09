from woorden import*
from family import*
from weather import*
from colours import*
from ttime import*
from gtts import gTTS
lst = adjective, family, weather, colours, ttime
b = "_"
themes = 'adjective', 'family', 'weather', 'colours', 'ttime'
folder = input(''.join(list('\t' + str(k) + " - {}\n" for k in range(1, len(themes) + 1))).format(*themes) + "Enter the theme: ")
theme = lst[int(folder) - 1]
folder = themes[int(folder) - 1]
language = input('\t0 - ENG\n\t1 - NED\nEnter the language: ')
if language == '0' or not language:
	language = langg = 'en'
elif language == '1':
	language, langg = 'nd', 'nl'
# print(lst)
for col in theme:
	if type(col[language]) == tuple:
		for word in col[language]:
			tts = gTTS(word, lang = langg)
			tts.save(fr"./sounds/{folder}/{language}/{word.strip('?., ').replace(' ', b)}.mp3")
	else:
		tts = gTTS(col[language], lang = langg)
		tts.save(fr"./sounds/{folder}/{language}/{col[language].strip('?,. ').replace(' ', b)}.mp3")