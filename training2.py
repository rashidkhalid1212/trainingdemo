# for x in range(3):
#     for y in range(5):
#         print('*', end=' ')
#     print()

# ####################################################################

# for i in range(4):
#     print('*' * (i+1))

# ###################################################################

# n= 4
# for i in range (n,0,-1):
#     print((n-i) * ' ' + i * '*')

# ####################################################################

# rows = 4
# columns = 4
# for i in range(rows):
#     for j in range(columns):
#         if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
#             print('*', end = '  ')
#         else:
#             print(' ', end = '  ')
#     print()

# ####################################################################

# n = 0
# while(n < 5):
#     print(n+1)
#     n += 1

# ####################################################################

# a = 23
# b = 12
# print("arithmetic operator")
# print(a*b)
# print(a/b)
# print(a-b)
# print(a+b)
# print(a//b)
# print(a**b)

# print("comparison operator")
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
# print(a!=b)
# print(a==b)

# print("logical operator")
# print(a > b and a<b)
# print(a > b or a<b)
# print(not(a>b))

# print("bitwise operator")

# print(a&b)
# print(a|b)
# print(a^b)
# print(~a)
# print(~b)


##############################################################

# st = "1441"
# n = len(st)
# for i in range(n):
#     if st[i] == st[n-1-i]:
#         True
#         print("the string is palindrome")
#     else:
#         print("the string is not palindrome")

#----------------------------or-------------------------------#

num=int(input("Enter a value:"))
temp=num
rev=0
while(num>0):
    dig=num % 10
    rev=rev*10+dig
    num=num // 10
if(temp == rev):
    print("This value is a palindrome number!")
else:
    print("This value is not a palindrome number!")

###############################################################


