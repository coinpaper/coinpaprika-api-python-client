from .Coinpaprika import Coinpaprika


class CoinpaprikaPeople:

    @staticmethod
    def with_id(person_id):
        return Coinpaprika.get(f"/people/{person_id}")
