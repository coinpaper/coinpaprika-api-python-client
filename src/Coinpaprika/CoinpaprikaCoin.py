from .Coinpaprika import Coinpaprika


class CoinpaprikaCoin:

    def __call__(self):
        return CoinpaprikaCoin.all()

    @staticmethod
    def all():
        return Coinpaprika.get("/coins")

    @staticmethod
    def with_id(coin_id):
        coin = Coinpaprika.get(f"/coins/{coin_id}")
        Coinpaprika.convert_date_in_dict(coin, "started_at")
        Coinpaprika.convert_date_in_dict(coin, "first_data_at")
        Coinpaprika.convert_date_in_dict(coin, "last_data_at")
        return coin

    @staticmethod
    def twitter(coin_id):
        timeline = Coinpaprika.get(f"/coins/{coin_id}/twitter")
        for tweet in timeline:
            Coinpaprika.convert_date_in_dict(tweet, "date")
        return timeline

    @staticmethod
    def events(coin_id):
        return Coinpaprika.get(f"/coins/{coin_id}/events")

    @staticmethod
    def exchanges(coin_id):
        return Coinpaprika.get(f"/coins/{coin_id}/exchanges")

    @staticmethod
    def markets(coin_id, quotes=tuple(["USD"])):
        quotes_str = ",".join(quotes)
        markets = Coinpaprika.get(f"/coins/{coin_id}/markets", params={"quotes": quotes_str})
        for market in markets:
            Coinpaprika.convert_date_in_dict(market, "last_updated")
        return markets

    @staticmethod
    def historical_OHLC(coin_id, start, end, limit=1, quotes=tuple(["USD"])):
        params = {
            "start": start.timestamp(),
            "end": end.timestamp(),
            "limit": limit,
            "quotes": ",".join(quotes)
        }
        entries = Coinpaprika.get(f"/coins/{coin_id}/ohlcv/historical", params=params)
        for entry in entries:
            Coinpaprika.convert_date_in_dict(entry, "time_open")
            Coinpaprika.convert_date_in_dict(entry, "time_close")
        return entries

    @staticmethod
    def last_OHLC(coin_id, quotes=tuple(["USD"])):
        quotes_str = ",".join(quotes)
        entries = Coinpaprika.get(f"/coins/{coin_id}/ohlcv/latest", params={"quotes": quotes_str})
        for entry in entries:
            Coinpaprika.convert_date_in_dict(entry, "time_open")
            Coinpaprika.convert_date_in_dict(entry, "time_close")
        return entries

    @staticmethod
    def current_OHLC(coin_id, quotes=tuple(["USD"])):
        quotes_str = ",".join(quotes)
        entries = Coinpaprika.get(f"/coins/{coin_id}/ohlcv/today", params={"quotes": quotes_str})
        for entry in entries:
            Coinpaprika.convert_date_in_dict(entry, "time_open")
            Coinpaprika.convert_date_in_dict(entry, "time_close")
        return entries
