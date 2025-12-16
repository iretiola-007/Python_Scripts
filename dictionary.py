# dictionary
people = {
    "Yuliia": "+1-617-495-1000", 
    "David": "+1-617-495-1000", 
    "John": "+1-444-444-2750"
}

# get user search
search = input("Search here... ")

found = False


# loop through elements in the dict to find user input, then breaks the loop if input is found

for name in people:
	   if name in search:
	       print(f"{name}'s number is {people[name]}")
	       found = True
	       break
if not found:
    print("User not found")