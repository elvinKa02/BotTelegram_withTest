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
    keyboard0 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    buttons = ["IT", "Маркетинг", "Консультирование", "Наука, образование", "Транспортная отрасль"]
    keyboard0.add(*buttons)
    await message.answer("Приветствуем!\nРады видеть Вас в этом чате, где вы можете получить тестовое задание для "
                         "приема на стажировку.\nДля начала выберите сферу деятельности", reply_markup=keyboard0)


# Выбор профессии с inline-кнопками
@dp.message_handler(content_types=['text'])
async def choice_of_profession(message: types.Message):
    if message.text == "IT":
        buts1 = [
            types.InlineKeyboardButton(text="Backend-разработчик", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Frontend-разработчик", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Программист-тестировщик", callback_data='chat_redirect'),
        ]
        keyboard1 = types.InlineKeyboardMarkup(row_width=2)
        keyboard1.add(*buts1)
        await message.answer("Выберите профессию", reply_markup=keyboard1)
    if message.text == "Маркетинг":
        buts2 = [
            types.InlineKeyboardButton(text="Интернет-маркетинг", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Маркетолог", callback_data='chat_redirect'),
        ]
        keyboard2 = types.InlineKeyboardMarkup(row_width=2)
        keyboard2.add(*buts2)
        await message.answer("Выберите профессию", reply_markup=keyboard2)
    if message.text == "Консультирование":
        buts3 = [
            types.InlineKeyboardButton(text="Консультант-платформы", callback_data='chat_redirect'),
            types.InlineKeyboardButton(text="Менеджер по продажам", callback_data='chat_redirect'),
        ]
        keyboard3 = types.InlineKeyboardMarkup(row_width=2)
        keyboard3.add(*buts3)
        await message.answer("Выберите профессию", reply_markup=keyboard3)
    if message.text == "Наука, образование":
        buts4 = [
            types.InlineKeyboardButton(text="Методист", callback_data='chat_redirect'),
        ]
        keyboard4 = types.InlineKeyboardMarkup()
        keyboard4.add(*buts4)
        await message.answer("Выберите профессию", reply_markup=keyboard4)
    if message.text == "Транспортная отрасль":
        buts5 = [
            types.InlineKeyboardButton(text="Специалист по оценке антитеррористической защищенности объектов "
                                            "траснпортного комплекса", callback_data='chat_redirect'),
        ]
        keyboard5 = types.InlineKeyboardMarkup(row_width=2)
        keyboard5.add(*buts5)
        await message.answer("Выберите профессию", reply_markup=keyboard5)


# Перенаправление пользователя в чат с тестовым заданием
@dp.callback_query_handler(text="chat_redirect")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer("Отлично, сейчас вас перенаправим в чат с тестовым заданием!")
    await call.message.edit_reply_markup(reply_markup=None)

# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp)
