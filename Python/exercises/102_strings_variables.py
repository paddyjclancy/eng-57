# Practice strings
# Welcome to Sparta - exercise
# Version 1 specs - with concatenation
# define a variable name, and assign a string

name = " "

# prompt the user for input and ask the user for his/her name
# re assign the original variable this this input

name = input("What is your go-to name?  ")

# use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)

print("Hello {}! Welcome to this .py file... let's go a bit further.".format(name.strip()))

# Version 2 - with interpolation
# ask the user for a first name, save it in a variable
# ask the user for a last name, save it in a variable
# use interpolation to print the message

first_name = input("What is your first name?  ")
last_name = input("What is your last name?  ")

print("Thank you, {} {}...".format(first_name.strip(), last_name.strip()))


# Calculate year of birth
# gather details on age and name
# print something like
# OMG <person>, you are <age> years old so you were born in <year>

age = " "
age = input("{}, how old are you?  ".format(first_name))
birth_year = 2020 - int(age)

print("Wowza {}, you are {} years old, I'm therefore guessing you were born in {}".format(first_name, age, birth_year))