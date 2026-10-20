import pandas as pd
import numpy as np

data = {
    'order_id': list(range(1001, 1016)),
    'customer_id': [1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'customer_name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan', 'Alice', 'Fiona', 'George', 'Hannah', 'Ian', 'Julia', 'Kevin', 'Laura', 'Michael', 'Nina'],
    'region': ['North', 'South', 'East', 'West', 'North', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'expected_delivery_date': ['2026-10-05', '2026-10-05', '2026-10-06', '2026-10-06', '2026-10-07', '2026-10-07', '2026-10-08', '2026-10-08', '2026-10-09', '2026-10-09', '2026-10-10', '2026-10-10', '2026-10-11', '2026-10-11', '2026-10-12'],
    'actual_delivery_date': ['2026-10-08', '2026-10-04', '2026-10-10', '2026-10-06', '2026-10-12', '2026-10-07', None, '2026-10-09', '2026-10-09', '2026-10-14', '2026-10-10', None, '2026-10-15', '2026-10-11', '2026-10-18'],
    'issue_category': ['Traffic Delay', 'None', 'Damaged Packaging', 'None', 'Weather', 'None', 'Driver Issue', 'Traffic Delay', 'None', 'Late Delivery', 'None', 'Wrong Item', 'Traffic Delay', 'None', 'Damaged Packaging']
}

df = pd.DataFrame(data)
df['expected_delivery_date'] = pd.to_datetime(df['expected_delivery_date'])
df['actual_delivery_date'] = pd.to_datetime(df['actual_delivery_date'])
ref_date = pd.Timestamp('2026-10-20')
effective_delivery = df['actual_delivery_date'].fillna(ref_date)
df['delay_days'] = (effective_delivery - df['expected_delivery_date']).dt.days
df['is_delayed'] = np.where(df['delay_days'] > 0, 1, 0)

df.to_csv('cleaned_orders_week2.csv', index=False)
print("Created 'cleaned_orders_week2.csv'.")