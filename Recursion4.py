#Calling the function frmo itself
#Static local variable to control recusion
#Major Drawback - StackOverflow
#Time and memory space used in Recursion is more than loop
#Write normal function with While
#Recursion TYPE -  Head and Tail
#If recursive call at head then it is head recusrsion , Tail recursion


def Display(No):

    while(No>0):
        print(No)
        No = No -1

Display(4)



#Output - RecursionError: maximum recursion depth exceeded while calling a Python object


def Display(No):

    if (No>0):
        No = No - 1
        Display(No)              #This indentation if is wrong it will be in recursion
        print(No)                #Backtracking -

Display(4)
