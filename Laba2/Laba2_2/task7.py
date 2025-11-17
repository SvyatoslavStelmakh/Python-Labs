def merge_sorted_list(list1, list2):
    
    result = []
    i = j = 0
    
    # савниваем элементы обоих списков и добавляем меньший в результат
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # добавляем оставшиеся элементы из первого списка (если есть)
    while i < len(list1):
        result.append(list1[i])
        i += 1
    
    # добавляем оставшиеся элементы из второго списка (если есть)
    while j < len(list2):
        result.append(list2[j])
        j += 1
    
    return result

input_data = input("Введите первый список через пробел: ")
list1 = map(int, input_data.split())
list1 = sorted(list1)

input_data = input("Введите второй список через пробел: ")
list2 = map(int, input_data.split())
list2 = sorted(list2)

print("Примеры работы функции")
merged = merge_sorted_list(list1, list2)
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"merged: {merged}")

