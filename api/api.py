import aiohttp
import asyncio
import json
import os
from dotenv import load_dotenv
# Load the environment variables from the .env file
load_dotenv()

API_KEY = os.environ['COIN_KEY']

CRYPTO_URL =  'https://api.coingecko.com/api/v3/simple/'

# Get Crypto Price
async def get_price(crypto):
    async with aiohttp.ClientSession() as session:
        url = f'{CRYPTO_URL}/price?ids={crypto}&vs_currencies=usd'
        headers={'Authorization': f'Token {API_KEY}'}
        async with session.get(url, headers=headers) as resp:
            data = await resp.json()
            return  data.get(crypto, ).get('usd')
