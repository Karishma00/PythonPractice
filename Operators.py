#range
print("Simple range")
list=[1,2,3,4]
for i in range(10):
    print(i)

#Range with steps
print("Range with steps :")
for i in range(1,10,2):
    print(i)

#Generators
print("Generators :")
#print(list(range(0,11,1)))

#Enumerate
for i, a in enumerate('abcd'):
    print(i,a)

#Zip
l1=[1,2,3]
l2=['a','b','c']
for i in zip(l1,l2):
    print(i)

l3=['@','#','$']
#print(list(zip(l1,l3)))

print('x' in [1,2,'x'])

print('Min',min(l3))
print('Max',max(l3))

#Random library
from  random import shuffle
l4=['a','n','d','f','e']
shuffle(l4)
print(l4)

#Generate random integer
from random import randint
a=randint(0,6)
print(a)

a=input('Enter the name :')
print(a)


