# Write a fizz-buzz game ##project

# as a user I should be able prompted for a number, the program will print all the numbers up to and including said number while following the constraints / specs. (fizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'

# write a program that take a number
# prints back each individual number, but

# if it is a multiple of 3 it returns fizz
# if a multiple of 5 it return buzz


pen_pineapple_pen = 6

while True:
    choice = int(input("Choose a number!   "))

    for i in range(1, choice + 1):
        if choice == pen_pineapple_pen:
            print("You beat the game!")
            break
        elif i % 15 == 0:
            print("FUZZBUZZ")
        elif i % 5 == 0:
            print("BUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        else:
            print(i)

