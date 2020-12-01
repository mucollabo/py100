import telegram

my_token = '1440678621:AAH9n8OfP_s4-438vqD6am5v5q0x04oq8Bs'

bot = telegram.Bot(token=my_token)

updates = bot.getUpdates()
print(updates)
print('\n')

for update in updates:
    print(update)
    print('\n')

latest_update = updates[-1]
print(latest_update.message.date)
print(latest_update.message.chat.id)
print(latest_update.message.text)
