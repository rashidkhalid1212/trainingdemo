st = input("Enter a string: ")

n = len(st)

a = 0

for i in range(n):

    if st[i] == st[n-1-i]:

        a = 1

    else:

        a = 0


if a == 1:

    print("the string is a palindrome")

else:

    print("the string is not a palindrome")

#######################################################################


def factorial(n):

    if n == 0 or n == 1:

        return 1


    else:

        return n * factorial(n-1)


n = int(input("Enter a number: "))

print(factorial(n))

#######################################################################


def fib(n):

    if n == 0:

        return 0

    elif n == 1:

        return 1

    else:

        return fib(n-1)+fib(n-2)


n = int(input("Enter a number: "))

print(fib(n))

#######################################################################


n = int(input("Enter a number: "))

t = n

sum = 0

while t > 0:

    digit = t%10

    sum += digit**3

    t = t // 10


if n == sum:

    print(n, "is an Armstrong number")

else:

    print(n, "is not an Armstrong number")

#######################################################################


a = int(input("Enter first number: "))

b = int(input("Enter second number: "))

o = input("Enter operator: ")


if o == '+':

    print(f"{a} + {b} = {a+b}")

elif o == '-':

    print(f"{a} - {b} = {a-b}")

elif o == '*':

    print(f"{a} * {b} = {a*b}")

elif o == '/':

    print(f"{a} / {b} = {a/b}")

elif o == '%':

    print(f"{a} % {b} = {a%b}")

else:

    print("You can use only +, -, *, / and % Operators")

#######################################################################


for i in range(4):

    for j in range(4):

        print('*', end=' ')
    print()

-----------------------------------------------------------------


for i in range(5):

    print("* " * (5 - i))

-----------------------------------------------------------------


for i in range(5):

    print("* " * i)

-----------------------------------------------------------------


n = 0

for i in range(5):

    for j in range(i):

        print(n, end=' ')

        n += 1
    print()

-----------------------------------------------------------------


n = int(input("Enter a number: "))

for i in range(n):

    for j in range(n):

        if i == 0 or j == 0 or i == n-1 or j == n-1:

            print("*", end=' ')

        else:

            print(" ", end=' ')
    print()

-----------------------------------------------------------------


# diagonal in a square/rectangle :-->


n = int(input("Enter a number: "))

for i in range(n):

    for j in range(n):

        if i == 0 or j == 0 or i == n-1 or j == n-1 or i == j:

            print("*", end=' ')

        else:

            print(" ", end=' ')
    print()

-----------------------------------------------------------------

#######################################################################


Year = int(input("Enter the number: "))


if Year % 400 == 0 or Year % 100 != 0 and Year % 4 == 0:

    print("Given Year is a leap Year")

else:

    print ("Given Year is not a leap Year")

#######################################################################


n = int(input("Enter a number: "))


a = 0

for i in range(2, n):

    if n % i == 0:

        a += 1


if a > 0:

    print(f"{n} is not a prime number")

else:

    print(f"{n} is a prime number")

#######################################################################


r = float(input("Enter the radius of circle: "))


area = 3.14 * r * r

print("Area of circle is ", area)

#######################################################################


myList = ['carrot', 'tomato', 'mango', 'apple', 'banana']

myList.reverse()
print(myList)

#######################################################################

myList = [3, 54, 5, 23, 94, 2, 5]

sum = 0
for i in myList:
    sum += i

print(sum)

#######################################################################

myList = [3, 54, 5, 23, 94, 2, 5]

sum = 0
for i in myList:
    sum += i

avg = sum/len(myList)
mn = min(myList)
mx = max(myList)

print("average of numbers in the list is: ", avg)
print("minimum of numbers in the list is: ", mn)
print("maximum of numbers in the list is: ", mx)

#######################################################################

list1 = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
mydict = {}

for i, j in list1:
    mydict.setdefault(i , []).append(j)

print(mydict)

#######################################################################

def nested_dictionary(l1, l2, l3):
    result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
    return result

ls1 = ["S001", "S002", "S003", "S004"] 
ls2 = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
ls3 = [85, 98, 89, 92]

print(nested_dictionary(ls1, ls2, ls3))

#######################################################################

a = {32, 53, 23, 75, 84}
b = {53, 75, 84}

c = b.issubset(a)
print("b is subset of a: ", c)

#######################################################################

a = {32, 53, 23, 75, 84}
b = {53, 75, 84}

c = a.symmetric_difference(b)
print(c)

#######################################################################

a = {32, 53, 23, 75, 84}
b = {53, 75, 84, 35, 23, 92}

c = a.difference(b)
print(c)

#######################################################################

MyList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

MyList = [t for t in MyList if t]
print(MyList)

#######################################################################

a = ((10,10,10,12), (30,45,56,45), (81,80,39,32), (1,2,3,4))

b = [sum(x)/len(x) for x in zip(*a)]
print(b)

########################################################################