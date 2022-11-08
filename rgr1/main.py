"""Програма розв'язання СЛР за допомоги методу Холецького"""

def printMatrix(matrA):
    for i in matrA:
        for j in i:
            print(f'{j:<5}', end=' ')
        print()

def newNulMatrix(i, j):
    matrixA = []
    for _ in range(i):
        temp = []
        for _ in range(j):
            temp.append(0)
        matrixA.append(temp)
    return matrixA

def editMatrix(matrA):
    for idx1, i in enumerate(matrA):
        for idx2, _ in enumerate(i):
            matrA[idx1][idx2] = input()

# matrixA = newNulMatrix(3, 5)
# editMatrix(matrixA)
# printMatrix(matrixA)

