### May 19
# Introduction to Python (2)

## Strings cont.

Different options due to potential for both single and double apostrophes (double best practice):

```Python
string = "I sad 'wow!'"
string = 'I said \'wow!\''
```

Slicing:
- Indexing begins on 0

```Python
print(variable["start":"end"])
```

len():
- Counts number of characters

```Python
len(string)
                #Will return '8'
```

strip()
- To remove white space within a string:

```Python
white_space = "Lots of spaces at the end    "
print(len(white_space))
print(len(white_space.strip()))
#                    Will return '31'
#                                '25'
```

count()
- Counts the number of occurances of a substring within a main string

```Python
text = "text and stuff"
print(text.count("text"))
print(text.count("t"))
#                  Will return '1'
#                              '3'
```

lower() / upper()
- Changes case of string to respective function


.capitalize()
- ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZz
- CapitaliZes first letter of string:

```Python
text = "text and stuff"
print(text.capitalize())
```

- Use concatenation to do slice the string and capitalize each word:

```Python
name1 = "text"
name2 = "and"
name3 = "stuff"
print(name1.capitalize() + name2.capitalize()
                         + name3.capitalize())
```

startwith() / endwith()
```Python
string.startwith([character])
```
- Will return Boolean


 replace()
- Edit a substring within main:

```Python
text = "text and stuff"
print(text.replace("text", "words"))
#                          Will return "words and stuff"
```

## Concatenation

- Combines strings together using + operator

```Python
x = 2
y = 10.5
z = "words"

print(z + " " + str(y) + " " + str(x) + " " + str(x+y))
#                               Will return 'words 10.5 2 12.5'
```

## Casting

- Changes a datatype:

```Python
print("age datatype = ", type(int(age)))
                         ---------------
```

## Booleans

True / False

Operators:

- '='
- '=='
- '!='
- '>='
- '<='
