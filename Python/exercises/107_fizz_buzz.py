# Write a fizz-buzz game ##project

# as a user I should be able prompted for a number, the program will print all the numbers up to and including said number while following the constraints / specs. (fizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'

# write a program that take a number
# prints back each individual number, but

# if it is a multiple of 3 it returns fizz
# if a multiple of 5 it return buzz



choice = int(input("Choose a number!   "))
pen_pineapple_pen = 6


for i in range(1, (choice + 1)):
    print(i)
    if choice == pen_pineapple_pen:
        print("You beat the game!")
        break
    if choice !=
    if i % 5 == 0:
        print("BUZZ")
    if i % 3 == 0:
        print("FIZZ")

