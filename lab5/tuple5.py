my_tuple = (1, 2, 3, 1)
print(my_tuple)
print(my_tuple[-1])

# my_tuple.append(100)
# print(my_tuple)
#Кортеж неможливо змінити після створення

print("\nОперації + та *")
my_t2 = (4, 5, 6)
result = my_tuple + my_t2
print(result)
result2 = my_t2 * 2
print(result2)

print ("\ncount(), index()")
print(my_tuple.count(1))
print(my_tuple.index(3))

print("Перетворення: tuple(list)")
my_list = [1, 2]
my_tuple3 = tuple(my_list)
print(my_tuple3)
print(type(my_tuple3))