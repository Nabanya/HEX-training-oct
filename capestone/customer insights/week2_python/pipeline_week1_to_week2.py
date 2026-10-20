import pandas as pd
import numpy as np
import mysql.connector
from pymongo import MongoClient

def run_integration_pipeline():
    print("1. Connecting to MySQL Database...")
    mysql_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rhhn2004",
        database="customer_orders_db"
    )

    query = """
    SELECT 
        c.customer_id, c.name AS customer_name, c.region,
        o.order_id, o.order_date,
        ds.expected_delivery_date, ds.actual_delivery_date, ds.status
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN delivery_status ds ON o.order_id = ds.order_id;
    """
    mysql_df = pd.read_sql(query, mysql_conn)
    mysql_conn.close()

    print("2. Connecting to MongoDB Collection...")
    mongo_client = MongoClient("mongodb://localhost:27017/")
    mongo_db = mongo_client["customer_orders_db"]
    feedback_docs = list(mongo_db["customer_feedback"].find({}, {"_id": 0}))
    mongo_df = pd.DataFrame(feedback_docs)
    mongo_client.close()

    print("3. Merging Datasets & Calculating Delay Metrics...")
    merged_df = pd.merge(mysql_df, mongo_df[['order_id', 'rating', 'issue_category']], on='order_id', how='left')

    merged_df['expected_delivery_date'] = pd.to_datetime(merged_df['expected_delivery_date'])
    merged_df['actual_delivery_date'] = pd.to_datetime(merged_df['actual_delivery_date'])

    ref_date = pd.Timestamp('2026-10-20')
    effective_delivery = merged_df['actual_delivery_date'].fillna(ref_date)

    merged_df['delay_days'] = (effective_delivery - merged_df['expected_delivery_date']).dt.days
    merged_df['is_delayed'] = np.where(merged_df['delay_days'] > 0, 1, 0)
    merged_df['issue_category'] = merged_df['issue_category'].fillna('None')

    merged_df.to_csv('cleaned_orders_week2.csv', index=False)
    print("Integration pipeline complete! Output saved to 'cleaned_orders_week2.csv'.")

if __name__ == '__main__':
    run_integration_pipeline()