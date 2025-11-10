A = {2, 8, 6, 13, 4, 6}
B = {15, -4, 339, 1505, 6}
C = {2, 13, 8}
print(A)

print("\n\tДодавання/Віднімання")
A.add(100)
print(A)
A.remove(100)
print(A)
A.discard(4)
print(A)

print("\n\tОперації над множинами")
print("1-ша множина: ",A)
print("2-га множина: ",B)

print("\tПерший спосіб(через методи):")
print("Об'єднання множин", A.union(B))
print("Перетин множин", A.intersection(B))
print("Різниця множин", A.difference(B))
print("Симетрична різниця множин", A.symmetric_difference(B))

print("\tДругий спосіб(через оператори):")
print("Об'єднання множин", A | B)
print("Перетин множин", A & B)
print("Різниця множин", A - B)
print("Симетрична різниця множин", A ^ B)

print("\n\tПорівняння множин: ")
print("1-ша множина: ",A)
print("2-га множина: ",C)
print(A < C)
print(A > C)
print(A <= C)
print(A >= C)

print("Перетворення: ")
print("Перетворення на list: ")
my_list1 = list(A)
print(my_list1)
print(type(my_list1))
print("Перетворення на set: ")
my_list2 = [29, 103, 58, 47]
my_set = set(my_list2)
print(my_set)
print(type(my_set))

