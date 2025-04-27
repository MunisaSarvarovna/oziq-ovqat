import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message,KeyboardButton,CallbackQuery,ReplyKeyboardRemove,ReplyKeyboardMarkup

from Keyboards import main_menu, food_menu, el_menu


TOKEN = "7426087731:AAFc-9bni7Fowfl6EAWoy1bt5ohHcoiP37U"


dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=main_menu)


@dp.callback_query()
async def ans_to_callback(callback: CallbackQuery):
    await callback.message.answer(text=f"{callback.data}")

@dp.message(F.text.isdigit())
async def echo_handler(message: Message) -> None:
    k = 1
    n = int(message.text)
    m = int(n ** 0.5)
    qoldiq = n - m * m

    if n == 0:
        await message.answer("Tozalandi", reply_markup=ReplyKeyboardRemove())
        return

    matrix = []

    for i in range(m):
        row = []
        for j in range(m):
            row.append(KeyboardButton(text=f"{k}"))
            k += 1
        matrix.append(row)

    row = []
    for i in range(qoldiq):
        row.append(KeyboardButton(text=f"{k}"))
        k += 1

    matrix.append(row)


    await message.answer("Tayyor", reply_markup=ReplyKeyboardMarkup(keyboard=matrix, resize_keyboard=True))


@dp.message(F.text == "Oziq-ovqat")
async def food_menu_handler(message: Message):
    await message.answer(text="Quyidagilardan birini tanlang:", reply_markup=food_menu)

@dp.message(F.text == "Elektronics")
async def food_menu_handler(message: Message):
    await message.answer(text="Quyidagilardan birini tanlang:", reply_markup=el_menu)

@dp.message(F.text == "Orqaga")
async def food_menu_handler(message: Message):
    await message.answer(text="Asosiy menu:", reply_markup=main_menu)

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
