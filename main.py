import telebot
import random
import time
from telebot import types

# Твой токен (старайся не светить его в публичных местах)
bot = telebot.TeleBot("8741598645:AAF2BraoIW7jmUoOkVyDkOckrAevOE2LhcQ")

# Данные для бота
ww = ["Повышение температуры океанов", "Сжигание мусора", "Ископаемое топливо", "Вырубка лесов", "Выбросы транспорта"]
ll = ["Чистая энергия", "Теплоизоляция дома", "Общественный транспорт", "Меньше мяса", "Сортировка мусора", "Посадка деревьев", "LED-лампы"]

challenges = [
    "✅ Сегодня не бери пластиковый пакет в магазине, используй свою сумку.",
    "✅ Откажись сегодня от мяса — это сильно снизит твой углеродный след.",
    "✅ Выключи из розеток приборы, которыми не пользуешься (зарядки, чайник).",
    "✅ Попробуй сегодня принять душ за 5 минут, чтобы сэкономить воду.",
    "✅ Собери все старые батарейки в доме, чтобы сдать их в переработку.",
    "✅ Пройдись пешком там, где обычно едешь на автобусе или машине."
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🌍 Причины"), types.KeyboardButton("💡 Эко-совет"))
    markup.add(types.KeyboardButton("🎯 Челлендж"), types.KeyboardButton("📝 Пройти квиз"))
    markup.add(types.KeyboardButton("🔗 Полезный сайт"))
    
    bot.send_message(message.chat.id, "Привет! Выбери действие, чтобы помочь планете:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🌍 Причины")
def send_prichina(message):
    bot.reply_to(message, f"Причина потепления: {random.choice(ww)}")

@bot.message_handler(func=lambda message: message.text == "💡 Эко-совет")
def send_sovet(message):
    bot.reply_to(message, f"Совет: {random.choice(ll)}")

@bot.message_handler(func=lambda message: message.text == "🎯 Челлендж")
def send_challenge(message):
    challenge = random.choice(challenges)
    bot.send_message(message.chat.id, f"Твое задание на сегодня:\n\n{challenge}\n\nСправишься? 💪")

@bot.message_handler(func=lambda message: message.text == "🔗 Полезный сайт")
def send_site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Открыть сайт ООН 🌍", url="https://un.org"))
    bot.send_message(message.chat.id, "Нажми для перехода:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "📝 Пройти квиз")
def run_quiz(message):
    # Вопрос 1
    bot.send_poll(
        message.chat.id, 
        "Что вносит самый большой вклад в глобальное потепление?", 
        ["Использование ископаемого топлива", "Космическое излучение", "Вулканическая активность"], 
        is_anonymous=False, type='quiz', correct_option_id=0
    )
    time.sleep(1)

    # Вопрос 2
    bot.send_poll(
        message.chat.id, 
        "Производство какого продукта требует больше всего воды и ресурсов?", 
        ["Картофель", "Яблоки", "Говядина"], 
        is_anonymous=False, type='quiz', correct_option_id=2
    )
    time.sleep(1)

    # Вопрос 3
    bot.send_poll(
        message.chat.id, 
        "Сколько времени разлагается обычный пластиковый пакет?", 
        ["До 5 лет", "Около 20 лет", "До 500 лет"], 
        is_anonymous=False, type='quiz', correct_option_id=2
    )
    time.sleep(1)

    # Вопрос 4
    bot.send_poll(
        message.chat.id, 
        "Какие лампочки самые энергоэффективные?", 
        ["Накаливания", "Светодиодные (LED)", "Галогенные"], 
        is_anonymous=False, type='quiz', correct_option_id=1
    )
    time.sleep(1)

    # Вопрос 5
    bot.send_poll(
        message.chat.id, 
        "Что из этого НЕЛЬЗЯ переработать бесконечное количество раз?", 
        ["Стекло", "Алюминий", "Пластик"], 
        is_anonymous=False, type='quiz', correct_option_id=2,
        explanation="Пластик теряет качество при каждой переработке, в отличие от металла и стекла."
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Используй кнопки в меню для управления ботом!")

if __name__ == '__main__':
    bot.polling(none_stop=True)
