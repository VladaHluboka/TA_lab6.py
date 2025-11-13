def item_max(my_list):
    """
    Шукає максимальний елемент у кожному підсписку вкладеного списку
    Параметр:
        my_list: список
    Повертає:
        max_values: список максимальних значень у кожному підписку
    """
    try:
        max_values = []
        for sublist in my_list:
            if sublist:
                maxi = sublist[0]
                _ = [maxi := item for item in sublist if item > maxi]
                max_values.append(maxi)
        return max_values
    except SyntaxError:
        print("Проблема в підсписку")



list1 = [[3, 5, 1], [10, 2, 8], [7, 9], []]
print(item_max(list1))




