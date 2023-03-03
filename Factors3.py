from sys import *

def facto(No):
    i = 1
    while (i <= int(No / 2)):
        if ((No % i) == 0):
            print(i)
        i = i + 1

def main():
    print("Welcome to : ", argv[0])
    Ret = facto(int(argv[1]))
    print(Ret)

if __name__ == "__main__":
    main()
