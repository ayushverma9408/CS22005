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
det = np.linalg.det(a)
rank = np.linalg.matrix_rank(a)

print(f"\nDeterminant: {det:.2f}")
print("Rank:", rank)

if abs(det) > 1e-10:
    inverse = np.linalg.inv(a)
    print("\nInverse:")
    print(np.round(inverse, 2))
else:
    print("\nInverse does not exist because determinant is zero.")