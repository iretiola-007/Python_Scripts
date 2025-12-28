print("Simple Calculator\n")
def calculate():
    if operation == "+":
        print(a + b)
    elif operation == "-":
        print(a - b)
    elif operation == "*":
        print(a * b)
    elif operation == "/":
        print(a / b)
    else:
        print("Please enter a valid operation.")
        
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("what operation? ")

calculate()