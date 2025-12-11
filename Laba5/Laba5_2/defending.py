# Функция которая считает сумму всех чисел кратных 3(передаем число, )

def sum_kratniy_3(number):

    if not isinstance(number, int):
        raise ValueError("Недопустимое значение для функции")

    total = 0
    if number >= 0:
        for i in range(number + 1):
            if i % 3 == 0:
                total += i
    else:
        number = abs(number)
        for i in range(number + 1):
            if i % 3 == 0:
                total -= i
    
    return total
    

print(sum_kratniy_3(-12))