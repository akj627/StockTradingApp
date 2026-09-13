from fastapi import FastAPI

from app import config
from app.models import Stock
from app.tickers import list_stocks

app = FastAPI()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "price_provider": config.PRICE_PROVIDER,
        "auth_provider": config.AUTH_PROVIDER,
    }


@app.get("/stocks")
def get_stocks() -> list[Stock]:
    return list_stocks()
