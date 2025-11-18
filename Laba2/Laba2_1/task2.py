input_data = input("Введите числа через пробел: ")

words_list = input_data.split()
num_list = [float(x) if '.' in x else int(x) for x in words_list]

unique_numbers = list(set(num_list))
print("1. Уникальные числа: ", unique_numbers)

repeating_numbers = []
for i in range(len(num_list)):
    counter = num_list.count(num_list[i])
    if counter > 1:
        counter = repeating_numbers.count(num_list[i])
        if counter == 0:
            repeating_numbers.append(num_list[i])
print("2. Повторяющиеся числа: ", repeating_numbers)            

even_numbers = [num for num in num_list if isinstance(num, int) and num % 2 == 0]
odd_numbers = [num for num in num_list if isinstance(num, int) and num % 2 != 0]
print("3. Чётные числа: ", even_numbers)
print("4. Нечётные числа: ", odd_numbers)

negative_numbers = [num for num in num_list if num < 0]
print("5. Отрицательные числа: ", negative_numbers)
    
float_numbers = [num for num in num_list if isinstance(num, float)]
print("6. Числа с плавающей точкой: ", float_numbers)
    
sum_multiple_5 = sum(num for num in num_list if isinstance(num, int) and num % 5 == 0)
print("7. Сумма чисел, кратных 5: ", sum_multiple_5)
    
max_number = max(num_list) if num_list else None
print("8. Самое большое число: ", max_number)

min_number = min(num_list) if num_list else None
print("9. Самое маленькое число: ", min_number)    
