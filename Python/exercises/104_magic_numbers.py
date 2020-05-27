# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.


# We should define/assign number to a variable called magic_number

magic_number = 6

# I need to ask user for input

print("I'm thinking of a number....")


# I need to check if this input matches a magic_number
while True:
    choice = int(input("Pick a number!   "))

    if choice == magic_number:
        print("Si- err correcto")
        break
    else:
        print("Computer says no")


# I need to let the user know if the response was write or not
#self five

