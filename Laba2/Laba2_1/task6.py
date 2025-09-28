input_data = input("Введите через пробел список, состоящий их любых элементов: ")

list = input_data.split()

result = []
for item in list:
    if item not in result:
        result.append(item)

print("Список без дубликатов:", result)