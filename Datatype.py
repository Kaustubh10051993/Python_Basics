print("Demonstration of list")

#Data : Heterogeneous
#Ordered : Yes  #Data is in line - and are placed at the index
#Indexed : Yes
#Mutable : Yes
#Duplicate :

#Commands -
#append -
#pop -
#remove -
#insert -


data = [11,21,51,101,11,21]

print(data)

data.append(501)
print(data)

data.remove(21)
print(data)

data.pop()
print(data)

for i in data:
    print(i,end = " ")

data.insert(0,'ABC')
print(data)

#output is [11, 21, 51, 101, 11, 21] - means that the data when is entered is inserted in line and at the index

tuple = ()
