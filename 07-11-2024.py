##super():
##    >> is a built-in function that is used to call methods or 
#             access properties from a parent (or superclass) class

class product:
    website="flipkart"   #statsic variable
    def __init__(self,p_name,p_brand,p_rating):
        self.p_name=p_name
        self.p_brand=p_brand
        self.p_rating=p_rating    #instance variable
        product.quality="a+"     #static varible
    def m1(self,price):
        product.quantiy="4pices"
        self.price=price 
        print(self.p_name)
        print(self.p_brand)
        print(self.p_rating)
        print(self.price) 
        print(product.quantiy)  

f=product("toy","grils",3.4)
print(f.website)
print(f.quality)
f.m1(200)


class company:
    def __init__(self):
        self.c_name="aa"
        
    def m1(self):
        print(self.c_name)

class manager(company):
    def __init__(self):
        super().__init__()
        self.m_name="ww"
        self.m_id=23
        self.m_salary=23000

    def m2(self):
        print(self.m_name)
        print(self.m_salary)
        print(self.m_id)


m=manager()
m.m1()
m.m2()  



class product:
    def __init__(self,name,price,brand):
        self.name=name
        self.price=price
        self.brand=brand

    def m1(self):
        print(self.name)
        print(self.price)
        print(self.brand)    

class phone(product):
    def __init__(self, name, price, brand,rating):
        super().__init__(name, price, brand)
        self.rating=rating

    def m2(self):
        super().m2()
        print(self.rating) 


c=phone("iphone",34000,"apple",4.5)

c.m1()
    




class bank:
    def __init__(self,name,acc_no,ph_no,address):
        self.name=name
        self.acc_no=acc_no
        self.ph_no=ph_no
        self.address=address

    def dispaly(self):
        print(self.name)
        print(self.acc_no)
        print(self.ph_no)
        print(self.address)

class person(bank):
    def __init__(self,name):





















