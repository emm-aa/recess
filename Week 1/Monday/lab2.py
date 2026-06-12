age = int(input("Enter age: "))

if 0 > age < 6:
    print("You are not a toddler")
elif 0 > age < 13:
    print("You're a pre-teen")
else:
    print("You are aged / do not exist")


name = "Golberg"
age = 25
height = 200

# formatted string
print(f"""name: {name} Age: {age} Height: {height}" 
All is well that ends well""")
