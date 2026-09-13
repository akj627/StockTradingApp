from app import config
from app.price_provider import PriceProvider
from app.simulated_price_provider import SimulatedPriceProvider


def create_price_provider() -> PriceProvider:
    if config.PRICE_PROVIDER == "simulated":
        return SimulatedPriceProvider()
    raise ValueError(f"Unknown PRICE_PROVIDER: {config.PRICE_PROVIDER}")
