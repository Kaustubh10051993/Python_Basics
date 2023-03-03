import time



def DisplayEven(No):

    for i in range(No):
        if (i % 2 == 0 ):
            print("Even Number:",i)

def DisplayOdd(No):
    for i in range(No):
        if (i % 2 != 0):
            print("Odd Number:", i)

def main():

    print("____Demonstation of Serial Programming____")

    DisplayEven(20)
    DisplayOdd(20)


if __name__ == "__main__":

    start_time = time.process_time()

    main()

    end_time = time.process_time()

    print("Execution time is:",end_time - start_time)
