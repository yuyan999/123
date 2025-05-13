# 13173249陳昱諺

# 導入 SymPy 函式庫
from sympy import symbols, Matrix, Eq, solve

# 定義r為符號變數
r = symbols('r')

# 第17題 定義矩陣S和定義向量V，r是未知數
S_17 = Matrix([[1, -1], [0, 3], [-1, 2]])
v_17 = Matrix([2, r, -1])

# x是係數向量
x_17 = symbols('x1 x2')

# 將方程式轉換成矩陣運算並求出r
eqs_17 = S_17 * Matrix(x_17) - v_17
sol_17 = solve(eqs_17, x_17 + (r,))

# 第19題 定義矩陣S和定義向量V，r是未知數
S_19 = Matrix([[-1, -1], [2, 1], [2, 0]])
v_19 = Matrix([2, r, -8])

# y是係數向量
x_19 = symbols('y1 y2')

# 將方程式轉換成矩陣運算並求出r
eqs_19 = S_19 * Matrix(x_19) - v_19
sol_19 = solve(eqs_19, x_19 + (r,))

print("第17題:", sol_17)
print("第19題:", sol_19)