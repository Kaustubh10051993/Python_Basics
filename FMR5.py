#list , even , +2 ,addition of these numbers.

from functools import reduce


def main():

    print("Enter number of elements you want to enter")
    iSize = int(input())
    Data_Input = []

    print("Please enter the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data_Input is",Data_Input)

    Data_filter =list(filter(lambda No: No% 2 == 0,Data_Input))
    print("Data after filter", Data_filter)

    Data_map = list(map(lambda No:No*2,Data_filter))
    print("Data after map",Data_map)

    Data_reduce = reduce(lambda A,B:(A+B),Data_map)

    print("Data after map", Data_reduce)

if __name__ == "__main__":
    main()