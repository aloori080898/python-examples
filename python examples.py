print("hello")

student_id = 100
print(student_id)

value = 10
print(value)

age = 20
print(age)

age = 20
name = "raju"
print(age)
print(name)


name = "praveen"
age = 23
id = 101
print(name)
print(age)
print(id)
print(name,age,id)

name = "rakesh"
print("iam", name)


a, b ,c,d ,e ,f = 12,23,45,67,8,7
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


a = b = c =3
print(a)
print(b)
print(c)


sal = 1000
sal = 2000
print("my salary is",sal)


sal = 1000
sal = 2000
sal = 4000
print("my salary is",sal)

emp_id =1
name = "praveen"
salary = 1000
print("My employee id is",emp_id)
print("My name is",name)
print("My salary is",salary)

mp_id =1
name = "praveen"
salary = 1000.8
print("My employee id is",emp_id)
print("My name is",name)
print("My salary is",salary)
print()
print("emp_id type is",type(emp_id))
print("name type is",type(name))
print("salary type is",type(salary))

a = 20 
print(a)
print(type(a))


b = 9999
print(b)
print(type(b))


c = 9999.999
print(c)
print(type(c))

name = "praveen"
print(name)
print(type(name))

a = True
b = False
print(a)
print(b)

a = None
print(a)
print(type(a))

name1 = 'raju'
name2 = "raju"
name3 = "'raju'"
name4 = """raju"""
print(name1)
print(name2)
print(name3)
print(name4)
print()
print(type(name1))
print(type(name2))
print(type(name3))
print(type(name4))


values = [10,20,30,40]
print(values)
print(type(values))

values = (10,20,30,40)
print(values)
print(type(values))

values = { 10,20,10,20,30,40}
print(values)
print(type(values))

values = {10,20,30,40}
print(values)
print(type(values))


details ={101:"raju", 102:"karthik", 103 : "charan"}
print(details)
print(type(details))


a = range(6)
print(a)
print(type(a))

a = range(1,10)
print(a)
print(type(a))

r = range(0 ,20)
for value in r:
    print(value)

a = 10
b = 20
c = a+b
print(c)

