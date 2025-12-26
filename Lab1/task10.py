a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))

sum = a + b
difference = a - b
product = a * b

if b != 0:
    quotient = a / b
    remainder = a % b
else:
    quotient = "неопределено (деление на ноль)"
    remainder = "неопределено (деление на ноль)"

power = a ** b

print("\nРезультаты математических операций:")
print(f"Сумма: {a} + {b} = {sum}")
print(f"Разность: {a} - {b} = {difference}")
print(f"Произведение: {a} * {b} = {product}")

if b != 0:
    print(f"Частное: {a} / {b} = {quotient}")
    print(f"Остаток от деления: {a} % {b} = {remainder}")
else:
    print(f"Частное: {a} / {b} = {quotient}")
    print(f"Остаток от деления: {a} % {b} = {remainder}")

print(f"Возведение в степень: {a} ** {b} = {power}")