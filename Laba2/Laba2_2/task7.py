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

print("Примеры работы функции")
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged = merge_sorted_list(list1, list2)
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"merged: {merged}")

list3 = []
list4 = [1, 2, 3]
merged2 = merge_sorted_list(list3, list4)
print(f"\nlist3: {list3}")
print(f"list4: {list4}")
print(f"merged: {merged2}")
