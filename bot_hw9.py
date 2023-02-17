from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token = '6070979657:AAHWIcrIZqNf4BKJHMWM1VkZ5yS7H1g6O1Q')
updater = Updater(token = '6070979657:AAHWIcrIZqNf4BKJHMWM1VkZ5yS7H1g6O1Q')
dispatcher = updater.dispatcher

def start(update, context):
    text = update.message.text.split()
    list=[]
    for elements in text:
        if 'абв' not in elements:
            list.append(elements)
    context.bot.send_message(update.effective_chat.id, ' '.join(list))


start_handler = MessageHandler(Filters.text, start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()