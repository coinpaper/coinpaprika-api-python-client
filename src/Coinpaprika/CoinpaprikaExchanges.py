from typing import List, Dict

from .Coinpaprika import Coinpaprika


class CoinpaprikaExchanges:

    def __call__(self, quotes=tuple(["USD"])) -> List[Dict]:
        """
        List exchanges
        :param quotes: List of quotes to return. Currently allowed values: BTC, ETH,
                       USD, EUR, PLN, KRW, GBP, CAD, JPY, RUB, TRY, NZD, AUD, CHF, UAH, HKD, SGD, NGN, PHP, MXN,
                       BRL, THB, CLP, CNY, CZK, DKK, HUF, IDR, ILS, INR, MYR, NOK, PKR, SEK, TWD, ZAR, VND, BOB,
                       COP, PEN, ARS, ISK
        :return: [
                  {
                    "id": "binance",
                    "name": "Binance",
                    "active": true,
                    "website_status": true,
                    "api_status": true,
                    "description": "Binance is a Malta-based cryptocurrency exchange founded in July 2017",
                    "message": "Currently under maintenance",
                    "links": {
                      "website": [
                        "https://www.binance.com/"
                      ],
                      "twitter": [
                        "https://twitter.com/binance"
                      ]
                    },
                    "markets_data_fetched": true,
                    "adjusted_rank": 1,
                    "reported_rank": 3,
                    "currencies": 150,
                    "markets": 385,
                    "fiats": [
                      {
                        "name": "US Dollars",
                        "symbol": "USD"
                      }
                    ],
                    "quotes": {
                      "$KEY": {
                        "reported_volume_24h": 794020873,
                        "adjusted_volume_24h": 794020873,
                        "reported_volume_7d": 153060819,
                        "adjusted_volume_7d": 153060819,
                        "reported_volume_30d": 301246828,
                        "adjusted_volume_30d": 301246828
                      }
                    },
                    "last_updated": "2018-11-14T07:20:41Z"
                  }
                ]
        """
        return self.all(quotes)

    @staticmethod
    def all(quotes=tuple(["USD"])) -> List[Dict]:
        """
        List exchanges
        :param quotes: List of quotes to return. Currently allowed values: BTC, ETH,
                       USD, EUR, PLN, KRW, GBP, CAD, JPY, RUB, TRY, NZD, AUD, CHF, UAH, HKD, SGD, NGN, PHP, MXN,
                       BRL, THB, CLP, CNY, CZK, DKK, HUF, IDR, ILS, INR, MYR, NOK, PKR, SEK, TWD, ZAR, VND, BOB,
                       COP, PEN, ARS, ISK
        :return: [
                  {
                    "id": "binance",
                    "name": "Binance",
                    "active": true,
                    "website_status": true,
                    "api_status": true,
                    "description": "Binance is a Malta-based cryptocurrency exchange founded in July 2017",
                    "message": "Currently under maintenance",
                    "links": {
                      "website": [
                        "https://www.binance.com/"
                      ],
                      "twitter": [
                        "https://twitter.com/binance"
                      ]
                    },
                    "markets_data_fetched": true,
                    "adjusted_rank": 1,
                    "reported_rank": 3,
                    "currencies": 150,
                    "markets": 385,
                    "fiats": [
                      {
                        "name": "US Dollars",
                        "symbol": "USD"
                      }
                    ],
                    "quotes": {
                      "$KEY": {
                        "reported_volume_24h": 794020873,
                        "adjusted_volume_24h": 794020873,
                        "reported_volume_7d": 153060819,
                        "adjusted_volume_7d": 153060819,
                        "reported_volume_30d": 301246828,
                        "adjusted_volume_30d": 301246828
                      }
                    },
                    "last_updated": "2018-11-14T07:20:41Z"
                  }
                ]
        """
        quotes_str = ",".join(quotes)
        exchanges = Coinpaprika.get(f"/exchanges", params={"quotes": quotes_str})
        for exchange in exchanges:
            Coinpaprika.convert_date_in_dict(exchange, "last_updated")
        return exchanges

    @staticmethod
    def with_id(exchange_id: str, quotes=tuple(["USD"])) -> Dict:
        """
        Get exchange by ID
        :param exchange_id: Example: binance
        :param quotes: List of quotes to return. Currently allowed values: BTC, ETH,
                       USD, EUR, PLN, KRW, GBP, CAD, JPY, RUB, TRY, NZD, AUD, CHF, UAH, HKD, SGD, NGN, PHP, MXN,
                       BRL, THB, CLP, CNY, CZK, DKK, HUF, IDR, ILS, INR, MYR, NOK, PKR, SEK, TWD, ZAR, VND, BOB,
                       COP, PEN, ARS, ISK
        :return: {
                  "id": "binance",
                  "name": "Binance",
                  "active": true,
                  "website_status": true,
                  "api_status": true,
                  "description": "Binance is a Malta-based cryptocurrency exchange founded in July 2017",
                  "message": "Currently under maintenance",
                  "links": {
                    "website": [
                      "https://www.binance.com/"
                    ],
                    "twitter": [
                      "https://twitter.com/binance"
                    ]
                  },
                  "markets_data_fetched": true,
                  "adjusted_rank": 1,
                  "reported_rank": 3,
                  "currencies": 150,
                  "markets": 385,
                  "fiats": [
                    {
                      "name": "US Dollars",
                      "symbol": "USD"
                    }
                  ],
                  "quotes": {
                    "$KEY": {
                      "reported_volume_24h": 794020873,
                      "adjusted_volume_24h": 794020873,
                      "reported_volume_7d": 153060819,
                      "adjusted_volume_7d": 153060819,
                      "reported_volume_30d": 301246828,
                      "adjusted_volume_30d": 301246828
                    }
                  },
                  "last_updated": "2018-11-14T07:20:41Z"
                }
        """
        quotes_str = ",".join(quotes)
        exchange = Coinpaprika.get(f"/exchanges/{exchange_id}", params={"quotes": quotes_str})
        Coinpaprika.convert_date_in_dict(exchange, "last_updated")
        return exchange

    @staticmethod
    def markets(exchange_id: str, quotes=tuple(["USD"])) -> List[Dict]:
        """
        List markets by exchange ID
        :param exchange_id: Example: binance
        :param quotes: List of quotes to return. Currently allowed values: BTC, ETH,
                       USD, EUR, PLN, KRW, GBP, CAD, JPY, RUB, TRY, NZD, AUD, CHF, UAH, HKD, SGD, NGN, PHP, MXN,
                       BRL, THB, CLP, CNY, CZK, DKK, HUF, IDR, ILS, INR, MYR, NOK, PKR, SEK, TWD, ZAR, VND, BOB,
                       COP, PEN, ARS, ISK
        :return: [
                  {
                    "pair": "BTC/USDT",
                    "base_currency_id": "btc-bitcoin",
                    "base_currency_name": "Bitcoin",
                    "quote_currency_id": "usdt-tether",
                    "quote_currency_name": "Tether",
                    "market_url": "https://www.binance.com/en/trade/BTC_USDT",
                    "category": "Spot",
                    "fee_type": "Percentage",
                    "outlier": false,
                    "reported_volume_24h_share": 30.29,
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
        market_pairs = Coinpaprika.get(f"/exchanges/{exchange_id}/markets", params={"quotes": quotes_str})
        for market_pair in market_pairs:
            Coinpaprika.convert_date_in_dict(market_pair, "last_updated")
        return market_pairs
