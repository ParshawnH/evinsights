import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

current_year = datetime.now().year
end_year = current_year + 15
years = list(range(current_year, end_year + 1))

baseline_EVs = 177
baseline_non_EVs = 1500
total_current_vehicles = baseline_EVs + baseline_non_EVs

fleet_growth_rate = 0.03
conservative_rate = 0.25
realistic_rate = 0.38
optimistic_rate = 0.50

projections = []

for i, year in enumerate(years):
    projected_fleet = round(total_current_vehicles * (1 + fleet_growth_rate) ** i)
    conservative_EVs = round(baseline_EVs + (projected_fleet - total_current_vehicles) * conservative_rate * (1 + i / 10))
    realistic_EVs = round(baseline_EVs + (projected_fleet - total_current_vehicles) * realistic_rate * (1 + i / 8))
    optimistic_EVs = round(baseline_EVs + (projected_fleet - total_current_vehicles) * optimistic_rate * (1 + i / 5))
    projections.append({
        'Year': year,
        'Conservative': conservative_EVs,
        'Realistic': realistic_EVs,
        'Optimistic': optimistic_EVs
    })

df = pd.DataFrame(projections)

plt.figure(figsize=(12, 6))
plt.plot(df['Year'], df['Conservative'], label='Conservative (25%)', color='#64748b', linewidth=2)
plt.plot(df['Year'], df['Realistic'], label='Realistic (38%)', color='#0ea5e9', linewidth=2)
plt.plot(df['Year'], df['Optimistic'], label=f'Optimistic ({int(optimistic_rate * 100)}%)', color='#10b981', linewidth=2)
plt.title('Electric Vehicle Projection to {}'.format(end_year))
plt.xlabel('Year')
plt.ylabel('Projected EVs')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
