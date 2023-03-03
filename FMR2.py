#list , even , +2 ,addition of these numbers.


def CheckEven(No):
    return (No % 2 == 0)

def filterX(helper_function,Data):
    Result = []
    for no in Data:
        if (helper_function(no)==True):
            Result.append(no)
    return Result

def Double(No):
        return No*2

def mapX(Helper_function,Data):
    Result = []
    for No in Data:
        Value = Helper_function(No)
        Result.append(No)

    return Result


def main():

    print("Enter number of elements you want to enter")
    iSize = int(input())
    Data_Input = []

    print("Please enter the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data_Input is",Data_Input)

    Data_filter = filterX(CheckEven,Data_Input)
    print("Data after filter", Data_filter)

    Data_map = mapX(Double,Data_filter)
    print("Data after map",Data_map)


if __name__ == "__main__":
    main()