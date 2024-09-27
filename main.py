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