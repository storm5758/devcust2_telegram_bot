import config
import telebot
import requests
import rdm
bot = telebot.TeleBot(config.token)

MethodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates'.format(token=config.token)
while True:
    response = requests.post(MethodGetUpdates)
    result = response.json()
    print(result) 

#рабочий бан
GROUP_ID = -269732476
user_id= 199844563
#try:
#	bot.kick_chat_member(GROUP_ID,user_id)
#except Exception as e:
#	print("Пользователь {user_id} уже удален".format(user_id=user_id))


if __name__ == '__main__':
	bot.polling(none_stop=True)

