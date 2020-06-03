
list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
list2 = []

for n in list1:
    if n not in list2:
        list2.append(n)

print(list2)