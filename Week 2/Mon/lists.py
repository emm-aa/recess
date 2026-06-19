# Used to store ordered collection of items
# Mutable e.g can be changed,added, updated
# Store data of multiple data types

# Creating a List
# a = [1, 2, 3, 4, 5]
# print(a)
# print(type(a))

Food = ["Sugar", "beans", "Sauce", "Rice"]
# print(Food)
# print(type(Food))
# print(Food[0])
# print(Food[1])
# print(Food[-3])

a = [4, 5, 6]
c = [7, 8]
a.append(c)
print(a)

b = list((1, 2, 3, "Yam"))
b.append(a)
print(b)

print(b[4][3][1])
