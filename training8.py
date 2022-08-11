class complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary

    def complex_num(self):
        num = f'{self.real} + {self.imag}i'
        print(num)

    def _sum(self, num1, num2):
        a = complex(0, 0)
        a.real = num1.real + num2.real
        a.imaginary = num1.imag + num2.imag
        return a

    def difference(self, num1, num2):
        b = complex(0, 0)
        b.real = num1.real - num2.real
        b.imaginary = num1.imag - num2.imag
        return b

    def product(self, num1, num2):
        b = complex(0, 0)
        b.real = num1.real * num2.real
        b.imaginary = num1.imag * num2.imag
        return b
        


ob1 = complex(2, 3)
ob1.complex_num()
ob2 = complex(4, 6)
ob2.complex_num()

ob3 = complex(0, 0)
ob3 = ob3._sum(ob1, ob2)
print(f'Sum of complex number:{ob3.real} + {ob3.imaginary}i')

ob3 = ob3.difference(ob1, ob2)
print(f'difference of complex number:{ob3.real} + {ob3.imaginary}i')

ob3 = ob3.product(ob1, ob2)
print(f'product of complex number:{ob3.real} + {ob3.imaginary}i')



from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    def area(self):
        pass
class Rectangle(Polygon):
    def perimeter(self,length,breadth):
        return 2*(length+breadth)
    def area(self,length,breadth):
        return length*breadth
class Square(Polygon):
    def perimeter(self,length,sides):
        return sides*length
    def area(self,length):
        return length*length
class Rpentagon(Polygon):
    def perimeter(self,length,sides):
        return sides*length
    def area(self,length,sides):
        return 1/2*sides*length*length
length=int(input("Enter length of polygon "))
breadth=int(input("Enter breadth of polygon "))
sidesR=int(input("Enter sides of rectangle "))
sidesS=int(input("Enter sides of square "))
sidesP=int(input("Enter sides of pentagon "))
R=Rectangle()
print("Perimeter and Area of Rectangle are ")
print(R.perimeter(length,breadth),R.area(length,breadth))
S=Square()
print("Perimeter and Area of square are ")
print(S.perimeter(length,sidesS),S.area(length))
P=Rpentagon()
print("Perimeter and Area of regular pentagon are ")
print(P.perimeter(length,sidesP),P.area(length,sidesP))

