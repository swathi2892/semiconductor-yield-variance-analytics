# Power BI Dashboard Architecture & DAX Metrics

This document outlines the data model and DAX formulas used for the enterprise Power BI **Yield Variance & Revenue Tracking Dashboard**.

---

## 📊 Data Model Schema
* **Fact Table:** `wafer_production_yield`
* **Relationships:** Joined on `lot_id` with `Dim_Wafer_Specs` (1:Many)

---

## 🧮 Custom DAX Calculated Measures

### 1. Total Financial Revenue Impact ($USD)
```dax
Total Revenue Variance = 
SUM(wafer_production_yield[revenue_variance_usd])
