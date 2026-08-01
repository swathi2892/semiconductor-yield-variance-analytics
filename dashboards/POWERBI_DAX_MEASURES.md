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

### 1. High-Yield Drop Flag (Dynamic Alert)
```dax
Yield Risk Status = 
IF(
    AVERAGE(wafer_production_yield[yield_variance_pct]) <= -5.0, 
    "Critical Alert", 
    "Normal"
)

### 2.Cumulative Revenue Loss ($USD) Across Batches
Cumulative Loss USD = 
CALCULATE(
    SUM(wafer_production_yield[revenue_variance_usd]),
    FILTER(
        ALLSELECTED(wafer_production_yield),
        wafer_production_yield[actual_yield_pct] <= EARLIER(wafer_production_yield[actual_yield_pct])
    )
)


### 3. Total Financial Revenue Impact ($USD)
Total Revenue Variance = 
SUM(wafer_production_yield[revenue_variance_usd])
