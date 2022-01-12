import pyowm
import pyTelegramBotAPI

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here
owm = OWM('0d3c477edbb595fcae03701464cd00f9', config_dict)
bot = telebot.TeleBot("5048204997:AAG36jQhiKzPvtGU0CHOsVkUvZ0YJ9L6DXo")

mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_echo(message):
	try:
		observation = mgr.weather_at_place( message.text ) 
		w = observation.weather
		temp = w.temperature('celsius')["temp"]

		answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
		answer += "Температура сейчас в районе " + str(temp) + "\n\n"


		if temp < 0:
			answer += "Сейчас ппц как холодно, стоит накинуть шмоток"
		elif temp < 20:
			answer += "Сейчас еще не достаточно тепло, но в целом комфортно"
		else:
			answer += "Температура отличная, можно надеть что угодно"

		bot.send_message(message.chat.id, answer)

	except:
    		bot.send_message(message.chat.id,'Ошибка! Город не найден.')


bot.polling( none_stop = True )
