from .adapters.currencybeacon import CurrencyBeaconAdapter
from .adapters.exchangerates import ExchangeRateAdapter
from .adapters.mockexchangerate import MockExchangeRateAdapter

ADAPTER_REGISTRY = {
    "mockExchangeRate": MockExchangeRateAdapter,
    "currencybeacon": CurrencyBeaconAdapter,
    "exchangerates": ExchangeRateAdapter
}