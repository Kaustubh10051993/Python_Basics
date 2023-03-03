#Calling the function frmo itself
#Static local variable to control recusion
#Major Drawback - StackOverflow
#Time and memory space used in Recursion is more than loop
#Write normal function with While
#Recursion TYPE -  Head and Tail
#If recursive call at head then it is head recusrsion , Tail recursion

def Display(No):
    Add = 0
    while (No>0):
        Add = Add + No
        No = No - 1
    print(Add)

Display(4)


def DisplayNew(No):
    Ans = 0

    if (No <= 0):
        return 0
    else:
        return (No+Display(No-1))

DisplayNew(4)