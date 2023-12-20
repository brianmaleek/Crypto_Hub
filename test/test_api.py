import unittest
from unittest.mock import Mock, patch
import asyncio
import sys
sys.path.append('..')
from api.api import get_top, get_price, get_price_history


class AsycMock(Mock):
    """Async Mock"""
    async def __call__(self, *args, **kwargs):
        return super(AsycMock, self).__call__(*args, **kwargs)

class TestCryptoApi(unittest.IsolatedAsyncioTestCase):

    """Test the crypto api"""


    @patch("api.api.get_top", new_callable=AsycMock)
    async def test_get_top(self, get_top_mock):
        """Test the get_top function"""
        get_top_mock.return_value = [
            {"name": "Bitcoin", "current_price": 50000, "market_cap": 900000000000, "total_volume": 100000000000},
            {"name": "Ethereum", "current_price": 5000, "market_cap": 900000000000, "total_volume": 100000000000},
            {"name": "Cardano", "current_price": 5, "market_cap": 900000000000, "total_volume": 100000000000}
        ]

        response = await get_top()

        self.assertTrue(isinstance(response, list))

    @patch("api.api.get_price", new_callable=AsycMock)
    async def test_get_price(self, get_price_mock):
        """Test the get_price function"""
        get_price_mock.return_value = {
            "bitcoin": {
                "usd": 50000
            }
        }

        response = await get_price("bitcoin")

        self.assertTrue(isinstance(response, dict))

    @patch("api.api.get_price_history", new_callable=AsycMock)
    async def test_get_price_history(self, get_price_history_mock):
        """Test the get_price_history function"""
        get_price_history_mock.return_value = {
            "market_data": {
                "current_price": {
                    "usd": 50000
                }
            }
        }

        response = await get_price_history("bitcoin", "01-01-2021")

        self.assertTrue(isinstance(response, dict))


if __name__ == '__main__':
    unittest.main()