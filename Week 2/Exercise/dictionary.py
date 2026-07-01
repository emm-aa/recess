shoes = {"brand": "Nick", "color": "black", "size": 40}
print(shoes.get("size"))

shoes["brand"] = "Adidas"
print(shoes)
shoes["type"] = "sneakers"
print(shoes)
list1 = []
list2 = []
for keys in shoes:
    list1.append(keys)
print(list1)
for values in shoes.values():
    list2.append(values)
print(list2)
if shoes["size"]:
    print("Key 'size' exists.")
for key, value in shoes.items():
    if type(value) != type(key):
        print(key + " --> " + str(value))
    else:
        print(key + " --> " + value)

del shoes["color"]
print(shoes)
shoes.clear()
print(shoes)

flowers = {"type": "bontanical"}
