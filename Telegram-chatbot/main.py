from dotenv import load_dotenv
import os 
from aiogram import executor, Dispatcher, Bot, types
import openai
import sys 

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class Reference:
    """
        A class to store previous response from openai API
    """
    def __init__(self) -> None:
        self.reference = ""
    


Reference = Reference()
model_name = "gpt-3.5-turbo"

bot = Bot(token = TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)

@dispatcher.message_handler(commands=['start'])
async def welcome(message:types.Message):

    await message.reply('Hello\nI am a Telebot \nHow can I help you?')

if __name__ == "__main__":
    executor.start_polling(dispatcher,skip_updates=False)
