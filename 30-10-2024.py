## variables in oop:

# types of variables:
## 1.instance variables:
##    >>declarations:
#          >>varable that changes from object to object
#          >>it is created by self keywords
#         >> we can create instance variables inside of constructor and instance method
# 
#     >>accesing :
#         >>we can access instance variable class by using self keyword
#         >>we can access outside of the class  using ORV(object refrence variable)
#

class emp:
    def __init__(self):
        self.name="sai"
        self.salary=20000

    def dispaly(self,age,id):
        self.age=age
        self.id=id
        print(self.name)
        print(self.salary)
        

e=emp()
e.dispaly(24,217)
print(e.name) # we can access outside the class
print(e.age)




class collage:
    def __init__(self,name,branch,rollno,classno,blockno):
        self.name=name
        self.branch="eee"
        self.rollno=rollno
        self.classno=classno
        self.blockno=blockno 

    def display(self):
        print(self.branch)
        print(self.name)
        print(self.rollno)
        print(self.classno)
        print(self.blockno)

c=collage("sai","eee",217,203,1608)
c.display()

c1=collage("nani","eee",218,204,1708)
c1.display()




class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def c(self):
        print(self.name)
        print(self.age)

c1=cat("chitt",2.5)
c1.c()
c2=cat("cat",1.4)
c2.c()        




#static variable:
#   >>declaration:
#        >>in static variable is not changing object to object
#       >>we can declare a static variable inside the class directly
#       >>inside the constructor ,instance methode using classname
#       >>outside of class using class name
#       >>inside the class methose using class variable
#
#    >>accessing :
#         >>using class name we can access inside the constructor and instance method
#         >>outside of a class using classname and ORV
#         >>inside of the class method using class variable
#  
#

class collage:
    collagename="sasi collage"  ##we can declare a static variable inside the class directly
    def __init__(self,name,branch,rollno):
        
        self.name=name
        self.rollno=rollno
        
        collage.branch="eee branch"  # inside the constructor ,instance methode using classname
        
        print(collage.branch) # class name we can access inside the constructor and instance method
    
    def d(self):
        collage.section="section B"
        print(self.name)
        print(self.rollno)
       

s=collage("sai","eee",217)
print(collage.collagename)

collage.age=22  ## outside of a class using classname and ORV  
s.d()  
print(collage.age)  





class cat:
    catbread="labour"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        cat.legs="4 legs"

    def c(self):
        cat.eyes="2 eyes"
        print(self.name)
        print(self.age)
s=cat("chitti",2.5)
s.c()
print(cat.catbread)
print(cat.legs)
print(cat.eyes)















