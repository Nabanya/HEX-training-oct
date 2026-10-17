# 1
weight = float(input("Enter weight:"))
cost = float(input("Enter cost:"))

# 2
cost_per_kg = cost / weight
print(f"2. Cost per kg: ₹{cost_per_kg:.2f}")

# 3
if weight > 20:
    category = "Heavy"
elif 10 <= weight <= 20:
    category = "Medium"
else:
    category = "Light"
print(f"3. Weight Category: {category}")

# 4
print("4. Shipment Numbers 1-20:")
for i in range(1, 21):
    print(i, end=" ")
print()

# 5
print("5. Even Shipment Numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 6
print("6. Simulating Processing Attempts:")
attempts = 1
while attempts <= 5:
    print(f"   Attempt {attempts} in progress...")
    attempts += 1

# 7
shipment_costs = [850, 620, 1250, 480, 1600, 740, 590, 1100, 920, 1750, 520, 1050]

# 8
total_cost = sum(shipment_costs)
avg_cost = total_cost / len(shipment_costs)
min_cost = min(shipment_costs)
max_cost = max(shipment_costs)
print(f"8. Total: ₹{total_cost}, Avg: ₹{avg_cost:.2f}, Min: ₹{min_cost}, Max: ₹{max_cost}")

# 9
destinations = ["Hyderabad", "Mumbai", "Bangalore", "Delhi", "Pune", "Hyderabad", "Mumbai"]
unique_destinations = set(destinations)
print(f"9. Unique Destinations: {unique_destinations}")

# 10
single_shipment = {
    "shipment_id": "S1001",
    "destination": "Hyderabad",
    "weight": 12.5,
    "status": "Delivered",
    "cost": 850
}

# 11
shipments_list = [
    {"shipment_id": "S1001", "destination": "Hyderabad", "status": "Delivered", "cost": 850},
    {"shipment_id": "S1002", "destination": "Mumbai", "status": "In Transit", "cost": 620},
    {"shipment_id": "S1003", "destination": "Bangalore", "status": "Delivered", "cost": 1250},
    {"shipment_id": "S1004", "destination": "Delhi", "status": "Pending", "cost": 480}
]

# 12
delivered_shipments = [s for s in shipments_list if s["status"] == "Delivered"]
print(f"12. Delivered Shipments Count: {len(delivered_shipments)}")

# 13
def calculate_cost(weight, rate=50):
    return weight * rate

# 14
def get_category(w):
    if w > 20:
        return "Heavy"
    elif 10 <= w <= 20:
        return "Medium"
    return "Light"

# 15
filtered_delivered = list(filter(lambda s: s["status"] == "Delivered", shipments_list))
print("15. Filtered Delivered:", [s["shipment_id"] for s in filtered_delivered])

# 16
all_dests = list(map(lambda s: s["destination"], shipments_list))
print("16. All Destinations:", all_dests)

# 17
sorted_shipments = sorted(shipments_list, key=lambda s: s["cost"])
print("17. Sorted by Cost:", [s["shipment_id"] for s in sorted_shipments])

# 18-20
class Shipment:
    def __init__(self, shipment_id, destination, weight, cost):
        self.shipment_id = shipment_id
        self.destination = destination
        self.weight = weight
        self.cost = cost

    def display(self):
        print(f"Shipment [{self.shipment_id}] -> Dest: {self.destination} | Weight: {self.weight}kg | Cost: ₹{self.cost}")

# 21-22
class ExpressShipment(Shipment):
    def __init__(self, shipment_id, destination, weight, cost, surcharge=200):
        super().__init__(shipment_id, destination, weight, cost)
        self.surcharge = surcharge

    def display(self):
        total_cost = self.cost + self.surcharge
        print(f"[EXPRESS] Shipment [{self.shipment_id}] -> Dest: {self.destination} | Base Cost: ₹{self.cost} + Surcharge: ₹{self.surcharge} | Total: ₹{total_cost}")

# 23
shipment1 = Shipment("S1001", "Hyderabad", 12.5, 850)
shipment2 = ExpressShipment("S1002", "Mumbai", 8.0, 620)

print("23. Polymorphism Demo:")
shipments_fleet = [shipment1, shipment2]
for s in shipments_fleet:
    s.display()

import json

# 24
with open("data/employees.json", "r", encoding="utf-8") as f:
    employees = json.load(f)

# 25
print("25. Employee Names:", [emp["name"] for emp in employees])

# 26
high_earners = [emp["name"] for emp in employees if emp["salary"] > 75000]
print("26. High Earners (>75000):", high_earners)

# 27
python_devs = [emp["name"] for emp in employees if "Python" in emp["skills"]]
print("27. Python Developers:", python_devs)

# 28
print("28. Employee Ratings:")
for emp in employees:
    print(f"    {emp['name']}: {emp['performance']['rating']}")

# 29
top_rated = [emp["name"] for emp in employees if emp["performance"]["rating"] > 4.5]
print("29. Ratings > 4.5:", top_rated)

# 30
sorted_employees = sorted(employees, key=lambda e: e["performance"]["rating"], reverse=True)

# 31
for emp in employees:
    # Handles both 'employee_id' and 'employee id' keys from raw dataset[cite: 10, 11]
    emp_id = emp.get("employee_id") or emp.get("employee id")
    if emp_id == 303:
        emp["skills"].append("Docker")

# 32
with open("employees_updated.json", "w", encoding="utf-8") as f:
    json.dump(employees, f, indent=4)
print("32. Saved updated employee data to 'employees_updated.json'")

# shipment_utils.py
# 33
def calculate_cost(weight, rate=50):
    return weight * rate

def get_weight_category(w):
    if w > 20:
        return "Heavy"
    elif 10 <= w <= 20:
        return "Medium"
    return "Light"

import pandas as pd

# 36
df_shipments = pd.read_csv("data/shipments.csv")
df_shipments.columns = df_shipments.columns.str.strip()

# 37
delivered = df_shipments[df_shipments['status'].str.strip() == 'Delivered']

# 38
print("38. Counts by Status:\n", df_shipments['status'].str.strip().value_counts())

# 39
df_shipments['shipment_date'] = pd.to_datetime(df_shipments['shipment_date'])

# 40
df_shipments['month'] = df_shipments['shipment_date'].dt.strftime('%Y-%m')
print("\n40. Count by Month and Status:\n", df_shipments.groupby(['month', 'status']).size())

# 41
print("\n41. Average Cost by Destination:\n", df_shipments.groupby('destination')['cost'].mean())

# 42
print("\n42. Total Weight by Destination:\n", df_shipments.groupby('destination')['weight'].sum())

# 43
selected_cols = ['shipment_id', 'destination', 'cost']
df_subset = pd.read_csv("data/shipments.csv", usecols=selected_cols)

# 44
df_hubs = pd.read_csv("data/hubs.csv")
df_hubs.columns = df_hubs.columns.str.strip()
df_shipments['hub_id'] = df_shipments['hub_id'].str.strip()
df_hubs['hub_id'] = df_hubs['hub_id'].str.strip()

# 45
df_merged = pd.merge(df_shipments, df_hubs, on='hub_id', how='inner')

# 46
# 47
# 48
hub_summary = df_merged.groupby(['hub_id', 'hub_name']).agg(
    total_cost=('cost', 'sum'),
    total_shipments=('shipment_id', 'count')
).sort_values(by='total_cost', ascending=False).reset_index()

# 49
hub_summary.to_csv("hub_summary.csv", index=False)

# 50
hub_summary.to_json("hub_summary.json", orient="records", indent=4)

import numpy as np

# 51
df_merged['cost_per_kg'] = df_merged['cost'] / df_merged['weight']

# 52
df_merged['cost_category'] = np.where(df_merged['cost'] >= 1200, 'Expensive', 'Normal')

# 53
df_merged['status'] = df_merged['status'].str.strip()
conditions = [
    (df_merged['status'] == 'Delivered') & (df_merged['cost_category'] == 'Normal'),
    (df_merged['status'] == 'Delivered') & (df_merged['cost_category'] == 'Expensive'),
    (df_merged['status'] != 'Delivered')
]
choices = ['High Performance', 'Premium Delivered', 'Delayed/Pending']
df_merged['performance_category'] = np.select(conditions, choices, default='Standard')

# 54
df_merged.to_csv("shipment_analysis.csv", index=False)
print("54. Final enriched dataset successfully saved to 'shipment_analysis.csv'!")