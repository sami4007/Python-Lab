import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

column_sum = np.sum(arr, axis=0)
row_sum = np.sum(arr, axis=1)

print("Column sums:", column_sum)
print("Row sums:", row_sum)