import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("traffic_data.csv")

df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
hourly = df.groupby("hour")['vehicle_count'].mean()

plt.plot(hourly.index, hourly.values)
plt.xlabel("Hour of Day")
plt.ylabel("Avg Vehicle Count")
plt.title("Peak Traffic Analysis")
plt.show()
