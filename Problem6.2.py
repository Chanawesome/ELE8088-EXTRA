from scipy.optimize import minimize
import numpy as np
import cvxpy as cp
import math

def fun(args):
    a = args
    v = lambda x: x[0] ** 2 + x[0] - (a * math.log(x[0], 10))
    return v

if __name__ == "__main__":
     args = (2022)  #a
     x0 = np.asarray((5))  # guess initial value
     res = minimize(fun(args), x0, method='SLSQP')
     print('Optimal value:',res.fun)
     print('Minimiser:',res.x)
     print('Whether the iteration terminates successfully:',res.success)
     print('Reason for iteration termination：', res.message)

