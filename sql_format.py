def spacing(name, marks, width=8, sep="|"):
    strlen = len(name)

    if strlen >= width:
        name = name[:width]
    else:
        name = name + " " * (width - strlen)

    print(name, sep, marks)


with open("marks.txt", "r") as file:
    for line in file:
        name, marks = line.split()
        spacing(name, marks)


# This formats the columns like you would see in SQL
# More explanations and notes later