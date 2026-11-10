import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([6, 17, 34, 57, 86, 121])

# Fit second-degree polynomial
coeff = np.polyfit(x, y, 2)

a = coeff[0]
b = coeff[1]
c = coeff[2]

print("Polynomial coefficients:")
print(f"a = {a:.2f}")
print(f"b = {b:.2f}")
print(f"c = {c:.2f}")

# Fitted polynomial
y_fit = a*x**2 + b*x + c

print(f"\nFitted polynomial:")
print(f"y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")

# Plot
plt.scatter(x, y, label="Original Data")

plt.plot(x, y_fit, label="Fitted Curve")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Second-Degree Polynomial Fitting")

plt.legend()
plt.show()