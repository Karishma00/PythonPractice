

#Opening the file
file1=open('myfile1.txt')

#Reading the file
print(file1.read())

print(file1.read())#Gives blank so we have to set the cursor to the begining

print(file1.seek(0))
print(file1.read())

print(file1.seek(0))
print(file1.readline())#one line read

print(file1.seek(0))
print(file1.readlines())#Whole file read gives in list

#From othe location reading the file
file2=open('D:\\Read.txt')
#For linux file2=open('/Users/Username/Folder/file.txt')
print(file2.read())

file1.close()
file2.close()

#By using this no need to close
with open('myfile1.txt') as f:
    print(f.read())

#Appending  into file

with open('myfile1.txt',mode='a+') as f: #a+ for reading and append
    f.write("\n Forth line..")
    print(f.read())

#Writing with W
with open('wr.txt',mode='w') as f1:
    f1.write("How are u ?..")

with open('wr.txt','r') as f2:
    print(f2.read())
