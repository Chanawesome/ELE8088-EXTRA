import numpy as np
import cvxpy as cp

# cvxpy
c = np.zeros(100)
for i in range(100):
    if i % 2 == 0:
        c[i] = -1
    else:
        c[i] = 1
x = np.ones(100)
x_cp = cp.Variable(100)
objective = cp.Minimize(2 * cp.sum_squares(x_cp) + 3 * cp.sum(x_cp[0:50]) + 2022)
constraints = [c.T @ x_cp == 100]
prob = cp.Problem(objective, constraints)
prob.solve()
x_star_cp = x_cp.value
f_star_cp = prob.value
print(x_star_cp)
print(f_star_cp)

# solution
b = 3 * np.ones(50)
b = np.hstack((b, np.zeros(50)))
lambda_ = (400 + np.dot(c, b)) / (np.dot(c, c))
x_star = (c * lambda_ - b) / 4
f_star = 2 * np.dot(x_star, x_star) + 3 * np.ones(50) @ x_star[0:50] + 2022
print(x_star)
print(f_star)