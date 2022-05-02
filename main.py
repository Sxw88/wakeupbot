from telegram.ext import Updater, CallbackContext, InlineQueryHandler, CommandHandler
from telegram import Update
import requests
from datetime import datetime
import time
import re

authorized_IDs = ['[REDACTED-USER-ID]','[REDACTED-USER-ID]']
stop_time = "01:00"
unauthorized_msg = "you are not authorized, please go away."

timenow = datetime.now()
printtime = timenow.strftime("%H:%M")
print(printtime)

def hi(update: Update, context: CallbackContext):
    hi_msg = "hi, what's up"
    context.bot.send_message(chat_id=update.effective_chat.id, text=hi_msg)

def sleepnow(update: Update, context: CallbackContext):
    if str(update.effective_chat.id) in authorized_IDs:
        sleepnow_msg = "are you asleep?"
        while datetime.now().strftime("%H:%M") != stop_time:
            print(datetime.now().strftime("%H:%M:%S"))
            for all_IDs in authorized_IDs:
                context.bot.send_message(chat_id=int(all_IDs), text=sleepnow_msg)
            time.sleep(10)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=unauthorized_msg)

def main():
    updater = Updater('[REDACTED-BOT-ID]', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('hi',hi))
    dp.add_handler(CommandHandler('sleepnow',sleepnow))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
