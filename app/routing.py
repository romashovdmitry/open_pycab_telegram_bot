# aiogram imports
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message # for typing

router = Router()

@router.message(Command("kek"))
async def kek(message: Message):
    ''' remove me '''
    await message.answer("ok, done")