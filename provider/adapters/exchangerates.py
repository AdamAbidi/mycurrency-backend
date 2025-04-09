import requests
from .base import BaseProviderAdapter

class ExchangeRateAdapter(BaseProviderAdapter):
    def get_exchange_rate_data(self, source_currency, exchanged_currency, valuation_date):
        url = f"{self.provider.api_url}/{valuation_date.strftime('%Y-%m-%d')}"
        params = {
            "access_key": self.api_key,
            "base": source_currency,
            "symbols": exchanged_currency,
        }

        response = requests.get(url, params=params)

        data = response.json()

        if response.status_code == 200 and "rates" in data:
            return data["rates"].get(exchanged_currency)
        else:
            raise Exception(f"ExchangeRate error: {data}")