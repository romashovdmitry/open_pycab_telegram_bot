# python imports
from typing import Union
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

@dp.message(CommandStart())
async def message_handler(message: types.Message) -> None:
    await message.answer(text="first try")

@app.on_event("startup")
async def run_bot_webhook():
    ''' run bot before starting app '''
    bot = Bot(os.getenv("TELEGRAM_TOKEN"), parse_mode=ParseMode.HTML)
#    router = Router()
#    dp.include_router(router)
    print('start')
    await dp.start_polling(bot)
    print('finish')


'''
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
'''
