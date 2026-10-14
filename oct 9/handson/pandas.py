import pandas as pd

df=pd.read_csv("orders.csv")
# print(df)

# Extract -- Transform -- Load -- ETL Process
#
# print(df.head())
#
# print(df.tail())
#
# print(df.columns)
#
# print(df.shape)
#
# print(df.dtypes)
#
# df.info()

# 2
# print(df["product"])
# print(df[["order_id","product","amount"]])
#
# # filter
# delv=df.query("status == 'Delivered'")
# print(delv)
#
# res=df.query("amount > 20000")
# print(res)


# eg1
print(df["status"].value_counts())

# eg2
result=(df.groupby("status").size())

print(result)

# eg3 sting to date
df["order_date"]=pd.to_datetime(df["order_date"])

df["month"]=df["order_date"].dt.month

print(df)
