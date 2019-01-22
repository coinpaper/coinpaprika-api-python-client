from typing import Dict

from .Coinpaprika import Coinpaprika
from .CoinpaprikaCoin import CoinpaprikaCoin
from .CoinpaprikaPeople import CoinpaprikaPeople
from .CoinpaprikaTags import CoinpaprikaTags
from .CoinpaprikaTickers import CoinpaprikaTickers
from .CoinpaprikaExchanges import CoinpaprikaExchanges


class Client():
    """
    Coinpaprika API delivers free & frequently updated market data from the
    world of crypto: coin prices, volumes, market caps, ATHs, return rates and more.
    """

    def __init__(self):
        self.coins = CoinpaprikaCoin()
        self.people = CoinpaprikaPeople()
        self.tags = CoinpaprikaTags()
        self.tickers = CoinpaprikaTickers()
        self.exchanges = CoinpaprikaExchanges()

    def global_market_overview(self) -> Dict:
        """
        Get market overview data
        :return: {
                    "market_cap_usd": 430252937008,
                    "volume_24h_usd": 430252937008,
                    "bitcoin_dominance_percentage": 36.67,
                    "cryptocurrencies_number": 1587,
                    "market_cap_ath_value": 835692000000,
                    "market_cap_ath_date": "2018-01-07T11:17:00Z",
                    "volume_24h_ath_value": 71990500000,
                    "volume_24h_ath_date": "2018-01-04T17:17:00Z",
                    "market_cap_change_24h": 1.98,
                    "volume_24h_change_24h": 1.98,
                    "last_updated": 1525089441
                 }
        """
        return Coinpaprika.get("/global")


