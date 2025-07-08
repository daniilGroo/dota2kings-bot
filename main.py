
import logging
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = 'TOKEN_HERE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот турниров Dota2Kings. Скоро начнём!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
