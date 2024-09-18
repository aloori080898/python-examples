class Employee:
    def display(self):
        print("Hello my name is Daniel")

emp = Employee()
emp.display()


class Employee:
    def display(self):
        print("Hello my name is Daniel")
    def teaching(self):
        print("I like teaching")

emp = Employee()
emp.display()
emp.teaching()


class Employee:
    def __init__(self):
        print("constructor is executed")
emp = Employee()



class Employee:
    def __init__(self):
        print("constructor is executed")
emp = Employee()
emmp = Employee()



class Employee:
    def __init__(self,number):
        self.number = number
        print("Empolyee id is:",self.number)
emp = Employee(1)
emp = Employee(2)
emp = Employee(3)
emp = Employee(4)

class Employee:
    def __init__(self, number):
        self.number = number
    def display(self):
        print("Employee id is:", self.number)

e1 = Employee(1)
e2 = Employee(2)
e3 = Employee(3)
e1.display()
e2.display()
e3.display()

class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name
    def display(self):
        print("Hello my id is :", self.number)
        print("My name is :", self.name)

e1=Employee(1, 'Daniel')
e1.display()
e2=Employee(2, 'Arjun')
e2.display()

class Employee:
    def __init__(self, number, name, age):
        self.number = number
        self.name = name
        self.age = age
    def display(self):
        print("Hello my id is :", self.number)
        print("My name is :", self.name)
        print("My age is sweet :", self.age)

e1=Employee(1, 'Daniel', 16)
e1.display()
e2=Employee(2, 'Arjun', 17)
e2.display()
e3=Employee(3, 'Prasad', 18)
e3.display()



class Student:
    def __init__(self, name, number):
        self.name=name
        self.number=number
s1 = Student('Daniel', 101)
s2 = Student('Prasad', 102)
print("Studen1 info:")
print("Name: ", s1.name)
print("Id : ", s1.number)
print("Studen2 info:")
print("Name: ", s2.name)
print("Id : ", s2.number)


class Employee:
    def __init__(self):
        self.eno = 10
        self.ename = "Daniel"
        self.esal = 10000

emp = Employee()
print("Employee number:", emp.eno)
print("Employee name:", emp.ename)
print("Employee salary:", emp.esal)


class Demo:
    def __init__(self, a):
        self.a=a
    def m(self):
        print(self.a)

d=Demo(10)
d.m()



