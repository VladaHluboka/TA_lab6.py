text = "Edge-cases: empty, null, None, zero."
text = text.lower()

import string
punct = string.punctuation.replace("-", "")
for ch in punct:
    text = text.replace(ch, "")
text_list = text.split()
print(text_list)

print("\tСтворюємо мн. унікальних слів:")
text_set = set(text_list)
print(text_set)

print("\tВідсортований кортеж:")
sorted_list = list(text_set)
sorted_list.sort(key = len)
text_tuple = tuple(sorted_list)
print(text_tuple)

print("\tБудуємо словник частот появи слів:")
words_count = {}
for word in text_list:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
print(words_count)

print("\tВиводимо статистику:")

print("Скільки слів у реченні: ", len(text_list))

print("Кількість унікальних слів: ",len(text_set))

top_5 = sorted(words_count.items(), key=lambda x: x[1]) [:5]
print("Топ-5 найчастіших:", top_5)

