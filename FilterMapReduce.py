#FMP are used within Lambda function - These are built in functions
#Filter - to select #Should know what you want
#Map - Processing #processing on filtered data
#Reduce - Reduced #

#list , even , +2 ,addition of these numbers.

List = [10,21,12]

#Filter Syntax
#
#Map Syntax
#
#Reduce Syntax

def CheckEven(No):
    return (No % 2 == 0)

def Increament():
    return No+2

def filterX(Arr,Function_Name):
    Result = []
    for no in Arr:
        if (Function_Name(no)):
            Result.append(no)
    return Result

def mapX(Arr,Function_Name):
    Result = []
    for no in Arr:
        Value = Function_Name(no)
        Result.append(Value)
    return Result

def main():
    Data = [2,3,1,6,4,5]
    print("Original Data:",Data)

    Data_Filter = filterX(Data,CheckEven)

    print("Data after Filter",Data_Filter)
    print("Data type of Data_Filter : ",type(Data_Filter))

    Data_map = mapX(Data_Filter,Increament)

    print("Data after map", Data_map)

if __name__ =="__main__":
    main()

