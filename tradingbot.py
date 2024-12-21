from includes import *
from tradinglogic import start_trading
from decissionchart import plot_decision_chart

if __name__ == "__main__":
    print("TradingBot is starting...")
    # Esimerkkitoiminto: Aloitetaan kaupankäynti
    start_trading()
    # Esimerkkitoiminto: Näytetään päätöskaavio
    plot_decision_chart()

