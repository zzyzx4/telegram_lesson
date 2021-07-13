from pyowm import OWM
import telebot
from token_api import api

owm = OWM(api) # token from open weather map
manager = owm.weather_manager()
bot = telebot.TeleBot("1730913516:AAEv9CNUdbskOOf8nWauz66Erkpwrks9KDE", parse_mode=False)


@bot.message_handler(content_types=['text'])
def send_echo(message):
    obs = manager.weather_at_place(message.text)
    w = obs.weather
    temp = w.temperature('celsius')['temp']
    answer = "Погода в " + str(message.text) + " " + str(round(temp)) + " градуса по цельсию"
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)


#
# city_weather = input("Введите город: ")
# obs = manager.weather_at_place(city_weather)
#
# w = obs.weather
#
# temp = w.temperature('celsius')['temp']
#
# print("Погода в" + str(city_weather) + " " + str(round(temp)) + " градуса по цельсию")
