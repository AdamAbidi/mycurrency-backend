import requests
from .base import BaseProviderAdapter

class CurrencyBeaconAdapter(BaseProviderAdapter):
    def get_exchange_rate_data(self, source_currency, exchanged_currency, date):
        url = f"{self.provider.api_url}/historical"
        params = {
            "api_key": self.api_key,
            "base": source_currency,
            "symbols": exchanged_currency,
            "date": date.strftime('%Y-%m-%d')
        }

        response = requests.get(url, params=params)

        data = response.json()

        if response.status_code == 200 and "rates" in data:
            return data["rates"].get(exchanged_currency)
        else:
            raise Exception(f"CurrencyBeacon error: {data}")