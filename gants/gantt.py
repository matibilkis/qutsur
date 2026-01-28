import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np

# Data Setup
phases = {
    "Phase 1: Foundation": {
        "start": "2024-01-01",
        "end": "2024-06-30",
        "tasks": {
            "Finalize workflows": ("2024-01-01", "2024-03-31"),
            "Develop MVP dashboard": ("2024-04-01", "2024-06-30")
        },
        "color": "#4E79A7"
    },
    "Phase 2: Scaling": {
        "start": "2024-07-01",
        "end": "2025-06-30",
        "tasks": {
            "Hire quantum analysts": ("2024-07-01", "2024-09-30"),
            "Secure EU defense contracts": ("2024-10-01", "2025-06-30")
        },
        "color": "#59A14F"
    },
    "Phase 3: Industrialization": {
        "start": "2025-07-01",
        "end": "2026-12-31",
        "tasks": {
            "Automate data pipelines": ("2025-07-01", "2025-12-31"),
            "International expansion": ("2026-01-01", "2026-12-31")
        },
        "color": "#F28E2B"
    }
}

milestones = [
    ("Pilot clients onboarded", "2024-06-30"),
    ("ISO 27001 certification", "2024-12-31"),
    ("EU defense contract", "2025-06-30"),
    ("SaaS MVP launch", "2025-12-31")
]

# Convert dates
def str_to_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plot phases
for i, (phase_name, phase_data) in enumerate(phases.items()):
    phase_start = str_to_date(phase_data["start"])
    phase_end = str_to_date(phase_data["end"])

    # Main phase bar
    ax.barh(phase_name,
            width=(phase_end - phase_start).days,
            left=phase_start,
            color=phase_data["color"],
            alpha=0.6,
            edgecolor='black')

    # Tasks
    for task_name, (task_start, task_end) in phase_data["tasks"].items():
        start = str_to_date(task_start)
        end = str_to_date(task_end)
        ax.barh(phase_name,
                width=(end - start).days,
                left=start,
                color=phase_data["color"],
                alpha=1.0,
                height=0.3,
                edgecolor='black')
        ax.text(start + (end - start)/2, i, task_name,
                ha='center', va='center', color='white', fontsize=9)

# Add milestones
for milestone, date in milestones:
    mdate = str_to_date(date)
    ax.plot(mdate, 2.5, 'D', markersize=10, color='red')
    ax.text(mdate, 2.7, milestone, ha='center', va='bottom', fontsize=9)

# Formatting
ax.set_xlim(str_to_date("2024-01-01"), str_to_date("2027-01-31"))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b '%y"))
plt.xticks(rotation=45)
plt.ylabel("Development Phases")
plt.title("Quantum Surveillance Spin-Off Development Plan", pad=20)

# Add legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#4E79A7', label='Foundation'),
    Patch(facecolor='#59A14F', label='Scaling'),
    Patch(facecolor='#F28E2B', label='Industrialization'),
    plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='red', markersize=10, label='Milestones')
]
ax.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()
plt.grid(axis='x', alpha=0.3)
plt.savefig('quantum_gantt.png', dpi=300, bbox_inches='tight')
plt.show()
