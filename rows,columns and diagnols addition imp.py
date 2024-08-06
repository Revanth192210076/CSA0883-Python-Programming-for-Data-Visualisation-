#columns
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

col_sums = []
for j in range(len(matrix[0])):  
    col_sum = 0
    for i in range(len(matrix)): 
        col_sum += matrix[i][j]
    col_sums.append(col_sum)

print(col_sums)



#rows
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    sum = 0
    for element in row:
        sum += element
    print(sum)


#Diagnols

import numpy as np
a = [[11,2,4],[4,5,6],[10,8,-12]]
b = np.asarray(a)
print('Diagonal (sum): ', np.trace(b))
print('Diagonal (elements): ', np.diagonal(b))


#nrml
def sum_of_diagonals(matrix):

  n = len(matrix)
  primary_sum = 0
  secondary_sum = 0

  for i in range(n):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][n - i - 1]

  return primary_sum + secondary_sum

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(sum_of_diagonals(matrix))
