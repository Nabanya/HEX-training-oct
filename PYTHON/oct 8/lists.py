prod=["Laptop","Mouse","Keyboard","Monitor"]
print(prod)
print(prod[0])
print(prod[1])

print(prod[-1])

prod[1]="Wireless Mouse"
print(prod)

prod.append("Disk")
print(prod)

prod.insert(1,"Led Monitor")
print(prod)

prod.remove("Disk")
print(prod)

prod.pop()
print(prod)