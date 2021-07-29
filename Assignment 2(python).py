#Delete all occurrences of an element in a list
li = [0, 4, 2, 0, 5, 0, 8, 0]
val = 0
li = [i for i in li if i != val]
print(li)
