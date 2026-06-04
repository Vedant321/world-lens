import requests


class WorldBankIngestor:

    BASE_URL = "https://api.worldbank.org/v2"

    def fetch_indicator(
        self,
        indicator_code,
        start_year,
        end_year
    ):
        url = (
            f"{self.BASE_URL}/country/all/indicator/"
            f"{indicator_code}"
            f"?format=json"
            f"&per_page=20000"
            f"&date={start_year}:{end_year}"
        )

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        return response.json()