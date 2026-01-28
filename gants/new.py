import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd

# Define project tasks and their adjusted timelines for slight overlap
tasks = [
    ("Finalize proprietary workflows", "2025-01-01", "2025-06-30"),
    ("Onboard 2–3 pilot clients (€200K revenue)", "2025-02-01", "2025-06-30"),
    ("Build on existing team expertise", "2025-01-01", "2025-06-30"),
    ("Strategic hires (2 quantum analysts)", "2025-06-01", "2026-06-30"),
    ("ISO 27001 certification", "2025-07-01", "2026-06-30"),
    ("Expand to EU defense contracts (€500K ARR)", "2025-07-01", "2026-06-30"),
    ("Develop hybrid SaaS platform", "2026-06-01", "2027-12-31"),
    ("Automate data ingestion", "2026-07-01", "2027-12-31"),
    ("Preserve expert review in SaaS", "2026-07-01", "2027-12-31"),
    ("International expansion", "2026-08-01", "2027-12-31"),
]

# Convert to DataFrame
df = pd.DataFrame(tasks, columns=["Task", "Start", "End"])
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])
df["Duration"] = df["End"] - df["Start"]

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot tasks
for i, row in df.iterrows():
    ax.barh(y=i, width=row["Duration"].days, left=row["Start"], height=0.6)

# Set labels
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df["Task"])
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.xticks(rotation=45)
plt.title("Gantt Chart: 3-Phase Project Plan")
plt.tight_layout()

# Save as PDF
plt.savefig("gantt_chart_project_plan.pdf")
