from typing import List, Dict
from datetime import datetime

from .Coinpaprika import Coinpaprika


class CoinpaprikaTickers:

    def __call__(self, quotes=tuple(["USD"])) -> List[Dict]:
        """
        Get tickers for all coins
        :param quotes: List of quotes to return. Currently allowed values: BTC, ETH,
                       USD, EUR, PLN, KRW, GBP, CAD, JPY, RUB, TRY, NZD, AUD, CHF, UAH, HKD, SGD, NGN, PHP, MXN,
                       BRL, THB, CLP, CNY, CZK, DKK, HUF, IDR, ILS, INR, MYR, NOK, PKR, SEK, TWD, ZAR, VND, BOB,
                       COP, PEN, ARS, ISK
        :return: [
                  {
                    "id": "btc-bitcoin",
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "rank": 1,
                    "circulating_supply": 17007062,
                    "total_supply": 17007062,
                    "max_supply": 21000000,
                    "beta_value": 0.735327,
                    "first_data_at": "2010-11-14T07:20:41Z",
                    "last_updated": "2018-11-14T07:20:41Z",
                    "quotes": {
                      "BTC": {
                        "price": 1,
                        "volume_24h": 1414951.9739396,
                        "volume_24h_change_24h": -4.03,
                        "market_cap": 17646575,
                        "market_cap_change_24h": 0.01,
                        "percent_change_15m": 0,
                        "percent_change_30m": 0,
                        "percent_change_1h": 0,
                        "percent_change_6h": 0,
                        "percent_change_12h": 0,
                        "percent_change_24h": 0,
                        "percent_change_7d": 0,
                        "percent_change_30d": 0,
                        "percent_change_1y": 0,
                        "ath_price": null,
                        "ath_date": null,
                        "percent_from_price_ath": null
                      },
                      "USD": {
                        "price": 5162.15941296,
                        "volume_24h": 7304207651.1585,
                        "volume_24h_change_24h": -2.5,
                        "market_cap": 91094433242,
                        "market_cap_change_24h": 1.6,
                        "percent_change_15m": 0,
                        "percent_change_30m": 0,
                        "percent_change_1h": 0,
                        "percent_change_6h": 0,
                        "percent_change_12h": -0.09,
                        "percent_change_24h": 1.59,
                        "percent_change_7d": 0.28,
                        "percent_change_30d": 27.39,
                        "percent_change_1y": -37.99,
                        "ath_price": 20089,
                        "ath_date": "2017-12-17T12:19:00Z",
                        "percent_from_price_ath": -74.3
                      }
                    }
                  }
                ]
        """
        return self.all(quotes)

    @staticmethod
    def all(quotes=tuple(["USD"])) -> List[Dict]:
        """
        Get tickers for all coins
        :param quotes: List of quotes to return. Currently allowed values: BTC, ETH,
                       USD, EUR, PLN, KRW, GBP, CAD, JPY, RUB, TRY, NZD, AUD, CHF, UAH, HKD, SGD, NGN, PHP, MXN,
                       BRL, THB, CLP, CNY, CZK, DKK, HUF, IDR, ILS, INR, MYR, NOK, PKR, SEK, TWD, ZAR, VND, BOB,
                       COP, PEN, ARS, ISK
        :return: [
                  {
                    "id": "btc-bitcoin",
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "rank": 1,
                    "circulating_supply": 17007062,
                    "total_supply": 17007062,
                    "max_supply": 21000000,
                    "beta_value": 0.735327,
                    "first_data_at": "2010-11-14T07:20:41Z",
                    "last_updated": "2018-11-14T07:20:41Z",
                    "quotes": {
                      "BTC": {
                        "price": 1,
                        "volume_24h": 1414951.9739396,
                        "volume_24h_change_24h": -4.03,
                        "market_cap": 17646575,
                        "market_cap_change_24h": 0.01,
                        "percent_change_15m": 0,
                        "percent_change_30m": 0,
                        "percent_change_1h": 0,
                        "percent_change_6h": 0,
                        "percent_change_12h": 0,
                        "percent_change_24h": 0,
                        "percent_change_7d": 0,
                        "percent_change_30d": 0,
                        "percent_change_1y": 0,
                        "ath_price": null,
                        "ath_date": null,
                        "percent_from_price_ath": null
                      },
                      "USD": {
                        "price": 5162.15941296,
                        "volume_24h": 7304207651.1585,
                        "volume_24h_change_24h": -2.5,
                        "market_cap": 91094433242,
                        "market_cap_change_24h": 1.6,
                        "percent_change_15m": 0,
                        "percent_change_30m": 0,
                        "percent_change_1h": 0,
                        "percent_change_6h": 0,
                        "percent_change_12h": -0.09,
                        "percent_change_24h": 1.59,
                        "percent_change_7d": 0.28,
                        "percent_change_30d": 27.39,
                        "percent_change_1y": -37.99,
                        "ath_price": 20089,
                        "ath_date": "2017-12-17T12:19:00Z",
                        "percent_from_price_ath": -74.3
                      }
                    }
                  }
                ]
        """
        quotes_str = ",".join(quotes)
        tickers = Coinpaprika.get(f"/tickers", params={"quotes": quotes_str})
        for ticker in tickers:
            Coinpaprika.convert_date_in_dict(ticker, "first_data_at")
            Coinpaprika.convert_date_in_dict(ticker, "last_updated")
        return tickers

    @staticmethod
    def for_coin(coin_id: str, quotes=tuple(["USD"])) -> Dict:
        """
        Get ticker information for specific coin
        :param coin_id: Example: btc-bitcoin
        :param quotes: List of quotes to return. Currently allowed values: BTC, ETH,
                       USD, EUR, PLN, KRW, GBP, CAD, JPY, RUB, TRY, NZD, AUD, CHF, UAH, HKD, SGD, NGN, PHP, MXN,
                       BRL, THB, CLP, CNY, CZK, DKK, HUF, IDR, ILS, INR, MYR, NOK, PKR, SEK, TWD, ZAR, VND, BOB,
                       COP, PEN, ARS, ISK
        :return: {
                  "id": "btc-bitcoin",
                  "name": "Bitcoin",
                  "symbol": "BTC",
                  "rank": 1,
                  "circulating_supply": 17007062,
                  "total_supply": 17007062,
                  "max_supply": 21000000,
                  "beta_value": 0.735327,
                  "first_data_at": "2010-11-14T07:20:41Z",
                  "last_updated": "2018-11-14T07:20:41Z",
                  "quotes": {
                    "BTC": {
                      "price": 1,
                      "volume_24h": 1414951.9739396,
                      "volume_24h_change_24h": -4.03,
                      "market_cap": 17646575,
                      "market_cap_change_24h": 0.01,
                      "percent_change_15m": 0,
                      "percent_change_30m": 0,
                      "percent_change_1h": 0,
                      "percent_change_6h": 0,
                      "percent_change_12h": 0,
                      "percent_change_24h": 0,
                      "percent_change_7d": 0,
                      "percent_change_30d": 0,
                      "percent_change_1y": 0,
                      "ath_price": null,
                      "ath_date": null,
                      "percent_from_price_ath": null
                    },
                    "USD": {
                      "price": 5162.15941296,
                      "volume_24h": 7304207651.1585,
                      "volume_24h_change_24h": -2.5,
                      "market_cap": 91094433242,
                      "market_cap_change_24h": 1.6,
                      "percent_change_15m": 0,
                      "percent_change_30m": 0,
                      "percent_change_1h": 0,
                      "percent_change_6h": 0,
                      "percent_change_12h": -0.09,
                      "percent_change_24h": 1.59,
                      "percent_change_7d": 0.28,
                      "percent_change_30d": 27.39,
                      "percent_change_1y": -37.99,
                      "ath_price": 20089,
                      "ath_date": "2017-12-17T12:19:00Z",
                      "percent_from_price_ath": -74.3
                    }
                  }
                }
        """
        quotes_str = ",".join(quotes)
        ticker = Coinpaprika.get(f"/tickers/{coin_id}", params={"quotes": quotes_str})
        Coinpaprika.convert_date_in_dict(ticker, "first_data_at")
        Coinpaprika.convert_date_in_dict(ticker, "last_updated")
        return ticker

    @staticmethod
    def historical_ticker_for_coin(coin_id: str, start: datetime, end: datetime, limit=1000, quote="USD", interval="5m") -> List[Dict]:
        """
        Get historical tickers for specific coin
        :param coin_id: Example: btc-bitcoin
        :param start: start point for historical data
        :param end: end point for historical data
        :param limit: limit of result rows (max 5000)
        :param quote: returned data quote (available values: usd btc)
        :param interval: Returned points interval
                         (available values: 5m 10m 15m 30m 45m 1h 2h 3h 6h 12h 24h 1d 7d 14d 30d 90d 365d)
        :return: [
                  {
                    "timestamp": "2018-03-01T00:00:00Z",
                    "price": 855.53,
                    "volume_24h": 1968587956,
                    "market_cap": 83761787514
                  }
                ]
        """
        params = {
            "start": int(start.timestamp()),
            "end": int(end.timestamp()),
            "limit": limit,
            "quote": quote,
            "interval": interval,
        }
        tickers = Coinpaprika.get(f"/tickers/{coin_id}/historical", params=params)
        for ticker in tickers:
            Coinpaprika.convert_date_in_dict(ticker, "timestamp")
        return tickers
