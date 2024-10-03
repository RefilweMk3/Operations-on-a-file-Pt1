file=open("ref.txt","r")
print(file.read(8))
file.close()

file=open("ref.txt","r")
print(file.readline())
file.close()

file=open("ref.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open("ref.txt","r")
print(file.readlines())
file.close()

file=open("ref.txt","r")
for x in file:
    print(x)
file.close

f1=open("main.txt","r")
f2=open("py.txt","w")

for line in f1.readlines():
    if not(line.startswith('Coding')):
        f2.write(line)
f1.close()
f2.close()

b1 = open("main.txt","r")
b2 = open("ref.txt","w")

cont = b1.readlines()
type(cont)
for i in range(1,len(cont)+1):
    if(i % 2 !=0):
        b2.write(cont[i-1])
    else:
        pass
b2.close()
b2 = open("ref.txt","r")
cont1 = b2.read()
print(cont1)
b1.close()
b2.close()
