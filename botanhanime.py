import logging
import requests
import telebot
from telebot import types

# Đặt token bot anh em ở đây
BOT_TOKEN = 'Đặt token bot anh em ở đây'
bot = telebot.TeleBot(BOT_TOKEN)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
# Dev by thanhsangdev
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Chào bạn! Gõ /anime để nhận hình ảnh anime.')

@bot.message_handler(commands=['anime'])
def get_anime_image(message):
    response = requests.get('https://api.sumiproject.net/images/anime')
    if response.status_code == 200:
        image_url = response.json().get('url')
        if image_url:
            bot.send_photo(message.chat.id, photo=image_url)
        else:
            bot.reply_to(message, 'Không tìm thấy hình ảnh anime.')
    else:
        bot.reply_to(message, 'Có lỗi xảy ra khi lấy hình ảnh anime.')
bot.polling()

if __name__ == '__main__':
    bot.polling(none_stop=True)
