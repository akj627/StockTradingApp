import random

from app.price_provider import PriceProvider
from app.models import Stock
from app.tickers import SEED_STOCKS


class SimulatedPriceProvider(PriceProvider):
    """Starts from the seeded prices and nudges each one by a small random
    percentage every tick, so prices drift realistically instead of jumping
    around."""

    def __init__(self, max_move_pct: float = 0.005):
        self._stocks = {symbol: stock.model_copy() for symbol, stock in SEED_STOCKS.items()}
        self._max_move_pct = max_move_pct

    def get_all(self) -> list[Stock]:
        return list(self._stocks.values())

    def tick(self) -> None:
        for stock in self._stocks.values():
            change_pct = random.uniform(-self._max_move_pct, self._max_move_pct)
            stock.price = round(stock.price * (1 + change_pct), 2)
