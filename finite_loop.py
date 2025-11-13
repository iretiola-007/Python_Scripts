## Loops
# "for" loops
# string
i = 0
for i in range(5):
    print("Ciao!") # Prints "Ciao!" 5 times

my_name = "Iretiola"
for char in my_name:
    print(char) # prints each character/letter of my_name on a new  line

# numbers
i = 0
for i in range(5):
    print(i) # prints each number from 0 - 4 (inclusive) on a new line

# using start and stop parameters
for i in range(1, 6):
    print(i) # prints the numbers from 1 and stops at 6, this means it won't print 6


# while loop
i = 3
while i < 13:
    print(i)
    i += 3 # this is a way to print the multiples of 3 up until 13
# In other words, it prints: 3, 6, 9, and 12 on a new line

# using a "for" loop for that same purpose
for i in range(0, 12, 2):
    print(i) # this prints: 0, 2, 4, 8, 10. Note that it won't print 12 because the stop parameters is the cutoff point so it won't be included in the output