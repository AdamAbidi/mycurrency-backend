import random
from .base import BaseProviderAdapter

class MockExchangeRateAdapter(BaseProviderAdapter):
    def get_exchange_rate_data(self, source_currency, exchanged_currency, valuation_date):
        # Return a random float between 0.5 and 1.5
        return round(random.uniform(0.5, 1.5), 4)