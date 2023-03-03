#Inner Function cannot be called
#Function can be passed as parameter
#
#

def Demo():
    print("Inside Demo")

def Fun():
    print("Inside Fun")

def Hello(FPT):               #Nacked parameter
    print("Inside Hello")
    FPT()

Hello(Demo)
Hello(Fun)




