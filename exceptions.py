try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
except Exception as e:
    print(f"Unexpected error: {e}")

# comments come in later
