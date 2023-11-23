import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Crypto Hub, where you can get information about "
                 "BlockChain and crypto currencies.\n\nYou can control me by "
                 "sending the following commannds: "
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
    
bot.infinity_polling()