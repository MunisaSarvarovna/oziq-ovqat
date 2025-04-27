from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

prev = KeyboardButton(text="Orqaga")
food = KeyboardButton(text="Oziq-ovqat")
el = KeyboardButton(text="Elektronics")

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [food, el]
    ],
    resize_keyboard=True
)


apple = KeyboardButton(text="apple")
banana = KeyboardButton(text="banan")
kakos = KeyboardButton(text="kakos")
orange = KeyboardButton(text="orange")


food_menu = ReplyKeyboardMarkup(
    keyboard=[
        [apple, banana],
        [kakos, orange],
        [prev]
    ],
    resize_keyboard=True
)


phone = KeyboardButton(text="S24 Ultra")
headphone = KeyboardButton(text="airpods")

el_menu = ReplyKeyboardMarkup(
    keyboard=[
        [phone, headphone],
        [prev]
    ],
    resize_keyboard=True
)
