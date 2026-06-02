import requests


class WorldBankIngestor:

    BASE_URL = "https://api.worldbank.org/v2"

    def fetch_indicator(self, indicator_code):
        url = (
            f"{self.BASE_URL}/country/all/indicator/"
            f"{indicator_code}?format=json&per_page=20000"
        )

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        return response.json()