from abc import ABC, abstractmethod

from app.models import Stock


class PriceProvider(ABC):
    """Anything that can report stock prices and advance them over time.

    SimulatedPriceProvider implements this now; a future LivePriceProvider
    (pulling from a real market data feed) would implement the same
    interface, so the rest of the app never needs to know which one it's
    talking to.
    """

    @abstractmethod
    def get_all(self) -> list[Stock]:
        ...

    @abstractmethod
    def tick(self) -> None:
        ...
