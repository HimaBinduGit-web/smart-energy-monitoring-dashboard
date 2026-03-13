import pandas as pd
import random

data = []

for i in range(100):
    voltage = random.randint(210, 250)
    current = random.uniform(0.5, 5.0)
    power = voltage * current
    
    data.append([voltage, current, power])

df = pd.DataFrame(data, columns=["Voltage", "Current", "Power"])
df.to_csv("energy_data.csv", index=False)

print("energy_data.csv created")
