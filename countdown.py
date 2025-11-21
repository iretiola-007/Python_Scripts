
import time

def countdown(n):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        time.sleep(1)  # 1 second delay
        countdown(n - 1)

print("Welcome to Launcher Countdown!")

while True:
    i = input("Enter 'y' to continue or any other key to quit: ").lower()
    if i != 'y':
        print("Exiting Countdown Program.")
        break

    try:
        t = int(input("Countdown from what number? "))
        countdown(t)
    except ValueError:
        print("Please enter a valid number.")

