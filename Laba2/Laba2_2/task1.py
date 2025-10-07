def flatten_list(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            flatten_list(lst[i])
            lst[i:i+1] = lst[i]       # вставляем элементы сглаженного списка на место текущего элемента
        else:
            i += 1

print("Пример работы функции\n")
list1 = [[1, [2, 3, [4, 5, 6]], 8, 9], 10]
print(f"Исходный список: {list1}")
flatten_list(list1)
print(f"Сглаженный список: {list1}")  