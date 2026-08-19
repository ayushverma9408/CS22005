import numpy as np

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter Matrix A:")
a = []

for i in range(r):
    row = list(map(int, input().split()))
    a.append(row)

print("Enter Matrix B:")
b = []

for i in range(r):
    row = list(map(int, input().split()))
    b.append(row)

a = np.array(a)
b = np.array(b)

print(f"\nMatrix A:\n{a}")

print(f"\nMatrix B:\n{b}")

print(f"\nAddition:\n{a + b}")

print(f"\nSubtraction:\n{a - b}")

print(f"\nMatrix Multiplication:\n{np.dot(a, b)}")

print(f"\nTranspose of A:\n{a.T}")

print(f"\nTranspose of B:\n{b.T}")