"write a program to find the largest of three number using if statement"
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
n3=int(input("enter a number:"))
if n1>n2 and n1>n3:
    print("return n1")
elif(n2>n1 and n2>n3):
    print("retrun n2")
else:
    print(n3)
