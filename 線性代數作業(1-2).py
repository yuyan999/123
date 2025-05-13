# 13173249陳昱諺

# 載入sympy套件、# 載入numpy套件
import sympy as sp

import numpy as np

# -------------------------

# 定義符號變數 a 和 b
a, b = sp.symbols('a b')

# 定義矩陣 A1
A1 = sp.Matrix([[1, 0], 
                [0, 1]])

# 定義向量 v1
v1 = sp.Matrix([[a], 
               [b]])

# 計算 A1 * v (第5題)
result_5 = A1 * v1

# 轉換為 NumPy 陣列
result_np = np.array(result_5).astype(object)

print("(第5題) A1 * V1:\n", result_np)

# -------------------------

# 定義符號變數 s、t、u
s,t,u = sp.symbols('s t u')

# 定義符號變數 a、b、c
a,b,c = sp.symbols('a b c')

# 定義矩陣 A2
A2 = sp.Matrix([[s, 0, 0], 
                [0, t, 0],
                [0, 0, u]])

# 定義向量 v2
v2 = sp.Matrix([[a], 
               [b],
               [c]])              

# 計算 A2 * v2 (第9題)
result_9 = A2 * v2

# 轉換為 NumPy 陣列
result_np = np.array(result_9).astype(object)

print("(第9題) A2 * V2:\n", result_np)

# -------------------------

# 定義矩陣 A 和 B
A = np.array([[2.1, 1.3, -0.1, 6.0],
    [1.3, -9.9, 4.5, 6.2],
    [4.4, -2.2, 5.7, 2.0],
    [0.2, 9.8, 1.1, -8.5]])

B = np.array([[4.4, 1.1, 3.0, 9.9],
    [-1.2, 4.8, 2.4, 6.0],
    [1.3, 2.4, -5.8, 2.8],
    [6.0, -2.1, -5.3, 8.2]])

# 定義向量 u 和 v
u = np.array([1, -1, 2, 4])
v = np.array([7, -1, 2, 5])

print("(第91題)")

# (a) 計算 Au
Au = np.dot(A, u)
print("(a) Au =", Au)

# (b) 計算 B(u + v)
Bu_v = np.dot(B, u + v)
print("(b) B(u + v) =", Bu_v)

# (c) 計算 (A + B)v
AB_v = np.dot(A + B, v)
print("(c) (A + B)v =", AB_v)

# (d) 計算 A(Bv)
ABv = np.dot(A, np.dot(B, v))
print("(d) A(Bv) =", ABv)