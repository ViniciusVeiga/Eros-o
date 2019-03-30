import cv2
import numpy as np

WHITE = [255,255,255]

iPadrao = cv2.imread('./img/padrao.png', 0)
iMenor = cv2.imread('./img/menor.png', 0)
iBorda = cv2.copyMakeBorder(iPadrao, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value = WHITE)

row, col = iPadrao.shape
rowMenor, colMenor = iMenor.shape
rowBorda, colBorda = iBorda.shape

array10x10 = np.zeros((row, col), dtype=np.int32)
array3x3 = np.zeros((rowMenor, colMenor), dtype=np.int32)
arrayBorda = np.zeros((rowBorda, colBorda), dtype=np.int32)

print('\n10x10:')
for i in range(row):
    for j in range(col):
        array10x10[i, j] = -((iPadrao[i, j] / 255) - 1)
        print(array10x10[i, j], end=' ')
    print('')

print('\n3x3:')
for i in range(rowMenor):
    for j in range(colMenor):
        array3x3[i, j] = -((iMenor[i, j] / 255) - 1)
        print(array3x3[i, j], end=' ')
    print('')

for i in range(rowBorda):
    for j in range(colBorda):
        arrayBorda[i, j] = -((iBorda[i, j] / 255) - 1)

for i in range(row):
    for j in range(col):
        count = 0
        if array3x3[int(rowMenor / 2), int(colMenor / 2)] == arrayBorda[i, j]:
            for a in range(rowMenor):
                for b in range(colMenor):
                    if array3x3[a, b] == arrayBorda[(i - int(rowMenor / 2)) + a, (j - int(colMenor / 2)) + b]:
                        count += 1
        if count == rowMenor * colMenor:
            for a in range(rowMenor):
                for b in range(colMenor):
                    arrayBorda[(i - int(rowMenor / 2)) + a, (j - int(colMenor / 2)) + b] = 2
            arrayBorda[i, j] = 5

print('\nResultado:')
for i in range(1, row + 1):
    for j in range(1, col + 1):
        if arrayBorda[i, j] == 5:
            arrayBorda[i, j] = 1
        else:
            arrayBorda[i, j] = 0
        print(arrayBorda[i, j], end=' ')
    print('')

cv2.destroyAllWindows()