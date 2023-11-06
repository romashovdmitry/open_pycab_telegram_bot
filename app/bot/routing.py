# Python imports
import logging
import asyncio

# aiogram imports
from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message # for typing

# import custom foos, classes, constants
from .constants import start_text


# router for handling signals from bot
router = Router()


@router.message(Command("new_text"))
async def kek(message: Message):
    ''' remove me '''
    await message.answer("ok, done")


@router.message(CommandStart())
async def message_handler(message: types.Message) -> None:
    ''' answer to start command '''
    await message.answer(text=start_text)