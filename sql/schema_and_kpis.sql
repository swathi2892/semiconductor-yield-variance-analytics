-- Create Wafer Production Analytics Schema
CREATE TABLE wafer_production_yield (
    lot_id VARCHAR(20) PRIMARY KEY,
    wafer_count INT,
    target_yield_pct DECIMAL(5,2),
    actual_yield_pct DECIMAL(5,2),
    wafer_cost_usd DECIMAL(10,2),
    price_per_chip_usd DECIMAL(10,2),
    chips_per_wafer INT,
    yield_variance_pct DECIMAL(5,2),
    revenue_variance_usd DECIMAL(12,2)
);

-- KPI Query: Extract High Financial Loss Lots for Executive Reporting
SELECT 
    lot_id,
    wafer_count,
    yield_variance_pct,
    revenue_variance_usd
FROM wafer_production_yield
WHERE yield_variance_pct < -5.0
ORDER BY revenue_variance_usd ASC;
