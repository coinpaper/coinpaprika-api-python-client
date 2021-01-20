from src import CoinpaprikaClient
from datetime import datetime, timedelta

if __name__ == "__main__":
    api_client = CoinpaprikaClient()
    binance_markets = api_client.exchanges.markets("binance")

    print(binance_markets)