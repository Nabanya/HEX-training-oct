prod={
    "prod_id":101,
    "prod_name":"Laptop",
    "category":"Electronics",
    "price":65000
}
print(prod)

print(prod["prod_id"])

print(prod.get("brand"))
prod["price"]=70000

prod["stock"]=20
print(prod)

prod.pop("category")
del prod["price"]