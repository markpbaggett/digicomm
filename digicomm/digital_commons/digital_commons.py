import requests
from typing import Literal, Tuple

class DigitalCommons:
    def __init__(self, site_url: str, key: str):
        self.site_url = site_url.replace('http://', '').replace('https://', '')
        self.headers = {"Authorization": key}

    def __request(self, url: str):
        r = requests.get(
            url=url,
            headers=self.headers,
        )
        return r.json()

    def get_indexed_fields(self, field_type: Literal['all', 'default'] = 'all'):
        return self.__request(
            f'https://content-out.bepress.com/v2/{self.site_url}/fields?field_type={field_type}'
        )

    def query(
            self,
            query: Tuple[Tuple[str, str], ...],
    ):
        query_params = '&'.join(f"{key}={value}" for key, value in query)
        return self.__request(
            f'https://content-out.bepress.com/v2/{self.site_url}/query?{query_params}'
        )
