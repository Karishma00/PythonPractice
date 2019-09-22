#Same as list but immutable

t1=(1,2,3,4,1)
l1=[1,2,3,4,5]

print("Tuple ",t1)
print("list ",l1)

#Types of both
print(type(l1))
print(type(t1))

#List can be changed but tuple are not
l1[2]=6
print(l1)

#Indexing in tuple
print(t1[3])
print(t1[::-1])#Reverse the tuple

#Methods of tuple
print(t1.count(1))#Count the occyrences of char
print(t1.index(3))

t2=(1, 'kbn',[3,6,9])
print(t2)



