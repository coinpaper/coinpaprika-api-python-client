from .Coinpaprika import Coinpaprika


class CoinpaprikaTickers:

    def __call__(self, quotes=tuple(["USD"])):
        return self.all(quotes)

    @staticmethod
    def all(quotes=tuple(["USD"])):
        quotes_str = ",".join(quotes)
        tickers = Coinpaprika.get(f"/tickers", params={"quotes": quotes_str})
        for ticker in tickers:
            Coinpaprika.convert_date_in_dict(ticker, "first_data_at")
            Coinpaprika.convert_date_in_dict(ticker, "last_updated")
        return tickers

    @staticmethod
    def for_coin(coin_id, quotes=tuple(["USD"])):
        quotes_str = ",".join(quotes)
        tickers = Coinpaprika.get(f"/tickers/{coin_id}", params={"quotes": quotes_str})
        for ticker in tickers:
            Coinpaprika.convert_date_in_dict(ticker, "first_data_at")
            Coinpaprika.convert_date_in_dict(ticker, "last_updated")
        return tickers

    @staticmethod
    def historical_ticker_for_coin(coin_id, start, end, limit=1000, quotes=tuple(["USD"]), interval="5m"):
        quotes_str = ",".join(quotes)
        params = {
            "start": start.timestamp(),
            "end": end.timestamp(),
            "limit": limit,
            "quotes": quotes_str,
            "interval": interval,
        }
        tickers = Coinpaprika.get(f"/tickers/{coin_id}/historical", params=params)
        for ticker in tickers:
            Coinpaprika.convert_date_in_dict(ticker, "timestamp")
        return tickers
