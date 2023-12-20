import os
import telebot
import logging
from dotenv import load_dotenv
from api.api import get_price, get_price_history, get_top
import asyncio
import datetime


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


################################
# Handle the /start command
################################

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Crypto Hub, where you can get information about "
                 "BlockChain and crypto currencies.\n\nYou can control me by "
                 "clicking on the following commands: 👇 "
                 "\n 👉 /crypto - Get information about cryptocurrencies "
                 "\n 👉 /blockchain - Get information about blockchain")

#####################
# Handle Crypto Query
#####################
    
@bot.message_handler(commands=['crypto'])
def send_crypto(message):
    bot.reply_to(message, "Crypto currencies are digital currencies that are "
                 "transferred between peers without the need for a central "
                 "authority, such as a bank or government. Transactions are "
                 "recorded on a distributed public ledger called a blockchain."
                 "\n\n  To find out more use click on any of the following commands:"
                "\n 👆 /top - Get top 10 cryptocurrencies"
                "\n 💰 /price - Get price of a specific cryptocurrency"
                "\n 📈 /history - Get Historical data of a specific cryptocurrency on a specific date")

    markup = telebot.types.InlineKeyboardMarkup(row_width=2)

    # Create a menu item for /top with an inline keyboard
    top_button = telebot.types.InlineKeyboardButton('Top 10 Cryptocurrencies', callback_data='top')
    # Send the message with the menu items
    bot.reply_to(message, "Choose an option:", reply_markup=markup)


#####################
# Handle Top Query
#####################

@bot.message_handler(commands=['top'])
def get_top_crypto(message):
    bot.reply_to(message, "You clicked on /top. Here's information about the top 10 cryptocurrencies.")
    
    asyncio.run(process_top_crypto_step(message))


async def process_top_crypto_step(message):
    try:
        data = await get_top() 
        if data:
            for i in range(10):
                name = data[i].get("name")
                price = data[i].get("current_price")
                market_cap = data[i].get("market_cap")
                total_volume = data[i].get("total_volume")
                # Construct the message
                response_message = (
                    f"{i+1}. {name}\n"
                    f"Price: {price} USD\n"
                    f"Market Cap: {market_cap} USD\n"
                    f"Total Volume: {total_volume} USD"
                )
                bot.send_message(message.chat.id, response_message)  

    except Exception as e:
        print(f"An error occurred: {e}")
        bot.send_message(message.chat.id, 'Oops! Something went wrong. Please try again.')  



#####################
# Handle Price Query
#####################

@bot.message_handler(commands=['price'])
def send_price(message):
    bot.reply_to(message, "You clicked on /price. Please enter the name of the cryptocurrency you want to know the price of. If it is more than one enter the names separated by a comma. For example: bitcoin, ethereum, litecoin")
    
    # Handle the message with the crypto name
    @bot.message_handler(func=lambda message: True)
    def handle_crypto_name(message):
        crypto_name = message.text.split(",")
        asyncio.run(process_crypto_price_step(message.chat.id, crypto_name))

# api consumption
async def process_crypto_price_step(chat_id, crypto_name):
    try:
        for input_crypto_name in crypto_name:
            crypto_name = input_crypto_name.strip().lower()
            data = await get_price(crypto_name)

            # print debug statement
            # logging.debug(f"Debug: {crypto_name=}, {data=}")
            # print(f"Debug: {crypto_name=}, {data=}")

            price = data.get(crypto_name, {}).get("usd")

            if price is not None:
                # get the current timestamp
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                message = (
                    f"The price of {crypto_name} is {price} USD\n"
                    f"Last updated: {timestamp}"
                )
                bot.send_message(chat_id, message)
            else:
                bot.send_message(chat_id, f"Could not fetch the price for {crypto_name}")

            # print for testing
            # logging.info(f"Testing {crypto_name} - Price {price}")
            # print(f"Testing {crypto_name} - Price {price}")

    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")
        bot.send_message(chat_id, 'Oops! Something went wrong. Please try again.')


#########################
# Handle History Query
#########################

@bot.message_handler(commands=['history'])
def send_history(message):
    bot.reply_to(message, "You clicked on /history. Please enter the name of the cryptocurrency you want to know the historical data of.")
    bot.register_next_step_handler(message, handle_crypto_name)

# Handle the message with the crypto name and get date
def handle_crypto_name(message):
    crypto_name = message.text
    bot.send_message(message.chat.id, f"You entered {crypto_name}. Please enter the date in the format DD-MM-YYYY.")
    bot.register_next_step_handler(message, lambda msg: handle_date(msg, crypto_name))

# Handle the message with the date
def handle_date(message, crypto_name):
    date = message.text
    asyncio.run(process_crypto_history_step2(message.chat.id, crypto_name, date))


async def process_crypto_history_step2(chat_id, crypto_name, date):
    try:
        data = await get_price_history(crypto_name, date)

        # Check if the required data is present
        market_data = data.get("market_data")
        if not market_data or not all(key in market_data for key in ("current_price", "market_cap", "total_volume")):
            bot.send_message(chat_id, f"Could not fetch the data for {crypto_name} on {date}")
            return

        current_price = market_data["current_price"]["usd"]
        market_cap = market_data["market_cap"]["usd"]
        total_volume = market_data["total_volume"]["usd"]

        if current_price is not None and market_cap is not None and total_volume is not None:
            message = (
                f"The historical data for {crypto_name} on {date}:\n"
                f"Current Price: {current_price} USD\n"
                f"Market Cap: {market_cap} USD\n"
                f"Total Volume: {total_volume} USD"
            )
            bot.send_message(chat_id, message)

    except Exception as e:
        print(f"An error occurred: {e}")
        bot.send_message(chat_id,'Oops! Something went wrong. Please try again.')


##########################
# Handle Blockchain Query
##########################

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
        elif call.data == 'top':
            bot.send_message(call.message.chat.id, "You clicked on /top. Here's information about the top 10 cryptocurrencies.")
            # Add your logic to fetch and display information about the top 10 cryptocurrencies.

        elif call.data == 'history':
            bot.send_message(call.message.chat.id, "You clicked on /history. Here's information about the historical data of a specific cryptocurrency.")
            # Add your logic to fetch and display historical data for a cryptocurrency.
    except Exception as e:
        logging.error(f"Error handling callback query: {str(e)}")


# Start the bot

def main():
    try:
        bot.infinity_polling()
    except Exception as e:
        logging.error(f"Error polling: {str(e)}")

if __name__ == '__main__':
    main()
