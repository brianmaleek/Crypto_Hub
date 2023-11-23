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

@bot.message_handler(commands=['blockchain'])
def send_blockchain(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    btn1 = telebot.types.InlineKeyboardButton('What is Blockchain?', callback_data='blockchain')
    btn2 = telebot.types.InlineKeyboardButton('How does it work?', callback_data='how')
    btn3 = telebot.types.InlineKeyboardButton('What is mining?', callback_data='mining')
    btn4 = telebot.types.InlineKeyboardButton('What is a smart contract?', callback_data='smart')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id,"What do you want to know?:", reply_markup=markup)    
bot.infinity_polling()