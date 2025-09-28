string = input("Введите строку: ")
    
result_str = ""
current_char = string[0]
symbol_count = 1
    
for i in range(1, len(string)):
    if string[i] == current_char:
        symbol_count += 1
    else:
        result_str += current_char + str(symbol_count)
        current_char = string[i]
        symbol_count = 1
    
result_str += current_char + str(symbol_count)     # добавляем последний символ и его количество

print("Сжатая строка: ", result_str)
