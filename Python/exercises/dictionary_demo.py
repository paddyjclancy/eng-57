
# dictionary = {key : value, key2: value2, key3: value3, etc...}
my_hero = {"Name": "Bruce Wayne/Batman", "Alias": "Batman", "Location": "Gotham", "Weakness": "Parents"}


# Re-assigning a value
my_hero["Name"] = "Bruce Wayne"

# Adding a new attribute
my_hero["Ability"] = "Money"

# Removing a value
del(my_hero["Ability"])

# Display everything
for key, value in my_hero.items():
    print(key, ": ", value)

