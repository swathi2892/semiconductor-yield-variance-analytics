import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/wafer_production_yield.csv")

# Set visualization style
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Chart 1: Seaborn Barplot - Revenue Variance by Production Lot
sns.barplot(
    data=df, 
    x="lot_id", 
    y="revenue_variance_usd", 
    palette="vlag", 
    ax=axes[0]
)
axes[0].set_title("Financial Revenue Variance ($USD) by Wafer Lot", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Wafer Production Lot", fontsize=10)
axes[0].set_ylabel("Revenue Variance ($USD)", fontsize=10)
axes[0].tick_params(axis='x', rotation=45)

# Chart 2: Matplotlib Scatter Plot - Actual vs Target Yield %
sns.scatterplot(
    data=df, 
    x="target_yield_pct", 
    y="actual_yield_pct", 
    hue="yield_variance_pct", 
    size="wafer_count", 
    palette="coolwarm", 
    sizes=(50, 200),
    ax=axes[1]
)
axes[1].plot([80, 100], [80, 100], 'r--', label="Target Baseline")
axes[1].set_title("Actual vs. Target Yield (%) Performance", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Target Yield (%)", fontsize=10)
axes[1].set_ylabel("Actual Yield (%)", fontsize=10)
axes[1].legend(loc="upper left")

plt.tight_layout()
plt.savefig("reports/yield_variance_dashboard.png", dpi=300)
print("✅ Visualization dashboard successfully generated at reports/yield_variance_dashboard.png")
