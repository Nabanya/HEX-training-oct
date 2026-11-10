from pathlib import Path

import numpy as np
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
API_URL = "https://api.sampledata.com/orders"   # placeholder from the brief
LOCAL_JSON = ROOT / "data" / "orders.json"
OUTPUT_CSV = ROOT / "output" / "week2_cleaned_orders.csv"


def fetch_orders() -> pd.DataFrame:
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        print(f"Loaded data from API: {API_URL}")
        return pd.DataFrame(response.json())
    except (requests.RequestException, ValueError) as exc:
        print(f"API unavailable ({type(exc).__name__}); using local file {LOCAL_JSON.name}")
        return pd.read_json(LOCAL_JSON)


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset="order_id")
    df = df.dropna(subset=["order_id", "supplier_id", "quantity", "delivery_date"]).copy()

    for col in ["order_date", "expected_delivery_date", "delivery_date"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    df = df.dropna(subset=["order_date", "expected_delivery_date", "delivery_date"])

    df["quantity"] = df["quantity"].astype(int)
    return df.reset_index(drop=True)


def add_metrics(df: pd.DataFrame) -> pd.DataFrame:
    # positive = delivered after the promised date
    df["delay_days"] = (df["delivery_date"] - df["expected_delivery_date"]).dt.days
    df["is_delayed"] = np.where(df["delay_days"] > 0, 1, 0)
    df["lead_time_days"] = (df["delivery_date"] - df["order_date"]).dt.days

    # simple stock-level calc: quantity of each order vs. the average order size
    df["qty_vs_avg_pct"] = np.round(df["quantity"] / df["quantity"].mean() * 100, 1)
    return df


def main() -> pd.DataFrame:
    raw = fetch_orders()
    print(f"Raw rows: {len(raw)}")

    df = add_metrics(clean_orders(raw))
    print(f"Clean rows: {len(df)}")

    print("\nSample of processed data:")
    print(df[["order_id", "supplier_id", "delay_days", "is_delayed"]].head())

    print("\nSummary:")
    print(f"  Delayed orders : {int(df['is_delayed'].sum())} of {len(df)}")
    print(f"  Average delay  : {df['delay_days'].mean():.2f} days")
    print(f"  Mean lead time : {df['lead_time_days'].mean():.2f} days")

    OUTPUT_CSV.parent.mkdir(exist_ok=True)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nSaved cleaned data to {OUTPUT_CSV}")
    return df


if __name__ == "__main__":
    main()
