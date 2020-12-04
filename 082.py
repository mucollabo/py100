import telegram

def send_telegram_message(message):

    my_token = '1440678621:AAH9n8OfP_s4-438vqD6am5v5q0x04oq8Bs'
    bot = telegram.Bot(token=my_token)
    
    chat_id = bot.getUpdates()[-1].message.chat.id
    bot.sendMessage(chat_id=chat_id, text=str(message))
    
    
if __name__ == '__main__':
    
    message = input('보낼 메시지를 입력하세요:')
    send_telegram_message(message)