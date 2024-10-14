# return N - Accenture (14 Oct 2024 Coding test)

import math

def rebound_height(H, V, Vn, N):
    # Calculate the coefficient of restitution
    e = V / Vn
    
    # Calculate the rebound height after N bounces
    rebound_h = H * (e ** (2 * N))
    
    # Return the integer value of the rebound height
    return int(rebound_h)

# Example usage:
H = 100  # Initial height
V = 20   # Initial velocity
Vn = 10  # Final velocity after N bounces
N = 2    # Number of bounces

result = rebound_height(H, V, Vn, N)
print(result)
