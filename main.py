from bot.basic_bot import BasicBot
from config import API_KEY, API_SECRET

bot = BasicBot(API_KEY, API_SECRET)

print("\n=== Binance Futures Testnet Trading Bot ===\n")

symbol = input("Symbol (e.g. BTCUSDT): ").upper()
side = input("Side (BUY / SELL): ").upper()
order_type = input("Order Type (MARKET / LIMIT): ").upper()
quantity = float(input("Quantity: "))

if order_type == "MARKET":
    result = bot.place_market_order(symbol, side, quantity)
elif order_type == "LIMIT":
    price = float(input("Price: "))
    result = bot.place_limit_order(symbol, side, quantity, price)
else:
    print("Invalid order type")
    exit(1)

if result:
    print("\n✅ Order placed successfully")
    print(result)
else:
    print("\n❌ Order failed. Check logs.")
