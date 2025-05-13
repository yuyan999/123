from sympy import symbols, Matrix, Eq, solve

# Define unknown variable r
r = symbols('r')

# Problem 17: Solve for r
S_17 = Matrix([[1, -1], [0, 3], [-1, 2]])
v_17 = Matrix([2, r, -1])
x_17 = symbols('x1 x2')
eqs_17 = S_17 * Matrix(x_17) - v_17
sol_17 = solve(eqs_17, x_17 + (r,))

# Problem 19: Solve for r
S_19 = Matrix([[-1, -1], [2, 1], [2, 0]])
v_19 = Matrix([2, r, -8])
x_19 = symbols('y1 y2')
eqs_19 = S_19 * Matrix(x_19) - v_19
sol_19 = solve(eqs_19, x_19 + (r,))

print("Solution for problem 17:", sol_17)
print("Solution for problem 19:", sol_19)
