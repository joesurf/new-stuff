import os
import logging
import requests
from pathlib import Path
from pprint import pprint
from dotenv import load_dotenv
from flask import Flask
from telegram import __version__ as TG_VER
from telegram import LabeledPrice, ShippingOption, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    """
    await update.message.reply_text(
        "HI",
        # reply_markup=markup, 
    )
    
    return


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(os.environ.get("TELEGRAM_BOT_TOKEN")).build()

    # simple start function
    application.add_handler(CommandHandler("start", start))

    # Run the bot until the user  presses Ctrl-C  
    application.run_polling()




from flask import Flask, request 

flask_app = Flask(__name__)
main() 