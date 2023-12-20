import aiohttp
import asyncio
import json
import os
from dotenv import load_dotenv
# Load the environment variables from the .env file
load_dotenv()

API_KEY = os.environ['COIN_KEY']

CRYPTO_URL =  'https://api.coingecko.com/api/v3/'

# Get Crypto Price
async def get_price(crypto):
    async with aiohttp.ClientSession() as session:
        url = f'{CRYPTO_URL}/simple/price?ids={crypto}&vs_currencies=usd'
        headers={'Authorization': f'Token {API_KEY}'}
        async with session.get(url, headers=headers) as resp:
            data = await resp.json()
            return  data
        

# Get Crypto Price History
async def get_price_history(crypto, date):
    async with aiohttp.ClientSession() as session:
    
        url = f'{CRYPTO_URL}/coins/{crypto}/history?&date={date}&localization=eng'
        headers={'Authorization': f'Token {API_KEY}'}
        async with session.get(url, headers=headers) as resp:
            data = await resp.json()
            return data

# Get Top 10 traded Crypto Market Data
async def get_top():
    try:
        async with aiohttp.ClientSession() as session:
            url = f'{CRYPTO_URL}/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false'

            headers={'Authorization': f'Token {API_KEY}'}

            async with session.get(url, headers=headers) as resp:
                data = await resp.json()

                # check if the expected keys are present in the response
                if isinstance(data, list) and len(data) > 0:
                    return data
                else:
                    raise ValueError('Invalid or empty response from API')
    except Exception as e:
        print(f"An error ocurred during API request: {e}")
        return None
