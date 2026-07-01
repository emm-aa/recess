# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Animal name", self.name)


# # Define child class
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def info(self, cool):
#         print("The Dog's name is", self.name, cool)

#     def details(self):
#         print(self.name, "consists of", self.breed)


# z = Dog("Tough", "Rockpup")

# z.info(5)
# z.details()


class Base:
    def action(self):
        print("Base action")


class A(Base):
    def action(self):
        print("A action")
        super().action()


class B(Base):
    def action(self):
        print("B action")
        super().action()


class Child(B, A):
    def action(self):
        print("Child action")
        super().action()


x = Child()
print(Child.mro())
x.action()
