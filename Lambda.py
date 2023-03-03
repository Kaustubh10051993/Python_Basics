#Ananymous functions are called as Lamda function
#no function - scripting.
#lambda function use - Functional programming -
#Def function - procedural coding
#Class create - Object oriented
#lambda is keyword and is considered as object which can be passed to someone else.


#Normal functions /Named Functions - defined using keyword def

def Add(no1,no2):
    return no1+no2

#Lambda function or unnamed function/Anonymous function

#syntax
#lambda parameters : body

AddFunction = lambda A,B : A+B

Ans1 = Add(10,11)
Ans2 = AddFunction(10,11)

print("Addition using normal function",Ans1)
print("Addition using Lambda function",Ans2)

print("Type of lambda function is",type(AddFunction))
#Class is function


