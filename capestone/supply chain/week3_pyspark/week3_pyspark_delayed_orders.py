from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

ROOT = Path(__file__).resolve().parents[1]
INPUT_CSV = str(ROOT / "data" / "orders.csv")
OUTPUT_DIR = str(ROOT / "output" / "week3_delayed_by_supplier")


def main():
    spark = (
        SparkSession.builder.appName("SupplyChainWeek3")
        .master("local[*]")
        .config("spark.ui.showConsoleProgress", "false")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("ERROR")

    # 1. Load
    df = spark.read.csv(INPUT_CSV, header=True, inferSchema=True)
    print(f"Loaded {df.count()} rows")

    # 2. Clean + compute delay
    df = (
        df.dropDuplicates(["order_id"])
        .dropna(subset=["supplier_id", "delivery_date"])
        .withColumn("expected_delivery_date", F.to_date("expected_delivery_date"))
        .withColumn("delivery_date", F.to_date("delivery_date"))
        .withColumn("delay_days", F.datediff("delivery_date", "expected_delivery_date"))
    )

    # 3. Filter delayed shipments
    delayed = df.filter(F.col("delay_days") > 0)
    print(f"Delayed shipments: {delayed.count()}")

    # 4. Group by supplier and count delayed orders
    result = (
        delayed.groupBy("supplier_id")
        .agg(
            F.count("*").alias("delayed_orders"),
            F.round(F.avg("delay_days"), 2).alias("avg_delay_days"),
        )
        .orderBy(F.desc("delayed_orders"))
    )
    result.show()

    # 5. Save (single CSV part file + Parquet)
    result.coalesce(1).write.mode("overwrite").option("header", True).csv(OUTPUT_DIR + "_csv")
    result.write.mode("overwrite").parquet(OUTPUT_DIR + "_parquet")
    print(f"Saved results under {OUTPUT_DIR}_csv and {OUTPUT_DIR}_parquet")

    spark.stop()


if __name__ == "__main__":
    main()
