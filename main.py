from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hi{message.from_user.full_name}")


@dp.message_handler(commands=['quiz'])
async def quiz_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Which direction will you choose? "
    answers = [
        'python', "C++", "C#", "java"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="питон",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    question = "угадай цвет машины"
    answers = [
        "Red", "blue", "green", "white"

    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="white",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )


@dp.message_handler(commands=["mem"])
async def mem_bot(message: types.Message):
    photo = open("media/maxresdefault.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    try:
        k = int(message.text)
        await bot.send_message(message.from_user.id, k * k)
    except:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
