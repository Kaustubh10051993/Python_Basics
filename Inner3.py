#Inner Function cannot be called
#Function can be passed as parameter
#
#

def Add(A,B):
    print("Inside ADD")
    return  A + B

def Sub(A,B):
    print("Inside Sub")
    return A-B

def Calculator(Name_of_Operation,Value1,Value2):
    return Name_of_Operation(Value1,Value2)

Ret = Calculator(Target = Add,Value1 = 10,Value2= 11)
print("Addition is:",Ret)

Ret = Calculator(Sub,10,11)
print("Substraction is:",Ret)

#We can Pass a function as a parameter to another function




