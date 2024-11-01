## all topics in python


#features:




##identifiers:
#      >>  identifier is to identify the entity like 
#                >variable,functions,classes
#      >> it must follow specific naming rules depending up on the programming language
#      >> it  should store with a letter or underscore 
#      >>  and they cannot contain space or special character



## variables:
#      >>it is a container to store the data
# 
# 
# 
# 
# 
# operators
#    >>operators are symbols or keywords that perform operations on one or more operands
#  arithmethic:
##       >>
#  relational
# logical
# identify
# bitwise
# membership
# assignment


## keywords
import keyword
print(keyword.kwlist)

##output
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 
 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 
 'in', 'is', 'lambda', 'nonlocal', 
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


##datatypes:
##    >: It specify the type of data a variable can hold in programming and databases.
##    int  :: It is used to represent whole numbers without any fractional or decimal components
#   float:   Float data types are used to represent real numbers that include decimal points. 
#  complex:  data structures that can hold multiple values and may consist of various datatypes



## controlflow statements: it execute code block conditionally or repetedly
# if >>if statment is correct it will execute
# elif  >> it check the multiple condtions
# else  >> if the "if statement is flase" it will execute
#
#  iterator statements:it execute group of statements multipule times 
#while loop:repeatedly execute a block of statement
#for loop: it iterate a sequence of items


## transfer statements:
# break: if the statement is stafity the loop will be automatically exit 
# continue:jumps the current iterations to beginning of the loop
# pass:by add the methode or functions to code we use the pass keyword

#

##stirng:  it is a sequence of character like letter,numbers or symbols
# it is a collections of alphabets and words
# it will represent in double qeotations

#   >>changing a case of a string:

#    1.upper
#    2.lower
#    3.swapcase
#    4.tittle :  first character in each word will converter into uppercase
#    5.capitalize: it will converter only the first character will be uppercase

##   >> checking type of a character in a string:
#   1.isupper
#   2.islower
#   3.isdigit
#   4.isspace
#   5.istittle
#   6.isalpha
#   7.isalnum 


##checking start and part of a string:

## starting  :   The startswith() method checks if a string starts with a specified substring.                    
# ## ending  :  The endswith() method checks if a string ends with a specified substring.

##methamcical operator:
##  +  >>concatination
##  *  >> repetation operator
##     to get space by using repetation ((s + " ")*10)

##  strip() :The strip() method will remove all occurrences of those characters from both ends of the string.
#    > lstrip : leftside space
#    >rstrip  :right side space 


## join:he join() method in Python is used to concatenate a sequence of strings into a single string, 
#              with a specified separator between each string

words = ["apple", "banana", "cherry"]
result = " ,".join(words)
print(result)  


## replace
##find

##indexing:

##sciling:






#list[ ]:collection of character and different datatypes and storing in a single variable
# adding elements:
#        >>append: adding element at end of the list
#        >>insert:adding a new element in the specific index postion
#        >>extent:adding a two list with  the same datatypes or different datatypes
#        >>pop():it will remove the last element from the list
#        >>remove():it will the specific element
#        >> clear(): it will clear the entry list
# >>ordering of list
#        >>sort(): ordering of elements
l=[1,4,6,2,3]
l.sort()
print(l)   # we will get the accending order of the list
#       
l.reverse()
print(l)

#        >>reverse(): it will reverse the list and we can use the scling  also
#
#alising : giving a refrence variable name to the existing variable
#    >>these means that cahnges made to one variables will effect other refrence the same object
#
#cloning:we will get different id in duplicate variables also
#     >> it means if changes made in to the class do not effect original object
#    >>slicing 
#    >>copy()    >>>[:]
#
# nested list[]: list present inside the one list
#
#
#list comprehesion: convertering a  large program into single line
# 
l=[x for x in range(1,11)]
print(l) 
#
#
#
## tuple():order collections of element and immutable
#     >> we cannot change the tuple once we given elements
#
#accessing of tuple():
# >>we can acess by using index and sciling
#
t=(1,2,3,4,5,6)
print(t[2])
print(t[2:5])
#

## methode of tuple():
#count()
#index()
# how can we find higest frequency of elements

# operator in tuple():
# addition:(a+b)
#repetation:(a*2)


##packing and unpacking of elemnts:
# packing : it is creating a tuple by group of elements
# unpacking: it is  extracting the values from a tuple into individual variables

## modifing of tuple elements in to list:
#    >> by using typecasting


t=(1,2,3,4,5,6)
l=list(t)
l.append(7)
print(l)
t=tuple(l)
print(t)




##set{}:set is an unordered and it is mutable and we can modify the data and it will not give dupliacete

#s={}
#s=set()
#type(s)

## adding element to set:
#add()
s={1,2,3,4}
s.add(7)
print(s)

#update()
s=set()
l=[1,2,3]
s.update(l)
print(l)

##removing of elements:
# 
#pop(): it will remove the first element from the set and it will get the accesding order
#
#discard():it will remove the paticular element from the set

## union():
#     >>it will add two set elements without dupliates (s.union(s1))
## intersection():
#    >> it will return only common elements in the both the sets
s={1,2,3,4,5}
s1={1,3,6,7,8,9}
print(s.intersection(s1))  #output {1, 3}
#
#difference():
#     >> it will return sl elements which are not present in s2
s={1,2,3,4,5}
s1={1,3,6,7,8,9}
print(s.difference(s1))   #output: {2, 4, 5}

##symetric_difference():
#     >>it will return both s1 and s2 which are not present in both the sets
s={1,2,3,4,5}
s1={1,3,6,7,8,9}
print(s.symmetric_difference(s1))   #output:   {2, 4, 5, 6, 7, 8, 9}
#



#dictinary:
#        >>it is a keyvalue pair
#        >> unique kays and value can be duplicates
#        >>we can cahnge values but not keys
#        >.we can add new elements
#       >>we can delect the elements
#
#       d={}
#       print(type(d))
# 
d = {"name": "preethi", "age": 30, True: "some_value"}
print(d)

#adding element to the dictionary:
dict={}
dict["name"]="nani"
dict["age"]=30
print(dict)

"""dict={}
for i in range (3):
    key=input("enter key:")
    value=input("enter value:") 
    dict[key]=value
print(dict)"""



#update the elements:
#          >> if the key avaliable in dict value is update  or else elements added to the dict
"""dict["name"]="sai"
print(dict)"""
#
###
##accesing of elements:
#print(dict("key"))
print(dict.get("key"))

##items:
#    >> we get all elmemts in the dict
#  print(dict.items())
#

##accesing only key():
# print(dict.key())

##accessing only values():
#   print(dict.values())


#removing elements:
#pop(): remove and return specified elements in dict
#
#dict={}
#print(dict)
#print(dict.pop("key"))
#
#popitems():remove and return last items
#   >>print(dict.popitem())

#add of values:
#print(x.values())
#print(sum(x.values()))



## varuables in oops:
#  types of variables:
#         >>instance variable
#           >declaration:
#             1.variable that cajnges from objext to object
#             2.it is creted by self keyword
#             3.we can create instance variable inside of constructor and instance methode
#        
#
#
#
#
#
##
#            >>static variable
#             >>local variable
#  