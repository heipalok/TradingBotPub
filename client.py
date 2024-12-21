from includes import *
import ccxt

def initialize_client(api_key, api_secret):
    """Alustaa Binance API -asiakkaan."""
    client = ccxt.binanceusdm({
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': True
    })
    print("Binance client initialized.")
    return client
