from scipy.optimize import minimize

def objective(x):
   return x[0]**2 + x[1]**2

cons = ({'type': 'ineq', 'fun': lambda x: x[0] - 1})
result = minimize(objective, [2, 2], constraints=cons, bounds=[(1, None), (None, None)])

print(result)