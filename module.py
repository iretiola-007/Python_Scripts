# a simple module

# define the class (blueprint)
class Greet:
    def __init__(self, name):
        self.name = name
    
    # define a method in your blueprint
    def msg(self ):
        print(f"Hello, {self.name}!")

# get user input
name = input("What's your name? ")
    
# create an object and call the function
Greet(name).msg()

# alternatively you can store the object in a variable like this👇🏻
welcome_message = Greet(name)
welcome_message.msg()


