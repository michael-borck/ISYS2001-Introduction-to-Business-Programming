def plot_demand(demand: List[int], promotion_day: Optional[int] = None) -> None:
    """
    Plots the demand simulation data with an optional marker for a marketing campaign.

    Parameters:
        demand (List[int]): A list of demand values to plot.
        promotion_day (Optional[int]): The day a marketing campaign starts, marked on the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(demand, label='Product Demand')
    if promotion_day is not None:
        plt.axvline(x=promotion_day, color='blue', linestyle='--', label='Marketing Campaign Start')
    plt.xlabel('Days')
    plt.ylabel('Demand Units')
    plt.title('Product Popularity Simulation')
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    sim = ProductPopularitySimulation(start_demand=500, days=180, growth_rate=0.02,
                                      marketing_impact=0.1, promotion_day=30, promotion_effectiveness=0.5)
    demand = sim.run_simulation()
    plot_demand(demand, sim.promotion_day)
