import os
from sys import*

def Directory_Watcher(Dir_Name):
    print("Inside Directory Watcher Method")
    print("Name of the input:",Dir_Name)

    for foldername,subfolder,Filenames in os.walk(Dir_Name):
        print("Folder Name is:" + foldername)

        for subf in subfolder:
            print("Subfolder name of"+foldername+ "is" +subf)

        for fnames in Filenames:
            print("File inside the folder"+foldername+ "is" +fnames+ "Having Size",os.path.getsize(fnames))

        print(" ")

def main():

    print("Directory watcher Application")

    if (len(argv) < 2):
        print("Insufficient Arguments")
        exit()

    if (argv[1] == "--h"):
        print("This script will travel the directory and display the name of all the entries")
        exit()

    if (argv[1] == "--u"):
        print("Usage:Application_NAME Directory Name")
        exit()

    Directory_Watcher(argv[1])

if __name__ == "__main__":
    main()
