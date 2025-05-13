# 13173249陳昱諺

# 載入numpy套件
import numpy as np

# 定義原始矩陣
original_A = np.array([[1, -1, 0, 2, -3], 
              [-2, 6, 3, -1, 1], 
              [0, 2, -4, 4, 2]])

# 第1列和第3列交換(第7題)
A = original_A.copy()
A[[0, 2]] = A[[2, 0]]
print("(第7題)Interchange rows 1 and 3:\n", A)

# 將第1列乘以-3(第8題)
A = original_A.copy()
A[0] = -3 * A[0]
print("(第8題)Multiply row 1 by -3:\n", A)

# 將2倍第1列加到第2列(第9題)
A = original_A.copy()
A[1] = A[1] + 2 * A[0]
print("(第9題)Add 2 times row 1 to row 2:\n", A)

# 第1列和第2列交換(第10題)
A = original_A.copy()
A[[0, 1]] = A[[1, 0]]
print("(第10題)Interchange rows 1 and 2:\n", A)

# 將第3列乘以1/2 (第11題)
A = original_A.copy()
A[2] = 1/2* A[2]
print("(第11題)Multiply row 3 by 1/2:\n", A)

# 將-3倍第3列加到第2列(第12題)
A = original_A.copy()
A[1] = A[1] + -3 * A[2]
print("(第12題)Add -3 times row 3 to row 2:\n", A)

# 將4倍第2列加到第3列(第13題)
A = original_A.copy()
A[2] = A[2] + 4 * A[1]
print("(第13題)Add 4 times row 2 to row 3:\n", A)

# 將2倍第1列加到第3列(第14題)
A = original_A.copy()
A[2] = A[2] + 2 * A[0]
print("(第14題)Add 2 times row 1 to row 3:\n", A)