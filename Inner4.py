#Inner Function cannot be called
#Function can be passed as parameter
#We can Pass a function as a parameter to another function
#Functions are the first - class object

def Outer():    # 100 ID
    print("Inside Outer")
    print(id(Outer))

    def Inner():  #200 ID
        print("Inside Inner")

    print(id(Inner))

    return Inner

ret = Outer()      #ret = 100() ID
print(type(ret))
print(id(ret))

ret()         #ret = 200() ID          #Breaking of Abstraction




