import telebot
import requests
from time import sleep

bot = telebot.TeleBot("7955678567:AAFuxFdjD__9-AoVOHZllzEt9htDyQOvDCw")

# رابط المنتج
product_url = "https://example.com/product"

def check_availability():
    response = requests.get(product_url)
    if "متاح" in response.text:
        return True
    return False

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "أهلاً! سأخبرك عندما يتوفر المنتج.")

def notify_availability():
    while True:
        if check_availability():
            bot.send_message(YOUR_CHAT_ID, "المنتج متوفر الآن!")
        sleep(3600)  # فحص مرة كل ساعة

if __name__ == "__main__":
    bot.polling()