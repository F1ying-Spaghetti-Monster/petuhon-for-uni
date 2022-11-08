from numpy import sqrt
from main import newNulMatrix, printMatrix


def decompose(A):
    B  = newNulMatrix(len(A), len(A))
    B[0][0] = sqrt(A[0][0])
    for i in range(1, len(A)):
        B[i][0] = A[i][0]/B[0][0]
        temp = 0
        for j in range(i):
            temp += B[i][j] * B[i][j]
        B[i][i] = sqrt(A[i][i] - temp) 
        temp = 0
        for j in range(i+1, len(A)):
            for k in range(i-1):
                temp += B[i][k] * B[j][k]
            B[j][i] = (A[j][i]-temp)/A[i][i]
    printMatrix(B)
    return B

# A = [[1,1,1],[2,1,7],[3,4,9]]
A = [[1,1,1],[1,2,0],[1,0,5]]
# A = [[2,1],[1,2]]
decompose(A)
