# mr Miyagi trainee

# make a mr miyagi virtual assistant


# as a user I should be able to speak with mr miyagi and get appropriate response s as I go
#
# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..'
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'
# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

# your_response = input('(MR.Miyagi)... -.-')

#  EXTRA:
#  make it run continuously
#  consider best practices of functions - make this functional

print("*Mr Miyagi has entered the chat*")

while True:
    user_input = input("M - Never trust a leader who cannot dance, ask me anything.   ")

    if not user_input.title().startswith("Sensei"):
        print("M - You are smart, but not wise - address me as Sensei.")
    else:
        if "Sensei, I am at peace" in user_input:
            print("M - Sometimes, what heart knows, head forget")
            break
        elif "?" in user_input:
            print("M - Questions are wise, but for now... wax on, wax off!")
        elif user_input.count("block") >= 1:
            print("M - Remember, best block is not to be there...")
        else:
            print("M - Do not lose focus. Wax on, wax off...")

