name1 = input("Enter first name: ")
name2 = input("Enter last name: ")
birth_year = int(input("Enter year of birth: "))
city = input("Enter current city: ")

current_year = 2026
age = current_year - birth_year
print(f"""
The user's name is {name1} {name2},
supposedly residing in {city},\n{age} years of age.""")
