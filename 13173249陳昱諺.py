# 載入numpy套件
import numpy as np

#打出矩陣A1、B1、A2、B2
A1 = np.array([[2, -1, 5], 
              [3,  4, 1]])

B1 = np.array([[1,  0, -2], 
              [2,  3,  4]])

A2 = np.array([[3, -1, 2, 4],
               [1, 5, -6, -2]])

B2 = np.array([[-4, 0],
               [2, 5],
               [-1, -3],
               [0, 2]])

# 計算 4A - 2B (第3題)
result_3 = 4 * A1 - 2 * B1

# 計算 A^T + 2B^T (第6題)
result_6 = A1.T + 2 * B1.T

# 計算 3A + 2B^T (第20題)
result_20 = 3 * A2 + 2 * B2.T

# 計算 (B ^ T - A) ^ T
result_24 = (B2.T - A2).T
# 顯示結果
print("(第3題) 4A - 2B:\n", result_3)
print("\n(第6題) A^T + 2B^T:\n", result_6)
print("\n(第20題) 3 * A2 + 2 * B2^T:\n", result_20)
print("\n(第24題) (B2^T - A2)^T:\n", result_24)