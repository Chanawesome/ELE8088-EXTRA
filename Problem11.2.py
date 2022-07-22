import control as ctrl
import numpy as np

A = np.array([[2, 1],[1, 0]])
B = np.array([[2], [-1]])
Q = np.array([[1, 1],[1, 1]])
R = 2
Pf = np.array([[2, 0],[0, 0]])
N = 10
n = 2
m = 1

P = np.zeros((n, n, N+1)) # tensor
K = np.zeros((m, n, N)) # tensor (3D array)
P[:,:,N] = Pf

P, _, K = ctrl.dare(A, B, Q, R)
K = -K
print("K =")
print(K)
print("P =")
print(P)