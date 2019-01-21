from typing import List, Dict

from datetime import datetime

from .Coinpaprika import Coinpaprika


class CoinpaprikaCoin:

    def __call__(self) -> List[Dict]:
        """
        List coins
        :return: [
                  {
                    "id": "btc-bitcoin",
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "rank": 1,
                    "is_new": false,
                    "is_active": true,
                    "type": "coin"
                  }
                ]
        """
        return CoinpaprikaCoin.all()

    @staticmethod
    def all() -> List[Dict]:
        """
        List coins
        :return: [
                  {
                    "id": "btc-bitcoin",
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "rank": 1,
                    "is_new": false,
                    "is_active": true,
                    "type": "coin"
                  }
                ]
        """
        return Coinpaprika.get("/coins")

    @staticmethod
    def with_id(coin_id: str) -> Dict:
        """
        Get coin by ID
        :param coin_id: Example: btc-bitcoin
        :return: {
                  "id": "btc-bitcoin",
                  "name": "Bitcoin",
                  "symbol": "BTC",
                  "parent": {
                    "id": "eth-ethereum",
                    "name": "Ethereum",
                    "symbol": "ETH"
                  },
                  "rank": 1,
                  "is_new": false,
                  "is_active": true,
                  "type": "coin",
                  "tags": [
                    {
                      "id": "blockchain-service",
                      "name": "Blockchain Service",
                      "coin_counter": 160,
                      "ico_counter": 80
                    }
                  ],
                  "team": [
                    {
                      "id": "vitalik-buterin",
                      "name": "Vitalik Buterin",
                      "position": "Author"
                    }
                  ],
                  "description": "Bitcoin is a cryptocurrency and worldwide payment system. It is the first decentralized digital currency, as the system works without a central bank or single administrator.",
                  "message": "string",
                  "open_source": true,
                  "hardware_wallet": true,
                  "started_at": "2009-01-03T00:00:00Z",
                  "development_status": "Working product",
                  "proof_type": "Proof of work",
                  "org_structure": "Decentralized",
                  "hash_algorithm": "SHA256",
                  "contract": "string",
                  "platform": "string",
                  "contracts": [
                    {
                      "contract": "string",
                      "platform": "string",
                      "type": "string"
                    }
                  ],
                  "links": {
                    "explorer": [
                      "http://blockchain.com/explorer",
                      "https://blockchair.com/bitcoin/blocks",
                      "https://blockexplorer.com/",
                      "https://live.blockcypher.com/btc/"
                    ],
                    "facebook": [
                      "https://www.facebook.com/bitcoins/"
                    ],
                    "reddit": [
                      "https://www.reddit.com/r/bitcoin"
                    ],
                    "source_code": [
                      "https://github.com/bitcoin/bitcoin"
                    ],
                    "website": [
                      "https://bitcoin.org/"
                    ],
                    "youtube": [
                      "https://www.youtube.com/watch?v=Um63OQz3bjo"
                    ],
                    "medium": null
                  },
                  "links_extended": [
                    {
                      "url": "http://blockchain.com/explorer",
                      "type": "explorer"
                    },
                    {
                      "url": "https://www.reddit.com/r/bitcoin",
                      "type": "reddit",
                      "stats": {
                        "subscribers": 1009135
                      }
                    },
                    {
                      "url": "https://github.com/bitcoin/bitcoin",
                      "type": "source_code",
                      "stats": {
                        "contributors": 730,
                        "stars": 36613
                      }
                    },
                    {
                      "url": "https://bitcoin.org/",
                      "type": "website"
                    }
                  ],
                  "whitepaper": {
                    "link": "https://static.coinpaprika.com/storage/cdn/whitepapers/215.pdf",
                    "thumbnail": "https://static.coinpaprika.com/storage/cdn/whitepapers/217.jpg"
                  },
                  "first_data_at": "2018-10-03T11:48:19Z",
                  "last_data_at": "2019-05-03T11:00:00"
                }
        """
        coin = Coinpaprika.get(f"/coins/{coin_id}")
        Coinpaprika.convert_date_in_dict(coin, "started_at")
        Coinpaprika.convert_date_in_dict(coin, "first_data_at")
        Coinpaprika.convert_date_in_dict(coin, "last_data_at")
        return coin

    @staticmethod
    def twitter(coin_id: str) -> List[Dict]:
        """
        Get twitter timeline for coin
        :param coin_id: Example: btc-bitcoin
        :return: [
                  {
                    "date": "2018-10-03T11:48:19Z",
                    "user_name": "bitcoincoreorg",
                    "user_image_link": "string",
                    "status": "Bitcoin Core 0.17.0 Released https://t.co/ciwCREngon",
                    "is_retweet": false,
                    "retweet_count": 0,
                    "like_count": 0,
                    "status_link": "string",
                    "status_id": "string",
                    "media_link": "string",
                    "youtube_link": "string"
                  }
                ]
        """
        timeline = Coinpaprika.get(f"/coins/{coin_id}/twitter")
        for tweet in timeline:
            Coinpaprika.convert_date_in_dict(tweet, "date")
        return timeline

    @staticmethod
    def events(coin_id: str) -> List[Dict]:
        """
        Get coin events by coin ID
        :param coin_id: Example: btc-bitcoin
        :return: [
                  {
                    "id": "17398-cme-april-first-trade",
                    "date": "2018-04-02T00:00:00Z",
                    "date_to": "string",
                    "name": "CME: April First Trade",
                    "description": "First trade of Bitcoin futures contract for April 2018.",
                    "is_conference": false,
                    "link": "http://www.cmegroup.com/trading/equity-index/us-index/bitcoin_product_calendar_futures.html",
                    "proof_image_link": "https://static.coinpaprika.com/storage/cdn/event_images/16635.jpg"
                  }
                ]
        """
        return Coinpaprika.get(f"/coins/{coin_id}/events")

    @staticmethod
    def exchanges(coin_id: str) -> List[Dict]:
        """
        Get exchanges by coin ID
        :param coin_id: Example: btc-bitcoin
        :return: [
                  {
                    "id": "binance",
                    "name": "Binance",
                    "fiats": [
                      {
                        "name": "US Dollars",
                        "symbol": "USD"
                      }
                    ],
                    "adjusted_volume_24h_share": 11.26
                  }
                ]
        """
        return Coinpaprika.get(f"/coins/{coin_id}/exchanges")

    @staticmethod
    def markets(coin_id: str, quotes=tuple(["USD"])) -> List[Dict]:
        """
        Get markets by coin ID
        :param coin_id: Example: btc-bitcoin
        :param quotes: List of quotes to return. Currently allowed values: BTC, ETH, USD, EUR, PLN,
                       KRW, GBP, CAD, JPY, RUB, TRY, NZD, AUD, CHF, UAH, HKD, SGD, NGN, PHP, MXN, BRL, THB, CLP, CNY,
                       CZK, DKK, HUF, IDR, ILS, INR, MYR, NOK, PKR, SEK, TWD, ZAR, VND, BOB, COP, PEN, ARS, ISK
        :return: [
                  {
                    "exchange_id": "binance",
                    "exchange_name": "Binance",
                    "pair": "BTC/USDT",
                    "base_currency_id": "btc-bitcoin",
                    "base_currency_name": "Bitcoin",
                    "quote_currency_id": "usdt-tether",
                    "quote_currency_name": "Tether",
                    "market_url": "https://www.binance.com/en/trade/BTC_USDT",
                    "category": "Spot",
                    "fee_type": "Percentage",
                    "outlier": false,
                    "adjusted_volume_24h_share": 30.29,
                    "quotes": {
                      "$KEY": {
                        "price": 4582.6967796728,
                        "volume_24h": 229658776.19514218
                      }
                    },
                    "last_updated": "2018-11-14T07:20:41Z"
                  }
                ]
        """
        quotes_str = ",".join(quotes)
        markets = Coinpaprika.get(f"/coins/{coin_id}/markets", params={"quotes": quotes_str})
        for market in markets:
            Coinpaprika.convert_date_in_dict(market, "last_updated")
        return markets

    @staticmethod
    def historical_OHLC(coin_id: str, start: datetime, end: datetime, limit=1, quotes=tuple(["USD"])) -> List[Dict]:
        """
        Open/High/Low/Close values with volume and market_cap.
        Request example: https://api.coinpaprika.com/v1/coins/btc-bitcoin/ohlcv/historical?start=2019-01-01&end=2019-01-20
        if the last day is current day it can an change with every request until actual close of the day at 23:59:59
        :param coin_id: Example: btc-bitcoin
        :param start: start point for historical data
        :param end: end point for ohlcv (max 1 year)
        :param limit: limit of result rows (max 366)
        :param quotes: returned data quote (available values: usd btc)
        :return: [
                  {
                    "time_open": "2018-03-01T00:00:00Z",
                    "time_close": "2018-03-01T23:59:59Z",
                    "open": 856.012,
                    "high": 880.302,
                    "low": 851.92,
                    "close": 872.2,
                    "volume": 1868520000,
                    "market_cap": 83808161204
                  }
                ]
        """
        params = {
            "start": int(start.timestamp()),
            "end": int(end.timestamp()),
            "limit": limit,
            "quotes": ",".join(quotes)
        }
        entries = Coinpaprika.get(f"/coins/{coin_id}/ohlcv/historical", params=params)
        for entry in entries:
            Coinpaprika.convert_date_in_dict(entry, "time_open")
            Coinpaprika.convert_date_in_dict(entry, "time_close")
        return entries

    @staticmethod
    def last_OHLC(coin_id: str, quote="USD") -> List[Dict]:
        """
        Open/High/Low/Close values with volume and market_cap
        :param coin_id: Example: btc-bitcoin
        :param quote: returned data quote (available values: usd btc)
        :return: [
                  {
                    "time_open": "2018-03-01T00:00:00Z",
                    "time_close": "2018-03-01T23:59:59Z",
                    "open": 856.012,
                    "high": 880.302,
                    "low": 851.92,
                    "close": 872.2,
                    "volume": 1868520000,
                    "market_cap": 83808161204
                  }
                ]
        """
        entries = Coinpaprika.get(f"/coins/{coin_id}/ohlcv/latest", params={"quote": quote})
        for entry in entries:
            Coinpaprika.convert_date_in_dict(entry, "time_open")
            Coinpaprika.convert_date_in_dict(entry, "time_close")
        return entries

    @staticmethod
    def today_OHLC(coin_id, quote="USD") -> List[Dict]:
        """
        Open/High/Low/Close values with volume and market_cap for today
        :param coin_id:
        :param quote: returned data quote (available values: usd btc)
        :return: [
                  {
                    "time_open": "2018-03-01T00:00:00Z",
                    "time_close": "2018-03-01T23:59:59Z",
                    "open": 856.012,
                    "high": 880.302,
                    "low": 851.92,
                    "close": 872.2,
                    "volume": 1868520000,
                    "market_cap": 83808161204
                  }
                ]
        """
        entries = Coinpaprika.get(f"/coins/{coin_id}/ohlcv/today", params={"quote": quote})
        for entry in entries:
            Coinpaprika.convert_date_in_dict(entry, "time_open")
            Coinpaprika.convert_date_in_dict(entry, "time_close")
        return entries
