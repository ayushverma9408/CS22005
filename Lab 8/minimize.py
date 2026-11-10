from scipy.optimize import minimize
def f(v):
    x=v[0]; y=v[1]
    return (x-2)**2+ (y-2)**2

result = minimize(f,[0, 0])
print(f"Minimum value of the function: {result.fun:.2f}")
print(f"Minimum found at x = {result.x[0]:.2f}, y = {result.x[1]:.2f}")