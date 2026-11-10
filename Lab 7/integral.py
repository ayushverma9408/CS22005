from scipy.integrate import quad

def f(x):
    return x**3 + 2*x + 5

result, error = quad(f, 0, 2)

print(f"Integration result: {result:.2f}")
print(f"Estimated error: {error:.2e}")