#Inner Function cannot be called
#Function can be passed as parameter
#We can Pass a function as a parameter to another function
#Functions are the first - class object
#To call function within function or NESTED Function

#Should know below details to use Decorator
#Function name , parameter , data type , output , work of function



def Substraction(No1,No2):
    print("Inside Sub")
    Ans = 0
    Ans = No1 - No2
    return Ans

def Decorated_Function(Function_name):
    def Inner(A,B):
        if(A<B):
            A,B = B,A              #Multiassignment statement- Swapping of Numbers
        return Function_name(A,B)
    return Inner

def main():
    Value1 = int(input("Enter the first number"))
    Value2 = int(input("Enter the Second number"))

    New_Function = Decorated_Function(Substraction)
    print(New_Function,Value1,Value2)

if __name__ =="__main__":
    main()

