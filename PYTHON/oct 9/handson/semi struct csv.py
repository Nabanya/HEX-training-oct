import csv

# with open("products.csv", "w", newline="") as file:
    #
    # writer = csv.writer(file)
    #
    # writer.writerow([
    #     "product_id",
    #     "product_name",
    #     "category",
    #     "price"
    # ])
    #
    # writer.writerow([101, "Laptop", "Electronics", 65000])
    # writer.writerow([102, "Mouse", "Accessories", 1500])
    # writer.writerow([103, "Office Chair", "Furniture", 9000])
    # writer.writerow([104, "Monitor", "Electronics", 18000])
#
#

with open("products.csv",'r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


with open("products.csv",'r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)