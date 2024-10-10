##Write a Python program to create a list of 5 integers and print the sum of all elements in the list.
l=[l for l in range(1,5+1)]
print(l)
sum=0
for i in l:
    sum+=i
print(sum) 