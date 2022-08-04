f = open('test.txt', 'r+')
f.write('Good morning')
f.writelines(["rakesh\n", "harsh\n", "gurpreet\n"])

f.close()

t = open('test.txt', 'r')
l = t.readlines()

for x in l:
    print(x)