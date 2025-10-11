def plot_prices(prices: List[float], supply_disruption_day: Optional[int] = None) -> None:
    """
    Plots the prices from a simulation with an optional vertical line marking a supply disruption.

    Parameters:
        prices (List[float]): A list of prices to be plotted.
        supply_disruption_day (Optional[int]): The day on which the supply disruption occurs (defaults to None).

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(prices, label='Resource Price')
    if supply_disruption_day is not None:
        plt.axvline(x=supply_disruption_day, color='r', linestyle='--', label='Supply Disruption')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.title('Resource Price Simulation')
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    sim = ResourceSimulation(start_price=100, days=250, volatility=0.015,
                             drift=0.0003, supply_disruption_day=100, disruption_severity=0.3)
    prices = sim.run_simulation()
    plot_prices(prices, sim.supply_disruption_day)
