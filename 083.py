import telegram

def send_telegram_channel_message(channel_id, message):

    my_token = '1440678621:AAH9n8OfP_s4-438vqD6am5v5q0x04oq8Bs'
    bot = telegram.Bot(token=my_token)

    bot.sendMessage(chat_id=channel_id, text=str(message))


if __name__ == '__main__':

    channel_id = '@py100'
    message = '채널에 보내는 메시지입니다.'
    send_telegram_channel_message(channel_id, message)