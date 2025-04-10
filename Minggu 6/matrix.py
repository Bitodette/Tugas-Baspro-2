matrix1 = [
    [2, 3, 2, 3, 2],
    [4, 2, 4, 2, 4],
    [2, 5, 2, 5, 2],
    [1, 2, 1, 2, 1],
    [3, 3, 2, 3, 3]
]

matrix2 = [
    [2, 3, 2, 3, 2],
    [4, 2, 4, 2, 4],
    [2, 5, 2, 5, 2],
    [1, 2, 1, 2, 1],
    [3, 3, 2, 3, 3]
]

result_matrix = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix2[0])):
        sum = 0
        for k in range(len(matrix2)):
            sum += matrix1[i][k] * matrix2[k][j]
        row.append(sum)
    result_matrix.append(row)

# hasil
print("Hasil perkalian matriks:")
for row in result_matrix:
    print(row)