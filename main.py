import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, \
                            MessageHandler, filters

# Load the environment variables from the .env file
load_dotenv()

# Enable logging
# The logging module is used to log errors and debug messages
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Tells the bot to send a message when the command /start is issued
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="I'm a bot, please talk to me!")


# Tells the bot to repeat the message sent by the user
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=update.message.text)


# Tells the bot to send a message in caps when the command /caps is issued
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=text_caps)


# Tells the bot to send a message when an unknown command is issued
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Sorry, I didn't understand that \
                                    command.")

# below is the main function that runs the bot
if __name__ == '__main__':
    # The token is the secret key used to identify your bot
    TOKEN = os.environ['TELEGRAM_API_KEY']

    # Create the application
    application = ApplicationBuilder().token(TOKEN).build()

    # handler to listen for regular messages and echo them
    # your bot should now echo all non-command messages it receives
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    # Tell the bot to listen for the command /start
    start_handler = CommandHandler('start', start)

    # Tell the bot to listen for the command /caps
    caps_handler = CommandHandler('caps', caps)

    # Tell the bot to listen for unknown commands
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    # add the handlers to the application
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(unknown_handler, group=1)

    # application.run_polling runs the bot until you press Ctrl-C
    application.run_polling()
