class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
 
    def get_employee_info(self):
        print(self.__name)
        print(self.__age)
        print(self.__salary)
 
    def increase_salary(self, percentage):
        self.__salary *= (1 + percentage / 100)
 
emp = Employee("nani", 25, 24000)
print(emp.get_employee_info())  
emp.increase_salary(10)
print(emp.get_employee_info())  
 
class bike:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0
 
    def accelerate(self):
        self.__speed += 10
 
    def brake(self):
        self.__speed -= 20
 
    def get_speed(self):
        return self.__speed
 
bike= bike("bullet", "battalion black", 2017)
bike.accelerate()
print(bike.get_speed())  
bike.brake()
print(bike.get_speed())  
 
 
class student:
    def __init__(self, name, rollno, dept):
        self.__name = name
        self.__rollno = rollno
        self.__dept = dept
 
    def get_student_info(self):
        print(self.__name)
        print(self.__rollno)
        print(self.__dept)

        
    def promot_nextsection(self, percentage):
        self.__dept *= (1 + percentage / 100)
 
std = student("nani", 25, 449)
print(std.get_student_info())  
std.promot_nextsection(10)
print(std.get_student_info())  