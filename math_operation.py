def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def factorial(a):
    fact = 1
    for num in range(1,a+1):
        fact*=num
    return fact