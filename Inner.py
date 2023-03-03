#Inner Function cannot be called
#Function can be passed as parameter


def Hello():
    print("Inside Hello")

    def Demo():
        print("Inside Demo")

    Demo()

Hello()
Hello().Demo()

