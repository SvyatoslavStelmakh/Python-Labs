import copy

def merge_dicts(dict_a, dict_b):
    
    result = copy.deepcopy(dict_a)  # Создаем копию первого словаря
    
    for key, value in dict_b.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_dicts(result[key], value)
            elif isinstance(result[key], (list, tuple, set)) and isinstance(value, (list, tuple, set)):
                if isinstance(result[key], list) and isinstance(value, list):
                    result[key] = result[key] + value
                elif isinstance(result[key], tuple) and isinstance(value, tuple):
                    result[key] = result[key] + value
                elif isinstance(result[key], set) and isinstance(value, set):
                    result[key] = result[key] | value
                else:
                    # Разные типы коллекций - заменяем значением из dict_b
                    result[key] = value
            else:
                # Простые типы или несовпадающие типы - заменяем значением из dict_b
                result[key] = value
        else:
            # Ключа нет в результате, просто добавляем
            result[key] = value
    
    return result