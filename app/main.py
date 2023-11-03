# python imports
from typing import Union
import logging
import os

# telegram imports
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.bot_command import BotCommand
from aiogram.utils.markdown import hbold
from aiogram.methods.send_message import SendMessage

# fastAPI imports
from fastapi import FastAPI


app = FastAPI()
dp = Dispatcher()
logging.config.fileConfig('logger_config.conf', disable_existing_loggers=False)
logger = logging.getLogger(name="open_pycab_telegram_logger")


@dp.message(CommandStart())
async def message_handler(message: types.Message) -> None:
    logger.info("first log")
    await message.answer(text="first try")

@app.on_event("startup")
async def run_bot_webhook():
    ''' run bot before starting app '''
    bot = Bot(os.getenv("TELEGRAM_TOKEN"), parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
