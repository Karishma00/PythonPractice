x=[1,2,3]
for i in x:
    #Just do nothing
    pass
print('Use of pass')

#continue
str="abcde"
for i in str:
    if(i=='c'):
        continue
    else:
        print(i)

#break
for i in str:
    if(i=='c'):
        break
    else:
        print(i)
