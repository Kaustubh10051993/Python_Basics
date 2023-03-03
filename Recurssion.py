#Calling the function frmo itself
#Static local variable to control recusion
#Major Drawback - StackOverflow
#Time and memory space is more

def Display(No):
    Cnt = 0
    while (Cnt < No):
        print("Hello")
        Cnt = Cnt + 1

Display(4)