import requests
from datetime import datetime

def fetch_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price"
    response = requests.get(url, params={"symbol": "BTCUSDT"})
    response.raise_for_status()
    return float(response.json()["price"])

if __name__ == "__main__":
    price = fetch_btc_price()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] BTC/USDT: ${price:,.2f}")

