print("Demonstration of dict")

#Data : Heterogeneous
#Ordered : Yes  #Data is in line - and are placed at the index
#Indexed : No   #integral
#Mutable : Yes
#Duplicates : No # for key No , for value Yes

programming = {"C":"Ritchie","C++":"Strostrup","Java":"Gosling","Python":"Rossum"}
# key and value both are string
Batches = {"PPA":18000,"LB":16700,"Python":16500,"Angular":15000}
#Here old value will be overwrite for key when duplicates are inserted.
Batches = {"PPA":18000,"LB":16700,"Python":16500,"Angular":15000,"PPA":"16700"}

#Accepts both Key Value same input
Batches = {"PPA":18000,"LB":16700,"Python":16500,"Angular":15000,"C":"C"}

#Key int , value int

print("Data of dictionary batches:",Batches)
print("Data type is :",type(Batches))
print("Length of the dictionary ",len(Batches))
#len tells no of pairs.

print("Value of PPA is:",Batches["PPA"])
print("Value of PPA is:",Batches["C"])
#Duplicates are
print()


