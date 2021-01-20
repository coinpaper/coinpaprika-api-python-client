from typing import Dict

from .Coinpaprika import Coinpaprika


class CoinpaprikaPeople:

    @staticmethod
    def with_id(person_id: str) -> Dict:
        """
        Get people by ID
        :param person_id: Example: vitalik-buterin
        :return: {
                  "id": "vitalik-buterin",
                  "name": "Vitalik Buterin",
                  "description": "Vitalik is the creator of Ethereum. He first discovered blockchain and cryptocurrency technologies through Bitcoin in 2011, and was immediately excited by the technology and its potential. He cofounded Bitcoin Magazine in September 2011, and after two and a half years looking at what the existing blockchain technology and applications had to offer, wrote the Ethereum white paper in November 2013. He now leads Ethereum's research team, working on future versions of the Ethereum protocol.",
                  "teams_count": 5,
                  "links": {
                    "github": [
                      {
                        "url": "http://example.com",
                        "followers": 6448
                      }
                    ],
                    "linkedin": [
                      {
                        "url": "http://example.com",
                        "followers": 6448
                      }
                    ],
                    "medium": [
                      {
                        "url": "http://example.com",
                        "followers": 6448
                      }
                    ],
                    "twitter": [
                      {
                        "url": "http://example.com",
                        "followers": 6448
                      }
                    ],
                    "additional": [
                      {
                        "url": "http://example.com",
                        "followers": 6448
                      }
                    ]
                  },
                  "positions": [
                    {
                      "coin_id": "eth-ethereum",
                      "coin_name": "Ethereum",
                      "position": "Author"
                    }
                  ]
                }
        """
        return Coinpaprika.get(f"/people/{person_id}")
