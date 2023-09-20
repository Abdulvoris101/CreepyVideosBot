from app import dp
from aiogram.filters import CommandStart
from aiogram import types

@dp.message(CommandStart())
async def start_command(message: types.Message):

    await message.answer("HI!")
