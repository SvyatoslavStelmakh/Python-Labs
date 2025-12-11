# Функция которая считает сумму всех чисел кратных 3(передаем число, )

def sum_kratniy_3(number):

    if not isinstance(number, int):
        raise ValueError("Недопустимое значение для функции")

    if number < 0:
        raise ValueError("Число не может быть отрицательным")
    
    total = 0
    for i in range(number + 1):
        if i % 3 == 0:
            total += i
    
    return total
    
