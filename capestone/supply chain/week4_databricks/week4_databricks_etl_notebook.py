from pyspark.sql import functions as F

INPUT_PATH = "/FileStore/tables/orders.csv"
DELTA_PATH = "/FileStore/supply_chain/cleaned_orders_delta"

# 1.extract

raw_df = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(INPUT_PATH)
)
print(f"Raw rows: {raw_df.count()}")
display(raw_df.limit(5))

# 2. transform 
clean_df = (
    raw_df.dropDuplicates(["order_id"])
    .dropna(subset=["order_id", "supplier_id", "quantity", "delivery_date"])
    .withColumn("order_date", F.to_date("order_date"))
    .withColumn("expected_delivery_date", F.to_date("expected_delivery_date"))
    .withColumn("delivery_date", F.to_date("delivery_date"))
    .withColumn("quantity", F.col("quantity").cast("int"))
    .withColumn("delay_days", F.datediff("delivery_date", "expected_delivery_date"))
    .withColumn("is_delayed", (F.col("delay_days") > 0).cast("int"))
)
print(f"Clean rows: {clean_df.count()}")

# 3.load

clean_df.write.format("delta").mode("overwrite").save(DELTA_PATH)

# Register as a table so it can be queried with SQL
clean_df.write.format("delta").mode("overwrite").saveAsTable("cleaned_orders")

# 4.Analysis queries

# top products by quantity ordered
top_products = (
    spark.read.format("delta").load(DELTA_PATH)
    .groupBy("product")
    .agg(F.sum("quantity").alias("total_quantity"))
    .orderBy(F.desc("total_quantity"))
)
display(top_products)
