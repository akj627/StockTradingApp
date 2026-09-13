from app.models import Stock

# Manually seeded with approximate real-world prices as a starting point.
# Step 3 will make these move over time; a later "live" provider can
# replace this file entirely without changing anything else in the app.
SEED_STOCKS = {
    "AAPL": Stock(symbol="AAPL", name="Apple Inc.", price=230.00),
    "MSFT": Stock(symbol="MSFT", name="Microsoft Corp.", price=430.00),
    "GOOGL": Stock(symbol="GOOGL", name="Alphabet Inc.", price=175.00),
    "AMZN": Stock(symbol="AMZN", name="Amazon.com Inc.", price=185.00),
    "TSLA": Stock(symbol="TSLA", name="Tesla Inc.", price=250.00),
    "NVDA": Stock(symbol="NVDA", name="NVIDIA Corp.", price=130.00),
    "META": Stock(symbol="META", name="Meta Platforms Inc.", price=580.00),
    "NFLX": Stock(symbol="NFLX", name="Netflix Inc.", price=700.00),
    "JPM": Stock(symbol="JPM", name="JPMorgan Chase & Co.", price=215.00),
    "DIS": Stock(symbol="DIS", name="Walt Disney Co.", price=95.00),
}


def list_stocks() -> list[Stock]:
    return list(SEED_STOCKS.values())
