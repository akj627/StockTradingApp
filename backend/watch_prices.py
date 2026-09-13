import time

from app.simulated_price_provider import SimulatedPriceProvider

provider = SimulatedPriceProvider()

while True:
    provider.tick()
    for stock in provider.get_all():
        print(f"{stock.symbol:6} ${stock.price:.2f}")
    print("---")
    time.sleep(1)
