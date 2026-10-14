sales = [
    ("North", 12000),
    ("South", 18000),
    ("West", 9500),
    ("North", 22000),
    ("East", 15000),
    ("South", 11000)
]

# 1
print("All Tuples:")
print(sales)

# 2
print("\nRegion Names:")
for s in sales:
    print(s[0])

# 3
print("\nSales Amounts:")
for s in sales:
    print(s[1])

# 4
print("\nSales Greater Than 12000:")
for s in filter(lambda x: x[1] > 12000, sales):
    print(s)

# 5
total_sales = sum(s[1] for s in sales)
print("\nTotal Sales:", total_sales)

# 6
amounts = [s[1] for s in sales]
print("\nHighest Sales:", max(amounts))
print("Lowest Sales:", min(amounts))

# 7
sales_amounts = list(map(lambda x: x[1], sales))
print("\nSales Amount List:", sales_amounts)

# 8
regions = set(map(lambda x: x[0], sales))
print("\nUnique Regions:", regions)

# 9
print("\nSorted by Sales Amount:")
print(sorted(sales, key=lambda x: x[1]))

# 10
print("\nSorted by Region Name:")
print(sorted(sales, key=lambda x: x[0]))
