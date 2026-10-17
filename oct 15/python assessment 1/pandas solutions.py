import pandas as pd

# 61
df_orders = pd.read_csv("orders.csv")
df_orders.columns = df_orders.columns.str.strip()

# 62
print("62. First 5 rows:\n", df_orders.head())

# 63
print("\n63. Column datatypes:\n", df_orders.dtypes)

# 64
print("\n64. Shape:", df_orders.shape)

# 65
delivered = df_orders.query("status.str.strip() == 'Delivered'")

# 66
qty_gt_2 = df_orders[df_orders['quantity'] > 2]

# 67
df_orders['order_value'] = df_orders['quantity'] * df_orders['unit_price']

# 68
print("\n68. Order count by status:\n", df_orders['status'].value_counts())

# 69
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])

# 70
df_orders['month'] = df_orders['order_date'].dt.strftime('%Y-%m')

# 71
print("\n71. Count by month and status:\n", df_orders.groupby(['month', 'status']).size())

# 72
print("\n72. Total order value by category:\n", df_orders.groupby('category')['order_value'].sum())

# 73
print("\n73. Avg order value by category:\n", df_orders.groupby('category')['order_value'].mean())

# 74
sorted_orders = df_orders.sort_values(by='order_value', ascending=False)

df_customers = pd.read_csv("customers.csv")
df_customers.columns = df_customers.columns.str.strip()
df_customers['customer_id'] = df_customers['customer_id'].str.strip()
df_orders['customer_id'] = df_orders['customer_id'].str.strip()

# 75
merged_df = pd.merge(df_orders, df_customers, on='customer_id', how='inner')

# 76
selected_cols = ['order_id', 'customer_name', 'city', 'product', 'status', 'order_value']
print("76. Joined view:\n", merged_df[selected_cols].head())

# 77
merged_df['city'] = merged_df['city'].str.strip()
merged_df['status'] = merged_df['status'].str.strip()
hyd_delivered = merged_df[(merged_df['status'] == 'Delivered') & (merged_df['city'] == 'Hyderabad')]

# 78
# 79
city_summary = merged_df.groupby('city').agg(
    total_orders=('order_id', 'count'),
    total_sales=('order_value', 'sum'),
    average_order_value=('order_value', 'mean')
).sort_values(by='total_sales', ascending=False).reset_index()

# 80
city_summary.to_csv("city_sales_summary.csv", index=False)

# 81
city_summary.to_json("city_sales_summary.json", orient="records", indent=4)

import numpy as np

# 82
conditions = [
    merged_df['order_value'] >= 50000,
    merged_df['order_value'] >= 15000
]
choices = ['High', 'Medium']
merged_df['order_size'] = np.select(conditions, choices, default='Low')

# 83
merged_df['segment'] = merged_df['segment'].str.strip()
merged_df['priority_customer'] = np.where(merged_df['segment'] == 'Corporate', 'Priority', 'Normal')

# 84
merged_df.to_csv("enriched_orders.csv", index=False)
print("84. Enriched orders saved to 'enriched_orders.csv'")