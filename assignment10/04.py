###Sorting and Reversing Lists:
##Write a Python program to sort a list of 10 random integers in ascending and 
# descending order using sort() and reverse().
##Create a list of strings and reverse the order of elements using both reverse() and 
# slicing [::-1]. Compare the results.


l=[1,3,4,2,6,9,1,0,11,44,66]
l.sort()
print(l)
l.reverse()
print(l)

##Create a list of strings and reverse the order of elements using both reverse() and 
# slicing [::-1]. Compare the results.
l=["nani","nagu","prasad","ramadevi"]
print(l)
l1=l
l1.reverse()
print(l1)
l2=l
l2[::-1]
print(l2)
if (l1==l2):
    print("true")
else:
    print("flase")    

