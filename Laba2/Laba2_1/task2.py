input_data = input("Введите числа через пробел: ")

num_words = input_data.split()
numbers = []

for number in num_words:
    if '.' in number:
        numbers.append(float(number))
    else:
        numbers.append(int(number))

unique_numbers = list(set(numbers))
print("1. Уникальные числа: ", unique_numbers)

repeating_numbers = []
for i in range(len(numbers)):
    counter = numbers.count(numbers[i])
    if counter > 1:
        counter = repeating_numbers.count(numbers[i])
        if counter == 0:
            repeating_numbers.append(numbers[i])
print("2. Повторяющиеся числа: ", repeating_numbers)            

even_numbers = [num for num in numbers if isinstance(num, int) and num % 2 == 0]
odd_numbers = [num for num in numbers if isinstance(num, int) and num % 2 != 0]
print("3. Чётные числа: ", repeating_numbers)
print("4. Нечётные числа: ", repeating_numbers)

negative_numbers = [num for num in numbers if num < 0]
print("5. Отрицательные числа: ", repeating_numbers)
    
float_numbers = [num for num in numbers if isinstance(num, float)]
print("6. Числа с плавающей точкой: ", repeating_numbers)
    
sum_multiple_5 = sum(num for num in numbers if isinstance(num, int) and num % 5 == 0)
print("7. Сумма чисел, кратных 5: ", repeating_numbers)
    
max_number = max(numbers) if numbers else None
print("8. Самое большое число: ", repeating_numbers)

min_number = min(numbers) if numbers else None
print("9. Самое маленькое число: ", repeating_numbers)    
