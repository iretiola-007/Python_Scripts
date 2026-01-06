# list of objects
listt = ["cable", "book", "pencil", "adapter"]
print(listt)

length = len(listt) # store the length of the elements in a variable

# define a sort() function to print sorted list
def sort():
    for i in range(length):
        for j in range(0, length - i - 1):
            if listt[j] > listt[j + 1]:
                listt[j], listt[j + 1] = listt[j + 1], listt[j]
    print(listt)

sort() # call the function

# the original list is printed before the sorted list


# in order to avoid using this long function, use this below
print(sorted(listt))
