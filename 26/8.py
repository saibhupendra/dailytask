"write a program to caculate the factorial of a number using a for loop"
n=int(input("enter a number:"))
fact=1
for i in range (1,n+1):
    fact=fact*i 
    print(fact)    