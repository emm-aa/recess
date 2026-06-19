# 1st list - people
people = ["Emily", "Joseph", "Tina", "George", "Victor"]
print(people[1])

people[0] = "Rachael"
print(people)

people.append("Faith")
print(people)

people.insert(2, "Bathel")
print(people)

people.pop(3)
print(people)

print(people[-1])

# 2nd list
items = [1, 2, 3, 4, 5, 6, 7]
print(items[2:5])

countries = ["Uganda", "Kenya", "Tanzania"]
countries_copy = countries.copy()
print(countries_copy)
for i in countries:
    print(i + " ", end="")
print()

# 3rd list
animals = ["Zebra", "Turkey", "Crab"]
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)
for a in animals:
    if "a" in a:
        print(a)
a = ["Arinda"]
b = ["Emmanuel", "Nsiimenta"]
a.extend(b)
print(a)
