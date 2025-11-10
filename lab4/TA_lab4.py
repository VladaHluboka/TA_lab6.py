#1
print('\nЗадання 1:')
numbers1 = [12, 2, 24]
#Середнє арифметичне
average = sum(numbers1) / len(numbers1)
print(average)
#добуток між найбільшим та найменшим
mult = min(numbers1) * max(numbers1)
print(mult)
#різниця між найбільшим та найменшим
dif = max(numbers1) - min(numbers1)
print(dif)

#2
print('\nЗадання 2:')
sentence = 'В цьому реченні рахуються Слова, Що починаються З Великої літери'
words = sentence.split()
count = sum(1 for word in words if word[0].isupper())
print(count)

#3
print('\nЗадання 3:')
number3 = int(input("Введіть будь-яке число: "))
if number3 > 50 or number3 % 7 == 0:
    print('Так')
else: print('Ні')

#4
print('\nЗадання 4:')
N = 40
for i in range(1, N + 1):
    if i * i < 500:
     print(i * i)

#5
print('\nЗадання 5:')
numbers5 = []
a = 0
num5 = int(input('Введіть число (0 для завершення): '))
while num5 != 0:
    numbers5.append(num5)
    num5 = int(input('Введіть число (0 для завершення): '))
if numbers5:
    average5 = sum(numbers5) / len(numbers5)
    print('Середнє значення =', average5)
    print('Числа менші за середнє:')
    for a in numbers5:
        if a < average5:
            print(a)
else:
    print('Числа не були введені')


