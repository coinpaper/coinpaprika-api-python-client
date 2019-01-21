from .Coinpaprika import Coinpaprika


class CoinpaprikaTags():

    def __call__(self, *additional_fields):
        return self.all(*additional_fields)

    @staticmethod
    def all(*additional_fields):
        additional_fields_str = ",".join(additional_fields)
        return Coinpaprika.get("/tags", params={"additional_fields": additional_fields_str})

    def with_id(tag_id, *additional_fields):
        additional_fields_str = ",".join(additional_fields)
        return Coinpaprika.get(f"/tags/{tag_id}", params={"additional_fields": additional_fields_str})
