#Program to find the mathematical values from formulas or equation

import InterstRate
def main():
    print("Please enter the below requested details to calculate the interest on your loan amount.")
    print("Current module name is",__name__)
    print("Enter the principal amount.")
    principal = int(input())
    print("Enter the expected time period of loan in years.")
    time = int(input())
    print("Enter the rate of interest")
    rate = float(input())

    interest = interstRate.interst(principal,time,rate)
    print("interest on principal at the rate for time given is",interest)



