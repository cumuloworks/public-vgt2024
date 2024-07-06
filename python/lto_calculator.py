import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_data_tb = 200
annual_increase_tb = 40
years = 10
tape_capacity_tb = 20
tape_cost_yen = 10000
drive_cost_yen = 1000000
usd_to_jpy = 150
glacier_cost_per_tb_per_month_usd = 0.00099 * 1000  # Cost in USD converted to TB for 1 month

# Data arrays
data_tb = np.array([initial_data_tb + i * annual_increase_tb for i in range(years)])

# LTO costs
lto_tape_count = np.ceil(data_tb / tape_capacity_tb) * 2  # Two copies
lto_tape_cost_yen = lto_tape_count * tape_cost_yen
lto_cumulative_tape_cost_yen = np.cumsum(lto_tape_cost_yen)  # Cumulative tape costs
lto_total_cost_yen = lto_cumulative_tape_cost_yen + drive_cost_yen  # Include drive cost in the first year

# Glacier costs
glacier_cost_per_year_usd = data_tb * glacier_cost_per_tb_per_month_usd * 12
glacier_total_cost_usd = np.cumsum(glacier_cost_per_year_usd)
glacier_total_cost_yen = glacier_total_cost_usd * usd_to_jpy

# Plotting the results
# plt.figure(figsize=(12, 6))
plt.plot(range(1, years + 1), lto_total_cost_yen / 1e6, label="LTO (Million JPY)")
plt.plot(range(1, years + 1), glacier_total_cost_yen / 1e6, label="Glacier (Million JPY)")
plt.xlabel("Years")
plt.ylabel("Total Cost (Million JPY)")
plt.title("Cost: LTO vs Amazon Glacier Deep Archive")
plt.legend()
plt.grid(True)
plt.show()
