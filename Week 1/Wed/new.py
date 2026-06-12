print(bool(0))  # Zero is falsy
print(bool(0.0))  # Zero float is falsy
print(bool(""))  # Empty string is falsy
print(bool([]))  # Empty list is falsy
print(bool({}))  # Empty dictionary is falsy
print(bool(set()))  # Empty set is falsy
print(bool(None))  # None is falsy

print("\n")
print(bool(1))  # Non-zero integer is truthy
print(bool(-1))  # Non-zero integer is truthy
print(bool(0.1))  # Non-zero float is truthy
print(bool("Hello"))  # Non-empty string is truthy
print(bool([1, 2, 3]))  # Non-empty list is truthy
print(bool({"key": "value"}))  # Non-empty dictionary is truthy
print(bool({1, 2, 3}))  # Non-empty set is truthy
print(bool(object()))  # Any object is truthy
