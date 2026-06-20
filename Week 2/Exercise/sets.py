beverages = set(("soda", "water", "coffee"))
print(beverages)
elements = ["milk", "porridge"]
for i in elements:
    beverages.add(i)
print(beverages)

mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave in set")

mySet.remove("kettle")
print(mySet)

for i in mySet:
    print(i.title() + " ", end="")
