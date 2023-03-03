
from sys import *

def Script_Task(No):

    if ((No%2)==0):
        print("It is even number")
    else:
        print("It is Odd number")

def main():
    print("____________Marvelllous Infosystem Automations_________________")

    print("Automation script stated with name:",argv[0])

    if (len(argv) != 2):
        print("Error: Isufficient Arguments")
        print("Use -h for help and -u for usage of the script")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help:This script is used to perform _________")

    elif ((argv[1] == "-u") or argv[1] =="-U"):
        print("Usage: Provide ---- number of argument as")
        print("First Argument as:______")
        print("Second Argument as:______")
        exit()
    else:
        Script_Task(int(argv[1]))

if __name__ == "__main__":
    main()

