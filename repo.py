# Simple multiplication and division

# Input two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Multiplication
product = a * b
print(f"Multiplication: {a} * {b} = {product}")

# Division
if b != 0:
    division = a / b
    print(f"Division: {a} / {b} = {division}")
else:
    print("Division by zero is not allowed.")
