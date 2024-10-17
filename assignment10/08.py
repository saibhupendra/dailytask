 ##Nested Lists:
##Write a Python program to create a 3x3 matrix (nested list) and print the matrix. 
# Then, access and print the element at row 2, column 3.
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    print(i)
print(l[2][2])  


##Create a nested list representing a list of students' names and their respective grades. 
# Write a Python program to print each student's name along with their grade.

student=[["nani","25"],["nagu","30"],["leela","35"]]
for i in student:
    name=i[0]
    grades=i[1]
    print(name +" :" + grades)
