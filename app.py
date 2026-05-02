import streamlit as st
import pandas as pd
import plotly.express as px
import subprocess

st.set_page_config(layout="wide")
st.title("Smart City Big Data Dashboard")
st.write("Analyze Traffic Data — Congestion, Peak Hours, and Flow Patterns")

# Load CSV
def load_data():
    return pd.read_csv("traffic_data.csv")

# --- UI Sections ---
st.sidebar.header("Choose Action")
choice = st.sidebar.radio(
    "Select Operation:",
    ["View Raw Data", "Analyze Congestion", "Peak Hour Analysis", "Visualize Charts"]
)

# ---- VIEW RAW DATA ----
if choice == "View Raw Data":
    st.header("Raw Traffic Data")
    df = load_data()
    st.dataframe(df)

# ---- ANALYZE CONGESTION ----
elif choice == "Analyze Congestion":

    st.header("Junction-wise Congestion Analysis")

    df = load_data()

    # Congestion rule
    df['congested'] = df.apply(lambda x: 1 if x.vehicle_count > 150 and x.avg_speed < 30 else 0, axis=1)

    # Summary
    summary = df.groupby("junction_id")['congested'].sum()
    st.subheader("Congestion Summary (Total Congested Events per Junction)")
    st.write(summary)

    fig = px.bar(summary, title="Junction Congestion Count")
    st.plotly_chart(fig, use_container_width=True)

# ---- PEAK HOUR ANALYSIS ----
elif choice == "Peak Hour Analysis":

    st.header("Average Traffic During Each Hour")

    df = load_data()
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour

    hourly = df.groupby("hour")['vehicle_count'].mean()

    st.subheader("Average Vehicle Count Per Hour")
    st.write(hourly)

    fig = px.line(hourly, title="Hourly Average Traffic")
    st.plotly_chart(fig, use_container_width=True)

# ---- VISUALIZATION ----
elif choice == "Visualize Charts":

    st.header("Traffic Visualizations")

    df = load_data()

    fig1 = px.line(df, x="timestamp", y="vehicle_count", title="Traffic Flow Over Time")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.scatter(df, x="vehicle_count", y="avg_speed",
    title="Vehicle Count vs Speed (Congestion Pattern)")
    st.plotly_chart(fig2, use_container_width=True)
