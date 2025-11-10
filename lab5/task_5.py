goods = {"laptop" : 1, "headphones" : 7, "phone" : 3, "monitor" : 6}
print (goods)

print("Виводимо список кортежів: ",list(goods.items()))

print("\tВиводимо товари, в яких кількість менше 5: ")
for item in goods:
    if goods[item] < 5:
        print(item)

