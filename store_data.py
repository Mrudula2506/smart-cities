import sqlite3
import pandas as pd

df = pd.read_csv("traffic_data.csv")

conn = sqlite3.connect("smartcity.db")
df.to_sql("traffic", conn, if_exists="replace", index=False)

print("Data stored in SQLite database smartcity.db")
