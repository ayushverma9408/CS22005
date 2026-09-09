marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]

temperatures = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]

sales = [12500, 13800, 14200, 11900, 15100, 14750, 16000]


def statistics(data, name):

    # Mean
    total = 0

    for x in data:
        total += x

    mean = total / len(data)

    # Median
    a = sorted(data)
    n = len(a)

    if n % 2 == 0:
        median = (a[n//2 - 1] + a[n//2]) / 2
    else:
        median = a[n//2]

    # Standard deviation
    total = 0

    for x in data:
        total += (x - mean) ** 2

    variance = total / len(data)
    sd = variance ** 0.5

    # Minimum and maximum
    minimum = min(data)
    maximum = max(data)

    print("\n", name)
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", sd)
    print("Minimum:", minimum)
    print("Maximum:", maximum)


statistics(marks, "Marks")
statistics(temperatures, "Temperatures")
statistics(sales, "Sales")