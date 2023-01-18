import os
import logging
import requests
from pathlib import Path
from pprint import pprint
from dotenv import load_dotenv

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def start(update: Update, context: CallbackContext):
    """
    """
    update.message.reply_text(
        "HI",
        # reply_markup=markup, 
    )
    
    return


def main() -> None:
    """
    Run the telegram bot.
    """
    # Create the Application and pass it your bot's token.
    updater = Updater(
        os.environ.get("TELEGRAM_BOT_TOKEN"),
        use_context=True
    )

    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Run the bot until the user presses Ctrl-C
    updater.start_polling()


main()