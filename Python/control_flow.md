### May 19
# Control Flow

- Dictates where the code will run
- In programming this is done with if functions and while loops

## if Functions

- Work with Booleans
- Usually used with comparison operators (==) to equate and compare objects, and result in True of False


Syntax

- Indentation is important!
- Most specific condition at top

```Python
if <condition == True>:
    <do this>
elif <second_condtition == True>:
    <do this>
else:
    <do this>
```
```Python
weather = input("What is the weather currently?  ")
safety_alert = "red"

if weather == "stormy" and safety_alert == "red":
    print ("Duck for cover!")
elif weather == "rainy":
    print("Carry an umbrella")
elif weather == "stormy":
    print("Stay at home and watch the storm!")
else:
    print("Put on some sun lotion?")
```
