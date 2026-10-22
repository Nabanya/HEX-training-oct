import pandas as pd
import numpy as np
import mysql.connector
from pymongo import MongoClient

def run_supply_chain_pipeline():
    print("1. Fetching Supplier & Order data from MySQL...")
    mysql_conn = mysql.connector.connect(
        host="localhost",
        user="root",         # Replace with your MySQL username
        password="password", # Replace with your MySQL password
        database="supply_chain_db"
    )

    sql_query = """
    SELECT 
        o.order_id,
        o.supplier_id,
        s.supplier_name,
        s.region,
        o.order_date,
        o.expected_delivery_date,
        o.actual_delivery_date,
        o.status AS order_status
    FROM orders o
    JOIN suppliers s ON o.supplier_id = s.supplier_id;
    """

    mysql_df = pd.read_sql(sql_query, mysql_conn)
    mysql_conn.close()
    print(f"   Fetched {len(mysql_df)} order records from MySQL.")

    print("2. Fetching Shipment Logs from MongoDB...")
    mongo_client = MongoClient("mongodb://localhost:27017/")
    mongo_db = mongo_client["supply_chain_db"]
    shipment_docs = list(mongo_db["shipment_logs"].find({}, {"_id": 0}))
    mongo_df = pd.DataFrame(shipment_docs)
    mongo_client.close()
    print(f"   Fetched {len(mongo_df)} shipment logs from MongoDB.")

    print("3. Merging Datasets & Calculating Delay / Risk Metrics...")
    merged_df = pd.merge(
        mysql_df, 
        mongo_df[['order_id', 'shipment_id', 'carrier', 'status', 'location', 'temperature_c']], 
        on='order_id', 
        how='left'
    )
    merged_df.rename(columns={'status': 'shipment_status'}, inplace=True)

    merged_df['expected_delivery_date'] = pd.to_datetime(merged_df['expected_delivery_date'])
    merged_df['actual_delivery_date'] = pd.to_datetime(merged_df['actual_delivery_date'])

    ref_date = pd.Timestamp('2026-10-20')
    effective_delivery = merged_df['actual_delivery_date'].fillna(ref_date)

    merged_df['delay_days'] = (effective_delivery - merged_df['expected_delivery_date']).dt.days
    merged_df['is_delayed'] = np.where(merged_df['delay_days'] > 0, 1, 0)

    conditions = [
        merged_df['delay_days'] <= 0,
        (merged_df['delay_days'] > 0) & (merged_df['delay_days'] <= 3),
        merged_df['delay_days'] > 3
    ]
    choices = ['Low Risk', 'Medium Risk', 'High Risk']
    merged_df['supplier_risk_level'] = np.select(conditions, choices, default='Unknown')

    output_path = "cleaned_supply_chain_week2.csv"
    merged_df.to_csv(output_path, index=False)
    print(f"\nPipeline Run Successful! Output saved to '{output_path}'.")

    print("\n--- SUPPLIER RISK METRICS SUMMARY ---")
    summary = merged_df.groupby(['region', 'supplier_risk_level'])['is_delayed'].count().reset_index()
    print(summary)

if __name__ == '__main__':
    run_supply_chain_pipeline()