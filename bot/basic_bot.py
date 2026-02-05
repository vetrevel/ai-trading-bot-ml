from binance import Client
from bot.logger import logger


class BasicBot:
    def __init__(self, api_key, api_secret):
        # IMPORTANT: testnet=True
        self.client = Client(api_key, api_secret, testnet=True)

        # Explicit Futures Testnet endpoint
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logger.info(order)
            return order
        except Exception as e:
            logger.error(f"Market order error: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logger.info(order)
            return order
        except Exception as e:
            logger.error(f"Limit order error: {e}")
            return None
