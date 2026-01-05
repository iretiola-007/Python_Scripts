import random


print("Guess the Number Game!")

# computer picks a random number between 1 and 100
actual_number = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")

# looping while user guess is incorrect
# handling errors in user input
while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < actual_number:
            print("Too low! Try again.")
        elif guess > actual_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")


