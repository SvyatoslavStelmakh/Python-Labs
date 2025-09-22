money = int(input('Введите сумму в рублях(целое число): '))

kupury_100 = money // 100
ostatok = money % 100

kupury_50 = ostatok // 50
ostatok %= 50

kupury_10 = ostatok // 10
ostatok %= 10

kupury_5 = ostatok // 5
ostatok %= 5

monety_2 = ostatok // 2
monety_1 = ostatok % 2

print(f"Для размена суммы {money} потребуется:")
print(f"купюр по 100 рублей: {kupury_100}")
print(f"купюр по 50 рублей: {kupury_50}")
print(f"купюр по 10 рублей: {kupury_10}")
print(f"купюр по 5 рублей: {kupury_5}")
print(f"монет по 2 рубля: {monety_2}")
print(f"монет по 1 рублю: {monety_1}")