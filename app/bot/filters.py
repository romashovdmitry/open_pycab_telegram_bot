from aiogram import Router
from aiogram.filters import Filter
from aiogram.types import Message

router = Router()


class MyFilter(Filter):
    ''' custom filter for creating texts '''

    def __init__(self, my_text: str) -> None:
        ''' initiliaze attributes '''
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        ''' check and processing message '''        
        return message.text == self.my_text