#Lambda function or unnamed function/Anonymous function
#syntax
#lambda parameters : body

def CheckEven(No):
    if (No % 2 == 0):
        return True
    else:
        return False

Even = lambda No : No % 2 == 0

Ret = Even(12)

def CheckEven2(No):
    return (No % 2 == 0)

Ret = CheckEven2(12)

if (Ret == True):
    print("Even")
else:
    print("Odd")

