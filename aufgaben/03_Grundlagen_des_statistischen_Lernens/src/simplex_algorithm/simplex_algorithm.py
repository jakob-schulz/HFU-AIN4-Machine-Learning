import numpy as np
from scipy.optimize import linprog
 
# Objective function 
c = np.array([-40, -30])  # Convert to minimization

# constraints on left side
A = np.array([
    [2, 1],   # 2x1 + x2  
    [1, 2],   # x1 + 2x2  
])

B = np.array([40, 50]) # Constraints on right side 

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=B, method='highs')

# Display the results
if result.success:
    print("Optimal solution found:")
    print(f"  x1 = {result.x[0]:.2f}")
    print(f"  x2 = {result.x[1]:.2f}")
    print(f"  Maximum Profit = {-result.fun:.2f}")  # Negate to get the actual maximum profit
else:
    print("No solution found.")