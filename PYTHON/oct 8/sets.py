cit={"Hyderabad","Mumbai","Delhi","Hyderabad"}
print(cit)

cit.add("Pune")
print(cit)

cit.remove("Mumbai")
print(cit)

cit.discard("Chennai")

cit=["Hyderabad","Mumbai","Delhi","Hyderabad","Mumbai"]
uniq_cit=set(cit)
print(uniq_cit)