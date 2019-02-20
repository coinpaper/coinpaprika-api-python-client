from urllib.parse import urlencode
from datetime import datetime
import time

import requests


requests_session = requests.Session()
requests_session.headers.update({
    'Accept': 'application/json',
    'User-Agent': 'coinpaper/coinpaper-api-client-python'
})


class Coinpaprika:

    API_URL = "https://api.coinpaprika.com/v1"
    session = requests_session

    _max_requests_per_second = 5 # Official limit is 10, but we keep it safe here
    _sent_request_timestamps = []

    @staticmethod
    def limit_rate():
        if len(Coinpaprika._sent_request_timestamps) > Coinpaprika._max_requests_per_second:
            time_difference = datetime.now().timestamp() - Coinpaprika._sent_request_timestamps[-Coinpaprika._max_requests_per_second]
            time_to_wait = max(1 - time_difference, 0)
            time.sleep(time_to_wait)
        Coinpaprika._sent_request_timestamps.append(datetime.now().timestamp())

    @staticmethod
    def get(endpoint, params=None):
        query_params = params if params else {}
        query_string = urlencode(query_params)
        request_url = f"{Coinpaprika.API_URL}{endpoint}?{query_string}"
        Coinpaprika.limit_rate()
        response = Coinpaprika.session.get(request_url)
        if not 200 <= response.status_code < 300:
            raise CoinpaprikaError(response, request_url)
        return response.json()

    @staticmethod
    def convert_date(date):
        if not date:
            return
        return datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')

    @staticmethod
    def convert_date_in_dict(dictionary, path_to_date):
        if "." in path_to_date:
            dict_key = path_to_date[:path_to_date.index(".")]
            stripped_path = path_to_date[path_to_date.index(".")+1:]
            reduced_dict = dictionary[dict_key]
            return Coinpaprika.convert_date_in_dict(reduced_dict, stripped_path)
        dictionary[path_to_date] = Coinpaprika.convert_date(dictionary[path_to_date])
        return


class CoinpaprikaError(BaseException):

    def __init__(self, response, request_url):
        self.status_code = 0
        self.request_url = request_url
        self.message = ""

        try:
            json_response = response.json()
        except ValueError:
            self.message = response.text
        else:
            self.message = json_response["error"]

        self.status_code = response.status_code
        self.response = response
        self.request = getattr(response, 'request', None)

    def __str__(self):
        return f"CoinpaprikaAPIException<status_code={self.status_code} message='{self.message}' url='{self.request_url}'>"

