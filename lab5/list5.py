#Створення списків
num = [1, 5, 3, 12, 7, 0, 9]
print(num)
items = num[5]
print(items)

print("\tДодавання:")
num.append(100)
print(num)
num2 = [220, 1212, 2]
num.extend(num2)
print(num)
num.insert(3, 2220)
print(num)

print("\tВидалення:")
num.remove(2220)
print(num)
num.pop() #Видалє останній ел.
num.pop(0) #Видаляє з індексом 0
print(num)
del num[3:5]
print(num)

print("\tСортування:")
num.sort()
print(num)
sorted_num = sorted(num)
print(sorted_num)
num.reverse()
print(num)

length = len(num)
print(f"\tДовжина: {length} ")

print("\tSlicing:")
print(num[::-1]) #перевертає рядок
print(num[1:7:2]) #[start:end:step]
print(num[::5]) #бере з кроком 5
print(num[:1]) #ел. від початку до кінця[1]
print(num[3:6]) #[start:end]

print("Перетворення")
my_tuple = (1, 2, 3, 1)
num = list(my_tuple)
print(num)
my_set = {1, 2, 3, 1}
num = list(my_set)
print(num)

