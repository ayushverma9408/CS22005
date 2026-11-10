import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [45000, 52000, 48000, 61000, 58000, 65000,
         62000, 70000, 68000, 75000, 72000, 80000]

# Find highest and lowest sales
high = max(sales)
low = min(sales)

high_month = months[sales.index(high)]
low_month = months[sales.index(low)]

print("Highest Sales:", high_month, high)
print("Lowest Sales:", low_month, low)

# Line Chart
plt.figure(figsize=(9, 4))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Months")
plt.ylabel("Sales (Rs)")
plt.grid(True)
plt.show()

# Bar Chart
plt.figure(figsize=(9, 4))
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales (Rs)")
plt.show()