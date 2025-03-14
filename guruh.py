
# # import asyncio
# # import logging
# # from aiogram import Dispatcher, Bot, types
# # from aiogram.filters import CommandStart

# # TOKEN = "7837319029:AAFZ33FZLb6mCiFTsmg4He7NxvySLUGXiMA"  # O'zingizning bot tokeningizni qo'ying
# # bot = Bot(TOKEN)
# # dp = Dispatcher()


# # @dp.message(CommandStart())
# # async def start_message(message: types.Message):
# #     await message.answer("Assalomu alaykum! Bu guruhda reklama taqiqlangan!")

# # # ❌ Reklama uchun taqiqlangan so‘zlar yoki linklar
# # restricted_words = [
# #     "reklama", "https://", "t.me/", "telegram.me/", "kanalga obuna bo‘ling",
# #     "@MoSizlyakAdv",
# #     "Валера",
# #     "Hужен челoвeк нa фирму",
# #     "собирать новyю мебель людям пocле пoкyпки y нашeго магазинa",
# #     "По большeй чаcти шкафы, кухни, тумбы, и т.п мебель",
# #     "Hа счeт дeнег",
# #     "7500-8000 рублeй за день",
# #     "бемплатны обeды",
# #     "нaш инcтрyмент",
# #     "рублей",
# #     "300 рублей",
# #     "7500-8000 рублeй за день", "бемплатны обeды", "нaш инcтрyмент", "рублей", "300 рублей",

# # ]

# # @dp.message()
# # async def filter_ads(message: types.Message):
# #     print("Keldi:", message.text)  # Debug uchun xabarni chiqaramiz

# #     if any(word.lower() in message.text.lower() for word in restricted_words):
# #         await message.delete()  # Xabarni o‘chirish
# #         await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")

# #         # 🛑 Odamni guruhdan chiqarish (bloklash)
# #         try:
# #             await bot.ban_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
# #             await message.answer(f"❌ {message.from_user.full_name} guruhdan chiqarildi!")
# #         except Exception as e:
# #             print(f"Foydalanuvchini bloklashda xatolik: {e}")

# # # Botni ishga tushirish
# # async def main():
# #     logging.basicConfig(level=logging.INFO)
# #     await dp.start_polling(bot)

# # if __name__ == '__main__':
# # #     asyncio.run(main())
# # import asyncio
# # import logging
# # import re  # Regex ishlatish uchun
# # from aiogram import Dispatcher, Bot, types
# # from aiogram.filters import CommandStart

# # TOKEN = "7837319029:AAFZ33FZLb6mCiFTsmg4He7NxvySLUGXiMA"  # Bot token
# # bot = Bot(TOKEN)
# # dp = Dispatcher()

# # # ❌ Reklama uchun taqiqlangan so‘zlar yoki linklar
# # restricted_words = [
# #     "reklama", "https://", "t.me/", "telegram.me/", "kanalga obuna bo‘ling",
# #     "@MoSizlyakAdv",
# #     "Валера",
# #     "Hужен челoвeк нa фирму",
# #     "собирать новyю мебель людям пocле пoкyпки y нашeго магазинa",
# #     "По большeй чаcти шкафы, кухни, тумбы, и т.п мебель",
# #     "Hа счeт дeнег",
# #     "7500-8000 рублeй за день",
# #     "бемплатны обeды",
# #     "нaш инcтрyмент",
# #     "рублей",
# #     "300 рублей",
# #     "7500-8000 рублeй за день", "бемплатны обeды", "нaш инcтрyмент", "рублей", "300 рублей",

# # ]

# # # ❌ Raqamlar bilan yozilgan reklama so‘zlarini bloklash uchun regex
# # restricted_patterns = [
# #     r"\d+\s*рублей",  # Masalan: "300 рублей", "5000 рублей"
# #     r"\d+\s*руб",     # Masalan: "300 руб"
# #     r"\d+\s*₽"        # Masalan: "300₽"
# # ]

# # # 🚫 Reklama aniqlansa, foydalanuvchini bloklash va xabarni o‘chirish
# # @dp.message()
# # async def filter_ads(message: types.Message):
# #     text = message.text.lower()  # Matnni kichik harflarga o‘tkazamiz

# #     # Oddiy restricted_words orqali tekshirish
# #     if any(word in text for word in restricted_words):
# #         await message.delete()
# #         await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")
# #         await bot.ban_chat_member(message.chat.id, message.from_user.id)  # Bloklash
# #         return

# #     # Regex orqali reklama tekshirish
# #     for pattern in restricted_patterns:
# #         if re.search(pattern, text):
# #             await message.delete()
# #             await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")
# #             await bot.ban_chat_member(message.chat.id, message.from_user.id)  # Bloklash
# #             return

# # # ✅ Start komandasini qo‘shish
# # @dp.message(CommandStart())
# # async def start_command(message: types.Message):
# #     await message.answer("Assalomu alaykum! Bu guruhda reklama taqiqlangan!")

# # # 🔄 Botni ishga tushirish
# # async def main():
# #     logging.basicConfig(level=logging.INFO)
# #     await dp.start_polling(bot)

