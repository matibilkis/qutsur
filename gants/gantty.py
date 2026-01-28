import plotly.express as px
import pandas as pd
from datetime import datetime

# Data Preparation
phases = [
    {"Task": "Foundation", "Start": "2024-01-01", "Finish": "2024-06-30", "Resource": "Phase", "Color": "#4E79A7"},
    {"Task": "Finalize workflows", "Start": "2024-01-01", "Finish": "2024-03-31", "Resource": "Task", "Color": "#4E79A7"},
    {"Task": "Develop MVP", "Start": "2024-04-01", "Finish": "2024-06-30", "Resource": "Task", "Color": "#4E79A7"},
    {"Task": "Scaling", "Start": "2024-07-01", "Finish": "2025-06-30", "Resource": "Phase", "Color": "#59A14F"},
    {"Task": "Hire analysts", "Start": "2024-07-01", "Finish": "2024-09-30", "Resource": "Task", "Color": "#59A14F"},
    {"Task": "Secure contracts", "Start": "2024-10-01", "Finish": "2025-06-30", "Resource": "Task", "Color": "#59A14F"},
    {"Task": "Industrialization", "Start": "2025-07-01", "Finish": "2026-12-31", "Resource": "Phase", "Color": "#F28E2B"},
    {"Task": "Automate pipelines", "Start": "2025-07-01", "Finish": "2025-12-31", "Resource": "Task", "Color": "#F28E2B"},
    {"Task": "Global expansion", "Start": "2026-01-01", "Finish": "2026-12-31", "Resource": "Task", "Color": "#F28E2B"}
]

milestones = [
    {"Task": "Pilot clients", "Date": "2026-03-30", "Color": "#E15759"},
    {"Task": "ISO Cert", "Date": "2024-12-31", "Color": "#E15759"},
    {"Task": "EU Contract", "Date": "2025-06-30", "Color": "#E15759"},
    {"Task": "SaaS Launch", "Date": "2025-12-31", "Color": "#E15759"}
]

# Create DataFrame
df = pd.DataFrame(phases)
df_milestones = pd.DataFrame(milestones)
df_milestones["Date"] = pd.to_datetime(df_milestones["Date"])

# Generate Gantt Chart
fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Task",
    color="Color",
    color_discrete_map={c: c for c in df["Color"].unique()},
    title="Quantum Tech Spin-Off Development Plan"
)

# Add milestones
fig.add_scatter(
    x=df_milestones["Date"],
    y=[df["Task"].iloc[-1]] * len(df_milestones),  # Position at bottom
    mode="markers+text",
    marker=dict(size=12, color=df_milestones["Color"]),
    text=df_milestones["Task"],
    textposition="top center",
    name="Milestones"
)

# Customize layout
fig.update_layout(
    height=500,
    showlegend=False,
    hovermode="closest",
    plot_bgcolor="white",
    xaxis_title="Timeline",
    yaxis_title="Phase/Task"
)

# Save as interactive HTML
fig.write_html("quantum_gantt.html")
print("Chart saved to quantum_gantt.html - open in any browser!")
