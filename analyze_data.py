import pandas as pd

df = pd.read_csv("traffic_data.csv")

# Congestion rule: more vehicles + low speed
df['congested'] = df.apply(
    lambda x: 1 if x.vehicle_count > 150 and x.avg_speed < 30 else 0, axis=1
)

# Junction-wise congestion count
congestion_summary = df.groupby("junction_id")['congested'].sum()

print("Junction-wise Congestion Summary:")
print(congestion_summary)

# Peak hours
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
hourly = df.groupby("hour")['vehicle_count'].mean()

print("\nAverage Vehicle Count Per Hour:")
print(hourly)
