from includes import *
import matplotlib.pyplot as plt

def plot_decision_chart():
    """Visualisoi päätökset ja indikaattorit."""
    # Esimerkki: yksinkertainen kaavio
    prices = [1, 2, 3, 4, 5]
    decisions = [1, 0, 1, 0, 1]  # Esim. 1=BUY, 0=SELL
    plt.plot(prices, label="Price")
    plt.scatter(range(len(decisions)), prices, c=decisions, cmap="coolwarm", label="Decisions")
    plt.legend()
    plt.title("Decision Chart")
    plt.show()
