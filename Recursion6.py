#Calling the function frmo itself
#Static local variable to control recusion
#Major Drawback - StackOverflow
#Time and memory space used in Recursion is more than loop
#Write normal function with While
#Recursion TYPE -  Head and Tail
#If recursive call at head then it is head recusrsion , Tail recursion

def Add(No):
    if (No <=0):
        return 1
    else:
        return (No*Add(No-1))

Ret = Add(4)
print(Ret)

#File IO