from class_animal import *
from class_cat import *
from class_dog import *



freddie = Dog(19, 'freddie')
brian = Dog(20, 'brian')
roger = Dog(14, 'roger')
john = Dog(16, 'john')
adam_lambert = Dog(7)


jimi = Cat('jimi', 6)


print("PRINTING INSTANCES  ---------------------------------------------------")
print("Dogs: ", freddie.name, ", ", brian.name, ", ", roger.name, ", ", john.name, ", ", adam_lambert.name)
print("Cats: ", jimi.name, "- ", jimi.getter_age())

print("-----------------------------------------------------------------------")
print("TESTING DOG FUNCTIONS  ------------------------------------------------")
print("nap()  ----------------------------------------------------------------")
print(john.nap())
print("fetch()  --------------------------------------------------------------")
print(roger.fetch("ball"))
print("bark()  ---------------------------------------------------------------")
print(freddie.bark())
print(adam_lambert.bark())
print("eat()  ----------------------------------------------------------------")
print(brian.eat())
print("walk()  ---------------------------------------------------------------")
print(roger.walk(independence = ''))


print("-----------------------------------------------------------------------")
print("TESTING CAT FUNCTIONS  ------------------------------------------------")
print("alarm() ---------------------------------------------------------------")
print(jimi.alarm())
print("Take cat on walks?  walk()  -------------------------------------------")
print(jimi.walk(independence = ''))
print("purr()  ---------------------------------------------------------------")
print(jimi.purr())
print("Give Jimi catnip...  --------------------------------------------------")
print(jimi.catnip())
print("nap()  ----------------------------------------------------------------")
print(jimi.nap())
jimi.birthday()
print(jimi.eat())

