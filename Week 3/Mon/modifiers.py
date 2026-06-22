class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price

    def display_car(self):
        print(
            f"This is a {self.brand} car, mode, {self._model} and costs {self.__price}."
        )


test = Car("BMV", "T10", 10000)
test.display_car()

print("-----")
print(test.brand)


class MobileMoneyAccount:
    def __init__(self, balance):
        self.__balance = balance

    def balance(self):
        return self.__balance

    def deposit(self, number):
        self.__balance += number
        print("Cash deposited")

    def withdraw(self, number):
        if number > self.balance():
            print(f"Insufficient funds. Transaction for {number} failed.")
        else:
            self.__balance -= number

    def check_balance(self):
        print(f"Balance: {self.__balance}")


test = MobileMoneyAccount(20000)

test.deposit(30000)
print()
test.withdraw(60000)
test.check_balance()

from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start():
        print("Car starts")


class Bmw(Car):
    def start():

        pass


car1 = Bmw("Mozzarella")
car1.start


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        print(f"Area is {self.length*self.width}")

    def perimeter(self):
        print(f"Perimeter is {2*(self.length+self.width)}")


class Circle(Shape):
    def __init__(self, radius):
        self.r = radius

    def area(self):
        print(f"Area is : {3.14*self.r*self.r:.2f}")

    def perimeter(self):
        print(f"Perimeter is {2*3.14*self.r:,.2f}")


test = Rectangle(4, 5)
test.area()
test.perimeter()

test2 = Circle(5)
test2.area()
