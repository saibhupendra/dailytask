## Aliasing and Cloning:
##Create a list of numbers. Assign the list to another variable and modify the original list. 
# Check if the second list also changes. Then, create a copy of the original list and show that 
# modifying the copy does not affect the original list.
l=["nani","nagu","prasad","ramadevi"]
ano_l=l
print(l)
print(ano_l)
l.append("neeru")
print(l)
print(ano_l)

l1=l.copy()
print(id(l))
print(id(l1))

print("---------------------------------------")



##Write a Python program to demonstrate how changes in a list's alias affect both lists, 
# while changes in a cloned list do not.
l=["nani","nagu","prasad","ramadevi"]
print(id(l))
x=l
print(id(x))


## cloning
l=["nani","nagu","prasad","ramadevi"]
print(id(l))
x=l
x=l[:]
print(id(l))
print(id(x))

