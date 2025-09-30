# Все гласные на 2, выводим в обратном порядке. В противном случае выводим с конца каждую третию 
string = input("Введите строку: ")

glas = "АЕИОУЮЯЫЭуеыаоэяию"

if glas in string:
    result = string.replace('А', '2').replace('Е', '2').replace('И', '2').replace('О', '2').replace('У', '2').replace('Ю', '2').replace('Я', '2').replace('Ы', '2').replace('Э', '2').replace('а', '2').replace('е', '2').replace('и', '2').replace('о', '2').replace('у', '2').replace('ю', '2').replace('я', '2').replace('ы', '2').replace('э', '2')
    print(f"Строка после преобразования: {result}")
else:
    print(string[-1:3:])