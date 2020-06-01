from class_cat import *
from class_dog import *

#    def __init__(self, name = 'Un-named member', age, fur = "", independence = "", playful = ""):
freddie = Dog(19, 'freddie')
brian = Dog(20, 'brian')
roger = Dog(14, 'roger')
john = Dog(16, 'john')
adam_lambert = Dog(7)

#    def __init__(self, name, age, fur ="", independence = "", agility = "", playful = ""):
jimi = Cat('jimi', 6)

print("PRINTING INSTANCE NAMES (SHOWING POLYMORPHISM)  -----------------------")
print("Dogs: ", freddie.name, ", ", brian.name, ", ", roger.name, ", ", john.name, ", ", adam_lambert.name)
print("Cats: ", jimi.name)

print("-----------------------------------------------------------------------")
print("TESTING DOG FUNCTIONS  ------------------------------------------------")
print("nap()  ----------------------------------------------------------------")
print(john.nap())
print("fetch()  --------------------------------------------------------------")
print(roger.fetch())
print("bark()  ---------------------------------------------------------------")
print(freddie.bark())
print(adam_lambert.bark())
print("eat()  ----------------------------------------------------------------")
print(brian.eat())
print("walk()  ---------------------------------------------------------------")
print(roger.walk(independence = ''))


print("-----------------------------------------------------------------------")
print("TESTING CAT FUNCTIONS  ------------------------------------------------")
print("How do cats wake owners up...  alarm() --------------------------------")
print(jimi.alarm())
print("Do cats want to go on walks?  walk()  ---------------------------------")
print(jimi.walk(independence = ''))
print("purr()  ---------------------------------------------------------------")
print(jimi.purr())
print("Give Jimi catnip...  --------------------------------------------------")
print(jimi.catnip())
print("nap()  ----------------------------------------------------------------")
print(jimi.nap())

