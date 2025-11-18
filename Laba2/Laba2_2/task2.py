def merge_dicts(dict_a, dict_b):
    for key, value in dict_b.items():
        if key in dict_a:       # если ключ из dict_b есть в dict_a
            if isinstance(dict_a[key], dict) and isinstance(value, dict):   # проверяем, являются ли оба значения словарями 
                merge_dicts(dict_a[key], value) # если являются, то рекурсивно сливаем их
            elif isinstance(dict_a[key], (list, tuple, set)) and isinstance(value, (list, tuple, set)): # если оба значения коллекции (списки, кортежи, множества), объединяем их
                # если являются, то рекурсивно сливаем их функций, в зависимости от типа коллекции
                if isinstance(dict_a[key], list):
                    dict_a[key].extend(value)
                elif isinstance(dict_a[key], tuple):
                    dict_a[key] = dict_a[key] + value
                elif isinstance(dict_a[key], set):
                    dict_a[key].update(value)
            else:
                dict_a[key] = value  # если типы простые или не совпадают, то заменяем значение из dict_a значением из dict_b
        else:
            dict_a[key] = value     # если ключа нет в dict_a, добавляем пару ключ-значение из dict_b

print("Пример работы функции")
dict_a = {"a": 1, "b": {"c": 1, "f": 4}, (1, 2, 3): {"1": 1, "2": 2}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}, (1, 2, 3): 3}

print(f"dict_a = {dict_a}")
print(f"dict_b = {dict_b}")

merge_dicts(dict_a, dict_b)
print("Результат после слияния")
print(f"dict_a = {dict_a}") 