# Demonstrate storage of heterogenous items

Name = {"John", "Snow", 10, 30, 100}
print(Name)
print(type(Name))

# Data Duplication

letters = {"a", "b", "c", "c", "a", "a"}
print(letters)
print(type(letters))

# Methods
# Use of the add method
letters.add("z")
print(letters)

Age = {20, 30, 40, 50}
students = {"Jackie", "Jackson", "Brian", "Hurdson"}
w = Age.union(students)
print(w)
print(type(w))
w.remove("Jackie")
print(w)

# Use of the update method
w.update({"John", "Snow"})
print(w)

# Other set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A.union(B))  # Union of A and B
print(A.intersection(B))  # Intersection of A and B
print(A.difference(B))  # Difference of A and B
print(B.difference(A))  # Difference of B and A
