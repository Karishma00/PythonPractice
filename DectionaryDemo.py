#Dictionary

dict={'key1': 'Abc','key2':'Mno','key3':'Pqr'}
print(dict)

#for value fetching
print(dict['key2'])

#Dict contains list and another dictionary in it
d={'k1': 234,'k2':[3,6,2,4,9],'k3':{1:'a',2:'b',3:'c'}}
print(d['k1'])

print(d['k2'])
print(d['k2'][3])

print(d['k3'])
print(d['k3'][2])

#grab the letter and upper to it
x=dict['key2']
print(x.upper())

#Another way of above into other dict
print(d['k3'][2].upper())

#add new key and valye
dict['key4']='JKL'
print(dict)

#change the value of key
dict['key1']='Changed'
print(dict)

#Get the keys of dictionary
print(dict.keys())
print(d.keys())

#Get the values of dictionary
print(dict.values())
print(d.values())

#Get the keys and values both of dictionary
print(d.items())
print(dict.items())