import logging
import os
import sqlite3
from pathlib import Path

import environ
from aiogram import Bot, Dispatcher, executor, types

BASE_DIR = Path(__file__).resolve().parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

API_TOKEN = env("BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot, dispatcher and db
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
con = sqlite3.connect("tutorial.db")


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    cur = con.cursor()
    cur.execute("INSERT INTO person VALUES (?, ?)", (message.from_user.id, 0))
    await message.reply("Hi!\nI'm Love Bot!")
    con.commit()


@dp.message_handler(commands=['love'])
async def echo(message: types.Message):
    cur = con.cursor()
    res = cur.execute("SELECT * FROM word ORDER BY RANDOM() LIMIT 1;").fetchone()
    if int(res[1] == 0):
        await message.answer(f"Ты крут. Вот, что говорили великие:\n\n*{res[0]}*", parse_mode='Markdown')
    else:
        await message.answer(f"Ты крут. Вот, что тебе подготовила нейросетка:\n\n*{res[0]}*", parse_mode='Markdown')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
