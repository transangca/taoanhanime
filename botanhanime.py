import logging
import requests
import telebot
from telebot import types

# Đặt token bot của bạn ở đây
BOT_TOKEN = '6380919096:AAGcL0HmiJ2ynJaHoGj-4sOLgquQS6g9208'

# Tạo đối tượng bot
bot = telebot.TeleBot(BOT_TOKEN)

# Đặt cấu hình logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Chào bạn! Gõ /anime để nhận hình ảnh anime.')

@bot.message_handler(commands=['anime'])
def get_anime_image(message):
    # Gửi yêu cầu đến API của Sumi Project để lấy hình ảnh anime
    response = requests.get('https://api.sumiproject.net/images/anime')

    if response.status_code == 200:
        # Lấy URL hình ảnh từ phản hồi JSON
        image_url = response.json().get('url')
        if image_url:
            # Gửi hình ảnh đến người dùng
            bot.send_photo(message.chat.id, photo=image_url)
        else:
            bot.reply_to(message, 'Không tìm thấy hình ảnh anime.')
    else:
        bot.reply_to(message, 'Có lỗi xảy ra khi lấy hình ảnh anime.')

# Bắt đầu bot
bot.polling()

if __name__ == '__main__':
    bot.polling(none_stop=True)
