from typing import List, Dict

from .Coinpaprika import Coinpaprika


class CoinpaprikaTags():

    def __call__(self, *additional_fields: str) -> List[Dict]:
        """
        List tags
        :param additional_fields: List of additional fields to include in query result for each tag.
                                  Currently supported values are: "coins" and "icos".
        :return: [
                  {
                    "id": "blockchain-service",
                    "name": "Blockchain Service",
                    "coin_counter": 160,
                    "ico_counter": 80,
                    "description": "A solution for companies wanting to build, host and use their own blockchain apps, smart contracts and functions on the blockchain.",
                    "type": "functional",
                    "coins": [
                      "dcr-decred",
                      "hc-hypercash",
                      "nxs-nexus"
                    ],
                    "icos": [
                      "kodakcoin-kodakone",
                      "acad-academy"
                    ]
                  }
                ]
        """
        return self.all(*additional_fields)

    @staticmethod
    def all(*additional_fields) -> List[Dict]:
        """
        List tags
        :param additional_fields: List of additional fields to include in query result for each tag.
                                  Currently supported values are: "coins" and "icos".
        :return: [
                  {
                    "id": "blockchain-service",
                    "name": "Blockchain Service",
                    "coin_counter": 160,
                    "ico_counter": 80,
                    "description": "A solution for companies wanting to build, host and use their own blockchain apps, smart contracts and functions on the blockchain.",
                    "type": "functional",
                    "coins": [
                      "dcr-decred",
                      "hc-hypercash",
                      "nxs-nexus"
                    ],
                    "icos": [
                      "kodakcoin-kodakone",
                      "acad-academy"
                    ]
                  }
                ]
        """
        additional_fields_str = ",".join(additional_fields)
        return Coinpaprika.get("/tags", params={"additional_fields": additional_fields_str})

    @staticmethod
    def with_id(tag_id, *additional_fields: str) -> Dict:
        """
        Get tag by ID
        :param additional_fields: List of additional fields to include in query result for each tag.
                                  Currently supported values are: "coins" and "icos".
        :return: {
                  "id": "blockchain-service",
                  "name": "Blockchain Service",
                  "coin_counter": 160,
                  "ico_counter": 80,
                  "description": "A solution for companies wanting to build, host and use their own blockchain apps, smart contracts and functions on the blockchain.",
                  "type": "functional",
                  "coins": [
                    "dcr-decred",
                    "hc-hypercash",
                    "nxs-nexus"
                  ],
                  "icos": [
                    "kodakcoin-kodakone",
                    "acad-academy"
                  ]
                }
        """
        additional_fields_str = ",".join(additional_fields)
        return Coinpaprika.get(f"/tags/{tag_id}", params={"additional_fields": additional_fields_str})
