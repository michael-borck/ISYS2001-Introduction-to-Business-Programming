def plot_prices(prices: List[float], event_day: Optional[int] = None) -> None:
    """
    Plots the stock prices from a simulation with an optional vertical line marking a major market event.

    Parameters:
        prices (List[float]): A list of stock prices to be plotted.
        event_day (Optional[int]): The day on which the major market event occurs (defaults to None).

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(prices, label='Stock Price')
    if event_day is not None:
        plt.axvline(x=event_day, color='red', linestyle='--', label='Major Market Event')
    plt.xlabel('Days')
    plt.ylabel('Price ($)')
    plt.title('Stock Market Simulation')
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    sim = StockMarketSimulation(start_price=100, days=365, volatility=0.03, 
                                drift=-0.001, event_day=100, event_impact=-0.2)
    prices = sim.run_simulation()
    plot_prices(prices, sim.event_day)