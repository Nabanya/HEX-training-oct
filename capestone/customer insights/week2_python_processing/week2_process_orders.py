from pathlib import Path

import numpy as np
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
API_URL = None   # e.g. "https://api.example.com/orders"; None = use the local CSV
ORDERS_CSV = ROOT / "data" / "orders.csv"
OUTPUT_CSV = ROOT / "output" / "week2_cleaned_orders.csv"


def load_orders() -> pd.DataFrame:
    # Load from the API if configured and reachable, otherwise from the CSV.
    if API_URL:
        try:
            response = requests.get(API_URL, timeout=5)
            response.raise_for_status()
            print(f"Loaded data from API: {API_URL}")
            return pd.DataFrame(response.json())
        except (requests.RequestException, ValueError) as exc:
            print(f"API unavailable ({type(exc).__name__}); using {ORDERS_CSV.name}")
    return pd.read_csv(ORDERS_CSV)


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    #Remove duplicates and missing fields; convert timestamps
    df = df.drop_duplicates(subset="order_id")
    df = df.dropna(subset=["order_id", "customer_id", "delivery_date"]).copy()

    for col in ["order_date", "expected_delivery_date", "delivery_date"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    df = df.dropna(subset=["order_date", "expected_delivery_date", "delivery_date"])

    df["customer_id"] = df["customer_id"].astype(int)
    df["delivery_issue"] = df["delivery_issue"].fillna("None")
    return df.reset_index(drop=True)


def add_delays(df: pd.DataFrame) -> pd.DataFrame:
    #Calculate delay with numpy (positive = delivered after the expected date).
    df["delay_days"] = (df["delivery_date"] - df["expected_delivery_date"]).dt.days
    df["delayed"] = np.where(df["delay_days"] > 0, 1, 0)
    return df


def print_summary(df: pd.DataFrame) -> None:
    print("\nDelay summary")
    print(f"  Orders analysed : {len(df)}")
    print(f"  Delayed orders  : {int(df['delayed'].sum())} ({df['delayed'].mean() * 100:.1f}%)")
    print(f"  Average delay   : {df.loc[df['delayed'] == 1, 'delay_days'].mean():.2f} days (delayed orders)")

    print("\nTop 5 delayed customers (number of delayed orders):")
    top = df.groupby("customer_id")["delayed"].sum().sort_values(ascending=False).head(5)
    print(top.to_string())

    print("\nMost common delivery issues:")
    issues = df.loc[df["delivery_issue"] != "None", "delivery_issue"].value_counts()
    print(issues.to_string())


def main() -> pd.DataFrame:
    raw = load_orders()
    print(f"Raw rows: {len(raw)}")

    df = add_delays(clean_orders(raw))
    print(f"Clean rows: {len(df)}")

    print("\nSample of processed data:")
    print(df[["order_id", "customer_id", "delay_days", "delayed"]].head())

    print_summary(df)

    OUTPUT_CSV.parent.mkdir(exist_ok=True)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nSaved cleaned dataset to {OUTPUT_CSV}")
    return df


if __name__ == "__main__":
    main()
