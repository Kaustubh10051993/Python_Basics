print("Demonstration of dict")

#Data : Heterogeneous
#Ordered : Yes  #Data is in line - and are placed at the index
#Indexed : No   #integral
#Mutable : Yes
#Duplicates : No # for key No , for value Yes

programming = {"C":"Ritchie","C++":"Strostrup","Java":"Gosling","Python":"Rossum"}
# key and value both are string
Batches = {"PPA":18000,"LB":16700,"Python":16500,"Angular":15000}
#Key int , value int

print("Data of dictionary batches:",Batches)

print("Data traversal using for loop")

#Returns values of Key
#for each loop in C

for x in Batches:
    print(x)


#Returns Key and value both

for x in Batches:
    print(x,Batches[x])

#Returns Key and value both


for x in Batches:
    print(x,Batches.get(x))

Keybatches = Batches.keys()
print(Keybatches)
print(type(Keybatches))


Valuebatches = Batches.values()
print(Valuebatches)


for i in range(0,len(Batches)):
    print("Batch name is:",Keybatches[i],end = " ")
    print("Fees are:ValueBatches[i]")
#TypeError: 'dict_keys' object is not subscriptable

for i in range(0,len(Batches)):
    print("Batch name is:",Keybatches[i],end = " ")
    print("Fees are:ValueBatches[i]")

