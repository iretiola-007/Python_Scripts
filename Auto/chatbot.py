print("Hi! I'm ChatBot. Type 'Hello' to talk and 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == 'bye':
        print("ChatBot: Goodbye!")
        break
    elif "hello" in user_input:
        print("ChatBot: Hello there!")
    elif "how are you" in user_input:
        print("ChatBot: I'm fine, thanks!")
    else:
        print("ChatBot: I don't understand.")

