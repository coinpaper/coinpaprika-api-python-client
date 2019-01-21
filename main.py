from src import CoinpaprikaClient

if __name__ == "__main__":
    client = CoinpaprikaClient()
    print(client.coins.with_id("btc-bitcoin"))


