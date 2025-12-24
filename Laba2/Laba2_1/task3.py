input_data = input("Введите числа через пробел: ")

words_list = input_data.split()
num_list = []

for number in words_list:
    if '.' in number:
        num_list.append(float(number))
    else:
        num_list.append(int(number))

max = num_list[0]
for number in num_list:
    if number > max:
        pre_max = max
        max = number

print("Второе по величине число: ", pre_max)         