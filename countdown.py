def countdown(n):
    if n == 0:
        print("Blast off!")
    else:
        time.sleep(1) # 1 second delay
        print(n)
        countdown(n - 1)

print("Welcome to Launcher Countdown!")

i = str(input("Enter 'y' to continue: "))

# The loop to continue using the countdown 
while i.lower() == 'y':
    t = int(input("Countdown from what number? "))
    countdown(t)
    i = str(input("Enter 'y' to continue: "))

# To exit the loop, type 'n' or any other character apart from 'y'.