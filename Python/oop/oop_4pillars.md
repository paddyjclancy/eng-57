### May 29

# Object-Orientated Programming: 4 Pillars

## Abstraction

- Showing only essential features of an object to the outside world.
- Other data contained within objects (Encapsulation)
- Easier interpretation
- TV example:
- To open your TV we only have a power button
- It is not required to understand how infra-red waves are getting generated in TV remote control

## Inheritance

- The concept of being able to create new classes FROM existing classes, ie subclass
- Subclasses have all the functionality of parent classes
- Improves dev efficiency, less code writing generally
- Use super function to call back parent functions for use



- Init for initialization - creation of instances within classes
- self represents instance - placeholder

```Python
class Animal:

  def __init__(self, species_family, legs, fur):
      self.species_family = ""
      self.legs = 4
      self.fur = True

  ...

class Cat(Animal):

  def __init__(self, name, age, independence="", playful="", agility=""):
      super().__init__("Feline", 4, True)
      self.name = name.title()
      self.__age = int(age)           # __age for encapsulation
      self.independence = True
      self.playful = True
      self.agility = True

  ...
```

```Python
class Monster:

    def __init__(self, name, age, tax_number, fur):
        self.name = name.title()
        self.age = int(age)
        self.tax_number = tax_number
        self.fur = fur

    ...

class MonsterStudent(Monster):

    def __init__(self, name, age, tax_number, fur, student_no, year_of_study, skills=[]):
        super().__init__(name, age, tax_number, fur)
        self.student_no = student_no
        self.year_of_study = int(year_of_study)
        self.skills = skills

    ...

sully = MonsterStudent("sully", 23, "S-4117", "blue-purple polka dot", 10001, 1, ["Horns", "Teeth", "Claws"])
```

## Encapsulation

- Accumulating similar data / methods together into single object - Class
- Also using __ to hide certain parameters / methods
  - More effort for these to be changed or overridden
- Assists organisation and interpretation
- Provides security, pairs well with Abstraction
- Getters used to return __ parameters
- Setters used to adjust __ parameters
  - Combined with other methods to create encapsulated method

```Python
def getter_age(self):                   # Getter method (Encapsulation)
    return self.__age

def birthday(self):
    print(f"It is your birthday, {self.name}.")
    self.__age_increase()               # Encapsulated method
    print(f"{self.name} is now {self.__age} years old.")

def __age_increase(self):               # Setter method (Encapsulation)
    self.__age += 1
```    


## Polymorphism

- Objects are adaptable to continue functionality even if differing data types
- Subclasses are free to create their own additional behaviours even though being already defined
- Subclass += Class
- Class != Subclass
                        "To take many forms"
