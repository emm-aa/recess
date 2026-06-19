computers = ("HP", "Mac", "Apple")
print(computers)
fake, *others = computers

# print(fake)

# others.append("Cool")
# print(tuple(others))

# # Concactenate
# computers = computers + ("Sony",)
# print(computers)

# Append
compute = list(computers)
compute.append("Microsoft")
computers = tuple(compute)
print(computers)
