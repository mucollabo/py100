import telegram

my_token = '1440678621:AAH9n8OfP_s4-438vqD6am5v5q0x04oq8Bs'

# 봇 생성
bot = telegram.Bot(token=my_token)
print(type(bot))
print(bot)

# 봇(사용자) 정보 확인
bot_info = bot.getMe()
print(type(bot_info))
print(bot_info)
