class base:
    yourname = ""
    def setname(self, songname):
        self.yourname = songname

    def getname(self):
        return self.yourname

a = base()
a.setname("khalid")
print(a.getname())

#################################################################

try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print(a/b)
except ZeroDivisionError as z:
    print(z)

else:
    print(a/5)

#################################################################


a = [1, 2, 3]
try: 
    print ("Second element = %d" %(a[1]))
    print ("Fourth element = %d" %(a[3]))
  
except:
    print ("An error occurred")

#################################################################

a = 14
if a <= 18:
    raise Exception("you are below 18")

#################################################################

from abc import ABC, abstractmethod 
class Polygon(ABC):  
    @abstractmethod
    def sides(self):   
      pass  
class Triangle(Polygon):   
   def sides(self):   
      print("Triangle has 3 sides")   
  
class Pentagon(Polygon):     
   def sides(self):   
      print("Pentagon has 5 sides")   
  
class Hexagon(Polygon):    
   def sides(self):   
      print("Hexagon has 6 sides")   
  
class square(Polygon):   
   def sides(self):   
      print("square have 4 sides")   
    
t = Triangle()   
t.sides()   
s = square()   
s.sides()   
p = Pentagon()   
p.sides()   
k = Hexagon()   
k.sides()


#################################################################


class Base:
    def __init__(self):
        self._a = 2

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("protected member of base class: ", self._a)
        self._a = 3
        print("modified protected member: ", self._a)
 
ob1 = Derived()
ob2 = Base()
print("Accessing protected member of obj1: ", ob1._a)
print("Accessing protected member of obj2: ", ob2._a)


#################################################################