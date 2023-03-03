import time
import threading


def DisplayEven(No):

    for i in range(No):
        if (i % 2 == 0 ):
            print("Even Number:",i)

def DisplayOdd(No):
    for i in range(No):
        if (i % 2 != 0):
            print("Odd Number:", i)

def main():
    print("____Demonstation of Parallel Programming using multiple Threads____")

    Number = 100

    p1 = threading.Thread(target = DisplayEven,args=(Number,))            # , = for further arguments can be passed.
    p2 = threading.Thread(target = DisplayOdd,args=(Number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of Main")


if __name__ == "__main__":
    start_time = time.process_time()
    main()

    end_time = time.process_time()
    print("Execution time is:",end_time - start_time)