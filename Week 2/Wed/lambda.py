# even number
even = lambda x: "even" if x % 2 == 0 else "odd"

print(even(4))

numbers = (1, 2, 3, 4, 5, 30)

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)

# filter number that is greater than 20

greater_than_20 = list(filter(lambda x: x > 20, numbers))

print(greater_than_20)

# using lambda

list = ["Cherry", "Banana", "Aate", "Apple", "Mango", "DragonFruit"]

list.sort(key=lambda x: len(x))

print(list)

factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)

print(factorial(3))


def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))


fibonacci = lambda a: (
    0 if a == 1 else 1 if a == 2 else fibonacci(a - 2) + fibonacci(a - 1)
)
print(fibonacci(4))


# returns nth fibo number
def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(3))


def binary_search(arr, target, left, right):
    mid = (left + right) // 2

    # Base case
    if arr[mid] == target:
        return str(arr[mid]) + " in list in position " + str(mid + 1)

    # Recursive cases
    elif arr[mid] < target and left < right:
        return binary_search(arr, target, mid + 1, right - 1)
    elif arr[mid] > target and left < right:
        return binary_search(arr, target, left, mid - 1)
    else:
        return "Not found"


sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
num = int(input("Enter number to find: "))
print(binary_search(sorted_array, num, 0, len(sorted_array)))
