#FileIO


import os
cwd = os.getcwd()                #To get the current path of file

print(cwd)

FD1 = open("Sales.xlsx",'r')

print(FD1)

FD1.close()

#<_io.TextIOWrapper name='Sales.xlsx' mode='r' encoding='cp1252'>

#FD2 = open("C:\Users\KAUSTUBH\Desktop\Python\Apps\Own\Sales.xlsx")

print(FD2)

