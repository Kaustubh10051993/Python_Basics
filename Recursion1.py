#Calling the function frmo itself
#Static local variable to control recusion
#Major Drawback - StackOverflow
#Time and memory space used in Recursion is more than loop


def Display(No):
    Cnt = 0

    if (Cnt < No):
        print("Hello")
        Cnt = Cnt + 1
        Display(No)

Display(4)

#Output - RecursionError: maximum recursion depth exceeded while calling a Python object

