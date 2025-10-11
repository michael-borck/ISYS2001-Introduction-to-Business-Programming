**Disease Spread Simulation**

**Purpose**

This simulation models the spread of an infectious disease within a population, helping students explore epidemiological concepts and the effectiveness of public health interventions.

**Parameters**

- `start_population`: The initial number of people in the population.
- `days`: The duration of the simulation.
- `infection_rate`: The probability that an individual will contract the disease each day.
- `recovery_rate`: The probability of an infected individual recovering each day.
- `outbreak_day`: Specifies the day on which a major outbreak event occurs (optional).
- `severity`: The magnitude of the outbreak's impact on infection rates, positive for an increase.

**Tasks**

- **Visualization:**
  - Plot the number of susceptible, infected, and recovered individuals over time.
  - Highlight any major outbreak events on the plot if included.

- **Analysis:**
  - Investigate how changes in the infection and recovery rates affect the disease dynamics.
  - Simulate a major outbreak event and analyze its effect on the epidemic curve.
  - (Optional) Model potential public health interventions, such as vaccination or quarantine, and evaluate their impact on the disease spread.

**Example Code**

```python
from simulacra import DiseaseSimulation
import matplotlib.pyplot as plt

# Example setup: High infection rate with a significant recovery rate,
# and a major outbreak event.
sim = DiseaseSimulation(start_population=1000, days=200, infection_rate=0.1, 
                        recovery_rate=0.05, outbreak_day=50, severity=0.25)

susceptible, infected, recovered = sim.run_simulation()

# Visualizing the disease spread
plt.figure(figsize=(10, 6))
plt.plot(susceptible, label='Susceptible')
plt.plot(infected, label='Infected', color='red')
plt.plot(recovered, label='Recovered', color='green')
plt.axvline(x=sim.outbreak_day, color='purple', linestyle='--', label='Major Outbreak')
plt.xlabel('Days')
plt.ylabel('Number of Individuals')
plt.title('Disease Spread Simulation')
plt.legend()
plt.show()
```

**Hints**

- Begin your analysis with baseline parameters before introducing an outbreak to understand the natural progression of the disease.
- Use clear labels and annotations on your plots to indicate significant simulation events, such as the introduction of an outbreak or intervention.
- Consider calculating metrics like peak infection rates, time until peak, and total recovered as part of your analysis to measure the impact of different scenarios.

**Experimentation Reminder:** Use the simulation to test hypotheses about disease spread and control measures. Adjust parameters, introduce interventions, and explore the resulting dynamics to gain insights into effective disease management strategies.
