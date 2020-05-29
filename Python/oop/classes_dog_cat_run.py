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
print("nap()  ################################################################")
print(john.nap())
print("fetch()  ##############################################################")
print(roger.fetch())
print("bark()  ###############################################################")
print(freddie.bark())
print("eat()  ################################################################")
print(brian.eat())
print("walk()  ###############################################################")
print(roger.walk(independence = ''))


print("#######################################################################")
print("TESTING CAT FUNCTIONS  ################################################")
print("Every morning as a cat owner...  alarm() ##############################")
print(jimi.alarm())
print("Does Jimi want to go on a walk?  walk()  ##############################")
print(jimi.walk(independence = ''))
print("purr()  ###############################################################")
print(jimi.purr())
print("Give Jimi catnip...  ##################################################")
print(jimi.catnip())
print("nap()  ################################################################")
print(jimi.nap())

