try:
    # prompt the user to enter a number and convert it to an integer
    num = int(input("Enter a number: "))
    
    # divide 10 by the entered number
    print(10 / num)

# handling the case where the input is not a valid integer
except ValueError:
    print("That's not a valid number.")

# handling the case where the user enters 0 (division by zero error)
except ZeroDivisionError:
    print("Can't divide by zero.")

# catch any other unexpected errors
except Exception as e:
    print(f"Unexpected error: {e}")