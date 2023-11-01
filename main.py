import os
import telebot
import openai

from dotenv import load_dotenv

load_dotenv()

tg_api = os.getenv("TELEGRAM_KEY")
ai_api = os.getenv("OPENAPI_KEY")

# Указать ключи
openai.api_key = ai_api
bot = telebot.TeleBot(tg_api)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! я ChatGPT.')
    #@TODO(Сделать проверку кода доступа)
    # Веддите код доступ

@bot.message_handler(content_types=['text'])
def talk(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        top_p=1.0,
        frequency_penalty=0.5,
    )

    gpt_text = response['choices'][0]['text']
    bot.send_message(message.chat_id, gpt_text)


bot.polling(none_stop=True)