# # if __name__ == '__main__':
# #     asyncio.run(main())
# # import asyncio
# # import logging
# # import re  # Regex ishlatish uchun
# # from aiogram import Dispatcher, Bot, types
# # from aiogram.filters import CommandStart

# # TOKEN = "7837319029:AAFZ33FZLb6mCiFTsmg4He7NxvySLUGXiMA"  # Bot tokenni bu yerga qo'ying
# # bot = Bot(TOKEN)
# # dp = Dispatcher()

# # # ❌ Reklama uchun taqiqlangan so‘zlar yoki linklar
# # restricted_words = [
# #     "reklama", "https://", "t.me/", "telegram.me/", "kanalga obuna bo‘ling",
# #     "валера", "нужен человек на фирму",
# #     "собирать новую мебель людям после покупки у нашего магазина",
# #     "по большей части шкафы, кухни, тумбы, мебель",
# #     "на счет денег", "бесплатны обеды", "наш инструмент",
# #     "Рублей"
# # ]

# # # ❌ Telegram username bloklash (katta-kichik harf farq qilmaydi)
# # restricted_usernames = [
# #     r"@mosizlyakadv"
# # ]

# # # ❌ Raqamlar bilan yozilgan reklama so‘zlarini bloklash uchun regex
# # restricted_patterns = [
# #     r"\d+\s*рублей",
# #     r"\d+\s*  РУБЛЕЙ",
# #     r"\d+\s*  Рублей",
# #     r"\d+\s*руб",     # Masalan: "300 руб"
# #     r"\d+\s*₽",       # Masalan: "300₽"
# #     r"\d{3,5}\s*-\s*\d{3,5}\s*рублей",  # Masalan: "7500-8000 рублей"
# # ]

# # # 🚫 Reklama aniqlansa, foydalanuvchini bloklash va xabarni o‘chirish
# # @dp.message()
# # async def filter_ads(message: types.Message):
# #     text = message.text.lower()  # Matnni kichik harflarga o‘tkazamiz

# #     # Oddiy restricted_words orqali tekshirish
# #     if any(word in text for word in restricted_words):
# #         await message.delete()
# #         await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")
# #         await bot.ban_chat_member(message.chat.id, message.from_user.id)  # Bloklash
# #         return

# #     # Telegram usernames uchun regex tekshirish
# #     for username in restricted_usernames:
# #         if re.search(username, text, re.IGNORECASE):  # Harflarni e’tiborsiz o‘tish
# #             await message.delete()
# #             await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")
# #             await bot.ban_chat_member(message.chat.id, message.from_user.id)  # Bloklash
# #             return

# #     # Raqamlar bilan reklama tekshirish
# #     for pattern in restricted_patterns:
# #         if re.search(pattern, text):
# #             await message.delete()
# #             await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")
# #             await bot.ban_chat_member(message.chat.id, message.from_user.id)  # Bloklash
# #             return

# # # ✅ Start komandasini qo‘shish
# # @dp.message(CommandStart())
# # async def start_command(message: types.Message):
# #     await message.answer("Assalomu alaykum! Bu guruhda reklama taqiqlangan!")

# # # 🔄 Botni ishga tushirish
# # async def main():
# #     logging.basicConfig(level=logging.INFO)
# #     await dp.start_polling(bot)

# # if __name__ == '__main__':
# #     asyncio.run(main())
# import asyncio
# import logging
# import re  # Regex ishlatish uchun
# from aiogram import Dispatcher, Bot, types
# from aiogram.filters import CommandStart

# TOKEN = "7837319029:AAFZ33FZLb6mCiFTsmg4He7NxvySLUGXiMA"  # Bot tokenni bu yerga qo'ying
# bot = Bot(TOKEN)
# dp = Dispatcher()

# # ❌ Reklama uchun taqiqlangan so‘zlar yoki linklar
# restricted_words = [
#     "reklama", "https://", "t.me/", "telegram.me/", "каналга обуна бўлинг",
#     "валера", "нужен человек на фирму",
#     "собирать новую мебель людям после покупки у нашего магазина",
#     "по большей части шкафы, кухни, тумбы, мебель",
#     "на счет денег", "бесплатны обеды", "наш инструмент",
#     "Ты готов к стабильному доходу?",
#     "1500₽ в день + проценты с продаж!",
#     "Просто аккаунт на Авито – и ты уже в деле!",
#     "Твоя задача – публиковать объявления (без звонков и переписок).",
#     "Заработок с первого дня! Оплата сразу после первого размещенного объявления.",
#     "Без рисков, без вложений – только реальный доход!",
#     "Не упусти свой шанс! Начни зарабатывать прямо сейчас!",
#     "Все вопросы сюда: @avitologvitaliy",
#     "@avitologvitaliy"
# ]

# # ❌ Telegram username bloklash (katta-kichik harf farq qilmaydi)
# restricted_usernames = [
#     r"@mosizlyakadv"
#     r"@avitologvitaliy"

# ]

