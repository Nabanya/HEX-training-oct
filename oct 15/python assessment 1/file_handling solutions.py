import csv
import json

# 40
# 41
with open("activity.txt", "w", encoding="utf-8") as f:
    f.write("System execution started.\n")
    f.write("Reading customer records.\n")
    f.write("Processing batch 1.\n")

# 42
with open("activity.txt", "a", encoding="utf-8") as f:
    f.write("Batch 1 successfully processed.\n")

# 43
print("43. File contents of activity.txt:")
with open("activity.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 44
# 45
customers_data = []
with open("customers.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        customers_data.append({k.strip(): v.strip() for k, v in row.items()})

# 46
print("46. Active Customers:")
for c in customers_data:
    if c['active'].lower() == 'true':
        print(f"    {c['customer_name']}")

# 47
print("47. Hyderabad Customers:")
for c in customers_data:
    if c['city'].lower() == 'hyderabad':
        print(f"    {c['customer_name']}")

# 48
with open("products.json", "r", encoding="utf-8") as f:
    products_json = json.load(f)

# 49
print("49. Product Names:", [p["product_name"] for p in products_json])

# 50
print("50. Products > 10000:", [p["product_name"] for p in products_json if p["price"] > 10000])

# 51
print("51. Supplier Details:")
for p in products_json:
    print(f"    {p['product_name']}: {p['supplier']['name']} ({p['supplier']['city']})")

# 52
all_colors = []
for p in products_json:
    all_colors.extend(p["colors"])
print("52. All Colors:", all_colors)

# 53
print("53. Unique Colors:", list(set(all_colors)))

# 54
for p in products_json:
    if p["product_id"] == 202:
        p["stock"] += 5

# 55
with open("products_updated.json", "w", encoding="utf-8") as f:
    json.dump(products_json, f, indent=4)



