import numpy as np
import time
 
# Create a large array
array = np.random.rand(1_000_000)

# Loop-based approach
L_start_time = time.time()
squared = []
for x in array:
   squared.append(x ** 2)
L_end_time = time.time()

# Vectorized approach
V_start_time = time.time()
squared = array ** 2  
V_end_time = time.time()