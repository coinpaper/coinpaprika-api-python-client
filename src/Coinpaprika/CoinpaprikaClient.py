import requests

from .Coinpaprika import Coinpaprika
from .CoinpaprikaCoin import CoinpaprikaCoin
from .CoinpaprikaPeople import CoinpaprikaPeople
from .CoinpaprikaTags import CoinpaprikaTags
from .CoinpaprikaTickers import CoinpaprikaTickers
from .CoinpaprikaExchanges import CoinpaprikaExchanges


class CoinpaprikaClient():

    def __init__(self):
        self.coins = CoinpaprikaCoin()
        self.people = CoinpaprikaPeople()
        self.tags = CoinpaprikaTags()
        self.tickers = CoinpaprikaTickers()
        self.exchanges = CoinpaprikaExchanges()


    def global_market_overview(self):
        return Coinpaprika.get("/global")


