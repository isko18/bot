from aiogram import Bot, Dispatcher, types, executor
import config
from random import randintrandint

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "go"])
async def start(message:types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}.")
    await message.answer(f"Нажмите /gamestart для начала игры.")

@dp.message_handler(commands="gamestart")
async def game(message:types.Message):
    await message.answer("Погнали !")
    await message.answer("Введите число от 1 до 10 .")

@dp.message_handler(regexp=r"^[1-9]")
async def randomizr(message:types.Message):
    integ = randintrandint(1, 10)
    user_int = int(message.text)
    if integ == user_int:
        await message.reply("Поздравляем! Вы угадали!")
        
    else:
        await message.reply("Вы проиграли!")
        
print("heelo")