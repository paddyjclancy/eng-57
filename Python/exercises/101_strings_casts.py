# Define the following variables
# name, last_name, age, eye_color, hair_color

first_name = ""
last_name = ""
eye_color = ""
hair_color = ""
age = ""

# Prompt user for input and Re-assign these

first_name = input("What is your first name?  ")
last_name = input("What is your last name?  ")
eye_color = input("What colour eyes do you have?  ")
hair_color = input("What colour hair do you have?  ")
age = input("How old are you?  ")

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

print("Hello {}! Welcome, your age is {}, your eyes are {} and your hair colour is {}".format(first_name, age, eye_color, hair_color))

#Extra - Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'

birth_year = 2020 - int(age)
print("You said you are {}, hence I estimate you were born in {}".format(age, birth_year))

# Extra - Section 3 - Cast your input
print("first_name datatype = ", type(first_name))
print("last_name datatype = ", type(last_name))
print("eye_color datatype = ", type(eye_color))
print("hair_color datatype = ", type(hair_color))

print("age datatype = ", type(int(age)))
print("birth_year datatype = ", type(int(birth_year)))