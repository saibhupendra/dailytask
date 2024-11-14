##Basic List Operations:
##Write a Python program to create a list of 5 integers and print the sum of all elements in the list.
l=[l for l in range(1,5+1)]
print(l)
sum=0
for i in l:
    sum+=i
print(sum) 


##Create a list of strings containing the names of 5 fruits. 
# Access and print the second and fourth elements using indexing.
fruits=["apple","orange","banana","pappya","mango"]
print(fruits)
print(fruits[2])
print(fruits[4])


##Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, 
# the last three numbers, and every second number in the list.
l=[l for l in range(1,10+1)]
print(l)
first_three=l[:3]
last_three=l[-3:]
print(first_three)
print(last_three)
every_second=l[::2]
print(every_second)