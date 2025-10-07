number = input("Введите число: ")

sum_digits = sum(int(digit) for digit in number)

if int(number) % 7 == 0:
    print("Магическое число!")
else:
    print(f"Сумма цифр: {sum_digits}")