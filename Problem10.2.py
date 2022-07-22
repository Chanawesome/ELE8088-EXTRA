import numpy as np
import cvxpy as cp

# cvxpy
n = 3
m = 2
A = np.array([[1, 2, 3], [0, 1, -2], [1, -1, 1]])
B = np.array([[1, 1], [2, 0], [0, 3]])
x0 = np.array([0, 1, -2])
xn = np.array([2, 1, 3])
x00 = x0 - xn
N = 3
x_0 = cp.Parameter(n)        # <--- x is a parameter of the optimisation problem P_N(x)
u_seq = cp.Variable((m, N))     # <--- sequence of control actions
x_seq = cp.Variable((n, N+1))
x_0.value = x0
cost = 0
constraints = [x_seq[:, 0] == x_0]       # x_0 = x
for t in range(N-1):
    xt_var = x_seq[:, t]      # x_t
    ut_var = u_seq[:, t]      # u_t
    cost += cp.norm2(A @ xt_var + B @ ut_var - xn)
    constraints += [x_seq[:, t+1] == A @ xt_var + B @ ut_var]
prob = cp.Problem(cp.Minimize(cost), constraints)
prob.solve()
for i in range(N):
    print('x_seq:', x_seq[:, i].value)
print('x_seq:', x_seq[:, N].value)
for i in range(N):
    print('u_seq:', u_seq[:, i].value)

# test
x0 = np.array([[0], [1], [-2]])
u0 = np.array([[-1.72990587], [1.07110789]])
u1 = np.array([[-0.05677045], [2.99522085]])
x1 = A @ x0 + B @ u0
x2 = A @ x1 + B @ u1
print(x1)
print(x2)