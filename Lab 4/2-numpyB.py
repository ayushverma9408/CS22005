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

# Addition
add = []

for i in range(r):
    row = []

    for j in range(c):
        row.append(a[i][j] + b[i][j])

    add.append(row)


# Subtraction
sub = []

for i in range(r):
    row = []

    for j in range(c):
        row.append(a[i][j] - b[i][j])

    sub.append(row)


# matrix multiplication
mul = []

for i in range(r):
    row = []
    for j in range(c):
        sum = 0
        for k in range(c):
            sum += a[i][k] * b[k][j]
        row.append(sum)
    mul.append(row)


# Transpose of A
trans = []

for j in range(c):
    row = []

    for i in range(r):
        row.append(a[i][j])

    trans.append(row)

print(f"\nMatrix A:{a}") 

print(f"\nMatrix B:{b}") 

print(f"\nAddition:{add}") 

print(f"\nSubtraction:{sub}") 

print(f"\nMultiplication:{mul}") 

print(f"\nTranspose of A:{trans}") 