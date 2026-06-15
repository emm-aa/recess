age_0 = int(input("Enter the age of first person: "))
age_1 = int(input("Enter the age of second person: "))


if age_0 >= 21 and age_1 >= 21:
    print("Both are adults. Entrance allowed.")
elif age_0 >= 21 or age_1 >= 21:
    print("One of them is an adult. Enter with trusted adult.")
else:
    print("You are not allowed to enter.")
