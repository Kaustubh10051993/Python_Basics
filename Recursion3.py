#Calling the function frmo itself
#Static local variable to control recusion
#Major Drawback - StackOverflow
#Time and memory space used in Recursion is more than loop


def Display(No):

    if (No > 0):           #Condition to stop the recursion
        print("Hello")
        No = No -1
        Display(No)         #Recursion Function call

Display(4)      #Function Call

#Output - RecursionError: maximum recursion depth exceeded while calling a Python object

