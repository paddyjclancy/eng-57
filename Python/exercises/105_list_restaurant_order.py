# SIMPLEST - Restaurant Waiter Helper

# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# starter code
menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras']
food_order = []


# I need to print each item from the list
# before I print I need to make them all capitalized
#  print everything

print("\nOur menu: \n")
for i in menu:
    print(i.capitalize())

while True:
    order_item = input("\nWhat would you like to order? Say 'When' when complete.  ")

    if order_item != "When":
        food_order.append(order_item)
    else:
        print("\nYour order:\n")
        for i in food_order:
            print(i.capitalize())
        break


# for i in food_order:
#     print(i.capitalize())
