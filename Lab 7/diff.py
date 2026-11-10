import numpy as np
from scipy.misc import derivative

def f(x):
    return np.sin(x) + np.cos(x)

x = 0.5

result = derivative(f, x, dx=1e-6)

print(f"Derivative at x = {x}: {result:.2f}")