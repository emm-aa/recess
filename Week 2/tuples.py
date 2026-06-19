x = ("samsung", "iphone", "tecno", "redmi")
print(x[2])
print(x[-2])

y = list(x)
y[1] = "itel"
x = tuple(y)
print(x)

x = x + ("huawei",)
print(x)

for i in x:
    print(i + " ", end="")
print()

y, *z = x
x = list(z)
print(x)

cities = ["Mbarara", "Gulu", "Kabale", "Arua"]
cities = tuple(cities)
print(cities)

a, b, *c = cities
print(a, b, c)

print(cities[1:])
a = ("Arinda",)
b = ("Emmanuel", "Nsiimenta")
c = a + b
print(c)

colours = ("Blue", "Red", "Green")
print(colours * 3)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
num = 0

print(thistuple.count(8))
