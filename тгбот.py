import telebot
import random
import time
from datetime import datetime


TOKEN = "8551144951:AAEK5sUgxk3e_f292qbl4OXGj62uVPkPrVI"

bot = telebot.TeleBot(TOKEN)


games = {}



def create_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(" НАЖМИ СЮДА!", callback_data="click")
    keyboard.add(button)
    return keyboard


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        " ИГРА НА РЕАКЦИЮ \n\n"
        "Как играть:\n"
        "1. Отправь команду /play\n"
        "2. Появится кнопка\n"
        "3. Нажми на неё как можно быстрее!\n\n"
        "Готов? /play"
    )


@bot.message_handler(commands=['play'])
def play(message):
    user_id = message.chat.id


    if user_id in games:
        bot.send_message(user_id, "⚠ У тебя уже есть активная игра! Найди кнопку и нажми.")
        return


    games[user_id] = time.time()


    bot.send_message(
        user_id,
        "⚡ БЫСТРО НАЖМИ! ⚡",
        reply_markup=create_keyboard()
    )


    def auto_cancel():
        time.sleep(10)
        if user_id in games:
            del games[user_id]
            bot.send_message(user_id, " Время вышло! Напиши /play чтобы сыграть снова.")

    import threading
    threading.Thread(target=auto_cancel, daemon=True).start()


@bot.callback_query_handler(func=lambda call: call.data == "click")
def handle_click(call):
    user_id = call.message.chat.id


    if user_id not in games:
        bot.answer_callback_query(call.id, "Сначала напиши /play!", show_alert=True)
        return


    reaction_time = time.time() - games[user_id]
    reaction_ms = int(reaction_time * 1000)


    del games[user_id]

    # Оценка
    if reaction_ms < 300:
        grade = " РЕКОРД! "
    elif reaction_ms < 600:
        grade = " КРУТО! "
    elif reaction_ms < 1000:
        grade = " Отлично!"
    elif reaction_ms < 2000:
        grade = " Неплохо"
    else:
        grade = " Нужно быстрее"


    bot.edit_message_text(
        f" Результат!\n\n"
        f"⏱️ Время: {reaction_ms} мс\n"
        f"{grade}\n\n"
        f"🎮 Сыграть ещё: /play",
        user_id,
        call.message.message_id
    )

    bot.answer_callback_query(call.id, f"Твоё время: {reaction_ms} мс")


@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(
        message.chat.id,
        "Используй команды:\n"
        "/start - правила\n"
        "/play - начать игру"
    )



print(" Бот запущен!")
bot.infinity_polling()