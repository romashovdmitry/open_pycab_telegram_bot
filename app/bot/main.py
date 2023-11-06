# Python imports
from typing import Dict, Any
import logging
from os import getenv

# Fastapi imports
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode

# custom foos and classes
from . import routing


# logger declaration, logging setup
logging.config.fileConfig(
    'logs/logger_config.conf',
    disable_existing_loggers=False
)
logger = logging.getLogger(name="open_pycab_telegram_logger")

# config data
TOKEN = getenv("TELEGRAM_TOKEN")
BASE_WEBHOOK_URL = getenv("WEBHOOK_URL")

# declare fastapi app
app = FastAPI()

# declare, setup bot
router = Router()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
dp.include_router(routing.router)


class WebhookData(BaseModel):
    ''' pydantic class for processing requests '''
    data: Dict[str, Any]


@app.on_event("startup")
async def run_bot_webhook():
    ''' set webhook on start of app '''
    await bot.set_webhook(
        f"{BASE_WEBHOOK_URL}/{TOKEN}",
    )


@app.post(f"/{TOKEN}")
async def feed_update(update: Dict[str, Any]) -> None:
    try:
        telegram_update = types.Update(**update)
#        this variant works too
#        await dp._process_update(update=types.Update(**update), bot=bot)
        await dp.feed_webhook_update(bot, telegram_update)
    except Exception as e:
        logger.error(f"Error processing update: {e}")    
