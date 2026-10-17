import csv
import json
import pandas as pd
import numpy as np

# section A
# 1
prod_name = input("Enter product name: ")
unit_price = float(input("Enter price per unit: "))
quantity = int(input("Enter quantity: "))

# 2
total_amount = unit_price * quantity

# 3
if total_amount >= 50000:
    discount_rate = 0.10
else:
    discount_rate = 0.05

discount = total_amount * discount_rate
final_amount = total_amount - discount

# 4
print(f"Product: {prod_name}")
print(f"Original Amount: ₹{total_amount:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")

# 5
stock_qty = 15
if stock_qty > 20:
    print("Stock Status: High Stock")
elif 1 <= stock_qty <= 20:
    print("Stock Status: Low Stock")
else:
    print("Stock Status: Out of Stock")

# 6
print("Numbers 1 to 10:", [i for i in range(1, 11)])

# 7
curr_stock = 5
while curr_stock >= 0:
    print(f"Current Stock: {curr_stock}")
    curr_stock -= 1

# 8
print("Skip 5:", [x for x in range(1, 11) if x != 5])

# 9
break_list = []
for i in range(1, 11):
    if i == 8:
        break
    break_list.append(i)
print("Break at 8:", break_list)


# section B
sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]

# 10
print("Total Sales:", sum(sales))

# 11
print("Highest Sale:", max(sales))
print("Lowest Sale:", min(sales))

# 12
print("Sales > 20000:", [s for s in sales if s > 20000])

# 13
print("Sorted Sales (Desc):", sorted(sales, reverse=True))

# 14
cities = ["Hyderabad", "Mumbai", "Delhi", "Hyderabad", "Pune", "Mumbai"]
unique_cities = set(cities)
print("Unique Cities:", unique_cities)

# 15
prod_tuple = (201, "Laptop", "Electronics", 65000)
p_id, p_name, p_cat, p_price = prod_tuple
print(f"Unpacked: ID={p_id}, Name={p_name}, Category={p_cat}, Price={p_price}")

# 16
customer = {
    "ID": "C101",
    "Name": "North Star Retail",
    "City": "Hyderabad",
    "Orders": 3,
    "Active status": True
}

# 17
customer["City"] = "Bangalore"

# 18
customer["Orders"] += 1

# 19
customer["Email"] = "contact@northstar.com"

# 20
print("Customer Dict Loop:")
for k, v in customer.items():
    print(f"  {k}: {v}")

# sectin C
# 21
def calculate_total(price, quantity):
    return price * quantity

# 22
def calculate_discount(amount):
    return amount * 0.10 if amount >= 50000 else amount * 0.05

# 23
def get_total_sales(sales_list):
    return sum(sales_list)

# 24
def check_availability(prod_dict):
    return "Available" if prod_dict.get("stock", 0) > 0 else "Out of Stock"

# 25
square = lambda x: x ** 2
print("Square of 7:", square(7))

# 26
sales_above_20k = list(filter(lambda x: x > 20000, sales))
print("Filtered Sales (>20000):", sales_above_20k)

# 27
cust_list = [{"name": "A", "city": "Hyderabad"}, {"name": "B", "city": "Mumbai"}]
cities_mapped = list(map(lambda c: c["city"], cust_list))

# 28
unique_mapped_cities = list(set(cities_mapped))
print("Unique Mapped Cities:", unique_mapped_cities)

# 29
products_list = [
    {"name": "Laptop", "price": 65000},
    {"name": "Mouse", "price": 1500},
    {"name": "Monitor", "price": 18000}
]
sorted_prods = sorted(products_list, key=lambda p: p["price"])
print("Sorted Products by Price:", sorted_prods)

# section D
# 30-33
class Product:
    def __init__(self, product_id, product_name, price, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def display_product(self):
        print(f"[{self.product_id}] {self.product_name} - Price: ₹{self.price}, Stock: {self.stock}")

    def calculate_value(self):
        return self.price * self.stock

p1 = Product(201, "Laptop", 65000, 12)
p2 = Product(202, "Monitor", 18000, 8)

# 34-37
class DiscountedProduct(Product):
    def __init__(self, product_id, product_name, price, stock, discount_percent):
        super().__init__(product_id, product_name, price, stock)
        self.discount_percent = discount_percent

    def display_product(self):
        print(f"[{self.product_id}] {self.product_name} - Price: ₹{self.price}, Stock: {self.stock}, Discount: {self.discount_percent}%")

# 38-39
class PremiumProduct(Product):
    def display_product(self):
        print(f"[PREMIUM] [{self.product_id}] {self.product_name} - VIP Price: ₹{self.price}, Stock: {self.stock}")

p_disc = DiscountedProduct(203, "Office Chair", 9000, 15, 10)
p_prem = PremiumProduct(204, "High-End Workstation", 150000, 3)

product_catalog = [p1, p_disc, p_prem]
print("Polymorphism Demo:")
for prod in product_catalog:
    prod.display_product()