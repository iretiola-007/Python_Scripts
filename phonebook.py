# search for contacts 

# dictionaries in a list
people = [
    {"name": "Yuliia", "number": "+1-617-495-1000"}, 
    {"name": "David", "number": "+1-617-495-1000"},
    {"name": "John", "number": "+1-949-468-2750"}
]

name = input("Name: ")

# loop through elements in the "people" list
for person in people:
    if person["name"] == name:
        print(f"Found {person['number']}")
        break
else:
    print("Not found")