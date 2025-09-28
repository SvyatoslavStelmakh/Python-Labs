str = input("Введите строку: ")
result = str.replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "").replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
print(f"Строка без гласных(a, e, i, o, u): {result}")