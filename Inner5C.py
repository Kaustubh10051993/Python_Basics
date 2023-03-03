
def Substraction(No1, No2): #200 id
    Ans = 0
    Ans = No1 - No2
    return Ans

def Decorated_Function(Function_Name):
    def Inner(A,B):
        if(A < B):
            A,B = B,A
        return Function_Name(A,B)
    return Inner

def main():
    Value1 = int(input("Enter first number : "))    #Value 8
    Value2 = int(input("Enter second number : "))   #Value 12
    
    New_Function = Decorated_Function(Substraction)    #Decorated_function(200)
    print(New_Function(Value1,Value2))


if __name__ == "__main__":
    main()     #Call 100()
