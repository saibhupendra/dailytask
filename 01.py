l=[[1,2,3],[4,5,6],[7,8,9]]
print(l[0])
print(l[1])
print(l[2])


name=["nani","nagu","prasad","ramadevi"]
name.remove("nani")
name.append("nani")
print(name)
print(name)
print(id(name))
x=name
print(x)
print(id(x))
#alising is giving a reference variable name to the existing vaiables    
## this means that changes made for one variable will effect the other that reference the same object
## and also it will give the same id's for the variables



##cloning  >>> it is used to creating of an object or data structure 
##         >>>which means if any changes made to the clone do not effect on original object
##slicing 
##        >> it will save the shallow copy of a list
name=["nani","nagu","prasad","ramadevi"]
x=name[:]
print(name)
print(x)
print(id(name))
print(id(x))

## copy >> it also create a copy of a list
name=["nani","nagu","prasad","ramadevi"]
cx=name[:]
print(name)
print(cx)
print(id(name))
print(id(cx))

## we will get the different id's in duplicate varablies also
