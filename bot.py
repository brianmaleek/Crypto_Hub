import os
import telebot
import logging
from dotenv import load_dotenv


# Load the environment variables from the .env file
load_dotenv()

# Enable logging
# The logging module is used to log errors and debug messages
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    filename='bot.log', level=logging.INFO)

# Get the bot token from the environment variables
BOT_TOKEN = os.environ['BOT_TOKEN']
if not BOT_TOKEN:
    logging.error("Could not connect to Telegram API")
    exit(1)

# Create a bot instance
bot = telebot.TeleBot(BOT_TOKEN)

# Command handlers
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Crypto Hub, where you can get information about "
                 "BlockChain and crypto currencies.\n\nYou can control me by "
                 "sending the following commands: "
                 "\n /crypto - Get information about cryptocurrencies "
                 "\n /blockchain - Get information about blockchain")

@bot.message_handler(commands=['crypto'])
def send_crypto(message):
    bot.reply_to(message, "Crypto currencies are digital currencies that are "
                 "transferred between peers without the need for a central "
                 "authority, such as a bank or government. Transactions are "
                 "recorded on a distributed public ledger called a blockchain."
                 "\n\n  To find out more use the following commands:"
                "\n /top - Get top 10 cryptocurrencies"
                "\n /price - Get price of a specific cryptocurrency"
                "\n /history - Get historical data of a specific cryptocurrency")

@bot.message_handler(commands=['blockchain'])
def send_blockchain(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    btn1 = telebot.types.InlineKeyboardButton('What is Blockchain?', callback_data='blockchain')
    btn2 = telebot.types.InlineKeyboardButton('How does it work?', callback_data='how')
    btn3 = telebot.types.InlineKeyboardButton('What is mining?', callback_data='mining')
    btn4 = telebot.types.InlineKeyboardButton('What is a smart contract?', callback_data='smart')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id,"What do you want to know?:", reply_markup=markup)

# Handle responses for the buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        if call.data == 'blockchain':
            bot.send_message(call.message.chat.id, "Blockchain is a system of recording information in a way "
                            "that makes it difficult or impossible to change, hack, or cheat the system. " 
                            "A blockchain is essentially a digital ledger of transactions that is duplicated "
                            "and distributed across the entire network of computer systems on the blockchain.")
        elif call.data == 'how':
            bot.send_message(call.message.chat.id, "Blockchain was invented by a person (or group of people) "
                            "using the name Satoshi Nakamoto in 2008 to serve as the public transaction ledger of the cryptocurrency bitcoin. "
                            "The invention of the blockchain for bitcoin made it the first digital currency to solve"
                            " the double-spending problem without the need of a trusted authority or central server. "
                            "The bitcoin design has inspired other applications.")
        elif call.data == 'mining':
            bot.send_message(call.message.chat.id, "Mining is the process of adding transaction records "
                            "to Bitcoin's public ledger of past transactions (and a 'mining rig' "
                            "is a colloquial metaphor for a single computer system that performs "
                            "the necessary computations for 'mining'.")
        elif call.data == 'smart':
            bot.send_message(call.message.chat.id, "A smart contract is a computer program or a "
                            "transaction protocol which is intended to automatically execute, "
                            "control or document legally relevant events and actions according "
                            "to the terms of a contract or an agreement.") 
    except Exception as e:
        logging.error(f"Error handling callback query: {str(e)}")

def main():
    try:
        bot.infinity_polling()
    except Exception as e:
        logging.error(f"Error polling: {str(e)}")

if __name__ == '__main__':
    main()