from fastapi import FastAPI

from app import config

app = FastAPI()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "price_provider": config.PRICE_PROVIDER,
        "auth_provider": config.AUTH_PROVIDER,
    }
