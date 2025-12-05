# # class-> blue print for creating objects
# class employee:
#     # name =" aqib"
#     language= "python"
#     salary=120000
#     def getinfo(self):
#         print(f"the language is {self.language} and salary is {self.salary}")
# harry = employee()
# # print(harry.language,harry.salary)
# harry.getinfo() #(this gets converted to ---->employee.getinfo(harry))


# jamid= employee()
# jamid.name="jamid fayaz" #we call it as instance attribute
# print(jamid.name,jamid.language,jamid.salary)
# #here name is the object attribute and language and salary is the class attribute as it dirrectly belong to the class
# #and instance or object attribute always is preferenced over class attribute


# aqib= employee()
# aqib.language="javascript"# as it is a object attribute it will take javascript as value bcx it has high prefernce over the class attribute
# aqib.name="aqib"
# print(aqib.name,aqib.language,aqib.salary)

class account():
    def __init__(self,name,age,balance):
        print("welcome to jkbank")
        self.name=name
        self.age=age
        self.balance=balance
    
    def Balance(self):
        print(self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    def withdrawl(self,amount):
        if amount>self.balance:
            return ("insufficeint balance")
            
        else:
            self.balance=self.balance-amount
            return self.balance
obj1=account("jamid",29,1000)
print(obj1.name)
print(obj1.balance)
# print(obj1.deposit(1200))
print(obj1.withdrawl(1200))

obj2=account("anayat",19,100000000)
print(obj2.name)
print(obj2.balance)
# print(obj2.deposit(1200))
print(obj2.withdrawl(1200))



#inheritince Using super() to Extend Parent Method
# class Person:
#     def show(self):
#         print("I am a person.")

# class Student(Person):
#     def show(self):
#         super().show()   # calling parent method
#         print("I am a student.")
#         print("i am aqib")

# s = Student()
# s.show()

    
# #adding new methods to a child class
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def work(self):
#         print(f"{self.name} is working...")

# class Manager(Employee):
#     def approve_leave(self):
#         print(f"{self.name} approved a leave request.")

# m = Manager("Rahul", 50000)
# m.work()
# m.approve_leave()


# #Multilevel inheritence

# class A:
#     def method1(self):
#         print("Method of A")

# class B(A):
#     def method2(self):
#         print("Method of B")

# class C(B):
#     def method3(self):
#         print("Method of C")

# obj = C()
# obj.method1()
# obj.method2()
# obj.method3()

# # Constructor Inheritance + Methods

       
# class Shape:
#     def __init__(self, color):
#         print("shape")
#         self.color = color

#     def show_color(self):
#         print("Color:", self.color)

# class Rectangle(Shape):
#     def __init__(self, color, width, height):
#         print("constructor of rectangle")
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
# class square(Rectangle):
#     def __init__(self, color, width, height):
#         print("square")
#         super().__init__(color, width, height)

# # r = Rectangle("Blue", 5, 4)
# p = square("red", 12, 56)
# # r.show_color()
# # print("Area:", r.area())


#DECORATOR 
