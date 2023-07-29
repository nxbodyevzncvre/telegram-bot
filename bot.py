import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from pyowm import OWM
from pyowm import *


owm = OWM('56bca329a171141090d33ab607b33d5f')
mgr = owm.weather_manager()



API_Token = "1888643620:AAF3NjtqBeOeAc7boonBu7lVL4_loW62uSI"


logging.basicConfig(level = logging.INFO)

bot = Bot(token = API_Token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
	user_first_name = str(message.chat.first_name)
	await message.reply(f"What is up, {user_first_name}!\nIt is a weather helper bot.\nHope you'll enjoy it!")
	await message.answer(f"{user_first_name},\nsend us your city and we'll give you recommendations about weather!")



@dp.message_handler()
async def begin(message: types.Message,state: FSMContext):
	try:
		msg = message.reply_to_message.text
	except:
		msg = "Almaty"
	await message.answer(f'Пользователь с города: {message.text}')
	mgr = owm.weather_manager()
	city = message.text
	observation = mgr.weather_at_place("Astana")
	w = observation.weather()
	temperature = w.get_temperature("celsius")["temp"]
	await message.answer(f"В городе {city} сейчас {temperature} градусов.")





if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
