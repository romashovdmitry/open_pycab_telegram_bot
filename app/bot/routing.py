# aiogram imports
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message # for typing

# import custom foos, classes

router = Router()

@router.message(Command("new_text"))
async def kek(message: Message):
    ''' remove me '''
    await message.answer("ok, done")