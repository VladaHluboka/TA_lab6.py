numbers = {1 : "first", 2 : "second", 3 : "third"}
print(numbers)

print("\nМетоди:")
num1 = numbers.get(1)
print(num1)

print(numbers.items())

print(numbers.keys())

print(numbers.values())

removed = numbers.pop(1)
print("\n",numbers)
print("Видалене значення:", removed)

numbers2 = {4 : "four", 5 : "five"}
numbers.update(numbers2)
print("\nОновлення словника:",numbers)

print("\nПеретворення:")

list_key = list(numbers.keys())
list_value = list(numbers.values())

print("Ключі",list_key)
print("Значення", list_value)

