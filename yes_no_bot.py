from os import getenv
import sys
import logging
from random import choice
import time
import emoji



from telebot import TeleBot, types

BOT_TOKEN = getenv('BOT_TOKEN')

ANSWERS_LIST = [
    'Однозначно ДА! \U0001F60D',
    'Да \U0001F643',
    'Да, но позже \U0001F60C',
    'Нет \U0001F611',
    'Точно НЕТ! \U0001F635',
    'В этом случае решение придется принять самому \U0001F978',
    'Ахахахах, конечно нет \U0001F481',
    'Да, но нет \U0001F645',
    'Извини, нет \U0001F4DB',
    'Иди поешь и попробуй снова \U0001F354',
    'Ну и вопрос \U0001F644',
    'Что??? \U0001F440',
    'Решение нужно принимать самому, а не доверять мне \U0001F0CF',
    'Да, нет, да, нет, ой реши сам(а) \U0001F485',
    'Да, повторяю ещё раз, ДА! \U0001F525',
    'Ну чёт нет, наверное \U0001F31A',
    'Да да да да! \U0001F680',
    'Плз не задавай больше вопросов \U0001F971',
    'Ну, давай, попробуй \U0001F921',
    'Конечно \U0001F970',
    'Спроси завтра \U0001F634',
    'Не сегодня, расслабься \U0001F486',
    'Спроси в следующем месяце \U0001F480',
    'Присмотрись к знакам \U0001F68F',
    'У мамы спроси \U0001F90C',
    'Звезды говорят да! \U0001F929',
    'Ой, иди поспи лучше, а \U0001F978'
    ]

bot = TeleBot(token=BOT_TOKEN)

def random_text():
    return choice(ANSWERS_LIST)

@bot.message_handler(commands=['start'])
def command_start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(
        types.KeyboardButton('Узнать ответ')
    )
    bot.send_message(
        chat_id=message.from_user.id,
        text=(f'Привет, {message.from_user.full_name}! Задай свой вопрос!'),
        reply_markup=keyboard
)

@bot.message_handler()
def send_random_answer(message):
    bot.send_chat_action(message.chat.id, 'typing')
    msg = bot.send_message(message.chat.id, text= emoji.emojize(":crystal_ball:"))
    time.sleep(2)
    bot.delete_message(message.chat.id, msg.message_id)
    bot.send_message(chat_id=message.from_user.id, text=random_text())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot.polling()