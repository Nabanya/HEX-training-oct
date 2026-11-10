"""Generate sample supply chain data (orders.csv and orders.json) used by Weeks 2-5.

Run from the project root:  python data/generate_sample_data.py
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent
rng = np.random.default_rng(42)

N_ORDERS = 200
suppliers = [f"S{str(i).zfill(3)}" for i in range(1, 9)]
products = ["Bearings", "Steel Rods", "Circuit Boards", "Packaging", "Lubricant", "Fasteners"]

order_dates = pd.to_datetime("2026-01-01") + pd.to_timedelta(rng.integers(0, 240, N_ORDERS), unit="D")
expected = order_dates + pd.to_timedelta(rng.integers(5, 15, N_ORDERS), unit="D")
# actual delivery is expected date +/- a few days (positive = late)
delivery = expected + pd.to_timedelta(rng.integers(-3, 8, N_ORDERS), unit="D")

df = pd.DataFrame({
    "order_id": [f"O{str(i).zfill(4)}" for i in range(1, N_ORDERS + 1)],
    "supplier_id": rng.choice(suppliers, N_ORDERS),
    "product": rng.choice(products, N_ORDERS),
    "quantity": rng.integers(10, 500, N_ORDERS),
    "order_date": order_dates.strftime("%Y-%m-%d"),
    "expected_delivery_date": expected.strftime("%Y-%m-%d"),
    "delivery_date": delivery.strftime("%Y-%m-%d"),
})

# Inject a few dirty rows so the Week 2 cleaning step has something to do
df.loc[5, "delivery_date"] = None
df.loc[17, "supplier_id"] = None
df.loc[30, "quantity"] = None
df = pd.concat([df, df.iloc[[3]]], ignore_index=True)  # duplicate row

df.to_csv(DATA_DIR / "orders.csv", index=False)
with open(DATA_DIR / "orders.json", "w") as f:
    json.dump(json.loads(df.to_json(orient="records")), f, indent=2)

print(f"Wrote {len(df)} rows to {DATA_DIR / 'orders.csv'} and orders.json")
