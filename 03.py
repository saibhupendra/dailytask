####Adding and Removing Elements:
##Write a Python program that initializes a list with some numbers and:
##Adds a new number to the list using the append() method.
##Inserts a number at the second position using insert().
##Extends the list with another list of numbers.
##Remove all occurrences of the number 3 from a list of integers.
##Write a Python program to remove the last element of a list using pop() and print the updated list.

l=[l for l in range(1,10+1)]
print(l)
l.append(11)
print(l)
l.insert(2,12)
print(l)
l1=[l1 for l1 in range (1,13+1)]
print(l1)
l.extend(l1)
print(l)

while 3 in l:        ## if 3 in l: l.remove(3) print(l) it will only delect first oocurance of 3 in list
    l.remove(3)
print(l)    

l.pop()
print(l)
