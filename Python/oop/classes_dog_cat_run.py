from class_cat import *
from class_dog import *


freddie = Dog('freddie')
brian = Dog('brian')
roger = Dog('roger')
john = Dog('john')
adam_lambert = Dog()

jimi = Cat('jimi')

print("PRINTING INSTANCE NAMES (SHOWING POLYMORPHISM)  #######################")
print("Dogs: ", freddie.name, ", ", brian.name, ", ", roger.name, ", ", john.name, ", ", adam_lambert.name)
print("Cats: ", jimi.name)

print("#######################################################################")
print("TESTING DOG FUNCTIONS  ################################################")
print(john.nap())
print(roger.fetch())
print(freddie.bark())
print(brian.eat())
print(roger.walk(independence = ''))
print(john.nap())

print("#######################################################################")
print("TESTING CAT FUNCTIONS  ################################################")
print(jimi.alarm())
print("Does Jimi want to go on a walk?")
print(jimi.walk(independence = ''))
print(jimi.purr())
print("Give Jimi catnip...")
print(jimi.catnip())
print(jimi.nap())

