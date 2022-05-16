from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import datetime
#import buttons
#from func import *
from config import TOKEN,ADMIN_ID


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
today = datetime.datetime.today()



@dp.message_handler(commands="start")
async def process_start_command(message: types.Message):
    await message.answer(f"{message.from_user.first_name} Приветствую я буду учитывать твое рабочие время")
    await message.answer(f"{message.from_user.first_name} Так же команда /help расскажет что я могу еще")
    print("Нажата кнопка старт")


@dp.message_handler(commands="help")
async def process_startsmena2_command(message: types.Message):
        await message.answer("Что-бы начать смену введи в чате 'Начать'" )
        await message.answer("Что-бы закончить смену введи в чате 'Закончить'")

@dp.message_handler(content_types="text")
async def process_startsmena2_command(message: types.Message):
    time = today.strftime('%Y-%m-%d-%H.%M.%S')
    time2 =today.strftime('%d-%m-%Y-%H.%M.%S')
    if "Начать" == message.text:
        replay_text = f"{message.from_user.first_name} вышел(а) на смену в {time}"
        await bot.send_message(ADMIN_ID, replay_text)
        await message.answer(f"{message.from_user.first_name} Ты начал(а) свое смену   {time2}")
        print("Нажата кнопка старт")
    elif "Закончить" == message.text:
        replay_text = f"{message.from_user.first_name} закончил(а) смену в {time}"
        await bot.send_message(ADMIN_ID, replay_text)
        await message.answer(f"{message.from_user.first_name} Ты закончил(а) свою смену  {time2}")
        print("Нажата кнопка закончить")

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)