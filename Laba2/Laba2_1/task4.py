input_data1 = input("Введите первый набор чисел: ")
input_data2 = input("Введите второй набор чисел: ")

words_list = input_data1.split()
set1 = set()

for number in words_list:
    if '.' in number:
        set1.add(float(number))
    else:
        set1.add(int(number))

words_list = input_data2.split()
set2 = set()

for number in words_list:
    if '.' in number:
        set2.add(float(number))
    else:
        set2.add(int(number))

intersection = set1 & set2
print("Числа, которые присутствуют в обоих наборах одновременно: ", intersection)

only_in_set1 = set1 - set2
only_in_set2 = set2 - set1
print("Числа, которые присутствуют только в 1 наборе: ", only_in_set1)
print("Числа, которые присутствуют только во 2 наборе: ", only_in_set2)

symmetric_diff = set1 ^ set2
print("Числа из обоих наборов, кроме общих:: ", symmetric_diff)