l1 = ['m', 'n']
l2 = []
n = 3

for i in range(n):
    a = l1[0]+str(i+1)
    l2.append(a)

for i in range(n):
    a = l1[1]+str(i+1)
    l2.append(a)

print(l2)

################################################################

mylist = [[4,5,3], [6,3,2], [6,9,1]]
nlist = []

sum = 0
for i in mylist:
    for j in i:
        sum += j
    nlist.append([sum])
    sum = 0

print(nlist)

################################################################

lis = [1, 2, 3, 0, 1, 1, 4, 5, 2, 3]
lis2 = []

for i in lis:
    if i not in lis2:
        lis2.append(i)

print(lis2)

# ################################################################

for i in range(1200, 3000):
    if i%4 ==0 and i%8 == 0 and i%6 != 0:
        print(i)
