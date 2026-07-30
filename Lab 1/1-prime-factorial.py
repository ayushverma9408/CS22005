'''
Develop a Python program to calculate the factorial of a number and determine whether a 
given number is prime using conditional and looping constructs. 
'''
def factorial(n):
    if n == 0: return 1
    else:  return n * factorial(n-1)

def prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  return False
    return True

n=int(input("Enter a number: "))

print(f"The factorial of {n} is: {factorial(n)}") 

if prime(n):  print(f"{n} is a prime number.")
else:  print(f"{n} is not a prime number.")
