num_list = [0,0,1,0,2,0,3]
print(num_list)

print("\tВидаляємо дублікати: ")
seen = set()
no_dup = []
for x in num_list:
    if x not in seen:
        seen.add(x)
        no_dup.append(x)
print(no_dup)

print("\tВиводимо парні числа у множині: ")
num_set = set(num_list)
for num in num_set:
    if num % 2 == 0:
        print(num)

print("\tВиводимо кортеж топ-5 мінмальних чисел: ")
num_sorted = sorted(num_list)
num_tuple = tuple(num_sorted)
min_num = num_tuple[0:5]
print(min_num)

print("\tБудуємо словник позиція - значення:")
num_dict = dict(enumerate(num_list))
print(num_dict)

print("\tВиводимо статистику: ")

print("Кількість чисел у списку: ",len(num_list))

seen2 = set()
dup = []
for item in num_list:
    if item in seen2 and item not in dup:
        dup.append(item)
    seen2.add(item)
print("Вивести дублікати: ", dup)

print("Виводимо мінімум списку:", min(num_list))

print("Виводимо максимум списку:", max(num_list))
