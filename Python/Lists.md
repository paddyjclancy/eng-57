### May 19

# Lists [ ]

- Organised via index, which starts at 0
- Can hold any datatypes


```Python
my_cringy_landlords = ["Alfredo", "Betty", "Joanna", "Mr.Summersbee"]
#             index = [   0     ,    1   ,     2   ,        3       ]
#             index = [  -4     ,   -3   ,    -2   ,       -1       ]

print(type([]))
print(my_cringy_landlords)
print(len(my_cringy_landlords))
print(my_cringy_landlords[2])
print(type(my_cringy_landlords[2]))
                  # <class 'list'>
                  # ['Alfredo', 'Betty', 'Joanna', 'Mr.Summersbee']
                  # 4
                  # Joanna
                  # <class 'str'>
```


.pop()

- Removes entrant at index position
- By default pops off the last entrant

```Python
my_cringy_landlords.pop(3)

print(my_cringy_landlords.pop(3))
                  # Mr.Summersbee
```
.remove()

- Removes entrant as specified object

```Python
my_cringy_landlords.remove("Mr.Summersbee")

```

.append()

- Adds a new entry to the end of the Lists

```Python
my_cringy_landlords.append('Alex')

print(my_cringy_landlords)
                  # ['Alfredo', 'Betty', 'Joanna', 'Alex']
```
