from includes import *
from datetime import datetime

def log(message):
    """Tulostaa viestin aikaleimalla."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
