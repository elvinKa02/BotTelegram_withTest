from os import getenv

import logging

from aiogram import Bot, Dispatcher, executor, types

# Задаём уровень логов
logging.basicConfig(level=logging.INFO)

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

# инициализируем бота
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


# Запуск и выбор области специализации
@dp.message_handler(commands=['start'])
async def start_and_specialization(message: types.Message):
    keyboard0 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = ["Продвижение, оптимизация, маркетинг", "Разработка, проектирование", "Дизайн, графика, анимация",
               "Администрирование на предприятии"]
    keyboard0.add(*buttons)
    await message.answer("Приветствую, хочешь работать с нами?\nДля начала ответь на некоторые вопросы\n1. Выберите "
                         "область специализации", reply_markup=keyboard0)


# Выбор профессии с inline-кнопками
@dp.message_handler(content_types=['text'])
async def choice_of_profession(message: types.Message):
    if message.text == "Продвижение, оптимизация, маркетинг":
        buts1 = [
            types.InlineKeyboardButton(text="Web-программист", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="SEO-маркетолог", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="SMM-специалист", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Контент-менеджер", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Копирайтер", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Верстальщик", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Web-аналитик", callback_data='chat_redirect')
        ]
        keyboard1 = types.InlineKeyboardMarkup(row_width=2)
        keyboard1.add(*buts1)
        await message.answer("Выберите профессию", reply_markup=keyboard1)
    if message.text == "Разработка, проектирование":
        buts2 = [
            types.InlineKeyboardButton(text="Frontend разработчик", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Backend разработчик", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="QA инженер", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Разработчик баз данных", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Системный аналитик", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="GameDev разработчик", callback_data='chat_redirect')
        ]
        keyboard2 = types.InlineKeyboardMarkup(row_width=2)
        keyboard2.add(*buts2)
        await message.answer("Выберите профессию", reply_markup=keyboard2)
    if message.text == "Дизайн, графика, анимация":
        buts3 = [
            types.InlineKeyboardButton(text="Game дизайнер", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="3D аниматор", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Web дизайнер", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="UX дизайнер", callback_data='chat_redirect'),
        ]
        keyboard3 = types.InlineKeyboardMarkup(row_width=2)
        keyboard3.add(*buts3)
        await message.answer("Выберите профессию", reply_markup=keyboard3)
    if message.text == "Администрирование на предприятии":
        buts4 = [
            types.InlineKeyboardButton(text="Архитектор баз данных", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Администратор сайта", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Системный администратор", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Администратор баз данных", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Системный инженер", callback_data='chat_redirect'),
        ]
        keyboard4 = types.InlineKeyboardMarkup(row_width=2)
        keyboard4.add(*buts4)
        await message.answer("Выберите профессию", reply_markup=keyboard4)


@dp.callback_query_handler(text="chat_redirect")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer("Отлично, сейчас вас перенаправим в чат с тестовым заданием!")
    await call.message.edit_reply_markup(reply_markup=None)

# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp)
