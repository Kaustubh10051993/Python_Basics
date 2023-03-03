#Arguments = position , keyword , default,
#Argument is input given to function
#Positional Argument- Required Argument
#Keywords Argument
#function call - Parameter and index known = use Positional Argument
#function call - Parameter and index not known = go for Keyword argument
# if you are writing a function - prepare - function documentation for user
#

def Area(Radius, PI = 3.14):
    Result = PI*Radius*Radius
    return Result


def main():
    RValue = 10.5
    PIValue = 3.14


    Ans = Area(RValue,PIValue)       # Ans = Area (10.5 , 3.14 )
    print("Area of circle is :",Ans)

    Ans = Area(PI =PIValue, Radius=RValue)       # Ans = Area (10.5 , 3.14 )
    print("Area of circle is :",Ans)

    Ans = Area(RValue)       # Ans = Area (10.5 , 3.14 )
    print("Area of circle is :",Ans)

    Ans = Area(Radius=10.5 , PI = 7.10)
    print("Area of circle is :",Ans)

if __name__ == "__main__":
    main()
