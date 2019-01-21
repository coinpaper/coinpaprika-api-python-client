from .Coinpaprika import Coinpaprika


class CoinpaprikaExchanges:

    def __call__(self, quotes=tuple(["USD"])):
        return self.all(quotes)

    @staticmethod
    def all(quotes=tuple(["USD"])):
        quotes_str = ",".join(quotes)
        exchanges = Coinpaprika.get(f"/exchanges", params={"quotes": quotes_str})
        for exchange in exchanges:
            Coinpaprika.convert_date_in_dict(exchange, "last_updated")
        return exchanges

    @staticmethod
    def exchange(exchange_id, quotes=tuple(["USD"])):
        quotes_str = ",".join(quotes)
        exchange = Coinpaprika.get(f"/exchanges/{exchange_id}", params={"quotes": quotes_str})
        Coinpaprika.convert_date_in_dict(exchange, "last_updated")
        return exchange

    @staticmethod
    def exchange_markets(exchange_id, quotes=tuple(["USD"])):
        quotes_str = ",".join(quotes)
        market_pairs = Coinpaprika.get(f"/exchanges/{exchange_id}/markets", params={"quotes": quotes_str})
        for market_pair in market_pairs:
            Coinpaprika.convert_date_in_dict(market_pair, "last_updated")
        return market_pairs