def unique_elements(nested_list):
    
    def flatten_and_collect(lst, result_set):
        
        for item in lst:
            if isinstance(item, list):
                flatten_and_collect(item, result_set)
            else:
                result_set.add(item)
    

    unique_set = set()
    flatten_and_collect(nested_list, unique_set)
    
    return list(unique_set)

# пример работы функции
list1 = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
result = unique_elements(list1)
print(result)