class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"Welcome to {self.restaurant_name}\nWe serve various cuisines, mainly {self.cuisine_type}"
        )

    def open_restaurant():
        print(f"Hey, the restaurant is open!")


restaurant1 = Restaurant("Milky Way", "Salads n' Dressings")
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)

restaurant1.describe_restaurant()
restaurant1.open_restaurant
print("\n-----")

item1 = Restaurant("Ndegs and Stegs", "Meats")
item2 = Restaurant("Blue Dining", "Milkshakes")
item3 = Restaurant("Cool Drinks", "Beverages")

item1.describe_restaurant()
item2.describe_restaurant()
item3.describe_restaurant()


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(input(f"Enter age for {self.first_name}: "))
        self.colour = input("Enter favourite colour: ")

    def describle_user(self):
        print(
            f"The user is {self.first_name} {self.last_name}, who is {self.age}\nThis person likes the colour {self.colour}"
        )

    def greet_user(self):
        print(f"Welcome {self.first_name}!")


print("----")
person = User("Emm", "Plura")
person1 = User("Jackson", "Mbuya")
print("-----")
person.describle_user()
person1.greet_user()
