## Mathematical Operations:
##Create two lists of numbers, and use the + operator to concatenate them. Then, use the * 
# operator to repeat the elements of one list 3 times.
l=[1,2,3,4]
l1=[5,6,7,8,9]
add=l+l1
print(add)

mul=add*3
print(mul)


##Given a list of numbers, write a Python program to create a new list where each element is 
# doubled (i.e., each element is multiplied by 2).
l=[1,2,3,4,5]
doubled=[]
for i in l:
    x=i*2
    doubled.append(x)
print(doubled)   
