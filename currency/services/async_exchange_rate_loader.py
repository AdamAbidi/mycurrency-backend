from currency.models import CurrencyExchangeRate
from provider.adapter_registry import ADAPTER_REGISTRY

import asyncio
from datetime import timedelta
from asgiref.sync import sync_to_async
import logging

logger = logging.getLogger(__name__)

@sync_to_async
def get_existing_rate(source_currency, target_currency, date):
    try:
        return CurrencyExchangeRate.objects.get(
            source_currency=source_currency,
            exchanged_currency=target_currency,
            valuation_date=date
        )
    except CurrencyExchangeRate.DoesNotExist:
        return None


@sync_to_async
def save_rate_in_db(source_currency, target_currency, date, rate):
    return CurrencyExchangeRate.objects.create(
        source_currency=source_currency,
        exchanged_currency=target_currency,
        valuation_date=date,
        rate_value=rate
    )


async def get_exchange_rate_async(source_currency, target_currency, date, providers):
    if source_currency == target_currency:
        return {
            "source_currency": source_currency.code,
            "target_currency": target_currency.code,
            "date": date.isoformat(),
            "rate": 1.0,
        }

    existing = await get_existing_rate(source_currency, target_currency, date)
    if existing:
        return {
            "source_currency": source_currency.code,
            "target_currency": target_currency.code,
            "date": date.isoformat(),
            "rate": float(existing.rate_value),
        }

    for provider in providers:
        logger.info(
            f"Trying provider: {provider.name} ({provider.adapter_key}) for {source_currency.code} to {target_currency.code} on {date}")

        adapter_class = ADAPTER_REGISTRY.get(provider.adapter_key)
        adapter = adapter_class(provider)

        try:
            rate = adapter.get_exchange_rate_data(
                source_currency.code, target_currency.code, date
            )

            await save_rate_in_db(source_currency, target_currency, date, rate)

            return {
                "source_currency": source_currency.code,
                "target_currency": target_currency.code,
                "date": date.isoformat(),
                "rate": float(rate),
            }

        except Exception as e:
            logger.info(f"Provider failed: {e}")
            continue  # try the next provider

    return {
        "source_currency": source_currency.code,
        "target_currency": target_currency.code,
        "date": date.isoformat(),
        "rate": None,
    }


async def get_exchange_rate_single_date_list_async(source_currency, target_list, date, providers):
    tasks = []

    for target_currency in target_list:
        task = get_exchange_rate_async(source_currency, target_currency, date, providers)
        tasks.append(task)

    return await asyncio.gather(*tasks)


async def get_exchange_rate_date_range_async(source_currency, target_list, start_date, end_date, providers):
    result = []
    current_date = start_date

    while current_date <= end_date:
        day_rates = await get_exchange_rate_single_date_list_async(
            source_currency, target_list, current_date, providers
        )
        result.extend(day_rates)
        current_date += timedelta(days=1)

    return result
