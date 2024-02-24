import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from config import tkn
from parser import parse

API_TOKEN = tkn
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id, 'steampricesbot\nsend url to your item')

@dp.message_handler()
async def steam_url(message:types.Message):
    if message.text.startswith('https://store.steampowered.com/'):
        url = message.text
        info = parse(url)
        await bot.send_message(message.chat.id, text=f'Name: {info["title"]},\n Price: {info["price"]}')
    else:
        await bot.send_message(message.chat.id, text='We receiving only steam urls')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)