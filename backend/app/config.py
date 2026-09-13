import os

from dotenv import load_dotenv

load_dotenv()

PRICE_PROVIDER = os.getenv("PRICE_PROVIDER", "simulated")
AUTH_PROVIDER = os.getenv("AUTH_PROVIDER", "username")
