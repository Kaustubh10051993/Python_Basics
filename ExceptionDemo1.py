
def main():

    try:

        print("Enter No")
        No1 = int(input())

        print("Enter No")
        No2 = int(input())

        Ans = No1/No2                   # if No2 = Zero then there is error - Exception prone line
        print("Divison",Ans)
                                        #First except gets called - Program moves to Finally not checking to other.
    except ZeroDivisionError:
        print("Inside ZeroDivisionError Error")

    except ValueError:
        print("Inside Value Error")

    except Exception:
        print("Inside last except block")

    finally:
        print("Insider Finally block")

if __name__ == "__main__":
    main()

