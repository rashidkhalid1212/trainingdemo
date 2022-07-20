class A:
    def f1(self):
        print('A')

class B(A):
    def f2(self):
        print("B")

ob = B()
ob.f1()
ob.f2()

############################################################

class A:
    def f1(self):
        print('A')

class B(A):
    def f2(self):
        print("B")

class C(B):
    def f3(self):
        print("C")

ob = C()
ob.f1()
ob.f2()
ob.f3()

############################################################

class A:
    a = 19
    b = 43
    def __init__(self):
        print('a')
    def m1(self):
        print('m1')
class B(A):
    a =23
    b =4
    def m2(self):
        print(self.a , self.b)
        print(super().a, super().b)
ob = B()
ob.m1()
ob.m2()

############################################################

class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add
 
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails
 
Emp_1 = Freelance(103, "Suraj", "Noida" , "KKK@gmail.com")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)

#############################################################

import math as m

a = 34
c = 12.54
d = 5
e = 234
b = m.sqrt(a)

print(b)
print(m.ceil(c))
print(m.factorial(d))
print(m.exp(e))
print(m.sqrt(d))
print(m.pow(a, d))
print(m.sin(a))

##############################################################
