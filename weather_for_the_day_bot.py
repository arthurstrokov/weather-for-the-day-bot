import telebot
from telebot import types
from weather_api import request_forecast
import schedule  # https://pypi.org/project/schedule/
import time

bot = telebot.TeleBot('bot_app_id')
chaat_id = 571618656

city_id = 625144

weather = [" ".join(x) for x in request_forecast(city_id)]
weather_for_day = "\n".join(weather)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = types.KeyboardButton("Погода")
    markup.add(btn)

    send_mess = f"<b>Привет {message.from_user.first_name}!</b>\nПогода на сегодня:\n{weather_for_day}"
    bot.send_message(message.chat.id, send_mess,
                     parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    send_mess = f"<b>Привет {message.from_user.first_name}!</b>\nПогода на ближайшее время:\n{weather_for_day}"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


# def morning_message():
#     send_mess = f"Погода на сегодня:\n{weather_for_day}"
#     bot.send_message(chaat_id, send_mess)


# schedule.every().day.at("20:19").do(morning_message)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

bot.polling(none_stop=True)
