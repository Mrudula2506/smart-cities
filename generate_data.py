import random
import pandas as pd
from datetime import datetime, timedelta

data = []
start = datetime.now()

for i in range(10000):
    timestamp = start + timedelta(seconds=i*10)
    record = {
        "junction_id": random.randint(1, 10),
        "vehicle_count": random.randint(20, 200),
        "avg_speed": random.uniform(20, 80),
        "pollution_level": random.uniform(30, 150),
        "timestamp": timestamp
    }
    data.append(record)

df = pd.DataFrame(data)
df.to_csv("traffic_data.csv", index=False)

print("Dataset created successfully! File saved as traffic_data.csv")
