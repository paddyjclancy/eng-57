# Lists!
# Fine a list with cool things inside!
    # Examples: Christmas list, things you would by with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: _______?????              Indeces
example_xmas = ['walkie talkies', 'socks', 'lynx']

favourite_artists = ["Foals", "Jimi Hendrix", "Kodaline", "Tash Sultana", "Walk Off The Earth"]

# Print the lists and check it's type

print("List: favourite_artists - ", favourite_artists)
print("Type - ", type(favourite_artists))

# Print the list's first object

print("First object - " + favourite_artists[0])

# Print the list's second object

print("Second object - ", favourite_artists[1])

# Print the list's last object

print("Last object - ", favourite_artists[-1])

# Re-define the first item on the list

favourite_artists[-1] = "Xavier Rudd"
print("Re-defined last item - ", favourite_artists[-1])

# Re-define another item on the list and print all the list

favourite_artists[2] = "Pink Floyd"
print("Re-defined item 3 - ", favourite_artists[2])

# Add an item to the list and print the list

favourite_artists.append("Aerosmith")
print("ADJUSTED & APPENDED LIST: ", favourite_artists)

# Remove an item from the list and print the list

favourite_artists.pop()
print("POPPED LIST: ", favourite_artists)

# Add two items to list and print the list
#example_xmas.append('iphone')
#example_xmas.append('money for icecream')
#print(example_xmas)

favourite_artists.append("Ben Howard")
favourite_artists.append("Bombay Bicycle Club")
print("Okay we appended it again, its tricky picking a select few: ", favourite_artists)
