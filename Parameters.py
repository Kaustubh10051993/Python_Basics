#Arguments = position , keyword , default,
#Argument is input given to function


#Positional Argument- Required Argument
#Keywords Argument
#function call - Parameter and index known = use Positional Argument
#function call - Parameter and index not known = go for Keyword argument
# if you are writing a function - prepare - function documentation for user


def Add1(No1,No2):
    print(type(No1))
    print("Value of No1 :",No1)
    print("Value of No2 :", No2)
    return No1 + No2

def Sub1(No1,No2):
    print("Value of No1 :",No1)
    print("Value of No2 :", No2)
    return No2 - No1

def main():
    Ans = 0                    #Syntaxctically not correct to not to mention  - prepare - function documentation. for user
    # = 0

#Standard practice to store a value in varaible once declared.
    Ans = Add1(No2=10,No1=11)  #Keyword Arguement
    print("Addition is:",Ans)

    Ans = Sub1(No2=10, No1=11)
    print("Substraction is:", Ans)

if __name__ == "__main__":
    main()
