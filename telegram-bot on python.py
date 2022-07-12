import telebot
from telebot import types
#подключаем токен бота
token='5478353034:AAGQ5cFEBHgHVh8YT345aKRYwcNO0AgbJ3g'
bot=telebot.TeleBot(token)
#метод для получения текстовых сообщений
@bot.message_handler(commands=['start']) #при нажатии функции "старт" бот здоровается нам
def start_message(message):
    bot.send_message(message.chat.id,"приветствую✌")
    bot.send_message(message.chat.id,"мой разработчик https://github.com/Hedge-creator")
    bot.send_message(message.chat.id,"как поживаешь?")

@bot.message_handler(content_types=['text']) #также можно вести небольшой диалог
def get_text_message(message):
    if message.text=="хорошо":
        bot.send_message(message.from_user.id, "приятная новость. это меня порадовало!🤗 ")
    if message.text=="плохо":
        bot.send_message(message.from_user.id, "жаль тебя... удачи, ты справишься!")

bot.infinity_polling()
