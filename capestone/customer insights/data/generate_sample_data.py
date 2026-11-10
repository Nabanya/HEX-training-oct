"""Generate sample data for the Customer Order Insights project.

Creates in data/:
  customers.csv        customer_id, customer_name, email, region
  orders.csv           order_id, customer_id, order_date, expected_delivery_date,
                       delivery_date, delivery_issue
  delivery_status.csv  order_id, status, status_date   (status history per order)

Run from the project root:  python data/generate_sample_data.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent
rng = np.random.default_rng(7)

# ---- customers -------------------------------------------------------
N_CUSTOMERS = 30
regions = ["North", "South", "East", "West"]
customers = pd.DataFrame({
    "customer_id": range(1, N_CUSTOMERS + 1),
    "customer_name": [f"Customer {i}" for i in range(1, N_CUSTOMERS + 1)],
    "email": [f"customer{i}@example.com" for i in range(1, N_CUSTOMERS + 1)],
    "region": rng.choice(regions, N_CUSTOMERS),
})

# ---- orders ----------------------------------------------------------
N_ORDERS = 300
order_dates = pd.to_datetime("2026-01-01") + pd.to_timedelta(rng.integers(0, 240, N_ORDERS), unit="D")
expected = order_dates + pd.to_timedelta(rng.integers(3, 10, N_ORDERS), unit="D")
delivery = expected + pd.to_timedelta(rng.integers(-2, 7, N_ORDERS), unit="D")
delay = (delivery - expected).days

issues_pool = ["Courier delay", "Weather", "Address not found", "Damaged package", "Stock shortage"]
issues = np.where(delay > 0, rng.choice(issues_pool, N_ORDERS), None)

orders = pd.DataFrame({
    "order_id": [f"ORD{str(i).zfill(4)}" for i in range(1, N_ORDERS + 1)],
    "customer_id": rng.integers(1, N_CUSTOMERS + 1, N_ORDERS),
    "order_date": order_dates.strftime("%Y-%m-%d"),
    "expected_delivery_date": expected.strftime("%Y-%m-%d"),
    "delivery_date": delivery.strftime("%Y-%m-%d"),
    "delivery_issue": issues,
})

# ---- delivery status history ----------------------------------------
rows = []
for i, r in orders.iterrows():
    od = pd.Timestamp(r["order_date"])
    dd = pd.Timestamp(r["delivery_date"])
    final = "DELAYED" if delay[i] > 0 else "DELIVERED"
    rows += [
        (r["order_id"], "PLACED", od),
        (r["order_id"], "SHIPPED", od + pd.Timedelta(days=1)),
        (r["order_id"], "OUT_FOR_DELIVERY", dd - pd.Timedelta(days=1)),
        (r["order_id"], final, dd),
    ]
status = pd.DataFrame(rows, columns=["order_id", "status", "status_date"])
status["status_date"] = status["status_date"].dt.strftime("%Y-%m-%d")

# ---- inject a few dirty rows so Week 2 cleaning has work to do --------
orders.loc[4, "customer_id"] = None
orders.loc[11, "delivery_date"] = None
orders = pd.concat([orders, orders.iloc[[8]]], ignore_index=True)  # duplicate

customers.to_csv(DATA_DIR / "customers.csv", index=False)
orders.to_csv(DATA_DIR / "orders.csv", index=False)
status.to_csv(DATA_DIR / "delivery_status.csv", index=False)
print(f"Wrote {len(customers)} customers, {len(orders)} orders, {len(status)} status rows to {DATA_DIR}")
