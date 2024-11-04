#local variable : 
# it will be allowed within the particular fuctions
# we cannot access outside the class or function
#  >declaration:
#         >>we are declaring thses local variable directly inside of static method


class test:
    def add(self):
        a=20
        b=4
        return a+b
    def sub(self):
        c=3
        d=3
        return c-d
       # return a+b  >> we cannot access outside the fuction to the another function or class 
    #return a+b
    
t=test()
print(t.add())
print(t.sub()) 



#instance method:
# >we can declaring and accessing a instance variable inside a method
# >while declaring instance method have to pass self as an first paramater
# >we can acces thses instance method using orv or classname


###instance method:

class fruits:
    def __init__(self,apple,orange,banana):
        self.apple=apple
        self.orange=orange
        self.banana=banana

    def m(self,totalprice):
        self.totalprice=totalprice 
        print(self.apple)
        print(self.banana)
        print(self.orange)  
        print(self.totalprice)

f=fruits(2,2,2)
f.m(200)   


class dog:
    def __init__(self,name,age):

        self.name=name
        self.age=age

    def m(self,bread):
        self.bread=bread
        print(self.name)
        print(self.age)
        print(self.bread)  

d=[]
m1=int(input("enter a number_of:"))  
for i in range(m1):
    name=input("enter a name:")
    age=int(input("enter a age:"))

    dog=dog(name,age)
    d.append(dog)

for dog in d:
    dog.m("labour")       



class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def wish(self):
        print(self.name)
        print(self.age)
 
    def introduce(self):
        self.wish()
        print("tomorrow is my birthday")

person= person("reddy", 25)
person.introduce()






#class method:
#  >inside the class method have  to use only static variable
# >while declaring class method have to pass @class method 
# >while declaring class method have to pass cls as first parameter
# > using cls keyword we can declare and can access the data in side class method

class fruit:
    totalprice=2000
    @classmethod
    def m(cls,apple,banana,orange):
        cls.shopname="NPR"
        print(apple)
        print(banana)
        print(orange)
        print(fruit.totalprice)
        print(cls.shopname)

p=fruit()
p.m(3,2,4)              



class collage:
    branch="eee"
    @classmethod
    def m(cls,name,rollno):
        cls.collagename="sasi"
        print(name)
        print(rollno)
        print(cls.branch)
        print(cls.collagename)

c=collage
c.m ("nani",217)       


class filpkart:
    price=20000
    @classmethod
    def m(cls,name,rating):
        cls.companyname="NPR"
        print(name)
        print(rating)
        print(cls.companyname)
        print(cls.price)

f=filpkart()
f.m("redmi","4star")



##static method:
#  >>we are not using instance and static variable
#  >we are not passing any paramter like self or cls
# >we have to pass @staticmethod decorate
# >we can access static method using class anem and cls variable
        

class add:
    @staticmethod  # >>it is a stasticmethod we acn access directly in the class
    def m():
        a=2
        b=4
        print(a+b)
    
a1=add()
a1.m()



class bank:
    @staticmethod
    def m():
        name="nani"
        age=25
        phone_no=7702616317
        acc_no=223
        return name ,age,phone_no,acc_no

b=bank()
print(b.m())    



class vegetables:
    @staticmethod
    def m():
        carrot=2
        beetroot=3
        tomato=4
        cucumber=5
        totaliteams=carrot+beetroot+tomato+cucumber

        return totaliteams
v=vegetables()
print(v.m())
 


  






class bank:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def m(self,acc_no,ph_no):
        self.acc_no=acc_no
        self.ph_no=ph_no 
        print(self.name)
        print(self.age)
        print(self.acc_no)
        print(self.ph_no)  

d=[]
m1=int(input("enter a number_of:"))  
for i in range(m1):
    name=input("enter a name:")
    age=int(input("enter a age:"))
    bank=bank(name,age)
    d.append(bank)

for bank in d:
    bank.m(223,7702616317)                