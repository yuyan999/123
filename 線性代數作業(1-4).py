# 13173249陳昱諺

# 載入numpy套件、從 scipy.linalg 模組引入 solve 函式
import numpy as np
from scipy.linalg import solve

# 定義矩陣A9(第9題)
original_A9 = np.array([
    [1, -1, -3, 1, 0],
    [-2, 1, 5, 0, -4],
    [4, -2, -10, 1, 5]])


# 定義矩陣A11(第11題)
original_A11 = np.array([
    [1, 3, 1, 1, -1],
    [-2, -6, -1, 0, 5],
    [1, 3, 2, 3, 2]])

# 定義矩陣A13(第13題)
original_A13 = np.array([
    [1, 2, 1, 1],
    [-2, -4, -1, 0],
    [5, 10, 3, 2],
    [3, 6, 3, 4]])

print('第9題')
print('第9 11 13題使用高斯消去法')
print(original_A9)
print('-------------------------')
# 將2倍第2列加到第3列，將1倍第2列加到第1列
A9 = original_A9.copy()
A9[2] = A9[2] + 2 * A9[1]
A9[0] = A9[0] + 1 * A9[1]
print(A9)

# 得知 X4 = -3 ，設 X3 = X3(X3有無限多組解)
print("-X1+2*X3-3=-4   X1 = 1+2*X3") #第1列求出來
# 得知 X1 = 1-2X3
print("-2(1+2*X3)+X2+5*X3+0=-4 -2-4*X3+X2+5*X3=-4  X2 = -1*X3-2") #第2列求出來
print("得知第9題有無限多組解 X1 = 1+2*X3   X2 = -2-1*X3  X3 = free   X4 = -3")
print('-------------------------')

print('第11題')
print(original_A11)
print('-------------------------')
# 將2倍第1列加到第2列，將-1倍第1列加到第3列，再將-1倍的第二列加到第3列
A11 = original_A11.copy()
A11[1] = A11[1] + 2 * A11[0]
A11[2] = A11[2] + -1 * A11[0]
A11[2] = A11[2] + -1 * A11[1]
print(A11)
print('第三列係數和常數項都為0 得知此線性方程組為無限多組解')
# 設 X4 = X4(X4有無限多組解)
print('X3+2*X4=3  X3=3-2*X4') #從第2列求出
# 設 X2 = X2(X2有無限多組解)
print('X1+3*X2+3-2*X4+X4=-1  X1=-3*X2-3+2*X4-X4-1 X1=-3*X2+X4-4') #從第1列求出
print("第11題有無限多組解 X1 = -4-3*X2+X4   X2 = free  X3 = 3-2*X4  X4 = free")
print('-------------------------')

print('第13題')
print(original_A13)
print('-------------------------')
# 將-3倍第1列加到第4列
A13 = original_A13.copy()
A13[3] = A13[3] + -3 * A13[0]
print(A13)
print('第四列係數為0 但常數項不為0 得知第13題的線性方程組無解')
print('第13題無解 not consistent')