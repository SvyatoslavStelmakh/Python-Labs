def transpose_matrix(matrix):
    
    if not matrix or not matrix[0]:
        return []
    
    transposed = []
    for j in range(len(matrix[0])):
        new_row = []
        for i in range(len(matrix)):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = []
row = []

print("Вводите элементы матрицы построчно, разделяя их пробелами")

for i in range(rows):
    row_input = input()
    row = list(map(int, row_input.split()))
    matrix.append(row)

print("Исходная матрица")
for row in matrix:
    print(row)

transpose = transpose_matrix(matrix)

print("Транспонированная матрица")
for row in transpose:
    print(row)