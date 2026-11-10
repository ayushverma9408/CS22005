import numpy as np

n = int(input("Enter size of matrix: "))

a = []

print("Enter matrix elements:")

for i in range(n):
    row = list(map(float, input().split()))
    a.append(row)

a = np.array(a)

print("\nMatrix:")
print(a)

eigenvalues, eigenvectors = np.linalg.eig(a)

print("\nEigenvalues:")
for x in eigenvalues:
    print(f"{x:.2f}")

print("\nEigenvectors:")
print(np.round(eigenvectors, 2))