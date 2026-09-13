import asyncio
import json

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from app import config
from app.models import Stock
from app.price_provider_factory import create_price_provider

app = FastAPI()
price_provider = create_price_provider()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "price_provider": config.PRICE_PROVIDER,
        "auth_provider": config.AUTH_PROVIDER,
    }


@app.get("/stocks")
def get_stocks() -> list[Stock]:
    return price_provider.get_all()


async def _price_events():
    while True:
        price_provider.tick()
        payload = [stock.model_dump() for stock in price_provider.get_all()]
        yield f"data: {json.dumps(payload)}\n\n"
        await asyncio.sleep(1)


@app.get("/stream/prices")
async def stream_prices():
    return StreamingResponse(_price_events(), media_type="text/event-stream")
