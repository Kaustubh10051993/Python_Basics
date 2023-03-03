#Function - Argument - Lamda function , Filter Map Reduce
#Functions - First class entity - Programers most know things.
#Function which accepts nothing and returns nothing
#Service providers functions -

def Demo1():
    print("Inside Demo1")

#One I/P , One O/P

def Demo2(No):
    print("Inside Demo 2 with argument:",No)

def Demo3(No):
    print("Inside Demo 3 with argument",No)
    return No+2                         #return - to go back to call function with value

#Input 2 , output 1
def Demo4(No1,No2):
    print("Inside Demo4")
    Add = No1 + No2
    return Add

#Input 2 , output 2
#position , keyword , default,
def Demo5(No1,No2):
    print("Inside Demo5")
    Add = No1 + No2
    Sub = No1 - No2
    return Add,Sub             #output is List

def main():
    Demo1()
    Demo2(11)
    Ans  = Demo3(10)                    #stores the return value
    print("Return value of Demo3 is:",Ans)
    Ans = Demo4(10,11)
    print("Return value is:",Ans)
    Ans1,Ans2 = Demo5(11,10)
    print("First reurn value",Ans1)
    print("Second reurn value", Ans2)


if __name__ == "__main__":
    main()

