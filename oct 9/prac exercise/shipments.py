import csv
#
# data = [
#     ["S101", "Alpha Stores", "Hyderabad", 12.5, "Delivered", 850],
#     ["S102", "Metro Mart", "Mumbai", 8.2, "In Transit", 620],
#     ["S103", "Fresh Foods", "Hyderabad", 15.0, "Delivered", 1100],
#     ["S104", "Quick Shop", "Pune", 5.5, "Pending", 450],
#     ["S105", "Urban Retail", "Mumbai", 20.0, "Delivered", 1450],
#     ["S106", "Daily Needs", "Delhi", 9.8, "In Transit", 700],
#     ["S107", "Smart Bazaar", "Hyderabad", 7.5, "Pending", 550],
#     ["S108", "Green Market", "Delhi", 18.2, "Delivered", 1300]
# ]
#
# with open("shipments.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#
#     writer.writerow([
#         "shipment_id", "customer", "city",
#         "weight", "status", "cost"
#     ])
#
#     writer.writerows(data)
#
# print("Shipment values loaded successfully!")


# 1
with open("shipments.csv", "r") as file:
    reader = csv.DictReader(file)
    shipments = list(reader)

# 2
print("All Shipments:")
print(shipments)

# 3
print("\nComplete Shipment Records:")
for s in shipments:
    print(s)

# 4
print("\nShipment ID, Customer and Status:")
for s in shipments:
    print(s["shipment_id"], s["customer"], s["status"])

# 5
for s in shipments:
    s["weight"] = float(s["weight"])
    s["cost"] = float(s["cost"])

print("\nNumeric Weight and Cost:")
print(shipments)

# 6
total_cost = sum(s["cost"] for s in shipments)
print("\nTotal Shipping Cost:", total_cost)

# 7
print("\nShipments with Cost Above 700:")
for s in filter(lambda x: x["cost"] > 700, shipments):
    print(s)

# 8
print("\nDelivered Shipments:")
for s in filter(lambda x: x["status"] == "Delivered", shipments):
    print(s)

# 9
print("\nShipments Weighing More Than 10:")
for s in filter(lambda x: x["weight"] > 10, shipments):
    print(s)

# 10
cities = list(map(lambda x: x["city"], shipments))
print("\nAll Cities:", cities)

# 11
unique_cities = set(map(lambda x: x["city"], shipments))
print("\nUnique Cities:", unique_cities)

# 12
print("\nSorted by Cost:")
for s in sorted(shipments, key=lambda x: x["cost"]):
    print(s)

# 13
print("\nSorted by Weight:")
for s in sorted(shipments, key=lambda x: x["weight"], reverse=True):
    print(s)

# 14
print("\nSorted by Customer Name:")
for s in sorted(shipments, key=lambda x: x["customer"]):
    print(s)

# 15
cost_per_kg = lambda cost, weight: cost / weight

print("\nCost Per Kg:")
for s in shipments:
    print(s["shipment_id"], round(cost_per_kg(s["cost"], s["weight"]), 2))