a = 20
b =30
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a<b)
print(a>b)
print(a**b)
print(a//b)
print(a%b)
print(type(a+b))
print(type(a-b))
print(type(a/b))
print(type(a*b))
print(type(a<b))
print(type(a>b))
print(type(a**b))
print(type(a//b))
print(type(a%b))

a = 11
print(a)
a += 5
print(a)
print(type(a))


a = 10
print(a)
print(-a)

a = 20
print(a)
print(-a)
print(type(a))

a = 20
b = 24
print(a>b)
print(a<b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)


a = True
b = False
print(a and a)
print(a and b)
print(a or a)
print(a or b)
print(not a)
print(not b)

a = 4
b = 6
c = 8
print((a>b) and (a<b))
print((a<b) and (a>c))
print((b>c) and (c<d))

values = [10,20,30]
print(20 in values)
print(25 in values)
print(30 in values)
print(35 in values)

text = "Welcome to new house "
print("is"in text)
print("house"in text)
print("or"in text)
print("Welcome"in text)

name = input("Enter the name")
print("You entered name as",name)

name = input("Enter the name")
age = input("Enter the age")
print("You entered name as",name)
print("You entered age as",age)

value = input("Enter the value ")
print("Entered value as: ", value)
print("type is: ", type(value))


a = "123"
print(a)
print(type(a))

p1 = input("Enter First product price:")
p2 = input("Enter Second product price:")
a = int(p1)
b = int(p2)
print("Total price is:", a+b)


p1 = input("Enter First product price:")
p2 = input("Enter Second product price:")

print("Total price is:", p1+p2)


x =1 
y =3
print("x=y value is:",(x==y))
if x ==y:
    print("if block statements executed")

x = 1
y = 2
print("x==y value is: ", (x==y))
if x == y:
    print("if block statements executed")
    print("out of if block statements")

x = 1
y = 1
print("x==y value is: ", (x==y))
if x == y:
    print("if block statements executed")
else:
    print("else block statements executed")

x = 1
y = 1
print("x==y value is: ", (x==y))
if x == y:
    print("if block statements executed")
else:
    print("else block statements executed")

print("Please enter the values from 0 to 4")
x = int(input("Enter a number: "))
if x == 0:
        print("You entered:", x)
elif x == 1:
    print("You entered:", x)
elif x == 2:
    print("You entered:", x)
elif x == 3:
    print("You entered:", x)
elif x == 4:
    print("You entered:", x)
else:
    print("Beyond the range than specified")

values = [10, 20, 30, "Daniel"]
for value in values:
    print(value)


x = 1
while x <= 5:
    print(x)
x = x+1
print("End")


x = 1
while x<=10:
    print("x=", x)
x = x + 1
print("out of loop")


x = 1 
while x<= 10:
    print("x=",x)
    x = x +1
    if  x== 5:
        break
    print("out of loop")


x =1 
while x<=6:
    print("x=",x)
    x = x+1
    if x ==3:
        continue
    print("out of loop")

x =3
while x<=5:
    print("x=",x)
    x =x+1
    if x==6:
        pass
    print("out of loop")

name1= 'Daniel'
name2 = "Prasad"
name3 = '''Mouli'''
name4 = """Veeru"""
print(name1, "name is created by using single quotes")
print(name2, "name is created by using double quotes")
print(name3, "name is created by using triple single quotes")
print(name4, "name is created by using triple double quotes")


loc1 ='''TCS company
white field
hyderabad'''

loc2 = """TCS company
banglore
IT tech"""
print(loc1)
print(loc2)

wish = "Hello world"
print(wish[0])
print(wish[1])
print(wish[2])
print(wish[0:7])


wish ="Hello world"
for char in wish:
    print(char)

name = "pravven"
print(name)
print(name[0])
print(name[1])

a =  "Python"
b =  "programming"
print(a+b)

a = "race"
b = "booking"
print(a+b)

booking ="racing"
print(booking*8)

course = "python"
print(course*8)

course ="python"
print(len(course))

booking ="racing"
print(len(booking))

print('p'in "python")
print('r' in "python")
print('s'in "python")
print('on'in "python")


print('b'not in 'apple')



name = "praveen"
print(name.upper())

name = "PRAVVEN"
print(name.lower())

course ="python                           "
print(course.strip())

a = "python programming language"
print(a.count("python"))
print(a.count("hello"))


a = "java programming language"
print(a.count("programming"))
print(a.count("hello"))

s1 = "Java programming language"
s2 = s1.replace("Java", "Python")
print(s1)
print(s2)
print(id(s1))
print(id(s2))


a = "python programming language"
print(a.replace("python", "java"))


a = "python programming language"
print(a.split())

a = "python programming language"
a1 = a.split()
print(a)
print(a1)


def display():
    print("hello")

def display():
    print("python programming")
display()


def display():
    print("hello the world")
display()
display()

def first():
    print("hello")
def second():
    print("hi")
first()
second()

def m1 ():
    print("hi")
def m2():
    print("hello")
m1()
m2()


def m1():
    print("first columns")
def m2():
    print("second column")
m2()
m2()
m1()
m1()

def display(a):
    print("hello:",a)
display(10)


def details(a,b):
    print("hi:",a,b)
details(1,2)

def details(a,b):
    print("hi:",(a+b))
details(10,20)

def display(a):
    print("hello:",a)
display("daniel")


def balance ():
    print("my balance is:")
balance()

def balance():
    print("My balance is:")
    return 100
b = balance
print(100)


def balance():
    return 100
b = balance()
if b ==0:
    print("balance is:",b)
elif b<=0:
    print("balance is:",b,"negative please deposit")
else:
    print("balance:",b)

def balance():
    return 0
b = balance()
if b ==0:
    print("balance is:",b)
elif b<=0:
    print("balance is:",b,"negative please deposit")
else:
    print("balance:",b)

def balance():
    return -50
b = balance()
if b ==0:
    print("balance is:",b)
elif b<=0:
    print("balance is:",b,"negative please deposit")
else:
    print("balance:",b)


def balance():
    return -0.25
b = balance()
if b ==0:
    print("balance is:",b)
elif b<=0:
    print("balance is:",b,"negative please deposit")
else:
    print("balance:",b)

def balance ():
    print("my balance is:")
    return 100
print(balance())


def balance():
    print("my balance is")
    return -30
print(balance())


def m1():
    a =10
    b=20
    return a,b
x,y = m1()
print("first values is:",x)
print("second values is",y)

def m1():
    a =10
    b =23
    c =30
    return a,b,c
x,y,z = m1()
print("first value is:",x)
print("second value is:",y)
print("third value is:",z)

def m1():
    a =10
    b =23
    c =30
    return a,b,c
x = m1()
print("all values:",x)


def add (x,y,z):
    result = x+y+z
    return result
r = add(10,20,30)
print("addition of values:",r)

def add(a,b):
    c = a+b
    print(c)
x = 10
y = 13
add(x,y)


def sub(x,y):
    print(x-y)
sub(30,12)

def cart(booking,price):
    print("booking is:",booking)
    print("cost is:",price)
cart(booking ="hotel",price = 20000)



def cart(product, price):
    print("Product is :" , product)
    print("cost is :" , price)
cart(product = "handbag ", price = 100000)

def cart(product, price):
    print("Product is:" , product)
    print("cost is:" , price)
cart(price = 1200, product = "shirt")


def cart(product, price = 40.0):
    print("product is :", product)
    print("cost is :", price)
cart(product = "handbag", price = 10000)


def m1(*x):
    print(x)
m1(10,20)

def square(t):
    return t*t
s = square(4)
print(s)


def add(x,y):
    return x+y
b = add(23,45)
print(b)

without_gst_cost = [100, 200, 300, 400]
with_gst_cost = map(lambda x: x+10, without_gst_cost)
x = list(with_gst_cost)
print("Without GST items costs: ", without_gst_cost)
print("With GST items costs: ", x)


items_cost = [999, 888, 1100, 1200, 1300, 777]
gt_thousand = filter(lambda x : x>1000, items_cost)
x = list(gt_thousand)
print("Eligible for discount:", x)


from functools import reduce
items_cost = [111, 222, 333, 444]
total_cost = reduce(lambda x, y : x+y, items_cost)
print(total_cost)

a = []
print(a)
print(type(a))

numbers = [10,20,30,40]
print(numbers)
print(type(a))


booking = ["raju",10,20,30,40]
print(booking)
print(type(booking))

r = range(1,10)
a = list(r)
print(a)

r = range(1,10)
for values in  r:
    print(values)

r = range(0,20)
for values in r:
    print(a)
    
a = [10,20,30,40,40]
print(a)
print(type(a))


names =["raju","praveen","karthik"]
print(names)

names =["raju","praveen","karthik"]
print(names[0])
print(names[1])


n = [1,2,3,3,4,5,5,6,67,7]
print(n)
print(n[:])
print(n[::])
print(n[0:5:])


n = [1,23,4,5,6,7,78,8,8]
print(n)
print(n[:0])
print(n[:1])
print(n[0:2:])
print(n[1:5:])

values = [100,200,300,400]
for value in values:
    print(value)

values = [100,200,300,400]
print(values)
print(len(values))

n =[1,2,3,4,5,6,55,55,55,77,88]
print(n.count(5))
print(n.count(2))
print(n.count(55))

n = [10,20,30,40,50]
n.append(60)
n.append("raju")
print(n)

n  = [10,20,30,40,50]
n.insert(0,20)
n.insert(1,24)
n.insert(2,34)
print(n)

n = [10,20,30,40,50]
n.remove(50)
n.remove(40)
print(n)


n = [10,20,30,40,50,50,60,50,60,60,60,60]
n.remove(50)      
n.remove(60)
print(n)


n = [10,20,30,40,50]
n.reverse()
print(n)

n = [10,20,30,40]
print(n.reverse())


n = [10,2,3,4,5,6,7,7]
n.sort()
print(n)

number = (0,3,4,5)
print(number)
print(type(number))

emp_id=()
print(emp_id)
print(type(emp_id))


emp_id = (10,20,30,40)
print(emp_id)
print(type(emp_id))

t = (11,22,33,"raju")
print(t)
print(type(t))

a = [11,22,33]
t = tuple(a)
print(t)

t = (10,20,30,40,50)
print(t[0])
print(t[1])


t = (10,20,30,4,50)
print(t.count(2))
print(t.count(10))

t =(10,20,30,40)
print(t.index(10))
print(t.index(20))


s = {10,20,30,40,50}
print(s)
print(type(s))


s = {1,"raju",20.9,"karthik"}
print(s)
print(type(s))

s = set(range(4))
print(s)
print(type(s))

r = range(0,19)
l = set(r)
print(l)
print(type(l))

s = {}
print(s)
print(type(s))

s = set()
print(s)
print(type(s))

s = {10,20,30}
s.add(40)
print(s)

s = {10,20,30,40}
s.add(12)
print(s)
print(type(s))

s = {10,20,30,40}
s.remove(40)
print(s)

s = {10,20,30,40}
s.clear()
print(s)


d = {1:"raju",2:"karthik",3:"praneeth"}
print(d)
print(type(d))

d = {1:"raju",2:"karthik",3:"praneeth"}
print(d)
del d
print(d)


d = {10:"Ramesh",20:"Arjun",30:"Daniel"}
print(d)
d.clear()
print("After cleared entries in dictionary:", d)


d = {100: "Ramesh", 200: "Daniel", 300: "Mohan"}
print(d)
print(d.keys())

d = {100: "Ramesh", 200: "Daniel", 300: "Mohan"}
print(d)
print(d.values())

d = {100:"Ramesh", 200:"Daniel", 300:"Mohan"}
for k,v in d.items():
    print(k,v)

squares = {a: a*a for a in range(1,6)}
print(squares)


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










