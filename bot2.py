import config
import telebot
from time import time

bot = telebot.TeleBot(config.token)


GROUP_ID = -269732476  # ID вашей группы

@bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == GROUP_ID)
def delete_links(message):
    for entity in message.entities:
        if entity.type in ["url", "text_link"]:
            bot.kick_chat_member(message.chat.id,199844563)
        else:
            return  

if __name__ == "__main__":
    bot.polling(none_stop=True)