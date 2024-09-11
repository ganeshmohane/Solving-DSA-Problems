# file handling

## Read
f = open('D:\Desktop\Solving-DSA-Problems\demo.txt','r') 
print(f.read())
print(f.read(5))
print(f.readline())
for x in f:
    print(x)
f.close()

## Append
w = open('D:\Desktop\Solving-DSA-Problems\demo.txt','a') 
w.write("New Writing")
w = open('D:\Desktop\Solving-DSA-Problems\demo.txt','r')
print(w.read())
w.close()

## Overwrite
ow = open('D:\Desktop\Solving-DSA-Problems\demo.txt','w')
ow.write("Overwriting everything in file")
ow = open('D:\Desktop\Solving-DSA-Problems\demo.txt','r')
print(ow.read())
ow.close()

## Create
c = open('create.txt','x')

## Delete
import os 
if os.path.exists('D:\Desktop\Solving-DSA-Problems\Python\create.txt'):
    os.remove('D:\Desktop\Solving-DSA-Problems\Python\create.txt')
    print('file successfully removed')
else :
    print('File is already removed')