# # ❌ Raqamlar bilan yozilgan reklama so‘zlarini bloklash uchun regex
# restricted_patterns = [
#     r"\bрублей\b",  # "Рублей" ni har qanday shaklda bloklash (katta-kichik harflarga e'tiborsiz)
#     r"\bруБлей\b",
#     r"\bРУБЛЕЙ\b",
#     r"\d+\s*рублей",
#     r"\d+\s*руб",
#     r"\d+\s*₽",
#     r"\d{3,5}\s*-\s*\d{3,5}\s*рублей"
# ]

# # 🚫 Reklama aniqlansa, foydalanuvchini bloklash va xabarni o‘chirish
# @dp.message()
# async def filter_ads(message: types.Message):
#     text = message.text  # Matnni o'z holida olish

#     # Oddiy restricted_words orqali tekshirish
#     if any(word.lower() in text.lower() for word in restricted_words):
#         await message.delete()
#         await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")
#         await bot.ban_chat_member(message.chat.id, message.from_user.id)  # Bloklash
#         return

#     # Telegram usernames uchun regex tekshirish
#     for username in restricted_usernames:
#         if re.search(username, text, re.IGNORECASE):  # Harflarni e’tiborsiz o‘tish
#             await message.delete()
#             await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")
#             await bot.ban_chat_member(message.chat.id, message.from_user.id)  # Bloklash
#             return

#     # Raqamlar bilan reklama tekshirish
#     for pattern in restricted_patterns:
#         if re.search(pattern, text, re.IGNORECASE):  # Harflarni e’tiborsiz o‘tish
#             await message.delete()
#             await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")
#             await bot.ban_chat_member(message.chat.id, message.from_user.id)  # Bloklash
#             return

# # ✅ Start komandasini qo‘shish
# @dp.message(CommandStart())
# async def start_command(message: types.Message):
#     await message.answer("Assalomu alaykum! Bu guruhda reklama taqiqlangan!")

# # 🔄 Botni ishga tushirish
# async def main():
#     logging.basicConfig(level=logging.INFO)
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     asyncio.run(main())

import asyncio
import logging
import re
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

TOKEN = "7837319029:AAFZ33FZLb6mCiFTsmg4He7NxvySLUGXiMA"  # O'zingizning bot tokeningizni qo'ying
bot = Bot(token=TOKEN)
dp = Dispatcher()

# ❌ Reklama uchun taqiqlangan so‘zlar yoki linklar
restricted_words = [
    "reklama", "https://", "t.me/", "telegram.me/", "каналга обуна бўлинг",
    "валера", "нужен человек на фирму",
    "собирать новую мебель людям после покупки у нашего магазина",
    "по большей части шкафы, кухни, тумбы, мебель",
    "на счет денег", "бесплатны обеды", "наш инструмент",
    "Ты готов к стабильному доходу?",
    "1500₽ в день + проценты с продаж!",
    "Просто аккаунт на Авито – и ты уже в деле!",
    "Твоя задача – публиковать объявления (без звонков и переписок).",
    "Заработок с первого дня! Оплата сразу после первого размещенного объявления.",
    "Без рисков, без вложений – только реальный доход!",
    "Не упусти свой шанс! Начни зарабатывать прямо сейчас!",
    "Все вопросы сюда: @avitologvitaliy",
    "@avitologvitaliy"
]

# ❌ Telegram username bloklash (katta-kichik harf farq qilmaydi)
restricted_usernames = [
    r"@mosizlyakadv",
    r"@avitologvitaliy"
]

# ❌ Raqamlar bilan yozilgan reklama so‘zlarini bloklash uchun regex
restricted_patterns = [
    r"\bрублей\b",  # "рублей" har qanday shaklda bloklanadi (katta-kichik harflarga e'tiborsiz)
    r"\bруБлей\b",
    r"\bРУБЛЕЙ\b",
    r"\d+\s*рублей",  # Masalan: "500 рублей"
    r"\d+\s*руб",     # Masalan: "500 руб"
    r"\d+\s*₽",       # Masalan: "500₽"
    r"\d{3,5}\s*-\s*\d{3,5}\s*рублей"  # Masalan: "7500-8000 рублей"
]

# ✅ /start komandasi
@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! Bu guruhda reklama taqiqlangan!")

# 🚫 Reklama tekshirish va foydalanuvchini bloklash
@dp.message(F.text)
async def filter_ads(message: types.Message):
    text = message.text.lower()

    # Oddiy restricted_words orqali tekshirish
    if any(word in text for word in restricted_words):
        await message.delete()
        await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")
        await bot.ban_chat_member(message.chat.id, message.from_user.id)
        return

    # Telegram usernamesni tekshirish
    for username in restricted_usernames:
        if re.search(username, text, re.IGNORECASE):
            await message.delete()
            await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")
            await bot.ban_chat_member(message.chat.id, message.from_user.id)
            return

    # Regex orqali reklama tekshirish
    for pattern in restricted_patterns:
        if re.search(pattern, text):
            await message.delete()
            await message.answer(f"🚫 {message.from_user.first_name}, bu guruhda reklama taqiqlangan!")
            await bot.ban_chat_member(message.chat.id, message.from_user.id)
            return

# 🔄 Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
