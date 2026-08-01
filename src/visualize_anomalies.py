import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load production dataset
df = pd.read_csv("data/wafer_production_yield.csv")

# Generate correlation heatmap using Seaborn
plt.figure(figsize=(8, 6))
numeric_df = df[["wafer_count", "target_yield_pct", "actual_yield_pct", "yield_variance_pct", "revenue_variance_usd"]]
correlation_matrix = numeric_df.corr()

sns.heatmap(
    correlation_matrix, 
    annot=True, 
    cmap="Blues", 
    fmt=".2f", 
    linewidths=0.5
)

plt.title("AI Copilot Metric Correlation Matrix: Wafer Yields vs. Financial Loss", fontsize=11, fontweight="bold")
plt.tight_layout()
plt.savefig("reports/anomaly_correlation_heatmap.png", dpi=300)
print("✅ Anomaly correlation heatmap saved to reports/anomaly_correlation_heatmap.png")
